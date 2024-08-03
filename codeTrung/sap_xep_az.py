#Bài tập sắp xếp một dãy số theo thứ tự tăng dân
day_so = [9,8,7,4,5,6,3,2,1]
bien_tam = 0

for i in range(0,len(day_so)-1):

    if day_so[i] > day_so[i+1]:
        bien_tam = day_so[i]
        day_so[i] = day_so[i+1]
        day_so[i+1] = bien_tam

print(day_so)