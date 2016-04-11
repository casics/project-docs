#!/usr/bin/env python3.4

import pdb
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib import rcParams

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

plt.figure(figsize=(3.8, 1.85))
ax = plt.subplot(111)
ax = plt.gca()
ax.tick_params(width=1, length=3, color='#888888')

# Data.
total_responses = 69
raw_data = {"I always choose the software I use"               : 25,
            "More often than not, I choose the software I use" : 36,
            "Half the time, a situation or task requires using\npreselected software, and other times I get to choose" : 4,
            "Sometimes I get to choose the software I use"     : 4,
            "I never get to choose the software I use"         : 0}

# Sort the data by value, largest value first.

data = sorted(raw_data.items(), key=lambda x: x[1], reverse=True)
labels = [k for k, v in data]
values = [v for k, v in data]

# Plot.
# Barh() puts items in the reverse order of how we put them in the
# lists above, so first we do this to reverse the lists:
labels = labels[::-1]
values = values[::-1]
y_pos = np.arange(len(values))
plt.barh(y_pos, values, linewidth=0, align='center', color="#cccccc")
plt.yticks(y_pos, labels)

ax.text(0.7, 0.1, 'Total responses: {}.'.format(total_responses), transform=ax.transAxes)

# Styling.

# Remove the plot frame lines.
ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["right"].set_visible(False)

ax.spines['left'].set_bounds(-0.5, 4.5)
ax.spines['left'].set_color('#888888')

ax.get_xaxis().set_visible(False)
ax.get_yaxis().tick_left()
plt.tick_params(
    axis='y',                       # changes apply to the x-axis
    which='both',                   # both major and minor ticks are affected
    bottom='off',                   # ticks along the bottom edge are off
    left='off',                     # ticks along the top edge are off
    top='off')

# Write the value to the right of each bars.
for rect, value in zip(ax.patches, values):
    width = rect.get_width()
    percent = value/total_responses*100
    text = '{} ({: >2.0f})\%'.format(value, percent)
    offset = 4 if value > 4 else 3
    ax.text(rect.get_x() + width + offset, rect.get_y() + rect.get_height()/2,
            text, ha='center', va='center', fontsize=10)

plt.savefig('how-often-choose-software.pdf', bbox_inches='tight')
plt.close()
