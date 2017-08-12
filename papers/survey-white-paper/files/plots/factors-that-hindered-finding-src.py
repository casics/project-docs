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

plt.figure(figsize=(2, 2.1))

# Data.

total_responses = 52

# Choices were not mutually exclusive.

raw_data = {
    "Lack of time to do a proper search and/or evaluate the results"                : 24,
    "Unable to locate any suitable or working software source code for my purposes" : 36,
    "Concerns about intellectual property issues"                                    : 6,
    "Lack of trust in the options found"                                             : 12,
    "My specific requirements were too unique"                                       : 33,
    "Using 3rd-party source code is prevented by policies"                          : 2,
    "Other"                                                                          : 6,
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

plt.yticks(y_pos, labels, fontsize=10, color=textcolor)
plt.xticks(x, fontsize=10, color=textcolor)
plt.ylim([ylim_bottom, ylim_top])

plt.gca().text(1.3, 0.05,
               'Total responses: {}\nMult. selections allowed'.format(total_responses),
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
    offset = 7.5 if value > 2 else 5
    plt.gca().text(rect.get_x() + width + offset,
                   rect.get_y() + rect.get_height()/2,
                   text, ha='center', va='center', fontsize=10, color=textcolor)

plt.savefig('factors-that-hindered-finding-src.pdf', bbox_inches='tight')
plt.close()
