import pandas as pd 

df = pd.read_csv('Glassdoor_jobs.csv')
df.columns


# salary parsing

df = df[df['Salary Estimate']!= '-1']
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minue_kd = salary.apply(lambda x: x.replace('K','').replace('CA$',''))

# df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary' in x.lower() else 0)

# min_hr = minue_kd.apply(lambda x: x.lower().replace('per hour',''))

df['min_salary'] = minue_kd.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = minue_kd.apply(lambda x: int(x.split('-')[1]))
df['ave_salary'] = (df['min_salary'] + df['max_salary'] )/ 2

# company name test_only
df['company name'] = df.apply(lambda x: x['Company Name'] if x['Rating']<0 else x['Company Name'][:-3], axis = 1)

# state filed
df['headquater'] = df['Headquarters'].apply(lambda x: x.split(',')[0])
df['same_state'] = df.apply(lambda x: 1 if x['Location'] == x['headquater'] else 0, axis = 1)

# age of company
df['age'] = df['Founded'].apply(lambda x: x if x < 1 else 2020 - x )

# parsing of job dp( python etc)

df['Job Description'][0]

# python
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0 )
# r studio
df['r studio'] = df['Job Description'].apply(lambda x: 1 if 'r ' in x.lower() or 'r ' in x.lower() else 0 )
# spark
df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0 )
# aws 
df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0 )
# excel
df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0 )

df.to_csv('salary_data_cleaned.csv',index = False)

