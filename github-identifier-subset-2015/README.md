GitHub project subset, by identifier
====================================

This directory contains a list of project identifiers chosen from the set of GitHub projects that we had in our database at the end of 2015.  The selection was performed using the Python program "randomly-select-projects.py" in this directory.  The program performs a straightforward random sample from an input file; for the input, we used the list of all known GitHub identifiers.  (This list is available in the neighboring directory "../github-project-identifiers-2015/".)

This randomly-selected set of identifiers is preserved in this directory in the following files:

* one-million-project-ids.txt
* two-million-project-ids.txt
* four-million-project-ids.txt

Random sampling was achieved using the Python 3.4 "random" module as it existed in the Python 3.4 distribution in December, 2015.  This implementation is known to use a Mersenne Twister algorithm for generating pseudo random numbers.  The Mersenne Twister is known not to be a "great" random number generator, but for the purposes of selecting projects from GitHub, we believe it is adequate.

