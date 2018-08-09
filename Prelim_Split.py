import pandas as pd
import datetime
import numpy as np

sample_data= pd.read_csv("LIWC_INFO_separated.csv")
#split first column into userID and date
sample_data['userID'], sample_data['date'] = sample_data['A'].str.split('_', 1).str
cols = sample_data.columns.tolist()
sample_data.pop('A')
print(sample_data['userID'])

#split date to year and month
sample_data['date'] = pd.to_datetime(sample_data['date'])
sample_data['year'] = sample_data['date'].dt.year
sample_data['month'] = sample_data['date'].dt.month
sample_data['day'] = sample_data['date'].dt.day

#reorganize columns in specific order
cols = ['userID', 'date', 'year', 'month', 'day', 'WC', 'Analytic', 'Clout', 'Authentic', 'Tone', 'WPS', 'Sixltr', 'Dic', 'function', 'pronoun', 'ppron', 'i', 'we', 'you', 'shehe', 'they', 'ipron', 'article', 'prep', 'auxverb', 'adverb', 'conj', 'negate', 'verb', 'adj', 'compare', 'interrog', 'number', 'quant', 'affect', 'posemo', 'negemo', 'anx', 'anger', 'sad', 'social', 'family', 'friend', 'female', 'male', 'cogproc', 'insight', 'cause', 'discrep', 'tentat', 'certain', 'differ', 'percept', 'see', 'hear', 'feel', 'bio', 'body', 'health', 'sexual', 'ingest', 'drives', 'affiliation', 'achieve', 'power', 'reward', 'risk', 'focuspast', 'focuspresent', 'focusfuture', 'relativ', 'motion', 'space', 'time', 'work', 'leisure', 'home', 'money', 'relig', 'death', 'informal', 'swear', 'netspeak', 'assent', 'nonflu', 'filler', 'AllPunc', 'Period', 'Comma', 'Colon', 'SemiC', 'QMark', 'Exclam', 'Dash', 'Quote', 'Apostro', 'Parenth', 'OtherP']
sample_data = sample_data[cols]


#convert object type to integer
for col in sample_data.columns[4:]:
    sample_data[col] = pd.to_numeric(sample_data[col], errors='coerce')

# group data by userID, year, month for all 40 mil users and write in file
group_data = sample_data.groupby(['userID', 'year', 'month']).mean()
group_data.to_csv("LIWC_INF0_grouped.csv")

# print all ungrouped data in other file
sample_data.to_csv("LIWC_INFO_organized.csv")
