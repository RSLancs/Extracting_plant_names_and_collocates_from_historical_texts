## Python 27

from pprint import pprint
import pandas as pd


#..............load csv to remove duplicates..................
df = pd.read_csv('./data/no_overlaps-abrev_collocate_results_15.01.19.csv') # read in Gazetteer


species_finds = [list(x) for x in df.values]# transform dataframe to nested list

pprint(species_finds[0])
# pprint(NBN_species_find_windows[0][7])


##.............open acc-syn dups...............
with open('./data/Accepted_names_also_listed_as_synonyms.txt', 'r') as f: 
	acc_to_syn_dups = f.read().split('\n')


##.................syn-syn dups........................
with open('./data/synonym duplicates.txt', 'r') as f: 
	syn_to_syn_dups = f.read().split('\n')


##.........remove finds with duplicate root plant names
collocates_without_dups = []

for i in species_finds:
	if i[4] not in acc_to_syn_dups and i[4] not in syn_to_syn_dups:
		collocates_without_dups.append(i)
	else:
		print i[4]

# print(len(species_finds),len(collocates_without_dups))
# #print(dups2)


##..........write results out................
my_df1 = pd.DataFrame(collocates_without_dups)

my_df1.columns = ['result_No.','text','year','spc_acc','spc_syn','find_index','window']

my_df1.to_csv('./data/no_overlaps-abrev-dups_collocate_results_15.01.19.csv', index=False, header=True)

