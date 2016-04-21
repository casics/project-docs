#!/usr/bin/env python3.4

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib import rcParams
import operator

textcolor = '#222222'

rcParams['text.usetex']         = True
rcParams['text.latex.preamble'] = [r"\usepackage{fourier}", r"\usepackage[T1]{fontenc}"]
rcParams['text.color']          = textcolor
rcParams['font.family']         = 'serif'
rcParams['font.serif']          = ['Utopia']
rcParams['font.weight']         = 'normal'
rcParams['font.size']           = 10
rcParams['xtick.labelsize']     = rcParams['ytick.labelsize'] = 10
rcParams['ytick.major.width']   = rcParams['xtick.major.width'] = 1
rcParams['ytick.major.size']    = rcParams['xtick.major.size'] = 3
rcParams['patch.facecolor']     = "#cccccc"
rcParams['patch.linewidth']     = 0

plt.figure(figsize=(3.75, 3.4))

# Data.

total_responses = 54

# Choices were not mutually exclusive.

raw_data = {
    "To reuse code as-is (either in whole or in part)"                                         : 38,
    "To find code examples of\nhow specific APIs are used"                                     : 41,
    "To find examples of how to implement a\nparticular algorithm, data structure or approach" : 41,
    "To find a more efficient approach to\nsomething you have already written"                 : 22,
    "To remember syntactic details or\ninfrequently used functionality"                        : 24,
    "To discover new algorithms or data structures"                                            : 19,
    "To learn unfamiliar concepts"                                                             : 24,
    "To confirm or refute that some given\nsoftwarehas a defect/bug"                           : 15,
    "Other"                                                                                    : 2
}

x = [0, 10, 20, 30, 40, 50]

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

plt.yticks(y_pos, labels, fontsize=10, color=textcolor)
plt.xticks(x, fontsize=10, color=textcolor)
plt.ylim([ylim_bottom, ylim_top])

plt.gca().text(1.05, 0.025,
               'Total individual responses: {}\nMultiple selections allowed'.format(total_responses),
               horizontalalignment='right',
               transform=plt.gca().transAxes, color=textcolor)

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
    text = '{} ({: >2.0f}\%)'.format(value, percent)
    width = rect.get_width()
    plt.gca().text(rect.get_x() + width + 5.5,
                   rect.get_y() + rect.get_height()/2,
                   text, ha='center', va='center', fontsize=10, color=textcolor)

plt.savefig('bar-graph-why-search-for-src.pdf', bbox_inches='tight')
plt.close()
