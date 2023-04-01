import pandas as pd
a=pd.read_csv("C:\\Users\\goyal\\OneDrive\\Desktop\\tvmarketing.csv")
print("the maximum value of TV column is ",a['TV'].max())
print("the maximum value of Sales column is ",a['Sales'].max())
print("the minimum value of TV column is ",a['TV'].min())
print("the minimum value of Sales column is ",a['Sales'].min())
print("the mean value of TV column is ",a['TV'].mean())
print("the mean value of Sales column is ",a['Sales'].mean())
print("the standard deviation value of TV column is ",a['TV'].std())
print("the standard deviation value of Sales column is ",a['Sales'].std())
print("the value count of TV column is ",a['TV'].count())
print("the value count of Sales column is ",a['Sales'].count())
print("25% of Sales column is",a.Sales.quantile(0.25))
print("25% of TV column is",a.TV.quantile(0.25))


