import quicksort_method1 as qs1
import quicksort_method2 as qs2
import matplotlib.pyplot as plt
import time

listSizes = list(range(100, 10001, 100))
times = []

for size in listSizes:
    A = list(range(size, 0, -1))
    startTime = time.time()
    qs1.QuickSort1(A)
    endTime = time.time()
    times.append(endTime - startTime)

# for size in listSizes:
#     A = list(range(size, 0, -1))
#     startTime = time.time()
#     qs2.QuickSort2(A)
#     endTime = time.time()
#     times.append(endTime - startTime)

plt.plot(listSizes, times, marker='o')
plt.xlabel('Size of List')
plt.ylabel('Time (Seconds)')
plt.show()


# my conclusion from looking at both graphs is that the time complexity for both quicksorts is O(n).
# they take place within a similar timeframe as well, of less than 0.025 secs for 1 and 2.
# 1 seems to be slightly faster but not by very much.