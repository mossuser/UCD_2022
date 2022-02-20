import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv(r'C:\UCD_2022\flights.csv')
#print(flights)
print(df.head())
df.dtypes
df.info


plt.plot(df['2018'])
plt.plot(df['2019'])
plt.plot(df['2025'])
plt.plot(df['2030'])
plt.plot(df['2035'])
plt.plot(df['2040'])

plt.xticks(range(0,24,1))
plt.grid(True)
plt.legend(['2018', '2019','2025','2030','2035', '2040'])
plt.show()