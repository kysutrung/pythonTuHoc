"""Câu hỏi2:
Viết chương trình nhập: số giờ làm mỗi tuần, thù lao trên mỗi giờ làm tiêu chuẩn,
từ đó tính ra số tiền thực lĩnh của nhân viên. Biết rằng: số giờ tiêu chuẩn mỗi tuần
là 44 giờ, và mỗi giờ vượt chuẩn được trả gấp rưỡi so với giờ làm chuẩn. 
"""
n = int(input("Gio lam tieu chuan: "))
m = int(input("Thù lao trên mỗi giờ làm tiêu chuẩn: "))
thulao = n * m *4
tien_thuong = (n-44)*m*1.5
if n == 44:
    print("Tiền lương tháng vừa qua của bạn là: ", thulao)
elif n > 44:
    print("Tiền lương tháng vừa qua của bạn là: ", thulao + tien_thuong)

