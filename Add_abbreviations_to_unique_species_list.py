## python27
from pprint import pprint
import pandas as pd


##............load in rooted plant search list...............
df = pd.read_csv('./data/FULL_API_LIST-striped.csv', header=None) # read in nested species list as DF

df = df.fillna('') 

tups = [list(x) for x in df.values]# transform dataframe to nested list

na_filter = [filter(None, sets) for sets in tups]

flatten_species_list = [item for sublist in na_filter for item in sublist]# flatted species list

unique_species_list = set(item.strip() for item in flatten_species_list)#remove duplicates and unicode
#pprint(unique_species_list)


# create abbreviated synonyms - eg. Viola tricolor becomes V. tricolor
species_list_with_abbreviations = []

for i in unique_species_list:
	if i != '' and i != ' ':
		ext = i[0] + '.'
		ext2 = i.split()
		ext3 = ext2[1]	
		ext4 = ext + " " + ext3		
		species_list_with_abbreviations.append(i)
		species_list_with_abbreviations.append(ext4)
								
#pprint(species_list_with_abbreviations)

unique_abbreviations = set(species_list_with_abbreviations)# get all unique plant names
#pprint(species_list_with_abbreviations)

print(len(species_list_with_abbreviations),len(unique_abbreviations))


##############################################################
###................write new list to file..........

thefile = open('./data/species_list_with_abbreviations-unique.txt', 'w')

for item in unique_abbreviations:
 		thefile.write("%s\n" % item)




