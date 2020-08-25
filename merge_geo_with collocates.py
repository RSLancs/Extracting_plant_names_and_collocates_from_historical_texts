##python27

from pprint import pprint
import pandas as pd


##..............open manually merged geoparsed results
geo = pd.read_csv('./data/merger_xml_extracted_geoparsed_collocates.csv')
geo = [tuple(x) for x in geo.values] # df to list
print(geo[1])


##..........open collocate results....
collocate = pd.read_csv('./data/INDEXED_no_overlaps-abrev-dups_collocate_results_15.01.19.csv')
collocate = [tuple(x) for x in collocate.values] # df to list
print(collocate[1])


#............merge results........................

merged = []
for ig in geo:
	for ic in collocate:
		if ig[0] == ic[0]:
			merged.append([ic[0],ic[2],ic[3],ic[4],ic[5],ic[6],ic[7],ig[0],ig[3],ig[5],ig[6]])

my_df = pd.DataFrame(merged) # transform result list to dataframe

my_df.columns = ['para_index',
					'text',
					'year',
					'spc_acc',
					'spc_syn',
					'find_index',
					'window',  
					'geo_para_index',
					'standoff_loc_word',
					'lat',
					'lon' ] # add column labels

a = my_df.to_csv('./data/geo_locations_collocate_merger.csv')