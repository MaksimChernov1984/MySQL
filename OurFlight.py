print('Полуось орбиты точки вылета, млн км')
r1 = float(input()) 

print('Полуось орбиты объекта назначения, млн км')
r2 = float(input()) 

print('Скорость ракеты, км/сек')
v1_sec = float(input()) 

print('Скорость объекта, км/с')
v2_sec = float(input()) 

print()
orb2 = round(r2*3.12*2)
print('Длина орбиты объекта '+str('{0:,}'.format(orb2).replace(',', ' '))+' млн км')

print() 
v1_hour = round(v1_sec*3600)
v1_day = round(v1_sec*3600*24)
v1_year = round(v1_sec*3600*24*365)

print('Скорость ракеты:')
print(str('{0:,}'.format(v1_hour).replace(',', ' '))+' км/ч')
print(str('{0:,}'.format(v1_day).replace(',', ' '))+' км/сут')
print(str('{0:,}'.format(v1_year).replace(',', ' '))+' км/год')

print()
v2_hour = round(v2_sec*3600)
v2_day = round(v2_sec*3600*24)
v2_year = round(v2_sec*3600*24*365)

print('Скорость объекта:')
print(str('{0:,}'.format(v2_hour).replace(',', ' '))+' км/ч')
print(str('{0:,}'.format(v2_day).replace(',', ' '))+' км/сут')
print(str('{0:,}'.format(v2_year).replace(',', ' '))+' км/год')

print()
t1_hour = round((r2-r1)*1000000/v1_hour)
t1_day = round((r2-r1)*1000000/v1_day)
t1_year = round((r2-r1)*1000000/v1_year)

print('Время движения ракеты до объекта:')
print(str('{0:,}'.format(t1_hour).replace(',', ' '))+' час.')
print(str('{0:,}'.format(t1_day).replace(',', ' '))+' сут.')
print(str('{0:,}'.format(t1_year).replace(',', ' '))+' год/лет')

print()
l2 = round(v2_hour*t1_hour/1000000)
print('Путь, пройденный объектом за время движения ракеты: '+str('{0:,}'.format(l2).replace(',', ' '))+' млн км')

l2_cent = round(l2*100/orb2)
print('Процент пройденного объектом пути: '+str(l2_cent)+' %')