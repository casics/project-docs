#!/usr/bin/env python3.4
#
# @file    github-cataloguer.py
# @brief   Create a database of all GitHub repositories
# @author  Michael Hucka
#
# <!---------------------------------------------------------------------------
# Copyright (C) 2015 by the California Institute of Technology.
# This software is part of CASICS, the Comprehensive and Automated Software
# Inventory Creation System.  For more information, visit http://casics.org.
# ------------------------------------------------------------------------- -->

# Summary
# .............................................................................
# This uses the GitHub API to download basic information about every GitHub
# repository and stores it in a ZODB database.  The data is stored as a simple
# object for every repository, and has the following fields:
#
#    id = repository unique id (an integer)
#    path = the GitHub URL to the repository, minus the http://github.com part
#    description = the description associated with the repository
#    owner = the name of the owner account
#    owner_type = whether the owner is a user or organization
#
# This code pays attention to the GitHub rate limit on API calls and pauses
# when it hits the 5000/hr limit, restarting again after the necessary time
# has elapsed to do another 5000 calls.  Each GitHub API call nets 100
# records, so a rate of 5000/hr = 500,000/hr.  GitHub is estimated to have
# 19,000,000 projects now, so that works out to 38 hours to download it all.
#
# This uses the github3.py module (https://github.com/sigmavirus24/github3.py),
# a convenient and reasonably full-featured Python GitHub API library.

import github3
from datetime import datetime
from timeit import default_timer as timer
from time import sleep

import ZODB
import persistent
import transaction
from BTrees.OOBTree import BTree

import sys
import pdb


# Globals.
# .............................................................................

dbfile          = "github-data.fs"
github_login    = 'mhucka'
github_password = '<github4me>'
max_fails       = 5


# Helper classes.
# .............................................................................

class GitHubRecord(persistent.Persistent):
    def __init__(self, id=0, path='', description='', owner='', owner_type=''):
        self.id = id
        self.path = path
        self.description = description
        self.owner = owner
        self.owner_type = owner_type


# Helper functions.
# .............................................................................

def msg(*args):
    print(*args, flush=True)

def api_calls_left(githubobj):
    '''Returns an integer.'''
    rate_limit = githubobj.rate_limit()
    return rate_limit['resources']['core']['remaining']

def api_reset_time(githubobj):
    '''Returns a timestamp value, i.e., seconds since epoch.'''
    rate_limit = githubobj.rate_limit()
    return rate_limit['resources']['core']['reset']


# Main body.
# .............................................................................

# Beware the GitHub rate limit: https://developer.github.com/v3/#rate-limiting
# "For requests using Basic Authentication or OAuth, you can make up to 5,000
# requests per hour."
#
# In the code below, we track the number of requests made and the reset time.
# When we hit the limit, we pause until the reset time and then continue.

github = github3.login(github_login, github_password)
calls_left = api_calls_left(github)

msg('Started at ', datetime.now())
started = timer()

msg('Opening database "{}"'.format(dbfile))
dbconnection = ZODB.connection(dbfile)
dbroot = dbconnection.root()

if not 'github' in dbroot.keys():
    msg('Empty database -- creating root object')
    dbroot['github'] = BTree()
else:
    print('"{}" contains {} entries'.format(dbfile, len(dbroot['github'])))

db = dbroot['github']

msg('Initial GitHub API calls remaining: ', calls_left)
msg('Generating list of all repositories:')

# If we're restarting this process, we will already have entries in the db.

count = len(dbroot['github'])

# The iterator returned by github.all_repositories() is continuous; behind
# the scenes, it uses the GitHub API to get new data when needed.  Each API
# call nets 100 repository records, so after we go through 100 objects in the
# 'for' loop below, we expect that github.all_repositories() will have made
# another call, and the rate-limited number of API calls left in this
# rate-limited period will go down by 1.  When we hit the limit, we pause
# until the reset time.

repo_iterator = None
try:
    repo_iterator = github.all_repositories()
except Exception as err:
    msg('github.all_repositories() failed with {0}'.format(err))
    sys.exit(1)

loop_count    = 0
fails         = 0
while fails < max_fails:
    try:
        repo = next(repo_iterator)
        if repo is None:
            msg('Empty return value from github3 iterator')
            break

        if not repo.full_name:
            msg('Empty repo name in data returned by github3 iterator')
            fails += 1
            continue

        if repo.full_name and repo.full_name in db:
            # print('Skipping {} -- already in the database'.format(repo.full_name))
            continue

        if repo.full_name and repo.full_name not in db:
            try:
                msg('Entry {} for {}'.format(count, repo.full_name))
                db[repo.full_name] = GitHubRecord(repo.id,
                                                  repo.full_name,
                                                  repo.description,
                                                  repo.owner.login,
                                                  repo.owner.type)
                transaction.commit()
                count += 1
                fails = 0
            except Exception as err:
                msg('Got exception creating GitHubRecord: {0}'.format(err))
                fails += 1
                continue

        loop_count += 1
        if loop_count > 100:
            calls_left = api_calls_left(github)
            if calls_left > 1:
                loop_count = 0
            else:
                reset_time = datetime.fromtimestamp(api_reset_time(github))
                time_delta = reset_time - datetime.now()
                msg('Sleeping until ', reset_time)
                sleep(time_delta.total_seconds() + 1)  # Extra second to be safe.
                calls_left = api_calls_left(github)

    except StopIteration:
        msg('github3 repository iterator reports it is done')
        break
    except Exception as err:
        msg('github3 generated an exception: {0}'.format(err))
        fails += 1

if fails >= max_fails:
    msg('Stopping because of too many repeated failures')
else:
    msg('Done')

stopped = timer()

msg('Stopped at {}'.format(datetime.now()))
msg('Time to get repositories: {}'.format(stopped - started))

dbconnection.close()
