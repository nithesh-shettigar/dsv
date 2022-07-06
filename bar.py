import matplotlib.pyplot as plt
import pandas as pd
  
  
# Initialize the lists for X and Y
data = pd.read_csv('E:\\my_data.csv')
  
df = pd.DataFrame(data)
  
X = list(df.iloc[:6, 0])
Y = list(df.iloc[:6, 1])
  
# Plot the data using bar() method
plt.xticks([1, 2, 3, 4])
plt.bar(X, Y, color='g')
plt.title("top 5 state")
plt.xlabel("state ")

  
# Show the plot
plt.show()





