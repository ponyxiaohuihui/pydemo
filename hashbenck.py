import time

time1 = time.time()
dic1 = {}
index = 1
while index < 100000000:
    dic1["1"] = 1
    index = index + 1
print(str(time.time() - time1))
