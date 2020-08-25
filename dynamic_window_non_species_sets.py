## python 27

import re
from pprint import pprint
import pandas as pd
import glob



#......................open compiled nested species list from file.................

with open('./data/species_list_with_abbreviations-unique.txt', 'r') as f: 
	species_list = f.read().split('\n')
#pprint(species_list)


files_in_folder_list = glob.glob('./corpus/*.txt') # collect files in directory


#................open and format text file...............................

def open_single_file_read(file): #read text
	"""
	function to pre=process corpus
	"""
	with open(file, 'r') as f:
		raw_data = f.read() # read and lower text
		new_data=re.sub(r'[^\x00-\x7f]',r'', raw_data)# remove unicode
		processed_text=re.sub(r'\s\.',r'.', new_data)# remove space before '.'  if there is one
		word_join1 = re.sub(r'-\s+\n+(\w+ *)', r'\1\n', processed_text)# join words split over 2 lines
		word_join2 = re.sub(r'-\n+(\w+ *)', r'\1\n', word_join1)# join words split over 2 lines
		word_join3 = re.sub(r'\n\n\n+',r'\n\n', word_join2)# remove excessive new lines
			
	return word_join3


#.......search corpus and create find window.....................

def look_for_match_in_folder(list_of_files_in_folder):
	"""
	function to find plant names across corpus from plant search list
	"""
	finds =[]
	find_index = []
	
	for index_1, file_name in enumerate(list_of_files_in_folder, start=1): # Open each text in turn from folder
		print(file_name)

		text = open_single_file_read(file_name) # collect and format text
		
		year = file_name[2:6] # collect the year the text was published
		
		for species in species_list: #iterate over species list
			if species != '' and species != ' ':			
				
				pro_species =re.sub(r'\.',r'\.', species) # escape the re '.' for an actual '.'
				re_species = re.compile(r'\b%s\b' % pro_species,re.I) #compile species into regex to keep word boundaries
								
				find_locations = [m.start() for m in re.finditer(re_species, text)] # find all exact matches in text
					
				[find_index.append([i,str(species)]) for i in find_locations]# update species finds for text

				
		find_index.sort(key=lambda x: x[0])# order list based on index to allow dynamic window extraction
		#print find_index

		just_index = [a[0] for a in find_index] # get just find index to split text
		#print just_index

		parts = [text[i:j] for i,j in zip(just_index, just_index[1:]+[None])]# split text on find index
		#pprint(parts)

		parts_zip = [[fd[0], fd[1], p] for fd, p in zip(find_index , parts)] # rejoin split text with species finds
		#pprint(parts_zip)

 		# form dynamic collocate window and write window and metadata to list
		for i in parts_zip:
			#print i
 			if len(i[2]) >= 500: # if window is over 500 cut window down to 500
 				finds.append([file_name, #text title
							year, # publication date
 							i[1], # for species find
 							str(index_1)+ '.' + str(i[0]), # index of find
 							i[2][:500]]) # max 150 if no other species in that window

 			else: # if window is under 500 already save window
 				finds.append([file_name, #text title
							year, # publication date
 							i[1], # species find
 							str(index_1)+ '.' + str(i[0]), # index of find
 							i[2]]) # max 150 if no other species in that window
		
		find_index = [] # reset species match for next text file
	
 		
 	return finds
			
matches = look_for_match_in_folder(files_in_folder_list)

#pprint(matches)


# # # #.....................transform results to dataframe and write to CSV...................

# my_df = pd.DataFrame(matches) # transform result list to dataframe

# my_df.columns = ['text','year','spc_acc','index','window',] # add column labels

# # write Raw output to CSV file 
# my_df.to_csv('./data/raw_collocate_results_15.01.19.csv', index=True, header=True)

