import pandas as pd 

df = pd.read_csv('Glassdoor_jobs.csv')
df.columns


# salary parsing
# company name test_only
# state filed
# age of company
# parsing of job dp( python etc)
df = df[df['Salary Estimate']!= '-1']
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minue_kd = salary.apply(lambda x: x.replace('K','').replace('CA$',''))
