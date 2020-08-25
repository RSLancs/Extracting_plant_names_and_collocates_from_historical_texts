##Python27

from pprint import pprint
import pandas as pd



df2 = pd.read_csv('./data/raw_collocate_results_15.01.19.csv')

#pprint(df2[0:4])

# remove loverlapping location matches - keep longest match
my_df2 = df2.groupby('index', as_index=False).apply(lambda x: x[x.spc_acc.str.len() == x.spc_acc.str.len().max()])

#.....write final output to file with overlapping locations removed 
my_df2.to_csv('./data/no_overlaps_collocate_results_15.01.19.csv', index=False, header=True)
