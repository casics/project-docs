#!/usr/bin/env python3.4

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib import rcParams

rcParams['figure.figsize']      = (10, 1.75)
rcParams['text.usetex']         = True
rcParams['text.latex.preamble'] = [r"\usepackage{fourier}", r"\usepackage[T1]{fontenc}"]
rcParams['font.family']         = 'serif'
rcParams['font.serif']          = ['Utopia']
rcParams['font.weight']         = 'normal'
rcParams['font.size']           = 11
rcParams['xtick.labelsize']     = rcParams['ytick.labelsize'] = 10
rcParams['ytick.major.width']   = rcParams['xtick.major.width'] = 1
rcParams['ytick.major.size']    = rcParams['xtick.major.size'] = 3
rcParams['patch.facecolor']     = "#cccccc"
rcParams['patch.linewidth']     = 0

# Data.
x = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
y = [0, 0,  0,  0,  1,  1,  1,  0,  1,  0,  8,  1,  3,  1,  4,  5,  8,  4, 14,  7,  9]

# Set up axes.
plt.ylim(0, 15)
plt.yticks([0, 5, 10, 15])
plt.xlim(0, 105)

# Plot.
plt.bar(x, y, width=2, align='center')

# Remove the plot frame lines.
for spine in ['top', 'bottom', 'left', 'right']:
    plt.gca().spines[spine].set_visible(False)

# Get rid of excess lines and make grid lines lighter in color.
plt.gca().tick_params(color='#888888')
plt.gca().yaxis.grid(True, color='#ffffff', linewidth=1, linestyle='solid')
plt.gca().yaxis.set_ticks_position('left')
plt.gca().xaxis.set_ticks_position('bottom')

# Custom labeling for the x axis:
def make_label(x): return '{:.0f}'.format(x) if x < 100 else '100\%'
plt.xticks(x, [make_label(value) for value in x])

# Labels above bars.
for rect, label in zip(plt.gca().patches, y):
    if label > 0:
        height = rect.get_height()
        plt.gca().text(rect.get_x() + rect.get_width()/2, height + 0.5, label,
                       ha='center', va='bottom', fontsize=10, fontweight='normal')

plt.savefig('histogram-time-spent-with-software.pdf', bbox_inches='tight')
