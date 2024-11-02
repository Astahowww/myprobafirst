a = """Трамплинадзе Сэм\n
Ванок Сидор\n
Фуртов Вася\n
Асмуфов Тимофей\n
Карабанов Джан\n
Чук Савелий"""

b = a.split('\n\n')
print(b)
C = []
for el in b:
    el = el.split(' ')
    C.append(el[0])
C.sort(key=len)
for i in b:
    if (C[len(C)//2]) in i:
        b.remove(i)
','.join(b)        
print(b)
