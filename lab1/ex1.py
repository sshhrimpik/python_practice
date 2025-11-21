import numpy as np

x=int(input("insert '1', '10' or '1000'"))
y=np.log(1+((x**2/np.e**(np.sin(x)+1))/((5/4)+(1/x**15))))
print(y)