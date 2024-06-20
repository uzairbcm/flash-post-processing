# flash-post-processing
TV, Mobile, and Physical activity processing and plot codes


## FLASH-TV post-processing 
Preparing the data before running the code
 - Create a folder `post-processed-data` to store results
   - create a folder `input/configs`
 - Create a folder with just participant ID `1234` at the local path, say `datapath`
 - Download the participant data from the server to this folder
   - Copy each device data zip folder format: `P1-1234XYZ_data.zip` where `XYZ` is the device ID. Extract the zip files
 - In each device data folder:
   - Move all the flash-tv txt logs files to a folder named `txts`
   - Edit the power log `P1-1234XYZ_tv_power_5s.csv`; replace the 3 first text lines with - `power;date;time` as column names
 - Prepare the input config file
   - In the folder `post-processed-data/inputs/configs/`, create a `1234.yaml` file
   - This file has a bunch of variables like
     - TV power threshold value
     - setting the power loss timestamps from the notes
     - exclude variable for any device where we decided to exclude the data from a particular TV        

Setting TV power threshold value for each value
 - Two steps to set the value of `power_threshold`
    - Read the threshold from the labeled screenshots obtained from visit 1 of the data collection
    - Plot the TV power consumption data using `code/tv_power.py` by setting values of `file_path; start_date`
       - Infer the threshold from these plots.

Process the logs with `code/run.py`
 - Download redcap rawdata in csv format from the redcap database
 ```
 cd code
 python run.py --base_path datapath --ppt_id 1234 --datacsv redcap_rawdata.csv --output path_to post-processed-data
 ```

Check and verify the summaries
