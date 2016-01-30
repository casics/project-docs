#!/usr/bin/env python3.4

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib import rcParams
import operator

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

plt.figure(figsize=(3.75, 4.5))

# Data.

total_responses = 55

# Choices were not mutually exclusive.

raw_data = {
    "Ask colleagues for suggestions"                                                                                     : 29,
    "Ask or search mailing lists or discussion\ngroups within to your organization"                                       : 7,
    "Ask or search public mailing lists or discussion groups"                                                            : 17,
    "Look in the scientific literature to\nfind what authors use in similar contexts"                                     : 25,
    "Ask or search social media (e.g.,\nTwitter, Facebook, LinkedIn, etc.)"                                               : 5,
    "Ask or search social help sites\n(e.g., StackOverflow, Quora, etc.)"                                                 : 20,
    "Search the web using specialized code search engines\n(e.g., OpenHUB, Google Code, Krugle, Snipplr, Smipple, etc.)" : 10,
    "Search the web using general-purpose search\nsystems (e.g., Google, Yahoo, Bing, DuckDuckGo)"                        : 50,
    "Search in public software project repositories\n(SourceForge, GitHub, BitBucket, etc.)"                              : 25,
    "Search in specialized software indexes/catalogs\n(e.g., ASCL.net, SBML Software Guide, BioPortal, etc.)"             : 12,
    "Search in my organization's code\ncollection or repository (if any)"                                                 : 12,
    "Other" : 4,
}

x = [0, 10, 20, 30, 40, 50]

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

plt.yticks(y_pos, labels, fontsize=9)
plt.xticks(x, fontsize=9)
plt.ylim([ylim_bottom, ylim_top])

# Remove the plot frame lines leaving only the left vertical one.

for spine in ['top', 'bottom', 'right']:
    plt.gca().spines[spine].set_visible(False)
plt.gca().spines['left'].set_bounds(ylim_bottom, ylim_top)
plt.gca().spines['left'].set_color('#888888')

# Get rid of excess lines and make grid lines lighter in color.

plt.gca().tick_params(color='#888888')
plt.gca().xaxis.grid(True, color='#ffffff', linewidth=1, linestyle='solid')
plt.gca().yaxis.set_ticks_position('none')
plt.gca().xaxis.set_ticks_position('bottom')

# Write the value to the right of each bars, except the ones that have value 0.
for rect, value in zip(plt.gca().patches, values):
    if value:
        width = rect.get_width()
        plt.gca().text(rect.get_x() + width + 1.5, rect.get_y() + rect.get_height()/2, value,
                ha='center', va='center', fontsize=9)

# Write the percentage inside the bars, but only if it's more than 1.
# (Bars are too short if the value is 1.)
# This requires a bit of fiddling with positioning.
for rect, value in zip(plt.gca().patches, values):
    rect.set_height(rect.get_height()/1.1)
    rect.set_y(rect.get_y()*1.001)
    percent = value/total_responses*100
    text = '{: >2.0f}\%'.format(percent)
    if value > 2:
        new_x = rect.get_x() + 0.5
        new_y = rect.get_y() + rect.get_height()/2.2
        plt.gca().text(new_x, new_y, text, ha='left', va='center', fontsize=9)

plt.savefig('how-find-src.pdf', bbox_inches='tight')
