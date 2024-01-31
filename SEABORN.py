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
# import seaborn as sns     
# import matplotlib.pyplot as plt 

# data = sns.load_dataset("tips")

# sns.histplot(data=data, x="size",hue="time",kde=True)

# sns.histplot(data=data, x="day",y="tip",hue="time")

# sns.histplot(data=data, x="day",y="total_bill")
 
# print(data.head(10))
# data["day"] = data['day'].astype(str)
# df = data['day'].count()
# print(df)
# plt.show()





# data = sns.load_dataset("titanic")


# sns.histplot(data = data , x="sex",y="age", kde=True ,hue="who", discrete=True ,bins=10)

# sns.histplot(data = data , x="age", kde=True , discrete=True ,bins=10,hue="who") 
# plt.title("Age of peoples in Titanic")
# # plt.legend(ncols=3)
# print(data.head(10))
# plt.show()












                                                                  # Scatter Plot
# import seaborn as sns          
# import matplotlib.pyplot as plt 
# import pandas as pd 


# data = sns.load_dataset("tips")

# sns.scatterplot(data= data, x="total_bill",y="tip",hue="sex")
# print(data)

# sns.scatterplot(data= data, x="total_bill",y="tip",hue="day",size="smoker")
# print(data)
# # plt.legend(ncols=2)
# plt.title("Total bills vs tips")
# plt.show()





# data = pd.read_excel("ESD.xlsx")

# print(data.head(10))

# sns.scatterplot(data= data , x="Age",y="Annual Salary",hue="Department",size="Gender")

# plt.legend(bbox_to_anchor = (0.2,0,1.1,1.1))

# plt.show()











                                                        #   HEATMAP PLOT
# import seaborn as sns          
# import matplotlib.pyplot as plt 
# import pandas as pd 


# data = sns.load_dataset("tips")

# gp = data.groupby("day").agg({"tip":"mean"})

# sns.heatmap(gp)
# sns.heatmap(gp,xticklabels='auto',center=2.2)

# plt.show()
                                                        
                                                        
                                                        
                                                        
                                            
                                            
# data = pd.read_excel("ESD.xlsx")

# dfx = data.groupby("Department").agg({"Annual Salary":"mean"})  

# sns.heatmap(dfx)

# sns.heatmap(dfx,center=1.5)
# plt.legend()
# print(data.head(10))
# plt.show()










                                                                        # Count PLot 
# import seaborn as sns          
# import matplotlib.pyplot as plt 
# import pandas as pd 

# data = sns.load_dataset("tips")

# sns.countplot(data= data, x="sex",hue="sex")

# sns.countplot(data= data, x="day",hue="sex")

# plt.show()
  
  
  
  
  
# df = pd.read_excel("ESD.xlsx")

# print(df.head(10))

# sns.countplot(data= df , x = "Department",hue="Gender",palette="viridis")

# plt.show()







                                                                     # VIOLIN PLOT 
                                                                     
# import seaborn as sns          
# import matplotlib.pyplot as plt 


# data = sns.load_dataset("tips")

# print(data.head(10))

# sns.violinplot(data = data, x = "total_bill",hue="day")
# sns.violinplot(data = data, x = "total_bill",hue="sex")
 
# sns.violinplot(data = data , x="tip",hue="sex",color="orange")


# sns.violinplot(data = data , x="smoker",hue="sex",color="orange")

# plt.show()      









                                                                      # PAIR PLOT
# import seaborn as sns          
# import matplotlib.pyplot as plt 

# data = sns.load_dataset("tips")
# data = sns.load_dataset("iris")


# sns.pairplot(data= data,hue="sex",diag_kind="")

# sns.pairplot(data= data,hue="species")
# print(data.head(10))
# plt.savefig("iris_analysis.png")
# plt.show()






                                                             # STRIP PLOT                                            
                                                             
import seaborn as sns 
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")

sns.stripplot(data= data, x = "day", y = "total_bill",hue="sex",dodge=True, jitter= 0.3 , marker = 'D',alpha = 1)

# sns.scatterplot(data= data, x = "day", y = "total_bill",hue="sex")

plt.legend()
print(data.head(10))
plt.show()
                                                     