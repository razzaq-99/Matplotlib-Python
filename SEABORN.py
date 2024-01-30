                                              # Line Plot Seaborn
import seaborn as sns
import pandas as pd 
import matplotlib.pyplot as plt 

# data = {"days":[1,2,3,4,5],"NOP":[40,20,50,30,60]}

# df = pd.DataFrame(data)

# print(df)

# sns.lineplot(data=data,x="days",y="NOP")
# plt.show()




# data = pd.read_excel("ESD.xlsx")
# print(data.head(10))

# sns.lineplot(data=data, x = "Business Unit", y= "Annual Salary",hue="Gender")                              # style="Ethnicity"

# sns.lineplot(data=data, x = "Department", y= "Bonus %",hue="Gender")

# plt.legend(loc = 9)
# plt.show()











                                                # Bar plot 
# import matplotlib.pyplot as plt 
# import seaborn as sns 

# data = sns.load_dataset("tips")
# data2 = sns.load_dataset("titanic")

# print(data2)      
# colors = ["red","blue","orange","brown"]

# sns.barplot(data = data, x="day",y="tip",color="orange",estimator="mean" , hue="sex", order= ["Sun","Sat","Fri","Thur"])
# sns.barplot(data = data, x="sex",y="smoker",color="orange")



# sns.barplot(data = data, x="day",y="tip",color="orange",estimator="mean" , hue="sex", ) 

# print(data)
# plt.legend(loc = 9, ncols=2)
# plt.show()







                                                # Histogram
import seaborn as sns     
import matplotlib.pyplot as plt 

# data = sns.load_dataset("tips")

# sns.histplot(data=data, x="size",hue="time",kde=True)

# sns.histplot(data=data, x="day",y="tip",hue="time")

# sns.histplot(data=data, x="day",y="total_bill")
 
# print(data.head(10))
# data["day"] = data['day'].astype(str)
# df = data['day'].count()
# print(df)
# plt.show()





data = sns.load_dataset("titanic")


# sns.histplot(data = data , x="sex",y="age", kde=True ,hue="who", discrete=True ,bins=10)

sns.histplot(data = data , x="age",y="survived", kde=True , discrete=True ,bins=10) 
# plt.legend(ncols=3)
print(data.head(10))
plt.show()
