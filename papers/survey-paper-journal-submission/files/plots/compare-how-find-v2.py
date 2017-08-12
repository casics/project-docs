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

plt.figure(figsize=(3, 4))

# Data.

total_ready_responses = 56         # Total who also said they're s/w developers.
total_src_responses = 55           # Total -- thes are already s/w devs.

# Choices were not mutually exclusive.

# Col 1 = total for finding ready-to-run
# Col 2 = total for finding sw

raw_data = {
    "Ask colleagues for opinions/suggestions"                                                          : [45, 29],
    "Ask or search mailing lists or discussion\ngroups within your organization"                       : [ 4,  7],
    "Ask or search public mailing\nlists or discussion groups"                                         : [12, 17],
    "Ask or search social help sites (e.g., \nStackOverflow, Quora, etc.)"                             : [25, 20],
    "Ask or search social media (e.g., Twitter,\nFacebook, LinkedIn, etc.)"                            : [7,   5],
    "Look in the scientific literature to find \nwhat authors use in similar contexts"                 : [34, 25],
    "Search in public software project repositories\n(SourceForge, GitHub, BitBucket, etc.)"           : [21, 25],
    "Search in topical software indexes/catalogs\n(e.g., ASCL.net, BioPortal, Alternative.to, etc.)"   : [ 7, 12],
    "Search the web using general-purpose search\nsystems (e.g., Google, Yahoo, Bing, DuckDuckGo)"     : [52, 50],
    "Other"                                                                                            : [ 3,  4],
}

x = [0, 10, 20, 30, 40, 50, 60]

# Sort the data by value, largest value first.

data   = sorted(raw_data.items(), key=lambda x: x[1][0], reverse=True)

# Create data arrays for what we will hand to barh().
# This time, we create percentages.

ready  = [(item[1][0]/total_ready_responses)*100 for item in data]
src    = [(item[1][1]/total_src_responses)*100 for item in data]
labels = [item[0] for item in data]

# Barh() puts items in the reverse order of how we put them in the
# lists above, so first we do this to reverse the lists:

ready  = ready[::-1]
src    = src[::-1]
labels = labels[::-1]

# Misc. axis setup.

y_pos = np.arange(len(data))
ylim_bottom = -0.5
ylim_top = len(data)-0.5

# Plot.
# Version with two side-by-side plots, using percentages.

f, (ax1, ax2) = plt.subplots(1, 2, sharey=True, figsize=(5, 4.2))
h_ready = ax1.barh(y_pos, ready, height=0.8, linewidth=0, align='center', color="#cccccc")
h_src = ax2.barh(y_pos, src, height=0.8, linewidth=0, align='center', color="#cccccc")

plt.subplots_adjust(wspace=0.25, right=0.75)

plt.yticks(y_pos, labels, fontsize=10, color=textcolor)
plt.yticks(y_pos, labels, fontsize=10, color=textcolor)
plt.xticks(x, fontsize=10)
plt.ylim([ylim_bottom, ylim_top])

# Remove the plot frame lines leaving only the left vertical one.
for spine in ['top', 'bottom', 'right']:
    for ax in [ax1, ax2]:
        ax.spines[spine].set_visible(False)
        ax.spines['left'].set_bounds(ylim_bottom, ylim_top)
        ax.spines['left'].set_color('#888888')
        ax.tick_params(color='#888888')
        ax.yaxis.set_ticks_position('none')
        ax.get_xaxis().set_visible(False)

# Write the value to the right of each bars.
for rect, value in zip(h_ready.patches, ready):
    text = '{: >2.0f}\%'.format(value)
    width = rect.get_width()
    offset = 12 if value > 5 else 10
    if value > 0:
        ax1.text(rect.get_x() + width + offset,
                 rect.get_y() + rect.get_height()/2.2,
                 text, ha='center', va='center', fontsize=10, color=textcolor)

for rect, value in zip(h_src.patches, src):
    percent = value/total_src_responses*100
    text = '{: >2.0f}\%'.format(value)
    width = rect.get_width()
    offset = 12 if value > 5 else 10
    if value > 0:
        ax2.text(rect.get_x() + width + offset,
                 rect.get_y() + rect.get_height()/2.2,
                 text, ha='center', va='center', fontsize=10, color=textcolor)

# Put some text above the plots
plt.gca().text(1.05, 1.01,
               'Ready-to-run software',
               horizontalalignment='right',
               transform=ax1.transAxes,
               color=textcolor)
plt.gca().text(.83, 1.01,
               'Source code',
               horizontalalignment='right',
               transform=ax2.transAxes,
               color=textcolor)


plt.savefig('compare-how-find-v2.pdf', bbox_inches='tight')
plt.close()
