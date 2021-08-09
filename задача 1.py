vvod = list(map(int,input().split())) #вводим числа
n,a,b,c = vvod[0],vvod[1],vvod[2],vvod[3]

m = 0 #мой максимум, который я ищу

for otrA in range(n): #переменные otr - количества определенных отрезков, которые я могу сделать
    otrB = 0 #я вполне мог otrB и otrC сделать в виде циклов, но 2-3 цикла будут работать дольше
    otrC = 0
    porezal = n - a*otrA #отрезаю отрезки А.
    if porezal < 0: #защита от ухода в отрицательные значения, т.к длина отрезка не может быть отрицательной
        continue
    if porezal >= 0 and porezal%c == 0: #если после отрезания А еще остались отрезки, проверяю, можно ли резать B или C
        otrC = porezal/c
    if porezal >= 0 and porezal%b == 0:
        otrB = porezal/b
    maxi = otrC + otrB + otrA #общее количество отрезков
    if maxi > m: #сравниваю с максимумом, если количество отрезков больше, то это мой максимум.
        m = maxi
print(int(m))