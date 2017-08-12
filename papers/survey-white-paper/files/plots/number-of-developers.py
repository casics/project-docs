#!/usr/bin/env python3.4

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib import rcParams

textcolor = '#222222'

rcParams['figure.figsize']      = (1.75, 1.75)
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
data = [56, 13]
labels = ['Yes', 'No']

# Histogram.
plt.pie(data, startangle=160, labels=labels, autopct='%1.f\%%', colors=['#bbbbbb', '#eeeeee'])

plt.gca().text(0, 1, 'Total responses: 69.', horizontalalignment='left',
               transform=plt.gca().transAxes, fontsize=10, color=textcolor)

plt.savefig('number-of-developers.pdf', bbox_inches='tight')
plt.close()
