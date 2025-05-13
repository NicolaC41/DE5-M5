import pandas as pd
df = pd.read_csv('03_Library Systembook.csv')
df_clean = df.dropna()

# Remove that row 16
df_clean.drop(16,axis=0,inplace =True) 
#= df.drop(16)

# RETRY Converting the date of purchase to date format
df_clean['Book checkout'] = df_clean['Book checkout'].str.replace('"', "", regex=True)
df_clean['Book checkout'] = pd.to_datetime(df_clean['Book checkout'], format='mixed' ) 
df_clean['Book Returned'] = pd.to_datetime(df_clean['Book Returned'], format='mixed' ) 

def enrich(df_clean, startcol ='Book checkout', end_col ='Book Returned', new_col= 'days_between'):

#df[new_col] = (df[end_col] - df[start_col]).dt.days
#df_clean[new_col] = (df['Book Returned'] - df['Book checkout']).dt.days





#move to csv
#df.to_csv('references/Cleandata.csv',index= False)