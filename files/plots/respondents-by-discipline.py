#!/usr/bin/env python3.4

import pdb
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

plt.rcParams.update({
    'text.usetex': True,
    'text.latex.preamble': [
        r"\usepackage{fourier}",
        r"\usepackage[T1]{fontenc}",
    ]
})

font = {'family' : 'serif',
        'serif'  : 'Utopia',
        'size'   : 9
}
matplotlib.rc('text', usetex=True)
matplotlib.rc('font', **font)

plt.figure(figsize=(3.75, 2.25))
ax = plt.subplot(111)
ax = plt.gca()
ax.tick_params(width=1, length=3, color='#888888')

# Data.
total_responses = 69
labels = ["``Aerospace Engineering (Robotics)''",
          "Social Sciences",
          "Cognitive and Brain Sciences",
          "Geological and Planetary Sciences",
          "Chemical and Chemical Engineering",
          "Biology and Biological Engineering",
          "Computing and Mathematical Sciences",
          "Physical Sciences",
]

# About the data: in the category of "other", we had the following responses:
#
# - One person answered thus: Computing & Math Sci. (CMS), "astrophysics",
#   "IT".  I added 1 to the count of physical sciences (the rationale being
#   that astrophysics is a physical science) but didn't change the count of
#   CMS because IT can be considered part of CMS at our level of granularity.
#
# - One person answered CMS, and "Pri. A&A" and "Cosmology".  I added 1 more
#   to physical sciences for the A&A and cosmology (because they did not also
#   select Physical Sciences, so this is a case where the count needs to be
#   adjusted).
#
# - One person answered "Data science" but not also CMS, so I added 1 to CMS.
#
# - Two people answered "Astronomy" for "other" as well as answering
#   "physical sciences".  We would lump astronomy under physical sciences, so
#   it does not change the count for physical sciences.
#
# - One person answered "Aerospace Engineering (Robotics)".  I don't know
#   where to put that one, so left it as a real "Other".

data = [1, 0, 0, 2, 2, 19, 32, 39]
y_pos = np.arange(len(data))
x = [0, 10, 20, 30, 40]

plt.barh(y_pos, data, linewidth=0, align='center', color="#cccccc")
plt.yticks(y_pos, labels)

# Styling.

# Remove the plot frame lines leaving only the left vertical one.
ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["right"].set_visible(False)

ax.spines['left'].set_bounds(-0.5, 7.5)
ax.spines['left'].set_color('#888888')

ax.text(1.1, 0.07,
        'Total individual responses: {}.\nMultiple selections allowed.'.format(total_responses),
        horizontalalignment='right',
        transform=ax.transAxes)

ax.get_xaxis().set_visible(False)
ax.get_yaxis().tick_left()
plt.tick_params(
    axis='y',                       # changes apply to the x-axis
    which='both',                   # both major and minor ticks are affected
    left='off',                     # ticks along the top edge are off
    right='off')                    # ticks along the top edge are off

# Write the value to the right of each bars, except the ones that have value 0.
for rect, value in zip(ax.patches, data):
    width = rect.get_width()
    x_pos = (rect.get_x() + width + 3 if value else 2.5)
    y_pos = rect.get_y() + rect.get_height()/2
    percent = value/total_responses*100
    text = '{} ({: >2.0f})\%'.format(value, percent)
    ax.text(x_pos, y_pos, text, ha='center', va='center', fontsize=8)

plt.savefig('respondents-by-discipline.pdf', bbox_inches='tight')
plt.close()
