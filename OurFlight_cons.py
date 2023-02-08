r1 = float(input('Полуось орбиты точки вылета, млн км  ')) 

r2 = float(input('Полуось орбиты объекта назначения, млн км  ')) 

v1_sec = float(input('Скорость ракеты, км/сек  ')) 

v2_sec = float(input('Скорость объекта, км/с  ')) 

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
t1_hour = round(abs(r2-r1)*1000000/v1_hour)
t1_day = round(abs(r2-r1)*1000000/v1_day)
t1_year = round(abs(r2-r1)*1000000/v1_year, 1)
t1_year_year = round(abs(r2-r1)*1000000//v1_year)
if 0.05 < (t1_year_year/10 - t1_year_year//10) < 0.15:
    t1_year_name = 'год'
elif 0.15 < (t1_year_year/10 - t1_year_year//10) < 0.45:
    t1_year_name = 'года'
else:
    t1_year_name = 'лет'
t1_year_mon = round(abs(t1_year - t1_year_year)*12)

print('Время движения ракеты до объекта:')
print(str('{0:,}'.format(t1_hour).replace(',', ' '))+' час.')
print(str('{0:,}'.format(t1_day).replace(',', ' '))+' сут.')
print(str('{0:,}'.format(t1_year_year).replace(',', ' '))+' '+str(t1_year_name)+' '+str(t1_year_mon)+' мес.')

print()
l2 = round(v2_hour*t1_hour/1000000)
print('Путь, пройденный объектом за время движения ракеты: '+str('{0:,}'.format(l2).replace(',', ' '))+' млн км')

l2_cent = round(l2*100/orb2)
print('Процент пройденного объектом пути: '+str(l2_cent)+' %')