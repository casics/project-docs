#!/usr/bin/env python3.4

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib import rcParams
import operator

textcolor = '#222222'

rcParams['text.usetex']         = True
rcParams['text.latex.preamble'] = [r"\usepackage{fourier}",
                                   r"\usepackage[rgb,dvipsnames,svgnames]{xcolor}",
                                   r"\definecolor{almostblack}{gray}{0.23}",
                                   r"\color{almostblack}",
                                   ]
rcParams['text.color']          = textcolor
rcParams['font.family']         = 'serif'
rcParams['font.serif']          = ['Utopia']
rcParams['font.weight']         = 'medium'
rcParams['font.size']           = 10
rcParams['xtick.labelsize']     = rcParams['ytick.labelsize'] = 10
rcParams['ytick.major.width']   = rcParams['xtick.major.width'] = 1
rcParams['ytick.major.size']    = rcParams['xtick.major.size'] = 3
rcParams['patch.facecolor']     = "#cccccc"
rcParams['patch.linewidth']     = 0

plt.figure(figsize=(3.4, 10))

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
    "How active development appears\nto have been over time" : [37, 31, 6],
    "How recently has the software been updated"            : [49, 42, 7],
    "License terms of software"                             : [54, 44, 10],
    "Metrics evaluating code quality"                       : [18, 15, 3],
    "Name of software"                                      : [61, 48, 13],
    "Name(s) of developer(s)"                               : [30, 25, 5],
    "Operating system(s) supported"                         : [63, 52, 11],
    "Programming language(s) software is\nwritten in"        : [39, 34, 5],
    "Purpose of software"                                   : [63, 50, 13],
    "Software libraries needed"                             : [47, 38, 9],
    "Specific workflow environments supported"              : [17, 14, 3],
    "Type(s) of user interfaces offered (e.g., GUI)"        : [39, 33, 6],
    "URL for software's home page"                          : [53, 44, 9],
    "Whether a programmable API is available"               : [36, 31, 5],
    "Whether a publication is\nassociated with the software" : [34, 28, 6],
    "Whether installation uses common\nfacilities or tools"  : [27, 23, 4],
    "Whether source code is available"                      : [42, 37, 5],
    "Whether the code base includes test cases"             : [20, 17, 3],
    "Whether the code base is well commented"               : [18, 16, 2],
    "Other"                                                 : [10, 10, 0],
}

x = [0, 10, 20, 30, 40, 50, 60, 70]

# Plot.

# Sort the data by value, largest value first.

data   = sorted(raw_data.items(), key=lambda x: x[1][0], reverse=True)

# Create data arrays for what we will hand to barh().

totals    = [item[1][0] for item in data]
swdevs    = [item[1][1] for item in data]
notswdevs = [item[1][2] for item in data]

labels    = [item[0] for item in data]

# Barh() puts items in the reverse order of how we put them in the
# lists above, so first we do this to reverse the lists:

labels    = labels[::-1]
totals    = totals[::-1]
swdevs    = swdevs[::-1]
notswdevs = notswdevs[::-1]

# Misc. axis setup.

y_pos = np.arange(len(data))
ylim_bottom = -0.5
ylim_top = len(data)-0.5

# Create the plot and the initial axes.
# .............................................................................
# Version using multiple horizontal bar graphs.

h_swdevs = plt.barh(y_pos + 0.215, [x/total_swdevs*100 for x in swdevs],
                    height=0.39, linewidth=0, align='center', color="#afafaf")
h_notswdevs = plt.barh(y_pos - 0.215, [x/total_notswdevs*100 for x in notswdevs],
                       height=0.39, linewidth=0, align='center', color="#dddddd")

plt.yticks(y_pos, labels, fontsize=10, color=textcolor)
plt.xticks(x, fontsize=10)
plt.ylim([ylim_bottom, ylim_top])

# plt.title('\emph{Suppose that it were possible to create a public, searchable catalog or index of software, one that would\n\emph{record information about software of all kinds found anywhere. What kind of information}\n\emph{would you find most useful to include for each entry in such a catalog or index?}',
#           fontsize=10, y=1.03, x=0.2)

plt.legend([h_swdevs, h_notswdevs],
           ['Involved in soft. dev. (n = {})'.format(total_swdevs),
            'Not involved in soft. dev. (n = {})'.format(total_notswdevs)],
           fontsize=8.5, ncol=1, loc='upper center',
           frameon=False, bbox_to_anchor=(0.83, 0.05))

# Remove the plot frame lines leaving only the left vertical one.
for spine in ['top', 'bottom', 'right']:
    plt.gca().spines[spine].set_visible(False)
plt.gca().spines['left'].set_bounds(ylim_bottom, ylim_top)
plt.gca().spines['left'].set_color('#888888')
plt.gca().tick_params(color='#888888')
plt.gca().yaxis.set_ticks_position('none')
plt.gca().get_xaxis().set_visible(False)

# Write the value to the right of each bars.
for rect, value in zip(h_swdevs.patches, swdevs):
    percent = value/total_swdevs*100
    width = rect.get_width()
    offset = 11 if value > 6 else 8
    if value > 0:
        text = '{} ({: >2.0f}\%)'.format(value, percent)
    else:
        offset = 1
        text = '0'
    plt.gca().text(rect.get_x() + width + offset,
                   rect.get_y() + rect.get_height()/2.4,
                   text, ha='center', va='center', fontsize=9.5,
                   color=textcolor)

for rect, value in zip(h_notswdevs.patches, notswdevs):
    percent = value/total_notswdevs*100
    width = rect.get_width()
    offset = 11 if value > 3 else 9
    if value > 0:
        text = '{} ({: >2.0f}\%)'.format(value, percent)
    else:
        offset = 3
        text = '0'
    plt.gca().text(rect.get_x() + width + offset,
                   rect.get_y() + rect.get_height()/2.4,
                   text, ha='center', va='center', fontsize=9.5,
                   color=textcolor)

# Write the value to the right of each bars.
for rect, value in zip(h_swdevs.patches, totals):
    percent = value/total_responses*100
    text = '{} ({: >2.0f}\%)'.format(value, percent)
    offset = 136
    plt.gca().text(rect.get_x() + offset,
                   rect.get_y() + rect.get_height() - 0.43,
                   text, ha='center', va='center', fontsize=10,
                   color=textcolor)

plt.gca().text(1.42, 1.002,
               r'\underline{Totals}',
               horizontalalignment='right',
               transform=plt.gca().transAxes)



plt.savefig('info-to-include-in-index-v5.pdf', bbox_inches='tight')
plt.close()
