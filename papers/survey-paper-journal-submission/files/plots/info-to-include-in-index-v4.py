#!/usr/bin/env python3.4

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib import rcParams
import operator

rcParams['text.usetex']         = True
rcParams['text.latex.preamble'] = [r"\usepackage{fourier}", r"\usepackage[T1]{fontenc}"]
rcParams['font.family']         = 'serif'
rcParams['font.serif']          = ['Utopia']
rcParams['font.weight']         = 'normal'
rcParams['font.size']           = 10
rcParams['xtick.labelsize']     = rcParams['ytick.labelsize'] = 10
rcParams['ytick.major.width']   = rcParams['xtick.major.width'] = 1
rcParams['ytick.major.size']    = rcParams['xtick.major.size'] = 3
rcParams['patch.facecolor']     = "#cccccc"
rcParams['patch.linewidth']     = 0

plt.figure(figsize=(3.5, 8))

# Data.

total_responses = 69
total_swdevs    = 56
total_notswdevs = 13

# Choices were not mutually exclusive.

raw_data = {
    "Availability of discussion lists/forums"               : [38, 32, 6],
    "Availability of public issue/bug tracker"              : [29, 26, 3],
    "Availability of support or help"                       : [34, 25, 9],
    "Data formats supported"                                : [53, 43, 10],
    "Domain/subject/field of application"                   : [54, 43, 11],
    "How active development appears to have been over time" : [37, 31, 6],
    "How recently has the software been updated"            : [49, 42, 7],
    "License terms of software"                             : [54, 44, 10],
    "Metrics evaluating code quality"                       : [18, 15, 3],
    "Name of software"                                      : [61, 48, 13],
    "Name(s) of developer(s)"                               : [30, 25, 5],
    "Operating system(s) supported"                         : [63, 52, 11],
    "Programming language(s) software is written in"        : [39, 34, 5],
    "Purpose of software"                                   : [63, 50, 13],
    "Software libraries needed"                             : [47, 38, 9],
    "Specific workflow environments supported"              : [17, 14, 3],
    "Type(s) of user interfaces offered (e.g., GUI)"        : [39, 33, 6],
    "URL for software's home page"                          : [53, 44, 9],
    "Whether a programmable API is available"               : [36, 31, 5],
    "Whether a publication is associated with the software" : [34, 28, 6],
    "Whether installation uses common facilities or tools"  : [27, 23, 4],
    "Whether source code is available"                      : [42, 37, 5],
    "Whether the code base includes test cases"             : [20, 17, 3],
    "Whether the code base is well commented"               : [18, 16, 2],
    "Other"                                                 : [10, 10, 0],
}

x = [0, 10, 20, 30, 40, 50, 60, 70]

# Plot.

# Sort the data by value, largest value first.

data   = sorted(raw_data.items(), key=lambda x: x[1][0], reverse=True)

# Create data arrays for what we will hand to barh().  Make the numbers
# be percentages of the totals for the subpopulations.

total     = [item[1][0] for item in data]
swdevs    = [item[1][1] for item in data]
notswdevs = [item[1][2] for item in data]

labels    = [item[0] for item in data]

# Barh() puts items in the reverse order of how we put them in the
# lists above, so first we do this to reverse the lists:

labels    = labels[::-1]
total     = total[::-1]
swdevs    = swdevs[::-1]
notswdevs = notswdevs[::-1]

# Misc. axis setup.

y_pos = np.arange(len(data))
ylim_bottom = -0.5
ylim_top = len(data)-0.5

# Create the plot and the initial axes.
# .............................................................................
# Version using stacked bars.

# Helper functions.

def neg(the_list): return [-value for value in the_list]
def sum(list1, list2): return [x+y for x, y in zip(list1, list2)]

h_swdevs = plt.barh(y_pos, swdevs,
                    linewidth=0, align='center', color="#8b8b8b")
h_notswdevs = plt.barh(y_pos, notswdevs, left=swdevs,
                       linewidth=0, align='center', color="#cccccc")

plt.yticks(y_pos, labels, fontsize=10)
plt.xticks(x, fontsize=10)
plt.ylim([ylim_bottom, ylim_top])

plt.legend([h_swdevs, h_notswdevs],
           ['Involved in software development',
            'Not involved in software dev.'],
           fontsize=9, ncol=1, loc='upper center',
           frameon=False, bbox_to_anchor=(0.625, 0.1))

# Remove the plot frame lines leaving only the left vertical one.
for spine in ['top', 'bottom', 'right']:
    plt.gca().spines[spine].set_visible(False)
plt.gca().spines['left'].set_bounds(ylim_bottom, ylim_top)
plt.gca().spines['left'].set_color('#888888')
plt.gca().tick_params(color='#888888')
plt.gca().yaxis.set_ticks_position('none')
plt.gca().get_xaxis().set_visible(False)


plt.savefig('info-to-include-in-index-v4.pdf', bbox_inches='tight')
plt.close()
