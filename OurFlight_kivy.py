import math
from kivy.app import App
from kivy.uix.checkbox import CheckBox
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.widget import Widget
from kivy.graphics import (Color, Ellipse, Line)


class Container(TabbedPanel): 
    # строим траекторию
    def pathed(self):
        try:
            global rad01, rad02, alf , bet1, t00, t02, bet2, l1, acos0
           
            rad01 = int(self.rad01.text)
            rad02 = int(self.rad02.text)
            alf = float(self.alf.text)*3.14159/180  
            bet1 = float(self.bet1.text)*3.14159/180
            t00 = int(self.t00.text) if self.spn_p00.text == 'сут' else int(self.t00.text)*365
            t02 = int(self.t02.text) if self.spn_p02.text == 'сут' else int(self.t02.text)*365 

            # значения для разработки
            # rad01 = 150
            # rad02 = 228
            # alf = 30*0.1745 
            # bet1 = 45*0.1745
            # t00 = 689
            # t02 = 489

            bet2 = bet1+t02*6.28/t00  
            l1 = ((rad02*math.cos(bet2)-rad01*math.cos(alf))**2+
                      ((rad02*math.sin(bet2)-rad01*math.sin(alf))**2))**0.5  # длина пути ракеты по теореме Пифагора
            self.lbl_l1.text = 'Длина пути ракеты '+str(round(l1))+' млн.км'
            self.lbl_v1.text = 'Скорость ракеты '+str(('{0:,}'.format(round(l1*1_000_000/(t02*3600*24), 1))).replace(',', ' '))+' км/сек'
            acos0 = math.acos((rad02*math.cos(bet2)-rad01*math.cos(alf))/l1)  # угол направления ракеты в радианах
            if bet2 >= 6.28319:  # если объект прошёл больше одного круга
                bet2 = bet2%6.28319
            if 0 < bet2 < alf or (3.14159-alf) < bet2 < 6.28319:  # если ракета севернее конечного положения объекта
                acos0 = -acos0 
            self.lbl_bet2.text = 'Курс ракеты '+str(round((acos0)*57.2958))+' град.'  # курс ракеты
        except:
            self.lbl_l1.text = 'Проверьте ввод.'
            self.lbl_v1.text = 'Проверьте ввод.'
            self.lbl_bet2.text = 'Проверьте ввод.'
        
    # чертим траекторию
    def draw_path(self):
        with self.canvas.after:
            try:
                self.canvas.after.clear()
                sunX = 350  # центр координат по X
                sunY = 700  # центр координат по Y
                maxrad = 250  # радиус бОльшей орбиты
                # sunY = 320  # временный центр координат по Y для разработки
                # maxrad = 120  # временный радиус бОльшей орбиты для разработки
                Ra = maxrad/max(rad01, rad02)  # коэффициент под размер экрана
                minrad = Ra*(min(rad01, rad02))  # радиус меньшей орбиты
                self.orbit2 = Ellipse(pos=(sunX-maxrad, sunY-maxrad), size=(maxrad*2, maxrad*2), color=Color(1, 1, 1))  # орбита 2
                self.orbit2a = Ellipse(pos=(sunX-maxrad+1, sunY-maxrad+1), size=(maxrad*2-2, maxrad*2-2), color=Color(0, 0.05, 0.1))  # линия орбиты 2
                self.orbit1 = Ellipse(pos=(sunX-minrad, sunY-minrad), size=(minrad*2, minrad*2), color=Color(1, 1, 1))  # орбита 1
                self.orbit1a = Ellipse(pos=(sunX-minrad+1, sunY-minrad+1), size=(minrad*2-2, minrad*2-2), color=Color(0, 0.05, 0.1))  # линия орбиты 1
                self.axX = Line(points=(sunX, sunY+maxrad+20, sunX, sunY-maxrad-20), 
                                color=Color(1,1,1), width=1)  # ось X
                self.axX = Line(points=(sunX+maxrad+20, sunY, sunX-maxrad-20, sunY), 
                                color=Color(1,1,1), width=1)  # ось Y
                self.orbit_center = Ellipse(pos=(sunX-10, sunY-10), size=(20, 20), color=Color(0.98, 0.98, 0.73))  # центр                    
                self.path = Line(points=(sunX+rad01*R*math.cos(alf), sunY+rad01*R*math.sin(alf),
                                        sunX+rad02*R*math.cos(bet2), sunY+rad02*R*math.sin(bet2)), 
                                        color=Color(0,0,1), width=2)
                self.obj_start = Ellipse(pos=(sunX+rad02*R*math.cos(bet1)-10, sunY+rad02*R*math.sin(bet1)-10), 
                                         size=(20, 20), color=Color(1, 0, 0))  # координаты старта объекта
                self.obj_start_a = Ellipse(pos=(sunX+rad02*R*math.cos(bet1)-9, sunY+rad02*R*math.sin(bet1)-9), 
                                           size=(18, 18), color=Color(0, 0.05, 0.1))  # координаты старта объекта (заливка)
                self.finish = Ellipse(pos=(sunX+rad02*R*math.cos(bet2)-10, sunY+rad02*R*math.sin(bet2)-10), 
                                      size=(20, 20), color=Color(1, 0, 0))  # координаты финиша объекта и ракеты
                self.rocket_start = Ellipse(pos=(sunX+rad01*R*math.cos(alf)-10, sunY+rad01*R*math.sin(alf)-10), 
                                            size=(20, 20), color=Color(0, 0, 1))  # координаты старта ракеты
            except:
                pass

    # стираем траекторию
    def clear_path(self):
        with self.canvas.after:
            self.canvas.after.clear()

    # чертим ракету
    def draw_rocket(self):
        with self.canvas.after:
            try:
                self.canvas.after.clear()

                # временные параметры ракеты для разработки
                # centX = 500  # центр по оси X
                # centY = 200  # центр низа 1 ступени по оси Y
                # line_width = 1  # толщина линии
                # con_h = 50  # высота конуса
                # con_w = 50  # ширина конуса
                # h3 = 50  # высота 3 ступени
                # h2 = 50  # высота 2 ступени
                # h1 = 50  # высота 1 ступени
                # side_h = 40  # высота бокового ускорителя
                # side_w = 30  # ширина бокового ускорителя
                # n_dus = 3  # количество сопел

                centX = 500  # центр по оси X
                centY = 200  # центр низа 1 ступени по оси Y
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
                                        centX-con_w*0.6, centY+h1+h2+h3+con_h*0.5), 
                                        close=True, width=line_width, color=Color(1, 1, 1))  # конус
                self.illuminator = Ellipse(pos=(centX-con_w*0.1, centY+h1+h2+h3+con_h*0.3), 
                                           size=(con_w*0.2, con_w*0.2), color=Color(1, 1, 1))  # иллюминатор
                self.h3_rect = Line(points=(centX+con_w*0.5, centY+h1+h2+h3,
                                            centX+con_w*0.5, centY+h1+h2,
                                            centX-con_w*0.5, centY+h1+h2,
                                            centX-con_w*0.5, centY+h1+h2+h3), 
                                            close=True, width=line_width, color=Color(1, 1, 1))  # 3 ступень
                self.wing_left = Line(points=(centX-con_w*0.5, centY+h1+h2+h3*0.6,
                                              centX-con_w*0.5, centY+h1+h2+h3*0.3,
                                              centX-con_w*0.8, centY+h1+h2+h3*0.3), 
                                              close=True, width=line_width, color=Color(1, 1, 1))  # левое крыло
                self.wing_right = Line(points=(centX+con_w*0.5, centY+h1+h2+h3*0.6,
                                              centX+con_w*0.5, centY+h1+h2+h3*0.3,
                                              centX+con_w*0.8, centY+h1+h2+h3*0.3), 
                                              close=True, width=line_width, color=Color(1, 1, 1))  # правое крыло
                self.h2_rect = Line(points=(centX+con_w*0.55, centY+h1+h2,
                                            centX+con_w*0.55, centY+h1,
                                            centX-con_w*0.55, centY+h1,
                                            centX-con_w*0.55, centY+h1+h2), 
                                            close=True, width=line_width, color=Color(1, 1, 1))  # 2 ступень
                self.h1_rect = Line(points=(centX+con_w*0.6, centY+h1,
                                            centX+con_w*0.6, centY,
                                            centX-con_w*0.6, centY,
                                            centX-con_w*0.6, centY+h1), 
                                            close=True, width=line_width, color=Color(1, 1, 1))  # 1 ступень
                self.side_left_tri = Line(points=(centX-con_w*0.6-side_w*0.5, centY+side_h*1.3,
                                                  centX-con_w*0.6, centY+side_h,
                                                  centX-con_w*0.6-side_w, centY+side_h), 
                                                  close=True, width=line_width, color=Color(1, 1, 1))  # кон.лев.бок.ускор.
                self.side_left_rect = Line(points=(centX-con_w*0.6, centY+side_h,
                                                   centX-con_w*0.6, centY,
                                                   centX-con_w*0.6-side_w, centY,
                                                   centX-con_w*0.6-side_w, centY+side_h), 
                                                   close=True, width=line_width, color=Color(1, 1, 1))  # левый бок.ускор.
                self.side_right_tri = Line(points=(centX+con_w*0.6+side_w*0.5, centY+side_h*1.3,
                                                   centX+con_w*0.6, centY+side_h,
                                                   centX+con_w*0.6+side_w, centY+side_h), 
                                                   close=True, width=line_width, color=Color(1, 1, 1))  # кон.прав.бок.ускор.
                self.side_right_rect = Line(points=(centX+con_w*0.6, centY+side_h,
                                                   centX+con_w*0.6, centY,
                                                   centX+con_w*0.6+side_w, centY,
                                                   centX+con_w*0.6+side_w, centY+side_h), 
                                                   close=True, width=line_width, color=Color(1, 1, 1))  #  правый бок.ускор.
                self.side_left_duse_tri = Line(points=(centX-con_w*0.6-side_w*0.5, centY,
                                                       centX-con_w*0.6-side_w*0.2, centY-h1*0.2,
                                                       centX-con_w*0.6-side_w*0.8, centY-h1*0.2), 
                                                       close=True, width=line_width, color=Color(1, 1, 1))  # левый дюз
                self.side_right_duse_tri = Line(points=(centX+con_w*0.6+side_w*0.5, centY,
                                                        centX+con_w*0.6+side_w*0.2, centY-h1*0.2,
                                                        centX+con_w*0.6+side_w*0.8, centY-h1*0.2), 
                                                        close=True, width=line_width, color=Color(1, 1, 1))  # правый дюз
                for i_dus in range(1, n_dus+1):
                    self.duse = Line(points=(centX-con_w*0.6+(con_w*1.2/(n_dus+1))*i_dus, centY,
                                             centX-con_w*0.6+(con_w*1.2/(n_dus+1)*i_dus-side_w*0.3), centY-h1*0.2,
                                             centX-con_w*0.6+(con_w*1.2/(n_dus+1)*i_dus+side_w*0.3), centY-h1*0.2), 
                                             close=True, width=line_width, color=Color(1, 1, 1))  # средние дюзы
            except:
                pass

    # стираем ракету
    def clear_rocket(self):
        with self.canvas.after:
            self.canvas.after.clear()

    # параметры орбит
    def circum(self):
        try:
            rad = float(self.rad.text)
            orb = round(rad*3.12*2)  # длина орбиты объекта
            self.lbl_orb.text = '   '+str('{0:,}'.format(orb).replace(',', ' '))+' млн км.'
        except:
            self.lbl_orb.text = 'Проверьте ввод.'

    # скорость из длины орбиты и периода обращения
    def vel0(self):
        try:
            if self.period0_time.text == 'час':
                v0 = round(((int(self.rad.text) * 2 * 3.14 * 1_000_000) / (int(self.period0.text) * 3600)),1)
            elif self.period0_time.text == 'сут':
                v0 = round(((int(self.rad.text) * 2 * 3.14 * 1_000_000) / (int(self.period0.text) * 3600 * 24)),1)
            elif self.period0_time.text == 'год':
                v0 = round(((int(self.rad.text) * 2 * 3.14 * 1_000_000) / (int(self.period0.text) * 3600 * 24 * 365)),1)
            self.lbl_v0.text = '    '+str('{0:,}'.format(v0).replace(',', ' ')) + ' км/сек'
        except:
            self.lbl_v0.text = '    Проверьте ввод.'

    # перевод км/сек в другие единицы
    def vel3(self):
        try:
            v3_sec = int(self.v3_sec.text)
            v3 = self.spn_v3.text
            v3_dict = {'км/час': 1, 'км/сут': 24, 'км/год': 24*365}
            if v3 in v3_dict:
                i_v3 = v3_dict[v3]
            self.lbl_v3.text = '    '+str('{0:,}'.format(round(float(v3_sec)*3600*i_v3)).replace(',', ' '))+' '+str(v3)
        except:
            self.lbl_v3.text = '    Проверьте ввод.'

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
    def on_start_select(self):
        self.lbl_start.text = 'Ваш старт: '+self.spn_start.text

    def on_destination_select(self):
        self.lbl_destination.text = 'Ваша цель: '+self.spn_destination.text    

    def on_side_select(self):
        self.lbl_side.text = 'Стороны от центра: '+self.spn_side.text

    def on_tariff_select(self):
        self.lbl_tariff.text = 'Тариф: '+self.spn_tariff.text

    def on_passengers_select(self):
        self.lbl_passengers.text = 'Число пассажиров: '+self.spn_passengers.text

    def on_cargo_select(self):
        self.lbl_cargo.text = 'Число тонн груза: '+self.spn_cargo.text

    def priced(self):
        try:
            s = self.spn_start.text  # стартовый объект
            d = self.spn_destination.text  # объект назначения
            sun_dict = {'Земля': 150, 'Луна': 149, 'Меркурий': 58, 'Венера': 108, 'Марс': 228, 'Церера': 414, 'Ио': 778, 'Европа': 778, 
                        'Ганимед': 778, 'Каллисто': 778,  'Титан': 1430, 'Титания': 2877, 'Тритон': 4503, 'Плутон': 5900, 
                        'Эрида': 10200}   # полуоси объектов
            earth_dict = {'Земля': 0, 'Луна': 1}
            jupiter_dict = {'Ио': 1, 'Европа': 2, 'Ганимед': 3, 'Каллисто': 4}
            if s and d in sun_dict:
                i_s = sun_dict[s]
                i_d = sun_dict[d]
            elif s and d in earth_dict:  # если старт и финиш в локальной системе Земли
                i_s = earth_dict[s]
                i_d = earth_dict[d]
            elif s and d in jupiter_dict:  # если старт и финиш в локальной системе Юпитера
                i_s = jupiter_dict[s]
                i_d = jupiter_dict[d]
            side = self.spn_side.text  # сторона относительно центра
            t = self.spn_tariff.text
            t_dict = {'простой': 1, 'быстрый': 2, 'супербыстрый': 3}  # коэффициенты тарифа
            if t in t_dict:
                i_t = t_dict[t]
            p = int(self.spn_passengers.text)  # количество пассажиров
            c = int(self.spn_cargo.text)  # масса груза в тоннах
            rub = 100_000  # рублей за единичный коэффициент
            if side == 'одна':
                delta_d_s = abs(i_d - i_s)
            else:
                delta_d_s = abs(i_d + i_s)
            price = delta_d_s * p * c * i_t * rub  # без разделения на триады
            price2 = '{0:,}'.format(price).replace(',', ' ')  # с разделением на триады      
            self.lbl_price.text = price2
        except:
            self.lbl_price.text = 'Проверьте ввод.'

    
class OurFlightApp(App):
    def build(self):
        return Container()
        

if __name__ == '__main__':
    OurFlightApp().run()