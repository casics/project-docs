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

plt.figure(figsize=(2.75, 5.5))

# Data.

total_responses = 55

# Choices were not mutually exclusive.

# There were 4 other write-in answers:
# - "What libraries are used by other software that I like"
# - "Netlib"
# - "Look at the web page for that software!"
# - "O'Reilly books"
#
# For analysis purposes, I think Netlib should be considered in the same
# category as ascl.net and others, so I added 1 to the count below.

raw_data = {
    "Ask colleagues for suggestions"                                                                                     : 29,
    "Ask or search mailing lists or discussion\ngroups within to your organization"                                      : 7,
    "Ask or search public mailing lists or discussion groups"                                                            : 17,
    "Look in the scientific literature to\nfind what authors use in similar contexts"                                    : 25,
    "Ask or search social media (e.g.,\nTwitter, Facebook, LinkedIn, etc.)"                                              : 5,
    "Ask or search social help sites\n(e.g., StackOverflow, Quora, etc.)"                                                : 20,
    "Search the web using specialized code search engines\n(e.g., OpenHUB, Google Code, Krugle, Snipplr, Smipple, etc.)" : 10,
    "Search the web using general-purpose search\nsystems (e.g., Google, Yahoo, Bing, DuckDuckGo)"                       : 50,
    "Search in public software project repositories\n(SourceForge, GitHub, BitBucket, etc.)"                             : 25,
    "Search in specialized software indexes/catalogs\n(e.g., ASCL.net, SBML Software Guide, BioPortal, etc.)"            : 13,
    "Search in my organization's code\ncollection or repository (if any)"                                                : 12,
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

plt.yticks(y_pos, labels, fontsize=10)
plt.ylim([ylim_bottom, ylim_top])

plt.gca().text(1.175, 0.01,
               'Total individual responses: {}\nMultiple selections allowed'.format(total_responses),
               horizontalalignment='right',
               transform=plt.gca().transAxes, color=textcolor)

# plt.title('\emph{Responses to the question "What are some approaches you have\n\emph{used to look for source code in the past?"}',
#           fontsize=10, y=1.03, x=-0.1)

# Remove the plot frame lines leaving only the left vertical one.

for spine in ['top', 'bottom', 'right']:
    plt.gca().spines[spine].set_visible(False)
plt.gca().spines['left'].set_bounds(ylim_bottom, ylim_top)
plt.gca().spines['left'].set_color('#888888')
plt.gca().tick_params(color='#888888')
plt.gca().yaxis.set_ticks_position('none')
plt.gca().get_xaxis().set_visible(False)

# Write the value to the right of each bars.
for rect, value in zip(plt.gca().patches, values):
    percent = value/total_responses*100
    text = '{} ({: >2.0f}\%)'.format(value, percent)
    width = rect.get_width()
    offset = 7 if value > 7 else 6
    plt.gca().text(rect.get_x() + width + offset,
                   rect.get_y() + rect.get_height()/2,
                   text, ha='center', va='center', fontsize=10, color=textcolor)

plt.savefig('how-find-src.pdf', bbox_inches='tight')
plt.close()
