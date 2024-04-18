import os 
import sys

import numpy as np 
import pandas as pd
import yaml

from datetime import timedelta

#path = '/home/akv/FLASH_PO1/flash-tv-post-processing/data/output'
path_mobile = '/home/akv/FLASH_PO1/tech_data_post_processed/study4_mobile_old'
mobile_details = './study4_mobile_details.csv'
num_days=3

df = pd.read_csv(mobile_details, delimiter=',')
df = df[df['mobile_count']>0]

for idx in df.index:
    if True:
        row = df.loc[idx]
        ppt = row['ppt_id']
        start_date = row['start_date']
        type_ = row['mobile_type']
        count = row['mobile_count']
        csv_path = None
        
        if type_ == 'Android':
            csv_path = '%s/%s_chronicle_android.csv'%(path_mobile,str(ppt))
            save_path = '%s/%s_android_final.csv'%(path_mobile,str(ppt))
        
        if type_ == 'iPhone':
            csv_path = '%s/%s_chronicle_ios.csv'%(path_mobile,str(ppt))
            csv_path = None
            if ppt == 591:
                csv_path = None
            save_path = '%s/%s_ios_final.csv'%(path_mobile,str(ppt))

        if type_ == 'iPad':
            csv_path = '%s/%s_ipad_data.csv'%(path_mobile,str(ppt))
            csv_path = None
            if ppt in [577,598]:
                csv_path = None
            save_path = '%s/%s_ipad_final.csv'%(path_mobile,str(ppt))
            
        if csv_path == None:
            continue
            
        
        print(row)            
        m_df = pd.read_csv(csv_path, delimiter=',')
        if 'iPhone' in type_ or 'iPad' in type_:
            m_df['event_timestamp'] = m_df['date'] + ' ' + m_df['start_timestamp']
        
        m_df['event_timestamp'] = pd.to_datetime(m_df['event_timestamp']).dt.tz_localize(None)
        m_df.sort_values('event_timestamp', inplace=True)
        m_df.set_index('event_timestamp', inplace=True)
        
        start_dts = pd.to_datetime(start_date) #+ timedelta(days=day)
        end_dts = start_dts + timedelta(days=num_days-1,hours=23,minutes=59,seconds=59)
        
        m_df = m_df[start_dts:end_dts]
        if 'index' in m_df.columns:
            m_df.drop(columns=['index'],inplace=True)
            
        m_df.username = m_df.username.astype(str)
        m_df.username = m_df.username.apply(lambda x : "None" if x=="nan" else x)
        m_df.to_csv(save_path, sep=',') 
        
        
        for day_ in range(num_days):
            start_dts = pd.to_datetime(start_date) #+ timedelta(days=day)
            
            start_dts = start_dts + timedelta(days=day_,hours=0,minutes=0,seconds=0)
            end_dts = start_dts + timedelta(hours=23,minutes=59,seconds=59)
        
            m_df_day = m_df[start_dts:end_dts]
            #print(m_df_day)
            
            m_df1 = m_df_day[m_df_day['username'].str.lower()=='target child']
            m_df2 = m_df_day[m_df_day['username'].str.lower()!='target child']
            
            start_ts = pd.to_datetime(m_df1['date'] + ' ' + m_df1['start_timestamp'])
            stop_ts = pd.to_datetime(m_df1['date'] + ' ' + m_df1['stop_timestamp'])
            tc_duration = (stop_ts - start_ts).dt.total_seconds()
            #print(tc_duration)
            #print(tc_duration[tc_duration<0])
            
            tc_duration = tc_duration.sum()

            print(tc_duration/60.0)
            
            start_ts = pd.to_datetime(m_df2['date'] + ' ' + m_df2['start_timestamp'])
            stop_ts = pd.to_datetime(m_df2['date'] + ' ' + m_df2['stop_timestamp'])
            un_duration = (stop_ts - start_ts).dt.total_seconds()
            
            
            
            un_duration = un_duration.sum()
            
            print(un_duration/60.0)



