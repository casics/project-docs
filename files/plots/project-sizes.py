#!/usr/bin/env python3.4

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
rcParams['font.size']           = 9
rcParams['xtick.labelsize']     = rcParams['ytick.labelsize'] = 10
rcParams['ytick.major.width']   = rcParams['xtick.major.width'] = 1
rcParams['ytick.major.size']    = rcParams['xtick.major.size'] = 3
rcParams['patch.facecolor']     = "#cccccc"
rcParams['patch.linewidth']     = 0

plt.figure(figsize=(4, 0.65))

# Data.  Not everyone answered the question.
# Only one answered something for "Other".
total_responses = 55
labels = ["Small (1--5 people)",
          "Medium (6--25 people)",
          "Large (more than 25 people)"]
data = [43, 11, 1]
x = [0, 10, 20, 30, 40, 50]

# Plot.
# Barh() puts items in the reverse order of how we put them in the
# lists above, so first we do this to reverse the lists:
labels = labels[::-1]
data = data[::-1]
y_pos = np.arange(len(data))
plt.barh(y_pos, data, linewidth=0, align='center', color="#cccccc")
plt.yticks(y_pos, labels, fontsize=9)
plt.xticks(x, fontsize=9)

# Remove the plot frame lines leaving only the left vertical one.
for spine in ['top', 'bottom', 'right']:
    plt.gca().spines[spine].set_visible(False)
plt.gca().spines['left'].set_bounds(-0.5, 2.5)
plt.gca().spines['left'].set_color('#888888')

# Get rid of excess lines and make grid lines lighter in color.
plt.gca().tick_params(color='#888888')
plt.gca().xaxis.grid(True, color='#ffffff', linewidth=1, linestyle='solid')
plt.gca().yaxis.set_ticks_position('none')
plt.gca().xaxis.set_ticks_position('bottom')

# Write the value to the right of each bars, except the ones that have value 0.
for rect, value in zip(plt.gca().patches, data):
    if value:
        width = rect.get_width()
        plt.gca().text(rect.get_x() + width + 1.5, rect.get_y() + rect.get_height()/2, value,
                ha='center', va='center', fontsize=9)

# Write the percentage inside the bars, but only if it's more than 1.
# (Bars are too short if the value is 1.)
# This requires a bit of fiddling with positioning.
for rect, value in zip(plt.gca().patches, data):
    rect.set_height(rect.get_height()/1.1)
    rect.set_y(rect.get_y()*1.001)
    percent = value/total_responses*100
    text = '{: >2.0f}\%'.format(percent)
    if value > 1:
        new_x = rect.get_x() + 2
        new_y = rect.get_y() + rect.get_height()/2.2
        plt.gca().text(new_x, new_y, text, ha='center', va='center', fontsize=9)

plt.savefig('project-sizes.pdf', bbox_inches='tight')
