# flash-post-processing
tv, mobile and physical activity processing and plot codes


## FLASH-TV post-processing 
Preparing the data before running the code
 - Create a folder `post-processed-data` to store results
   - create a folder `input/configs`
 - Create a folder with just participant ID `1234` at the local path say `datapath`
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
     - exclude variable for any we decided to exclude the data from a particular TV
  
TV power threshold

Process the logs with `run.py`

Check and verify the summaries
