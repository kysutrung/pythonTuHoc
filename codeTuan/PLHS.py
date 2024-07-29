"""Bài Tập: Chương Trình Phân Loại Điểm Số
Viết một chương trình Python để phân loại điểm số của học sinh thành các loại học lực theo tiêu chuẩn sau:

Điểm số từ 90 đến 100: Xuất sắc
Điểm số từ 80 đến 89: Giỏi
Điểm số từ 70 đến 79: Khá
Điểm số từ 60 đến 69: Trung bình
Điểm số dưới 60: Kém

Yêu Cầu:
Yêu cầu người dùng nhập điểm số (một số nguyên từ 0 đến 100).
Sử dụng cấu trúc if-else để phân loại điểm số và in ra kết quả tương ứng."""

a = int(input('Nhap diem cua hoc sinh: '))
if (90 <= a <= 100):
    print('Loai Xuat Sac')
elif (80 <= a <= 89):
    print('Loai Gioi')
elif (70 <= a <= 79):
    print('Loai Kha')
elif (60 <= a <= 69):
    print('Loai Trung Binh')
elif(0<= a <= 59):
    print('Loai Yeu')
else:
    print('Loi ket qua, vui long nhap lai')
