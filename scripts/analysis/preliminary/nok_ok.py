import pandas as pd
import numpy as np

df = pd.read_csv('../data/machining_drive_load.csv', header=0)
df2 = pd.read_csv('../data/prod_measurements2.csv', header=0, sep=';')

range1 = [4.500, 0.028, 0.040]
range2 = [19.20, -0.05, 0.00]
range3 = [15.15, 0.00, 0.05]
df2 = df2.set_index('trace:id')
df = df.set_index('trace:id')
#print(range1[0]+range1[1], range1[0]+range1[2])
mm1 = df2.manual_measure1.between(range1[0]+range1[1], range1[0]+range1[2])
a = df2[mm1]
mm2 = a.manual_measure2.between(range2[0]+range2[1], range2[0]+range2[2])
b = a[mm2]
mm3 = b.manual_measure3.between(range3[0]+range3[1], range3[0]+range3[2])
c = b[mm3]

print("Manual measures that indicate nok: ", len(df2)-len(c))
print("Status nok df2:", sum(df2.status=='nok'))
print("Status nok c:", sum(c.status=='nok'))
print(df2[-mm1].manual_measure1)
print(a[-mm2].manual_measure2)
print(b[-mm3].manual_measure3)
print(df2[-df2.manual_measure3.between(range3[0]+range3[1], range3[0]+range3[2])])
