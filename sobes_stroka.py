a = """Трамплинадзе Сэк\n
Ванок Сим\n
Фуртов Пром\n
Асмуфов Тимваролдд\n
Карабан Джан\n
Чук Сычмсчаавппарр"""

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
