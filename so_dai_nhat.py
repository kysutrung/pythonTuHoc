"""Bài tập 2: Tìm số dài nhất trong danh sách các số nguyên
Yêu cầu: Viết hàm tim_so_dai_nhat(list_a) để tìm số có nhiều chữ số
nhất trong danh sách các số nguyên list_a."""

list_a = [10, 304, 111, 2222, 'aasdfghj', 686868, 9999]
sodainhat = 0
for i in list_a:
    if len(str(i)) > len(str(sodainhat)):
        sodainhat = i
print(sodainhat)