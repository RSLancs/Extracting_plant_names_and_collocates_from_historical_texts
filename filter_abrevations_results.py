## python

import pandas as pd
from pprint import pprint


###########################################################
##...........load in my csv results file............................


my_df = pd.read_csv('./data/no_overlaps_collocate_results_15.01.19.csv') # load only accepted species matches

collocate_results = [list(x) for x in my_df.values]
pprint(collocate_results[1])


##......................open compiled nested species list from file.................

df = pd.read_csv('./data/FULL_API_LIST-striped.csv', header=None) # read in nested species list as DF

df = df.fillna('') # remove 'nan' 

tups = [list(x) for x in df.values]# transform dataframe to nested list

unique_nested_species_list = [filter(None, sets) for sets in tups]# remove duplicates WITHIN each nest

print(unique_nested_species_list[2])



# ##...................filter out abbreviated species.......................................

filtered = []
removed = []
for i in collocate_results:
	#print i
	for species_set in unique_nested_species_list: # species set
		for find_species in species_set: # species within each set
		
			if str(i[3]) == str(find_species):
				#print(i[3], '   -     match')
				filtered.append([i[1], #text title
								i[2], # publication date
	 							species_set[0], # accepted name for species find
								i[3], # species found in corpus
	 							i[4], # index of find
	 							i[5]]) 


###.................write filtered results to file................
my_df1 = pd.DataFrame(filtered) # transform result list to dataframe

my_df1.columns = ['text','year','spc_acc','spc_syn','index','window',] # add column labels

# write Raw output to CSV file 
my_df1.to_csv('./data/no_overlaps-abrev_collocate_results_15.01.19.csv', index=True, header=True)




