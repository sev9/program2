import matplotlib.pyplot as plt
import numpy as np 

fig=plt.figure()

x=[i for i in range(1,10)]
y1=np.random.randint(2,6,9)
y2=np.random.randint(2,6,9)
plt.ylabel('Средний балл')
plt.xlabel('Класс')

plt.plot(x,y1)
plt.plot(x,y2)

plt.legend(['мой средний балл','средний балл класса'])

plt.show()
