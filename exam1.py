import pandas as pd
df = pd.read_csv("indian_food.csv")

print("1.Find out how many unique dishes are present.")
n =len(pd.unique(df['name']))
print(n)

print("2.Which state has more dishes?")

n6=df.groupby(df['state']).max()
print(n6)

print("3.How many dishes from state Karnataka?")
n7=len(df['name'].unique())
print(n7)


#4
print("4.List number of unique regions")
n1=df['name'].value_counts()
print(n1)

#5
print("5.Count number of dishes from each region.")
n2=df.groupby(df['region']).count()
print(n2)


print("6List unique 'flavor_profile' and 'course'")
n10=len(df[['flavor_profile','course']].nunique())
print(n10)
#7
print("7Which state has more 'main course'?")
n3=df.groupby(df['region']).max()
print(n3)

print("8.Give the %of dishes from each region.")
n11=(df['name'].count() / df['region'].sum())*100
print(n11)

print("9.List the states which has more dishes from each region.")
n9=df.groupby(['name'], sort=False)['region'].max()

print(n9)
