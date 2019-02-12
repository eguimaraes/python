import seaborn as sns
import pandas as pd

data = pd.read_csv('Dataset.csv')

plt.figure(figsize=(40,40)) 
# play with the figsize until the plot is big enough to plot all the columns
# of your dataset, or the way you desire it to look like otherwise

sns.heatmap(data.corr())
