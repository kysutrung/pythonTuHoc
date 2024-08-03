#Bài tập tìm thủ công min và max của một tập hợp dãy số
day_so = [0, 3, 6, 9, 8, 0, 8, 4]

def tim_min(list_a):
    min = 0
    for i in range(0, len(list_a)):
        if min > list_a[i]:
            min = list_a[i]
    print("min = ", min)

def tim_max(list_a):
    max = 0
    for i in range(0, len(list_a)):
        if max < list_a[i]:
            max = list_a[i]
    print("max = ", max)

tim_max(day_so)
tim_min(day_so)

