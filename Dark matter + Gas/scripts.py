import yt.mods
from matplotlib import use; use('Agg')
from yt.mods import *
import pylab as plt

### define problem name
problem_name = 'dm_hydro'

### define simulation output directory and filename base
output_dir_base = 'RD'
datafile_base = 'RedshiftOutput'

### define output to be plotted
dumpid = '0001'

### construct input filename
filename = './' + output_dir_base + dumpid + '/' + datafile_base + dumpid
print("Plotting output file %s\n" % filename)

### some more filenames
png_filename = './' + problem_name + '.png'

### load data
pf = yt.load(filename)




### define fields vector
fields = ('Density')
logme = (True)

count = 0
for f in fields:
    plt.subplot(1,1,1)
plt.savefig(png_filename)
