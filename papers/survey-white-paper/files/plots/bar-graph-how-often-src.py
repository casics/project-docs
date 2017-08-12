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

plt.figure(figsize=(2, 2.5))

# Data.  Not everyone answered the question.
# Only one answered something for "Other".
total_responses = 56
raw_data = {
    "Never"                           : 1,
    "Rarely -- once every few months" : 11,
    "Once per month, on average"      : 17,
    "Once per week, on average"       : 15,
    "Once per day, on average"        : 5,
    "Many times per day"              : 7
}

x = [0, 5, 10, 15, 20]

# Sort the data by value, largest value first.
# Revision 2016-04-29 <mhucka@caltech.edu>: decided not to sort this one
# because readers found it more natural in the order given.

# data = sorted(raw_data.items(), key=lambda x: x[1], reverse=True)
# labels = [k for k, v in data]
# values = [v for k, v in data]

labels = [k for k, v in raw_data.items()]
values = [v for k, v in raw_data.items()]

# Plot.
# Barh() puts items in the reverse order of how we put them in the
# lists above, so first we do this to reverse the lists:
labels = labels[::-1]
values = values[::-1]
y_pos = np.arange(len(values))
plt.barh(y_pos, values, linewidth=0, align='center', color="#cccccc")
plt.yticks(y_pos, labels, color=textcolor)
plt.xticks(x, fontsize=10, color=textcolor)

plt.gca().text(1.5, 0.88,
               'Total responses: {}'.format(total_responses),
               horizontalalignment='right',
               transform=plt.gca().transAxes, color=textcolor)

# Remove the plot frame lines leaving only the left vertical one.
for spine in ['top', 'bottom', 'right']:
    plt.gca().spines[spine].set_visible(False)
plt.gca().spines['left'].set_bounds(-0.5, 5.5)
plt.gca().spines['left'].set_color('#888888')
plt.gca().tick_params(color='#888888')
plt.gca().yaxis.set_ticks_position('none')
plt.gca().get_xaxis().set_visible(False)

# Write the value to the right of each bars.
for rect, value in zip(plt.gca().patches, values):
    percent = value/total_responses*100
    text = '{} ({: >2.0f}\%)'.format(value, percent)
    width = rect.get_width()
    plt.gca().text(rect.get_x() + width + 3.5,
                   rect.get_y() + rect.get_height()/2,
                   text, ha='center', va='center', fontsize=10, color=textcolor)

plt.savefig('bar-graph-how-often-src.pdf', bbox_inches='tight')
plt.close()
