#!/usr/bin/env python3.4

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib import rcParams

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

plt.figure(figsize=(4.25, 5.5))

# Data.  Not everyone answered the question.
total_responses = 69
total_swdevs    = 56
total_notswdevs = 13

# Here are the values of "Other" that people provided:
#   search macports or similar package repositories
#   search the Debian archive
#   package manager (e.g. homebrew on OSX)
#   Never search internet first
# The last one is obviously stupid, so ignore it.  The other 3 are actually
# an unanticipated category.

# Columns:
#   1. Total
#   2. Answered "Yes" to "Are you involved in software development?"
#   3. Answered "No"

raw_data = {
    "Search the web using general-purpose search\nsystems (e.g., Google, Yahoo, Bing, DuckDuckGo)"   : [62, 52, 10],
    "Ask colleagues for opinions"                                                                    : [57, 45, 12],
    "Look in the scientific literature to find \nwhat authors use in similar contexts"               : [43, 34, 9],
    "Ask or search social help sites (e.g., \nStackOverflow, Quora, etc.)"                           : [27, 25, 2],
    "Use whatever is determined by my organization\nor work group's guidelines or practices"         : [22, 17, 5],
    "Search in public software project repositories\n(SourceForge, GitHub, BitBucket, etc.)"         : [22, 21, 1],
    "Ask or search public mailing\nlists or discussion groups"                                       : [15, 12, 3],
    "Ask or search social media (e.g., Twitter,\nFacebook, LinkedIn, etc.)"                          : [10, 7, 3],
    "Search in topical software indexes/catalogs\n(e.g., ASCL.net, BioPortal, Alternative.to, etc.)" : [7, 7, 0],
    "Ask or search mailing lists or discussion\ngroups within your organization"                     : [4, 4, 0],
    "Other"                                                                                          : [3, 3, 0],
}

x = [0, 10, 20, 30, 40, 50, 60, 70]

# Sort the data by the total.

data = sorted(raw_data.items(), key=lambda x: x[1][0], reverse=True)

# Create data arrays for what we will hand to barh().

total     = [item[1][0] for item in data]
swdevs    = [item[1][1] for item in data]
notswdevs = [item[1][2] for item in data]

labels    = [item[0] for item in data]

# Barh() puts items in the reverse order of how we put them in the
# lists above, so first we do this to reverse the lists:

labels    = labels[::-1]
total     = total[::-1]
swdevs    = swdevs[::-1]
notswdevs = notswdevs[::-1]

# Misc. axis setup.

y_pos = np.arange(len(data))
ylim_bottom = -0.5
ylim_top = len(data)-0.5

# Plot.
# These are percentages by total responses for each subgroup.

h_swdevs = plt.barh(y_pos + 0.2, [x/total_swdevs*100 for x in swdevs],
                    height=0.35, linewidth=0, align='center', color="#afafaf")
h_notswdevs = plt.barh(y_pos - 0.2, [x/total_notswdevs*100 for x in notswdevs],
                       height=0.35, linewidth=0, align='center', color="#dddddd")

plt.yticks(y_pos, labels, fontsize=10, color=textcolor)
plt.xticks(x, fontsize=10, color=textcolor)
plt.ylim([ylim_bottom, ylim_top])

plt.legend([h_swdevs, h_notswdevs],
           ['Involved in software dev. (n = {})'.format(total_swdevs),
            'Not involved in software dev. (n = {})'.format(total_notswdevs)],
           fontsize=9, ncol=1, loc='upper center',
           frameon=False, bbox_to_anchor=(0.695, 0.1))

# plt.gca().text(0.9, 0.25,
#                'Total individual responses: {}\nMultiple selections allowed.'.format(total_responses),
#                horizontalalignment='right',
#                transform=plt.gca().transAxes, fontsize=9)

# Remove the plot frame lines leaving only the left vertical one.
for spine in ['top', 'bottom', 'right']:
    plt.gca().spines[spine].set_visible(False)
plt.gca().spines['left'].set_bounds(ylim_bottom, ylim_top)
plt.gca().spines['left'].set_color('#888888')
plt.gca().tick_params(color='#888888')
plt.gca().yaxis.set_ticks_position('none')
plt.gca().get_xaxis().set_visible(False)

# Write the value to the right of each bars.
for rect, value in zip(h_swdevs.patches, swdevs):
    percent = value/total_swdevs*100
    width = rect.get_width()
    offset = 9 if value > 5 else 8
    if value > 0:
        text = '{} ({: >2.0f}\%)'.format(value, percent)
    else:
        offset = 1
        text = '0'
    plt.gca().text(rect.get_x() + width + offset,
                   rect.get_y() + rect.get_height()/2.2,
                   text, ha='center', va='center', fontsize=10, color=textcolor)

for rect, value in zip(h_notswdevs.patches, notswdevs):
    percent = value/total_notswdevs*100
    width = rect.get_width()
    offset = 9 if value > 5 else 8
    if value > 0:
        text = '{} ({: >2.0f}\%)'.format(value, percent)
    else:
        offset = 3
        text = '0'
    plt.gca().text(rect.get_x() + width + offset,
                   rect.get_y() + rect.get_height()/2.2,
                   text, ha='center', va='center', fontsize=10, color=textcolor)

plt.savefig('how-find-ready-to-run-v4.pdf', bbox_inches='tight')
plt.close()
