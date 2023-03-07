import math
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import (Line, Ellipse)


class Container(Widget):
    # параметры орбит
    def calculate(self):
        try:
            r1 = float(self.r1.text)
            r2 = float(self.r2.text)
            v1_sec = float(self.v1_sec.text)
            v2_sec = float(self.v2_sec.text)

            orb2 = round(r2*3.12*2)  # длина орбиты объекта
            v1_hour = round(v1_sec*3600)  # скорость ракеты, км/ч
            v1_day = round(v1_sec*3600*24)  # скорость ракеты, км/сут
            v1_year = round(v1_sec*3600*24*365)  # скорость ракеты, км/год
            v2_hour = round(v2_sec*3600)  # скорость объекта, км/ч
            t1_hour = round(abs(r2-r1)*1_000_000/v1_hour)  # время движения ракеты, час
            t1_day = round(abs(r2-r1)*1_000_000/v1_day)  # время движения ракеты, сут
            t1_year = round(abs(r2-r1)*1_000_000/v1_year, 1)  # время движения ракеты, год
            t1_year_year = round(abs(r2-r1)*1000000//v1_year)  # время движения ракеты, полных лет
            if 0.05 < (t1_year_year/10 - t1_year_year//10) < 0.15:
                t1_year_name = 'год'
            elif 0.15 < (t1_year_year/10 - t1_year_year//10) < 0.45:
                t1_year_name = 'года'
            else:
                t1_year_name = 'лет'
            t1_year_mon = round(abs(t1_year - t1_year_year)*12)  # время движения ракеты, месяцев после полных лет
            l2 = round(v2_hour*t1_hour/1_000_000)  # путь, пройденный объектом за время движения ракеты
            l2_cent = round(l2*100/orb2)  # процент от длины орбиты объекта, пройденный им

            self.lbl_orb2.text = 'Длина орбиты объекта '+str('{0:,}'.format(orb2).replace(',', ' '))+' млн км.'
            if self.spn_t.text == 'час':
                self.lbl_t1.text = 'Время движения ракеты '+str('{0:,}'.format(t1_hour).replace(',', ' '))+' час.'
            elif self.spn_t.text == 'сутки':
                self.lbl_t1.text = 'Время движения ракеты '+str('{0:,}'.format(t1_day).replace(',', ' '))+' сут.'
            elif self.spn_t.text == 'год':
                self.lbl_t1.text = 'Время движения ракеты '+str('{0:,}'.format(t1_year_year).replace(',', ' '))+' '+str(t1_year_name)+' '+str(t1_year_mon)+' мес.'
            self.lbl_l2.text = 'За это время объект прошёл '+str('{0:,}'.format(l2).replace(',', ' '))+' млн км.'
            self.lbl_l2_cent.text = 'Это составляет '+str(l2_cent)+' % от его орбиты.'
        except:
            self.lbl_orb2.text = 'Проверьте ввод.'
            self.lbl_t1.text = 'Проверьте ввод.'
            self.lbl_l2.text = 'Проверьте ввод.'
            self.lbl_l2_cent.text = 'Проверьте ввод.'


    # скорость из длины орбиты и периода обращения
    def vel0(self):
        try:
            if self.period0_time.text == 'час':
                v0 = round(((int(self.rad0.text) * 2 * 3.14 * 1_000_000) / (int(self.period0.text) * 3600)),1)
            elif self.period0_time.text == 'сут':
                v0 = round(((int(self.rad0.text) * 2 * 3.14 * 1_000_000) / (int(self.period0.text) * 3600 * 24)),1)
            elif self.period0_time.text == 'год':
                v0 = round(((int(self.rad0.text) * 2 * 3.14 * 1_000_000) / (int(self.period0.text) * 3600 * 24 * 365)),1)
            self.lbl_v0.text = '    '+str('{0:,}'.format(v0).replace(',', ' ')) + ' км/сек'
        except:
            self.lbl_v0.text = '    Проверьте ввод.'

    # перевод км/сек в другие единицы
    def vel3(self):
        try:
            if self.spn_v3.text == 'км/час':
                self.lbl_v3.text = ' '+str('{0:,}'.format(round(float(self.v3_sec.text)*3600)).replace(',', ' '))+' км/ч'
            elif self.spn_v3.text == 'км/сут':
                self.lbl_v3.text = ' '+str('{0:,}'.format(round(float(self.v3_sec.text)*3600*24)).replace(',', ' '))+' км/сут'
            elif self.spn_v3.text == 'км/год':
                self.lbl_v3.text = ' '+str('{0:,}'.format(round(float(self.v3_sec.text)*3600*24*365)).replace(',', ' '))+' км/год'
            print(self.lbl_v3.text)
        except:
            self.lbl_v3 = '    Проверьте ввод.'

    # перевод астрономические единиц в км
    def ae(self):
        try:
            ae = round(float(self.ae0.text) * 150)
            self.lbl_ae.text = '    '+str('{0:,}'.format(ae).replace(',', ' '))+' млн км'
        except:
            self.lbl_ae.text = '    Проверьте ввод.'

    # теорема Пифагора
    def pifagor(self):
        try:
            gipot = round(((int(self.cat1.text))**2 + (int(self.cat2.text))**2)**0.5)
            self.lbl_gipot.text = '    '+str('{0:,}'.format(gipot).replace(',', ' '))
        except:
            self.lbl_gipot.text = '     Проверьте ввод.'

        
    # стоимость полёта
    def on_destination_select(self):
        self.destination_select.text = 'Ваша цель: %s'%self.destination.text    

    def on_tariff_select(self):
        self.tariff_select.text = 'Тариф: %s'%self.tariff.text

    def on_passengers_select(self):
        self.passengers_select.text = 'Число пассажиров: %s'%self.passengers.text

    def on_cargo_select(self):
        self.cargo_select.text = 'Число тонн груза: %s'%self.cargo.text

    def priced(self):
        try:
            d = self.destination.text
            d_dict = {'Луна': 1, 'Марс': 2, 'Церера': 2.5, 'Ганимед': 3, 'Ио': 3, 'Калисто': 3, 'Европа': 3, 'Меркурий': 4,
                      'Венера': 4, 'Титан': 4, 'Титания': 5, 'Тритон': 6, 'Плутон': 7, 'Эрида': 8}   # коэффициенты цели
            if d in d_dict:
                i_d = d_dict[d]
            t = self.tariff.text
            t_dict = {'простой': 1, 'быстрый': 2, 'супербыстрый': 3}  # коэффициенты тарифа
            if t in t_dict:
                i_t = t_dict[t]
            p = int(self.passengers.text)  # количество пассажиров
            c = int(self.cargo.text)  # масса груза в тоннах
            rub = 1_000_000  # рублей за единичный коэффициент

            price = i_d * p * c * i_t * rub  # без разделения на триады
            price2 = '{0:,}'.format(price).replace(',', ' ')  # с разделением на триады      
            self.price_select.text = price2
        except:
            self.price_select.text = 'Проверьте ввод.'

    # рисуем ракету
    def draw_rocket(self):
        with self.canvas.after:
            try:
                self.canvas.after.clear()
                centX = 500  # центр по оси X
                centY = 400  # центр низа 1 ступени по оси Y
                line_width = 1  # толщина линии
                con_h = int(self.con_h.text)  # высота конуса
                con_w = int(self.con_w.text)  # ширина конуса
                h3 = int(self.h3.text)  # высота 3 ступени
                h2 = int(self.h2.text)  # высота 2 ступени
                h1 = int(self.h1.text)  # высота 1 ступени
                side_h = int(self.side_h.text)  # высота бокового ускорителя
                side_w = int(self.side_w.text)  # ширина бокового ускорителя
                n_dus = int(self.n_dus.text)  # количество сопел
                self.con = Line(points=(centX, centY+h1+h2+h3+con_h,
                                        centX+con_w*0.6, centY+h1+h2+h3+con_h*0.5,
                                        centX+con_w*0.6, centY+h1+h2+h3+con_h*0.1,
                                        centX+con_w*0.5, centY+h1+h2+h3,
                                        centX-con_w*0.5, centY+h1+h2+h3,
                                        centX-con_w*0.6, centY+h1+h2+h3+con_h*0.1,
                                        centX-con_w*0.6, centY+h1+h2+h3+con_h*0.5), close=True, width=line_width)  # конус
                self.illuminator = Ellipse(pos=(centX-con_w*0.1, centY+h1+h2+h3+con_h*0.3), size=(con_w*0.2, con_w*0.2))  # иллюминатор
                self.h3_rect = Line(points=(centX+con_w*0.5, centY+h1+h2+h3,
                                            centX+con_w*0.5, centY+h1+h2,
                                            centX-con_w*0.5, centY+h1+h2,
                                            centX-con_w*0.5, centY+h1+h2+h3), close=True, width=line_width)  # 3 ступень
                self.wing_left = Line(points=(centX-con_w*0.5, centY+h1+h2+h3*0.6,
                                              centX-con_w*0.5, centY+h1+h2+h3*0.3,
                                              centX-con_w*0.8, centY+h1+h2+h3*0.3), close=True, width=line_width)  # левое крыло
                self.wing_right = Line(points=(centX+con_w*0.5, centY+h1+h2+h3*0.6,
                                              centX+con_w*0.5, centY+h1+h2+h3*0.3,
                                              centX+con_w*0.8, centY+h1+h2+h3*0.3), close=True, width=line_width)  # правое крыло
                self.h2_rect = Line(points=(centX+con_w*0.55, centY+h1+h2,
                                            centX+con_w*0.55, centY+h1,
                                            centX-con_w*0.55, centY+h1,
                                            centX-con_w*0.55, centY+h1+h2), close=True, width=line_width)  # 2 ступень
                self.h1_rect = Line(points=(centX+con_w*0.6, centY+h1,
                                            centX+con_w*0.6, centY,
                                            centX-con_w*0.6, centY,
                                            centX-con_w*0.6, centY+h1), close=True, width=line_width)  # 1 ступень
                self.side_left_tri = Line(points=(centX-con_w*0.6-side_w*0.5, centY+side_h*1.3,
                                                  centX-con_w*0.6, centY+side_h,
                                                  centX-con_w*0.6-side_w, centY+side_h), close=True, width=line_width)  # кон.лев.бок.ускор.
                self.side_left_rect = Line(points=(centX-con_w*0.6, centY+side_h,
                                                   centX-con_w*0.6, centY,
                                                   centX-con_w*0.6-side_w, centY,
                                                   centX-con_w*0.6-side_w, centY+side_h), close=True, width=line_width)  # левый бок.ускор.
                self.side_right_tri = Line(points=(centX+con_w*0.6+side_w*0.5, centY+side_h*1.3,
                                                   centX+con_w*0.6, centY+side_h,
                                                   centX+con_w*0.6+side_w, centY+side_h), close=True, width=line_width)  # кон.прав.бок.ускор.
                self.side_right_rect = Line(points=(centX+con_w*0.6, centY+side_h,
                                                   centX+con_w*0.6, centY,
                                                   centX+con_w*0.6+side_w, centY,
                                                   centX+con_w*0.6+side_w, centY+side_h), close=True, width=line_width)  #  правый бок.ускор.
                self.side_left_duse_tri = Line(points=(centX-con_w*0.6-side_w*0.5, centY,
                                                       centX-con_w*0.6-side_w*0.2, centY-h1*0.2,
                                                       centX-con_w*0.6-side_w*0.8, centY-h1*0.2), close=True, width=line_width)  # левый дюз
                self.side_right_duse_tri = Line(points=(centX+con_w*0.6+side_w*0.5, centY,
                                                        centX+con_w*0.6+side_w*0.2, centY-h1*0.2,
                                                        centX+con_w*0.6+side_w*0.8, centY-h1*0.2), close=True, width=line_width)  # правый дюз
                for i_dus in range(1, n_dus+1):
                    self.duse = Line(points=(centX-con_w*0.6+(con_w*1.2/(n_dus+1))*i_dus, centY,
                                             centX-con_w*0.6+(con_w*1.2/(n_dus+1)*i_dus-side_w*0.3), centY-h1*0.2,
                                             centX-con_w*0.6+(con_w*1.2/(n_dus+1)*i_dus+side_w*0.3), centY-h1*0.2), close=True, width=line_width)  # средние дюзы
            except:
                pass

    # стираем ракету
    def clear_rocket(self):
        with self.canvas.after:
            self.canvas.after.clear()

    # строим траекторию
    def pathed(self):
        try:
            rad01 = int(self.rad01.text)
            rad02 = int(self.rad02.text)
            alf = float(self.alf.text)*3.14159/180  # угол начального положения ракеты в радианах
            bet1 = float(self.bet1.text)*3.14159/180  # угол начального положения объекта в радианах
            t00 = int(self.t00.text) if self.p00.text == 'сут' else int(self.t00.text)*365  # предполагаемое время прибытия на объект
            t02 = int(self.t02.text) if self.p02.text == 'сут' else int(self.t02.text)*365  # сидерический период

            bet2 = bet1+t02*6.28/t00  # угол конечного положения объекта в радианах
            l1 = ((rad02*math.cos(bet2)-rad01*math.cos(alf))**2+
                      ((rad02*math.sin(bet2)-rad01*math.sin(alf))**2))**0.5  # длина пути ракеты по теореме Пифагора
            self.lbl_l1.text = 'Длина пути ракеты '+str(round(l1))+' млн.км'
            self.lbl_v1.text = 'Скорость ракеты '+str(('{0:,}'.format(round(l1*1_000_000/(t02*3600*24), 1))).replace(',', ' '))+' км/сек'
            acos0 = math.acos((rad02*math.cos(bet2)-rad01*math.cos(alf))/l1)  # угол направления ракеты
            if bet2 >= 6.28319:  # если объект прошёл больше одного круга
                bet2 = bet2%6.28319
            if 0 < bet2 < alf or (3.14159-alf) < bet2 < 6.28319:  # если ракета севернее конечного положения объекта
                acos0 = -acos0 
            self.lbl_bet2.text = 'Курс ракеты '+str(round((acos0)*57.2958))+' град.'  # курс ракеты
        except:
            self.lbl_l1.text = 'Проверьте ввод.'
            self.lbl_v1.text = 'Проверьте ввод.'
            self.lbl_bet2.text = 'Проверьте ввод.'


class OurFlightApp(App):
    def build(self):
        return Container()
        

if __name__ == '__main__':
    OurFlightApp().run()