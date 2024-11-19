import time
list = [2,3,4,3,4,5,6,1]

# O(n^2) solution
def onn_solution(list):
    start = time.time()
    best_min = list[0]
    for i in range(1,len(list)):
        for j in range(len(list)):
            if list[i] > list[j]:
                min = list[j]
            else:
                min = list[i]
        if best_min > min:
            best_min = min
    end = time.time()
    return best_min, end-start
print("With O(n^2) solution")
for i in range(5):
    print("Min is %d required %10.7f seconds " % onn_solution(list))

# O(n) solution
def on_solution(list):
    start = time.time()
    best_min = list[0]
    for i in range(1,len(list)):
        if best_min > list[i]:
            best_min = list[i]
    end = time.time()
    return best_min, end-start
print("With O(n) solution")
for i in range(5):
    print("Min is %d required %10.7f seconds " % on_solution(list))