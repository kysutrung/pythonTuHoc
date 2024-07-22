#bài này dùng để hiểu về cách dùng hàm main và các hàm phụ

def chao_hoi():
    print("Xin chao co chu, xin chao cac ban")

def chuc_mung():
    print("Chuc ban may man lan sau")

def meo():
    for i in range(1,3):
        print("meo")

#đây là hàm main giống trong cpp, cái này sẽ chạy đầu tiên và gọi các hàm liên quan
#hàm nào không được gọi sẽ không chạy
def main(): 
    chao_hoi()
    chuc_mung()

if __name__ == "__main__":
    main()
