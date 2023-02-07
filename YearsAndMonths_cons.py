# Часть кода из OurFlight для выбора правильного варианта "год/года/лет" и указания количества полных лет и месяцев.
# Имена переменных соответствуют таковым к первоначальном коде.
t1_year = float(input('Количество лет с десятичной дробью: '))
t1_year_year = round(t1_year*10//10)  # полных лет
if 0.05 < (t1_year_year/10 - t1_year_year//10) < 0.15:
    t1_year_name = 'год'
elif 0.15 < (t1_year_year/10 - t1_year_year//10) < 0.45:
    t1_year_name = 'года'
else:
    t1_year_name = 'лет'
t1_year_mon = round(abs(t1_year - t1_year_year)*12)
print(str(t1_year_year)+' '+str(t1_year_name)+' '+str(t1_year_mon)+' мес.')