------ TV data -------
Contains TV viewing data from 10 days listed by day

####### FILENAMES Explanation #######
filename: 4 digit participant id + 3 digit device id + date

filename: 1147006_2023-11-10.csv
    1147 is participant ID
    006 is 1st FLASH-TV device ID
    Date is YYYY-MM-DD format

filename: 1147011_2023-11-10.csv
    1147 is participant ID
    011 is 2nd FLASH-TV device ID
    Date is YYYY-MM-DD format

####### CSV FILE CONTENTS #######
Three columns containing - dateTimeStamp,TC_gaze,TC_exposure_only

dateTimeStamp labels:
    contains datetimestamps in 5-second intervals
    
    2023-11-11 00:00:00
    2023-11-11 00:00:05
    2023-11-11 00:00:10
    2023-11-11 00:00:15
    2023-11-11 00:00:20
    2023-11-11 00:00:25


TC_gaze labels explanation:
    0: No-gaze with TV-ON
    1: Gaze with TV-ON
    2: FLASH-TV device is rebooting/restarting
    3: FLASH-TV device is powered off / no power supply

TC_exposure_only labels explanation:
    0: TC is absent
    1: TC is present but not watching TV, TV is ON
    2: FLASH-TV device is rebooting/restarting
    3: FLASH-TV device is powered off / no power supply


