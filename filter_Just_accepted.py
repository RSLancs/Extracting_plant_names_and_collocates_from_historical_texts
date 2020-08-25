## python27

from pprint import pprint
import pandas as pd



#.........find results that are just accepted species names..........

df1 = pd.read_csv('./data/geo_locations_collocate_merger.csv') # load geoparsed collocate results

df2 = df1[df1['spc_syn'] == df1['spc_acc']] # remove results that were found under a synonym

df2.to_csv('./data/ACCEPTED_geo_locations_collocate_merger.csv', index=False, header=True) # write out results 

