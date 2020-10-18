from django.test import TestCase

# Create your tests here.
import json
import pandas as pd
file = 'Cancer.json'
with open(file) as train_file:
    dict_train = json.load(train_file)

data = (dict_train)
df = pd.json_normalize(data['gXdpApi']['gIdpPayLoad'])
print(df)
writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1')

# Close the Pandas Excel writer and output the Excel file.
writer.save()
# converting json dataset from dictionary to dataframe
train = pd.DataFrame.from_dict(dict_train, orient='index')
print(str(train))
train.reset_index(level=0, inplace=True)
print(train)
for ele in train:
    print(ele)