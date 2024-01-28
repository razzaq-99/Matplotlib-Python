                                                       # Legend
# import matplotlib.pyplot as plt 

# x = [1,2,3,4,5]
# y = [11,22,00,44,55]
# z = [19,29,10,49,59]

# plt.plot(x,y,label="female")
# plt.plot(x,z,label="male")

# plt.xlabel("Index",fontsize=12)
# plt.ylabel("Values",fontsize=12)

# plt.legend(loc = 0)         # best position
# plt.legend(loc = 1)
# plt.legend(loc = 2)
# plt.legend(loc = 3)

# plt.legend(loc = 9,ncols=2)         # top middle
# plt.legend(loc = 10)      # center 
# plt.show()









                                            #    SUB PLOT 
import matplotlib.pyplot as plt 
import pandas as pd 

x = [1,2,3,4,5]
y = [45,30,50,35,55]  

plt.subplot(1,3,1)             # rows , columns , chart number
plt.plot(x,y)
plt.title("Age")
# plt.show()        

x = [1,2,3,4,5]
y = [50,25,55,30,60]

plt.subplot(1,3,2)             # rows , columns , chart number
plt.bar(x,y,color="red")
plt.title("Weight")

x = [1,2,3,4,5]
y = [100,50,90,40,75]

plt.subplot(1,3,3)             # rows , columns , chart number
plt.scatter(x,y,color ="green")
plt.title("Fitness")

plt.suptitle("Human Body Fitness",fontsize=15)
plt.show()      