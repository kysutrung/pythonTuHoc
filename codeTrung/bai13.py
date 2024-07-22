#bài này học về vòng lặp while

# khi nào điều kiện trong vòng while còn đúng thì nó còn chạy

# bài tính tổng một dãy số từ m đến n

m = 2
n = 10
sumA = 0

m1 = m
while m1 <= n:
    sumA += m1
    m1 += 1

print("Tong cac so tu", m, "den", n,"=",sumA)