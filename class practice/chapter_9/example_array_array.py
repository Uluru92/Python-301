import array

a = array.array('i', [2, 0, 0, 0, 0])

print(a[0])

a.append(5)
print(a)
a[2] = 10
print(a[2])  # 10
print(a)
a.append(20)
print(a)
a.insert(3, 30)
print(a)

last = a.pop()
print(last) 
print(a) 

middle = a.pop(2)
print(middle)  # 30
print(a)