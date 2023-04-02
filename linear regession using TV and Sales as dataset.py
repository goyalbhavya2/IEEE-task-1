import pandas as pd
import matplotlib.pyplot as plt
import math
a=pd.read_csv("C:\\Users\\goyal\\OneDrive\\Desktop\\tvmarketing.csv")
#loss=mean square error dunction
def loss(m,c,points):
    totalerror=0
    for i in range(len(points)):
        x=points.iloc[i].TV
        y=points.iloc[i].Sales
        totalerror+=pow((y-(m*x+c)),2)/float(len(points))
    

def gradient_descent(m_now,c_now,points,l):
    m_gradient=0
    c_gradient=0
    n=len(points)
    for i in range(n):
        x=points.iloc[i].TV
        y=points.iloc[i].Sales
        m_gradient+= -(2/n) * x * (y-(m_now * x + c_now))
        c_gradient+= -(2/n) *(y-(m_now * x + c_now))
    m=m_now - m_gradient * l
    c=c_now - m_gradient * l
    return m,c

m=0
c=0
l=0.000001
limit=100
for i in range(limit):
    m,c=gradient_descent(m,c,a,l)

a.plot.scatter("TV","Sales")
plt.plot(list(range(0,300)),[m*x+c for x in range(0,300)],color="orange")
plt.show()

    

