GitHub project subset, by identifier
====================================

This directory contains a list of project identifiers chosen from the set of GitHub projects that we had in our database at the end of 2015.  The selection was performed using the Python program "randomly-select-projects.py" in this directory.  The program performs a straightforward random sample from an input file.

The procedure followed was this:

1. Output a list of all known GitHub identifiers in our database.   (This list is preserved in the neighboring directory "../github-project-identifiers-2015/".)

2. Generate a list of 4 million randomly-selected identifiers from the list from step #1.

3. Generate a list of 2 million randomly-selected identifiers from the list of four million identifiers produced in step #2.  (In other words, this set of two million identifiers is a subset of the 4 million.)

4. Generate a list of 1 million randomly-selected identifiers from the list of two million identifiers produced in step #3.  (In other words, this set of one million identifiers is a subset of the two million.)

The randomly-selected set of identifiers are preserved in this directory in the following files:

* one-million-project-ids.txt
* two-million-project-ids.txt
* four-million-project-ids.txt

Random sampling was achieved using the Python 3.4 "random" module as it existed in the Python 3.4 distribution in December, 2015.  This implementation is known to use a Mersenne Twister algorithm for generating pseudo random numbers.  The Mersenne Twister is known not to be a "great" random number generator, but for the purposes of selecting projects from GitHub, we believe it is adequate.
