import pandas as pd
# # Create a Series from a list
# data = [10, 20, 30, 40, 50]
# s = pd.Series(data)
# print(s)

# Creating a DataFrame from a dictionary
# data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
#         'Age': [25, 30, 35, 28],
#         'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
# df = pd.DataFrame(data)
# print(df)
# print("\n")
# print(df['Age'])
# print("\n")
# print(df.iloc[3])
# print("\n")
# print(df[1:3])
# uniquefindings=df['Name'].unique()
# print("\n")
# print(uniquefindings)
# print("\n")
# print(df[df['Age']>=30])
# df.to_csv('training data.csv',index=False)

#Define a dictionary 'x'

x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 
      'Salary':[100000, 80000, 50000, 60000]}

#casting the dictionary to a DataFrame
df = pd.DataFrame(x)

#display the result df
print(df)
print("\n")
x = df[['ID']]
print(x)
print(type(x))
print("\n")
#df=df.drop(df.columns[0],index=1)
df = df.reset_index(drop=True)
print(df)

