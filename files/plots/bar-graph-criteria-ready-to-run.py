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

plt.figure(figsize=(4.5, 5.5))

# Data.  We had 69 respondents, but not everyone gave a rating to every
# item in the list.

total_responses = 69

# The columns are the categories, in this order:
#   Essential,
#   Usually of above-average importance
#   Average importance
#   Somewhat or occasionally important
#   Rarely or never important

raw_data = {
     "Availability of specific features"                    : [36, 27, 3, 0, 0],
     "Availability of source code"                          : [9, 22, 12, 15, 9],
     "Support for specific data standards and file formats" : [16, 40, 8, 3, 1],
     "How easy the software is to learn"                    : [12, 22, 22, 11, 2],
     "How easy the software is to extend"                   : [3, 17, 17, 25, 7],
     "How easy the software is to install"                  : [16, 12, 22, 14, 5],
     "Apparent quality of the software"                     : [15, 29, 18, 3, 1],
     "Reputation of the developers"                         : [5, 14, 23, 19, 7],
     "Quality of support for the software"                  : [3, 10, 28, 19, 9],
     "Quality of documentation"                             : [6, 27, 26, 8, 1],
     "Other people's opinions"                              : [4, 11, 29, 20, 3],
     "Speed/performance of the software"                    : [9, 18, 27, 11, 3],
     "Operating system requirements"                        : [30, 17, 14, 6, 1],
     "Hardware compatibility and requirements"              : [17, 16, 19, 10, 7],
     "Similarity to other software you used"                : [1, 7, 22, 28, 10],
     "Programming language(s) used in implementation"       : [1, 14, 14, 25, 14],
     "Software architecture"                                : [4, 5, 15, 25, 19],
     "Security provisions"                                  : [2, 13, 19, 19, 15],
     "Size of software"                                     : [1, 2, 15, 29, 21],
     "Price"                                                : [27, 27, 9, 4, 1],
     "License terms for usage"                              : [17, 23, 13, 9, 4],
     "License terms for source code"                        : [7, 20, 11, 17, 12]
}

x = [0, 10, 20, 30, 40, 50, 60, 70]

# Plot.

# Sort the data by the sum of ratings for "essential" and "above-average".

data = sorted(raw_data.items(), key=lambda x: x[1][0]+x[1][1], reverse=True)

# Create data arrays for what we will hand to barh().

essential = [item[1][0] for item in data]
aboveavg  = [item[1][1] for item in data]
avg       = [item[1][2] for item in data]
somewhat  = [item[1][3] for item in data]
rarely    = [item[1][4] for item in data]

labels    = [item[0] for item in data]

# Barh() puts items in the reverse order of how we put them in the
# lists above, so first we do this to reverse the lists:

labels    = labels[::-1]
essential = essential[::-1]
aboveavg  = aboveavg[::-1]
avg       = avg[::-1]
somewhat  = somewhat[::-1]
rarely    = rarely[::-1]

# Misc. axis setup.

y_pos = np.arange(len(data))
ylim_bottom = -0.5
ylim_top = len(data)-0.5

# Helper functions.

def neg(the_list): return [-value for value in the_list]
def sum(list1, list2): return [x+y for x, y in zip(list1, list2)]

# Let's do this thing.

h_essential = plt.barh(y_pos, essential,
         linewidth=0, align='center', color="#363636")
h_aboveavg = plt.barh(y_pos, aboveavg, left=essential,
         linewidth=0, align='center', color="#666666")
h_avg = plt.barh(y_pos, avg, left=sum(essential, aboveavg),
         linewidth=0, align='center', color="#8b8b8b")
h_somewhat = plt.barh(y_pos, somewhat, left=sum(sum(essential, aboveavg), avg),
         linewidth=0, align='center', color="#b2b2b2")
h_rarely = plt.barh(y_pos, rarely, left=sum(sum(sum(essential, aboveavg), avg), somewhat),
         linewidth=0, align='center', color="#dddddd")

plt.legend([h_essential, h_aboveavg, h_avg, h_somewhat, h_rarely],
           ['Essential',
            'Usually of above-average importance',
            'Average importance',
            'Somewhat or occasionally important',
            'Rarely or never important'],
           fontsize=8, ncol=3, loc='upper center',
           frameon=False, bbox_to_anchor=(0.12, -0.05))

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
plt.gca().xaxis.grid(True, color='#ffffff', linewidth=0.5, linestyle='solid')
plt.gca().yaxis.set_ticks_position('none')
plt.gca().xaxis.set_ticks_position('bottom')

# # Write the value to the right of each bars, except the ones that have value 0.
# for rect, value in zip(plt.gca().patches, data):
#     if value:
#         width = rect.get_width()
#         plt.gca().text(rect.get_x() + width + 1.5, rect.get_y() + rect.get_height()/2, value,
#                 ha='center', va='center', fontsize=9)

# # Write the percentage inside the bars, but only if it's more than 1.
# # (Bars are too short if the value is 1.)
# # This requires a bit of fiddling with positioning.
# for rect, value in zip(plt.gca().patches, data):
#     rect.set_height(rect.get_height()/1.15)
#     rect.set_y(rect.get_y()*1.005)
#     percent = value/total_responses*100
#     text = '{: >2.0f}\%'.format(percent)
#     if value > 1:
#         text_x = rect.get_x() + 0.5
#         text_y = rect.get_y() + rect.get_height()/2.2
#         plt.gca().text(text_x, text_y, text, ha='left', va='center', fontsize=9)

plt.savefig('bar-graph-criteria-ready-to-run.pdf', bbox_inches='tight')
plt.close()




# Stuff saved.

# "blue-gray" colors

# h_essential = plt.barh(y_pos, essential,
#          linewidth=0, align='center', color="#19476a")
# h_aboveavg = plt.barh(y_pos, aboveavg, left=essential,
#          linewidth=0, align='center', color="#3e8685")
# h_avg = plt.barh(y_pos, avg, left=sum(essential, aboveavg),
#          linewidth=0, align='center', color="#7ab790")
# h_somewhat = plt.barh(y_pos, somewhat, left=sum(sum(essential, aboveavg), avg),
#          linewidth=0, align='center', color="#a8dcaa")
# h_rarely = plt.barh(y_pos, rarely, left=sum(sum(sum(essential, aboveavg), avg), somewhat),
#          linewidth=0, align='center', color="#cbf09b")


# .............................................................................
# This next version centers the bars on the average values in the middle.
# But this doesn't make sense for us, because we don't have true negative ratings.

# halfavg=[value/2 for value in avg]

# h_rarely = plt.barh(y_pos, neg(rarely), left=sum(neg(halfavg), neg(somewhat)),
#          linewidth=0, align='center', color="#9fa09d")
# h_somewhat = plt.barh(y_pos, neg(somewhat), left=neg(halfavg),
#          linewidth=0, align='center', color="#d4d3cd")
# h_avg = plt.barh(y_pos, avg, left=neg(halfavg),
#          linewidth=0, align='center', color="#e8ebe6")
# h_aboveavg = plt.barh(y_pos, aboveavg, left=halfavg,
#          linewidth=0, align='center', color="#b3c5cd")
# h_essential = plt.barh(y_pos, essential, left=sum(halfavg, aboveavg),
#          linewidth=0, align='center', color="#6b7b8b")

# Version with "green" colors:
#
# plt.barh(y_pos, neg(rarely), left=sum(neg(halfavg), neg(somewhat)),
#          linewidth=0, align='center', color="#ccf29e")
# plt.barh(y_pos, neg(somewhat), left=neg(halfavg),
#          linewidth=0, align='center', color="#a6dca8")
# plt.barh(y_pos, avg, left=neg(halfavg),
#          linewidth=0, align='center', color="#77be99")
# plt.barh(y_pos, aboveavg, left=halfavg,
#          linewidth=0, align='center', color="#3e8685")
# plt.barh(y_pos, essential, left=sum(halfavg, aboveavg),
#          linewidth=0, align='center', color="#1a486a")
