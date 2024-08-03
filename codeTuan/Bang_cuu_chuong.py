"""Bài tập: In bảng cửu chương
   Yêu cầu: Viết một chương trình in bảng cửu chương từ 1 đến 10."""


sonhan1 = 0


while sonhan1 < 11:
    for sonhan2 in range(1,11):
        ketqua = sonhan1 * sonhan2
        print(sonhan1, "x", sonhan2, "=", ketqua)
    print("\n")
    sonhan1 += 1
       


