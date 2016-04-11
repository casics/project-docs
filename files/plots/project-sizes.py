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
rcParams['font.size']           = 10
rcParams['xtick.labelsize']     = rcParams['ytick.labelsize'] = 10
rcParams['ytick.major.width']   = rcParams['xtick.major.width'] = 1
rcParams['ytick.major.size']    = rcParams['xtick.major.size'] = 3
rcParams['patch.facecolor']     = "#cccccc"
rcParams['patch.linewidth']     = 0

plt.figure(figsize=(2.5, 0.85))

# Data.  Not everyone answered the question.
# Only one answered something for "Other".
total_responses = 56
labels = ["Small (1--5 people)",
          "Medium (6--25 people)",
          "Large (more than 25 people)"]
data = [43, 12, 1]
x = [0, 10, 20, 30, 40, 50]

# Plot.
# Barh() puts items in the reverse order of how we put them in the
# lists above, so first we do this to reverse the lists:
labels = labels[::-1]
data = data[::-1]
y_pos = np.arange(len(data))
plt.barh(y_pos, data, linewidth=0, align='center', color="#cccccc")
plt.yticks(y_pos, labels, fontsize=10)

# Remove the plot frame lines leaving only the left vertical one.
for spine in ['top', 'bottom', 'right']:
    plt.gca().spines[spine].set_visible(False)
plt.gca().spines['left'].set_bounds(-0.5, 2.5)
plt.gca().spines['left'].set_color('#888888')
plt.gca().yaxis.set_ticks_position('none')
plt.gca().tick_params(color='#888888')
plt.gca().get_xaxis().set_visible(False)

# Write the value to the right of each bars.
for rect, value in zip(plt.gca().patches, data):
    percent = value/total_responses*100
    text = '{} ({: >2.0f})\%'.format(value, percent)
    width = rect.get_width()
    plt.gca().text(rect.get_x() + width + 8 if value > 1 else 7,
                   rect.get_y() + rect.get_height()/2,
                   text, ha='center', va='center', fontsize=10)

plt.savefig('project-sizes.pdf', bbox_inches='tight')
plt.close()
