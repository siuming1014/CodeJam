import time

start_time = time.time()

[1 + 2 for _ in range(100000000)]

print(time.time() - start_time)