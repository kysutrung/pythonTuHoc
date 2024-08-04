#Tham số chính thức: parameter

def xinchao(name1, name2, name3):
    print('Xin chao', name1, name2, name3)

#code để chạy chương trình
"""if __name__ == '__main__':
    xinchao('X', 'Y','Z')
    xinchao(name2='dep', name1='Tuan', name3='trai')"""

#Hàm tính giai thừa
def giaithua(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res
#Hàm tính lũy thừa
def lt(a, b):
    res = 1
    for i in range (b):
        res *= a
    return res

if __name__ == '__main__':
    print(gt(5))
    print(lt(2,10))
    
