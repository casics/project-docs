#!/usr/bin/env python3.4

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib import rcParams

textcolor = '#222222'

rcParams['figure.figsize']      = (4.5, 1.5)
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

# Data straight from the spreadsheet.
data = [5, 10,  32,  35,  25,  15,  45,  16,  25,  30,  25,  10,  20,  5,
        23,  30,  30,  20,  9,  2,  30,  2,  3,  32,  25,  35,  20,  20,  10,
        28,  13,  1,  15,  13,  9,  5,  35,  25,  10,  35,  30,  30,  20,
        25,  25,  5,  10,  15,  13,  15,  15,  35,  27,  14, 25]

# Set up axes.
plt.xlim(0, 50)
plt.ylim(0, 10)

# Histogram.
plt.hist(data, bins=np.linspace(0, 45, 10), width=4.9, facecolor="#cccccc")

# Rugplot.
plt.gca().plot(data, [0.25]*len(data), '|', color='#cc0000')

# Info
total  = len(data)
minval = min(data)
maxval = max(data)
mean   = np.mean(data)
stdev  = np.std(data)
text   = 'Total responses: {}\nMean: {:.2f}\nStd. dev.: {:.2f}\nMinimum: {}\nMaximum: {}'.format(
    total, mean, stdev, minval, maxval)

plt.gca().text(1.075, 0.5, text, horizontalalignment='right', fontsize=10,
               transform=plt.gca().transAxes, color=textcolor)

# Remove the plot frame lines.
for spine in ['top', 'bottom', 'left', 'right']:
    plt.gca().spines[spine].set_visible(False)

# Get rid of excess lines and make grid lines lighter in color.
plt.gca().tick_params(color='#888888')
plt.gca().yaxis.grid(True, color='#ffffff', linewidth=1, linestyle='solid')
plt.gca().yaxis.set_ticks_position('left')
plt.gca().xaxis.set_ticks_position('bottom')

plt.savefig('histogram-years.pdf', bbox_inches='tight')
plt.close()
