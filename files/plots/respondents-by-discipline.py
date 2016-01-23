#!/usr/bin/env python3.4

import pdb
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

plt.rcParams.update({
    'text.usetex': True,
    'text.latex.preamble': [
        r"\usepackage{fourier}",
        r"\usepackage[T1]{fontenc}",
    ]
})

font = {'family' : 'serif',
        'serif'  : 'Utopia',
        'size'   : 9
}
matplotlib.rc('text', usetex=True)
matplotlib.rc('font', **font)

plt.figure(figsize=(4.5, 2.25))
ax = plt.subplot(111)
ax = plt.gca()
ax.tick_params(width=1, length=3, color='#888888')

# Data.
total_responses = 68
labels = ["``Aerospace Engineering (Robotics)''",
          "Social Sciences",
          "Cognitive and Brain Sciences",
          "Geological and Planetary Sciences",
          "Chemical and Chemical Engineering",
          "Biology and Biological Engineering",
          "Computing and Mathematical Sciences",
          "Physical Sciences",
]
data = [1, 0, 0, 2, 2, 19, 31, 39]
y_pos = np.arange(len(data))
x = [0, 10, 20, 30, 40]

plt.barh(y_pos, data, linewidth=0, align='center', color="#cccccc")
plt.yticks(y_pos, labels)

# Styling.

# Remove the plot frame lines leaving only the left vertical one.
ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["right"].set_visible(False)

ax.spines['left'].set_bounds(-0.5, 7.5)
ax.spines['left'].set_color('#888888')

ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()
plt.xticks(x, fontsize=9)
plt.tick_params(
    axis='y',                       # changes apply to the x-axis
    which='both',                   # both major and minor ticks are affected
    bottom='off',                   # ticks along the bottom edge are off
    left='off',                     # ticks along the top edge are off
    top='off')
plt.gcf().subplots_adjust(bottom=0.15)

ax.xaxis.grid(True, color='1', linestyle='solid', linewidth=1)

# Write the value to the right of each bars, except the ones that have value 0.
for rect, value in zip(ax.patches, data):
    width = rect.get_width()
    x_pos = (rect.get_x() + width + 1.2) if value else (rect.get_x() + 0.5)
    y_pos = rect.get_y() + rect.get_height()/2
    ax.text(x_pos, y_pos, value, ha='center', va='center', fontsize=8)

# Write the percentage inside the bars, but only if it's more than 1.
# (Bars are too short if the value is 1.)
# This requires a bit of fiddling with positioning.
for rect, value in zip(ax.patches, data):
    rect.set_height(rect.get_height()/1.1)
    rect.set_y(rect.get_y()*1.001)
    percent = value/total_responses*100
    text = '{: >2.0f}\%'.format(percent)
    if value > 1:
        new_x = rect.get_x() + 1.2
        new_y = rect.get_y() + rect.get_height()/2.2
        ax.text(new_x, new_y, text, ha='center', va='center', fontsize=9)

plt.savefig('respondents-by-discipline.pdf', bbox_inches='tight')
plt.close()
