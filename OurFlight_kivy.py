import math
from kivy.app import App
from kivy.uix.checkbox import CheckBox
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.widget import Widget
from kivy.graphics import (Line, Ellipse)


class Container(TabbedPanel): 
    # строим траекторию
    def pathed(self):
        try:
            rad01 = int(self.rad01.text)
            rad02 = int(self.rad02.text)
            alf = float(self.alf.text)*3.14159/180  # угол начального положения ракеты в радианах
            bet1 = float(self.bet1.text)*3.14159/180  # угол начального положения объекта в радианах
            t00 = int(self.t00.text) if self.spn_p00.text == 'сут' else int(self.t00.text)*365  # предполагаемое время прибытия на объект
            t02 = int(self.t02.text) if self.spn_p02.text == 'сут' else int(self.t02.text)*365  # сидерический период

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
    
    # временные значения по умолчанию для разработки
    def checkbox(self, value):
        if value == True:
            rad01 = 150
            rad02 = 228
            alf = 30*3.14159/180  
            bet1 = 45*3.14159/180 
            t00 = 689
            t02 = 689

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
        
    # чертим траекторию
    def draw_path(self):
        with self.canvas.after:
            try:
                self.canvas.after.clear()
                rad01 = int(self.rad01.text)
                rad02 = int(self.rad02.text)
                alf = float(self.alf.text)*3.14159/180  # угол начального положения ракеты в радианах
                bet1 = float(self.bet1.text)*3.14159/180  # угол начального положения объекта в радианах
                t00 = int(self.t00.text) if self.spn_p00.text == 'сут' else int(self.t00.text)*365  # предполагаемое время прибытия на объект
                t02 = int(self.t02.text) if self.spn_p02.text == 'сут' else int(self.t02.text)*365  # сидерический период
                bet2 = bet1+t02*6.28/t00  # угол конечного положения объекта в радианах

                sunX = 400
                sunY = 500
                self.orbit1 = Ellipse(pos=(sunX-rad01, sunY-rad01), size=(rad01*2, rad01*2))
                # self.orbit2 = Ellipse(pos=(), size=())
                self.path = Line(points=((sunX+rad01)*math.cos(alf), (sunY+rad01)*math.sin(alf),
                                        (sunX+rad02)*math.cos(bet2), (sunY+rad02)*math.sin(bet2)))
                
                # self.path = Line(points=(rad01*math.cos(alf), rad01*math.sin(alf),
                #                         rad02*math.cos(bet2), rad02*math.sin(bet2)))
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
        self.lbl_start.text = 'Ваш старт: '+self.start.text

    def on_destination_select(self):
        self.lbl_destination.text = 'Ваша цель: '+self.destination.text    

    def on_tariff_select(self):
        self.lbl_tariff.text = 'Тариф: '+self.tariff.text

    def on_passengers_select(self):
        self.lbl_passengers.text = 'Число пассажиров: '+self.passengers.text

    def on_cargo_select(self):
        self.lbl_cargo.text = 'Число тонн груза: '+self.cargo.text

    def priced(self):
        try:
            s = self.start.text  # стартовый объект
            d = self.destination.text  # объект назначения
            s_d_dict = {'Земля': 150, 'Луна': 149, 'Меркурий': 58, 'Венера': 108, 'Марс': 228, 'Церера': 414, 'Ганимед': 778, 
                        'Ио': 779, 'Калисто': 780, 'Европа': 781, 'Титан': 1430, 'Титания': 2877, 'Тритон': 4503, 'Плутон': 5900, 
                        'Эрида': 10200}   # коэффициенты объектов
            if s in s_d_dict:
                i_s = s_d_dict[s]
            if d in s_d_dict:
                i_d = s_d_dict[d]
            t = self.tariff.text
            t_dict = {'простой': 1, 'быстрый': 2, 'супербыстрый': 3}  # коэффициенты тарифа
            if t in t_dict:
                i_t = t_dict[t]
            p = int(self.passengers.text)  # количество пассажиров
            c = int(self.cargo.text)  # масса груза в тоннах
            rub = 10_000  # рублей за единичный коэффициент

            price = abs(i_d-i_s) * p * c * i_t * rub  # без разделения на триады
            price2 = '{0:,}'.format(price).replace(',', ' ')  # с разделением на триады      
            self.lbl_price.text = price2
        except:
            self.lbl_price.text = 'Проверьте ввод.'

    
class OurFlightApp(App):
    def build(self):
        return Container()
        

if __name__ == '__main__':
    OurFlightApp().run()