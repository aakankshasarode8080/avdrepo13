import pandas as pd

#create dictionary
data = {
    'Id': [101, 102, 103],
    'Name': ['Ram', 'Raj', 'Raja'],
    'Age': [29, 34, 42]
}

#convert to tabular format
df = pd.DataFrame(data)

#show data
print(df)
