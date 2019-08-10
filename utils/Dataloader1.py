import numpy as np
import pandas as pd
dffinal = pd.DataFrame()
all_data = pd.DataFrame(columns=['0'])
for f in ['Rainfall','Max Temperature','Min Temperature','Maximum Humidity','Min Humidity','CC','Wind Direction','EVP','Wind speed','Solar Radiation']:
    df_melt=pd.read_excel('Weather data from 2009-2018 edit2.xlsx',sheet_name=f)
    pd.set_option('display.max_rows', 9110)
    dffinal=df_melt.melt(id_vars=['0'],var_name='Weather Parameter')
    all_data=all_data.merge(dffinal,on='0', how='outer')
