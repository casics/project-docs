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
rcParams['font.size']           = 9
rcParams['xtick.labelsize']     = rcParams['ytick.labelsize'] = 10
rcParams['ytick.major.width']   = rcParams['xtick.major.width'] = 1
rcParams['ytick.major.size']    = rcParams['xtick.major.size'] = 3
rcParams['patch.facecolor']     = "#cccccc"
rcParams['patch.linewidth']     = 0

plt.figure(figsize=(3.5, 7))

# Data.

total_responses = 69

# Choices were not mutually exclusive.

raw_data = {
    "Name of software"                                      : 61,
    "Domain/subject/field of application"                   : 54,
    "Purpose of software"                                   : 63,
    "Name(s) of developer(s)"                               : 30,
    "Data formats supported"                                : 54,
    "License terms of software"                             : 54,
    "Operating system(s) supported"                         : 63,
    "Software libraries needed"                             : 47,
    "Programming language(s) software is written in"        : 39,
    "How recently has the software been updated"            : 49,
    "How active development appears to have been over time" : 37,
    "Availability of support or help"                       : 34,
    "Availability of public issue/bug tracker"              : 29,
    "Availability of discussion lists/forums"               : 38,
    "Whether the code base includes test cases"             : 20,
    "Whether the code base is well commented"               : 18,
    "Whether a programmable API is available"               : 36,
    "Specific workflow environments supported"              : 17,
    "Type(s) of user interfaces offered (e.g., GUI)"        : 39,
    "Whether source code is available"                      : 42,
    "Whether installation uses common facilities or tools"  : 27,
    "Whether a publication is associated with the software" : 34,
    "Metrics evaluating code quality"                       : 18,
    "URL for software's home page"                          : 53,
    "Other"                                                 : 10,
}

x = [0, 10, 20, 30, 40, 50, 60, 70]

# Plot.

# Sort the data by value, largest value first.

data   = sorted(raw_data.items(), key=lambda x: x[1], reverse=True)
labels = [k for k, v in data]
values = [v for k, v in data]

# Barh() puts items in the reverse order of how we put them in the
# lists above, so first we do this to reverse the lists:

labels = labels[::-1]
values = values[::-1]

# Misc. axis setup.

y_pos = np.arange(len(data))
ylim_bottom = -0.5
ylim_top = len(data)-0.5

# Create the plot and the initial axes.

plt.barh(y_pos, values, linewidth=0, align='center', color="#cccccc")

plt.yticks(y_pos, labels, fontsize=9)
plt.ylim([ylim_bottom, ylim_top])

plt.gca().text(1.025, 0.005,
               'Total individual responses: {}\nMultiple selections allowed'.format(total_responses),
               horizontalalignment='right',
               transform=plt.gca().transAxes)

# Remove the plot frame lines leaving only the left vertical one.

for spine in ['top', 'bottom', 'right']:
    plt.gca().spines[spine].set_visible(False)
plt.gca().spines['left'].set_bounds(ylim_bottom, ylim_top)
plt.gca().spines['left'].set_color('#888888')
plt.gca().tick_params(color='#888888')
plt.gca().yaxis.set_ticks_position('none')
plt.gca().get_xaxis().set_visible(False)

# Write the value to the right of each bars.
for rect, value in zip(plt.gca().patches, values):
    percent = value/total_responses*100
    text = '{} ({: >2.0f})\%'.format(value, percent)
    width = rect.get_width()
    plt.gca().text(rect.get_x() + width + 7,
                   rect.get_y() + rect.get_height()/2,
                   text, ha='center', va='center', fontsize=9)

plt.savefig('info-to-include-in-index.pdf', bbox_inches='tight')
plt.close()
