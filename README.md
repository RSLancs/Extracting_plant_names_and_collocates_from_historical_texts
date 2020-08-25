# Extracting_plant_names_and_collocates_from_historical_texts

The scripts in this project allow for a plant name list, which includes historical synonyms, to be searched across a corpus of historical text and for a dynamic collocate window of text around each match to be extracted. Guidance is also provided on using the Edinburgh Geoparser to search the extracted collocates to identify place names and assign x,y, coordinates. 


All input and output files are within folder [./data/](./data/). The historical corpus used is contained within [./corpus/](./corpus/) and a full list of texts in the corpus can be found [here](./scripts/corpus/corpus_list.md) and with links [here](./scripts/corpus/corpus_meta.csv).


## Install

To run the python scripts first download the scripts and the [./corpus/](./corpus/) and [./data/](./data/) folders. Install python 2.7 and use `pip install -r requirements.txt`. 


## Extracting collocates

To use the plant name search list to extract collocates from the corpus first run [Add_abbreviations_to_unique_species_list.py](./Add_abbreviations_to_unique_species_list.py). This takes the plant name search list and add abbreviation forms - for example for Viola tricolor the abbreviation form V. tricolour is added to the search list. 

The next script [dynamic_window_non_species_sets.py](./dynamic_window_non_species_sets.py) uses the search list with abbreviations to search the historical corpus and returns a .csv file with all match instances and collocate windows.

The following script [filter_overlapping_results.py](./filter_overlapping_results.py) removes overlapping results keeping the longest species name. For example, in the sentence 'The plant was found by J. B. Rapa oblonga in the Lake District,` both B. Rapa (Beta rapa) and Rapa oblonga could be matched as a plant name, however as they overlap only the latter would be retained. 

The script [filter_abbreviations_results.py](./filter_abbreviations_results.py) then filters out all plant name abbreviation plant name matches under. These were used to help form a dynamic collocate window. The output is written out as a .csv


## Geoparsing the collocates 

To geoparse the collocates, download and install the Edinburgh Geoparser by following the instructions at https://www.ltg.ed.ac.uk/software/geoparser/ (note the geoparser can be used with an Ordinance Survey Gazetteer and only runs in linux). This step identifies place names found within each collocate chunk and provides geographical coordinates.

To use the Edinburgh Geoparser the collocate .csv file needs to be transformed into the correct format manually. All columns except 'window' were deleted. The file was then imported into notepad++ and &, <, and > was replaced with the `.xml` escape characters of &amp;, &lt; and &gt;. The file was then saved and re-opened in excel where each collocate was wrapped in a <p></p> tag. This was then saved and copied and pasted into notepad (as a double check that no non-utf-8 characters remained in the file) and then finally in notepad++ all collocates were wrapped in tags:


        <?xml version="1.0" encoding="UTF-8"?>
        <document>
            <text>
                <!-- all collocates wrapped in <p></p> tags -->
            </text>
        </document>

Depending on memory available the collocate results might have to be split up and run in batches as was done here. 

The geoparserr will output a number of files including a *out.xml file. To extract the geoparsed output and re-merge with the collocate results file, run scripts [extract_geoparsed_out_V2.py](./extract_geoparsed_out_V2.py) and [merge_geo_with_collocates.py](./merge_geo_with_collocates.py). This will extract the place names and x,y coordinates identified in each collocate and merges the results (if the geoparser was run in batches the starting paragraph index will need to be set manually to allow or merger with collocate file) with the collocate file. The output .csv file can then be plotted using GIS software. 

Finally the script [filter_Just_accepted.py](./filter_Just_accepted.py) will allow for plant name matches mated under the modern accepted name to be extracted and written out as a separate .csv file which allows for comparison with plant names matched under their synonym names. 



