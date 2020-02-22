import pickle
from getPeriod import *

# load data
# data can be in any form as long as it is an array [x,y,yerr].
in_file = open('sample_data.dat','rb')
data = pickle.load(in_file)
in_file.close()

# clean up the data and run analysis
star_idx = 0 # pick a star
data_noNaN = get_noNaN(data)
vstars = period_analysis([data_noNaN[star_idx]],5,show_plot=True)
