from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivy.graphics import (Color, Line, Rectangle, Triangle, Ellipse)


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
            v2_day = round(v2_sec*3600*24)  # скорость объекта, км/сут
            v2_year = round(v2_sec*3600*24*365)  # скорость объекта, км/год
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
                self.lbl_v1.text = 'Скорость ракеты '+str('{0:,}'.format(v1_hour).replace(',', ' '))+' км/ч'
                self.lbl_v2.text = 'Скорость объекта '+str('{0:,}'.format(v2_hour).replace(',', ' '))+' км/ч'
                self.lbl_t1.text = 'Время движения ракеты '+str('{0:,}'.format(t1_hour).replace(',', ' '))+' час.'
            elif self.spn_t.text == 'сутки':
                self.lbl_v1.text = 'Скорость ракеты '+str('{0:,}'.format(v1_day).replace(',', ' '))+' км/сут'
                self.lbl_v2.text = 'Скорость объекта '+str('{0:,}'.format(v2_day).replace(',', ' '))+' км/сут'
                self.lbl_t1.text = 'Время движения ракеты '+str('{0:,}'.format(t1_day).replace(',', ' '))+' сут.'
            elif self.spn_t.text == 'год':
                self.lbl_v1.text = 'Скорость ракеты '+str('{0:,}'.format(v1_year).replace(',', ' '))+' км/год.'
                self.lbl_v2.text = 'Скорость объекта '+str('{0:,}'.format(v2_year).replace(',', ' '))+' км/год.'
                self.lbl_t1.text = 'Время движения ракеты '+str('{0:,}'.format(t1_year_year).replace(',', ' '))+' '+str(t1_year_name)+' '+str(t1_year_mon)+' мес.'
            self.lbl_l2.text = 'За это время объект прошёл '+str('{0:,}'.format(l2).replace(',', ' '))+' млн км.'
            self.lbl_l2_cent.text = 'Это составляет '+str(l2_cent)+' % от его орбиты.'
        except:
            self.lbl_orb2.text = 'Проверьте ввод.'
            self.lbl_v1.text = 'Проверьте ввод.'
            self.lbl_v2.text = 'Проверьте ввод.'
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
            # коэффициенты
            p = int(self.passengers.text)  # количество пассажиров
            c = int(self.cargo.text)  # масса груза в тоннах
            rub = 1_000_000  # рублей за единичный коэффициент
            
            # коэффициенты цели назначения
            if self.destination.text == 'Луна':
                d = 1
            elif self.destination.text == 'Марс':
                d = 2
            elif self.destination.text == 'Церера':
                d = 2.5
            elif self.destination.text == 'Ганимед' or 'Ио' or 'Калисто' or 'Европа':
                d = 3
            elif self.destination.text == 'Меркурий' or 'Венера' or 'Титан':
                d = 4
            elif self.destination.text == 'Титания':
                d = 5
            elif self.destination.text == 'Тритон':
                d = 6
            elif self.destination.text == 'Плутон':
                d = 7
            elif self.destination.text == 'Эрида':
                d = 8

                # коэффициенты тарифа
            if self.tariff.text == 'простой':
                t = 1
            elif self.tariff.text == 'быстрый':
                t = 2
            elif self.tariff.text == 'супербыстрый':
                t = 3

            price = d * p * c * t * rub  # без разделения на триады
            price2 = '{0:,}'.format(price).replace(',', ' ')  # с разделением на триады      
            self.price_select.text = price2
        except:
            self.price_select.text = 'Проверьте ввод.'

    # рисуем ракету
    def draw(self):
        with self.canvas.after:
            try:
                self.canvas.after.clear()
                centX = 550*0.5  # центр по оси X
                centY = 200  # центр низа 1 ступени по оси Y
                line_width = 1  # толщина линии
                con_h = int(self.con_h.text)  # высота конуса
                con_w = int(self.con_w.text)  # ширина конуса
                h3 = int(self.h3.text)  # высота 3 ступени
                h2 = int(self.h2.text)  # высота 2 ступени
                h1 = int(self.h1.text)  # высота 1 ступени
                side_h = int(self.side_h.text)  # высота бокового ускорителя
                side_w = int(self.side_w.text)  # ширина бокового ускорителя
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
                self.center_duse_tri = Line(points=(centX, centY,
                                                    centX+side_w*0.3, centY-h1*0.2,
                                                    centX-side_w*0.3, centY-h1*0.2), close=True, width=line_width)  # средний дюз
                self.side_right_duse_tri = Line(points=(centX+con_w*0.6+side_w*0.5, centY,
                                                        centX+con_w*0.6+side_w*0.2, centY-h1*0.2,
                                                        centX+con_w*0.6+side_w*0.8, centY-h1*0.2), close=True, width=line_width)  # правый дюз
            except:
                pass


class OurFlightApp(App):
    def build(self):
        return Container()
        

if __name__ == '__main__':
    OurFlightApp().run()