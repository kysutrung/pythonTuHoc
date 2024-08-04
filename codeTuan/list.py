a = [ 1, 2, 3, 4, 5, 6, 'Tuan']
#duyet thong qua chi so
for i in range(len(a)):
    print(a[i], end="")
print()
for i in range(-1, len(a)*(- 1) - 1, - 1):
    print(a[i], end = " ",)
print(' ')

#duyet bang for each
for item in a:
    print(item, end = " ")      

#chen ky tu
a.append(100)
a.insert(3, 20)
for i in range(len(a)):
    print(a[i], end="")

print()