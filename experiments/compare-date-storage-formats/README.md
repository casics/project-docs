2016-01-01 <mhucka@caltech.edu>

This was an experiment to evaluate the most compact representation of date+time values.  We need to store time stamps in the database, so I wondered: what format uses the least amount of space?

According to this, it is the POSIX time stamp format (a floating point number).
