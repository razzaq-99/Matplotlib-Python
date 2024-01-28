           # Legend
import matplotlib.pyplot as plt 

x = [1,2,3,4,5]
y = [11,22,00,44,55]
z = [19,29,10,49,59]

plt.plot(x,y,label="female")
plt.plot(x,z,label="male")

plt.xlabel("Index",fontsize=12)
plt.ylabel("Values",fontsize=12)

# plt.legend(loc = 0)         # best position
# plt.legend(loc = 1)
# plt.legend(loc = 2)
# plt.legend(loc = 3)

plt.legend(loc = 9,ncols=2)         # top middle
# plt.legend(loc = 10)      # center 
plt.show()
