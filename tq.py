import pandas as pd
import matplotlib.pyplot as plt
import seaborn as ssn
df=pd.read_csv("D:\\mtcars.csv")

mpg=df["mpg"]
plt.hist(mpg, color='g', edgecolor='black')
plt.xlabel("mpg")
plt.ylabel("frequency")
plt.title("Frequency Distribution of mpg")
plt.show()

wt=df["wt"]
iv=(range(len(df)))
plt.scatter(iv, wt, color='b', label='wt')
plt.scatter(iv, mpg, color='g', label='mpg')
plt.xlabel("mpg")
plt.ylabel("weight")
plt.legend()
plt.title("Relation of mpg and wt")
plt.show()

am=df["am"].value_counts()
c=['orange','black']
plt.bar(am.index, am.values, color=c, width=0.2)
plt.xticks([0,1],["0-automatic","1-manul"])
plt.xlabel("Transmission type")
plt.ylabel("No of cars")
plt.title("Frequency distribution of Transmission type")
plt.show()

ssn.boxplot(mpg,color='b')
plt.xlabel("MPG");plt.ylabel("Values") 
plt.title("BOX plot of MPG Vlues")