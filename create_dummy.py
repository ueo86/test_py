import time
import random
import pandas as pd


print(random.random())
print("")

dataList = []

print("start insert data in memory")
s = time.time()
for r in range(3000000):
    dataList.append([random.random() for _ in range(4)])
print("done write csv elpstime:", time.time()-s)


print("start write csv")
s = time.time()
# df = pd.DataFrame(dataList)
# df.to_csv("out.csv")
with open("out.csv", "w") as f:
    for d in dataList:
        r = ",".join([str(v) for v in d]) + "\n"
        f.write(r)

print("done write csv file:", time.time() - s)