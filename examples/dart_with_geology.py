from plog import Borehole, Dart, Log
import matplotlib.pyplot as plt
import numpy as np
import sys, os

import matplotlib
matplotlib.rcParams['figure.constrained_layout.use'] = True

plog_file = __file__.replace('dart_with_geology.py', 'dart_endelave_b6.plog')


B6geo = Log.geology(['Torvemuld', 'sand ler', 'gra sand', 'brown sand', 'gra fine sand', 'sand silt ler', 'gra moronler', 'til', 'sand', 'gra sand', 'sand'],
                         [0, 0.3, 0.6, 1.6, 2.3, 4.4, 7.1, 11.1, 15.2, 16, 16.6], [0.3, 0.6, 1.6, 2.3, 4.4, 7.1, 11.1, 15.2, 16, 16.6, 19.6], color='terrain', name='B6')
bh  = Dart.load(plog_file)

fig,axs = plt.subplots(1,6, width_ratios=[0.5, 1, 2, 2, 1, 1], sharey=True)
B6geo.plot(ax=axs[0])
bh.plot(axs=axs[1:])
plt.show()