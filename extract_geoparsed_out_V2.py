#from lxml import objectify
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import tostring
from pprint import pprint
import pandas as pd

#.............import xml geoparsed results 
tree = ET.parse('./data/col_trd_wght_2.out.xml')
tree = tree.getroot() # get root of xml tag structure
str_tree = tostring(tree) # convert to string


#############################################
##.......find max paragraph index....

index =[] 
for text in tree.iter('text'):
        print(text.tag)
        for e, para in enumerate(text, 15292): # set index to allow geoparsing outputs to be merged
          index.append(e)
                
print(index) # print out number of paragraph chunks in xml file


#######################################
##..... collect paragraph number and word id's....

parag = []
for text in tree.iter('text'):
        print(text.tag)
        for e, para in enumerate(text, 15292): # set index to allow geoparsing outputs to be merged
                #print(e, para.tag, para.attrib)
                for sen in para:
                        #print(e, sen.text, sen.attrib)
                        for word in sen:
                                #para.append([e, word.text, word.attrib['id']])

                                #print(e, word.text, word.attrib['id'])
                                try:
                                        parag.append([e, word.text, word.attrib['id']])
                                except:
                                        KeyError
                                

#############################################

loc = []
for stand in tree.iter('standoff'):
        #print(stand.tag)
        for ents_node in stand:
                #print(ents_node.tag, ents_node.attrib)
                if ents_node.attrib['source'] == 'ner-rb':
                        for ent_node in ents_node:
                                #print(ent_node.tag, ent_node.attrib)   
                                if ent_node.attrib['type'] == 'location':
                                        for parts in ent_node:
                                           for part in parts:
                                              #print(part.tag, part.attrib)
                                              #print(ent_node.attrib['lat'],ent_node.attrib['long'],part.attrib['ew'], part.text)

                                              try:
                                                 loc.append([ent_node.attrib['lat'],ent_node.attrib['long'],part.attrib['ew'], part.text])
                                              except:
                                                        TypeError
 

##########################################
##............write out..................

merges = []
for pi in parag:
    for li in loc:
        if pi[2] == li[2]:
            merges.append([pi[0], pi[1], pi[2], li[3], li[2], li[0], li[1]])


my_df = pd.DataFrame(merges) # transform result list to dataframe

# my_df.columns = ['para_index','text_word','text_word_id','standoff_word','standoff_word_id','lat','lon' ] # add column labels

# # write Raw output to CSV file 
# my_df.to_csv('./data/location_xml_extraction_third.csv', index=False, header=True)












