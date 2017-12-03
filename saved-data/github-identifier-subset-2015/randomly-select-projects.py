#!/usr/bin/env python3.4
#
# @file    randomly-select-projects.py
# @brief   Select randomly from a file
# @author  Michael Hucka
#
# <!---------------------------------------------------------------------------
# Copyright (C) 2015 by the California Institute of Technology.
# This software is part of CASICS, the Comprehensive and Automated Software
# Inventory Creation System.  For more information, visit http://casics.org.
# ------------------------------------------------------------------------- -->

import pdb
import sys
import os
import plac
import random
import time

# Main body.
# .............................................................................
# Currently this only does GitHub, but extending this to handle other hosts
# should hopefully be possible.

def main(input_file=None, desired_total=None):
    seed = time.time()
    generator = random.Random(seed)

    with open(input_file) as f:
        all_ids = [int(x) for x in f.read().splitlines()]

    subset = random.sample(all_ids, int(desired_total))
    for item in subset:
        print(item, flush=True)

# Plac annotations for main function arguments
# .............................................................................
# Argument annotations are: (help, kind, abbrev, type, choices, metavar)
# Plac automatically adds a -h argument for help, so no need to do it here.

main.__annotations__ = dict(
    input_file    = ('input file, from which selections are to be made', 'option', 'f'),
    desired_total = ('number of entries to select from the input file', 'option', 'n'),
)

# Entry point
# .............................................................................

def cli_main():
    plac.call(main)

cli_main()
