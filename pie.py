import requests
import matplotlib.pyplot as plt
import pandas as pd



df_tables = pd.read_html('https://en.wikipedia.org/wiki/List_of_institutions_of_higher_education_in_Karnataka#Universities')



df_tables[3].to_csv('Deemed to be University.csv', index=False, header=True)



d1= df_tables[3].groupby('Location').count()
places= list(d1.index)
loc_count = list(d1.University)



fig1, ax1 = plt.subplots()
ax1.pie(loc_count, labels = places)
plt.show()