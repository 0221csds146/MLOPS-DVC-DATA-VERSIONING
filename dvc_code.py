import pandas as pd
import os

# create a sample Datframe with colum names

data={'NAme':['Alice',"Bob","Charlie"],
      'Age':[20,40,60],
      'city':['New York','Los Angeles','Delhi']
      }

df=pd.DataFrame(data)

# ENSURE THE 'DATA' directory exists at the root level
data_dir='data'
os.makedirs(data_dir,exist_ok=True) #exist_ok=True maeans if this directory is already exist then it doesn't overwrite it

#Define file path
file_path=os.path.join(data_dir,"Sample_data.csv")

#Save the dataframe to a csv file,inluding colum names
df.to_csv(file_path,index=False)

print(f'Csv file saved to {file_path}')
