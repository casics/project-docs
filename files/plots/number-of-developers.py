#!/usr/bin/env python3.4

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib import rcParams

rcParams['figure.figsize']      = (2, 2)
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

# Data straight from the spreadsheet.
data = [56, 13]
labels = ['Yes', 'No']

# Histogram.
plt.pie(data, startangle=160, labels=labels, autopct='%1.f\%%', colors=['#bbbbbb', '#eeeeee'])

plt.gca().text(0, 1, 'Total responses: 69.', horizontalalignment='left',
               transform=plt.gca().transAxes, fontsize=9)

plt.savefig('number-of-developers.pdf', bbox_inches='tight')
plt.close()
