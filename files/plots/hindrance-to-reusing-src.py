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

plt.figure(figsize=(3.5, 5.5))

# Data.

total_responses = 52

# Choices were not mutually exclusive.

raw_data = {
    "Incompatible licensing terms"                        : 25,
    "Incompatible implementation language"                : 31,
    "Incompatible API"                                    : 9,
    "Incompatible operating system or other requirements" : 26,
    "Inability to compile source code"                    : 23,
    "Inability to install software"                       : 15,
    "Poor code quality"                                   : 18,
    "Poor code modularity"                                : 17,
    "Poor documentation or lack of documentation"         : 32,
    "Poor software performance"                           : 11,
    "Lack of support for desired standards"               : 8,
    "Lack of needed functionality"                        : 20,
    "Incomprehensible algorithm"                          : 15,
    "Inadequate verification and/or testing of code"      : 4,
    "Insufficient developer or vendor support"            : 12,
    "Unsuitable cost/price"                               : 16,
    "Source code too large"                               : 2,
    "Other"                                               : 3,
}

x = [0, 10, 20, 30, 40]

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

plt.yticks(y_pos, labels, fontsize=10)
plt.xticks(x, fontsize=10)
plt.ylim([ylim_bottom, ylim_top])

plt.gca().text(0.96, 0.01,
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
    width = rect.get_width()
    offset = 5 if value > 10 else 4
    plt.gca().text(rect.get_x() + width + offset,
                   rect.get_y() + rect.get_height()/2,
                   text, ha='center', va='center', fontsize=10)

plt.savefig('hindrance-to-reusing-src.pdf', bbox_inches='tight')
plt.close()
