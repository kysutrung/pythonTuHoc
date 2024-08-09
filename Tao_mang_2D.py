"""Câu hỏi3:
Viết một chương trình có 2 chữ số, X, Y nhận giá trị từ đầu vào và tạo
ra một mảng 2 chiều.
Giá trị phần tử trong hàng thứ i và cột thứ j của mảng phải là i*j.

Lưu ý: i=0,1,...,X-1; j=0,1,...,Y-1.

Ví dụ: Giá trị X, Y nhập vào là 3,5 thì đầu ra là:
[[0, 1, 2, 3, 4], 
 [1, 1, 2, 3, 4], 
 [2, 2, 4, 6, 8]]"""


X, Y = map(int,input("Nhap so hang X và so cot Y: ").split())
mang_1 = [[None]*Y]*X
for i in range(0,X):
    