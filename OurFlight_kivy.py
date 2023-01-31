from kivy.app import App
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget


class Container(Widget):
    def calculate(self):
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
        t1_hour = round((r2-r1)*1000000/v1_hour)  # время движения ракеты, час
        t1_day = round((r2-r1)*1000000/v1_day)  # время движения ракеты, сут
        t1_year = round((r2-r1)*1000000/v1_year, 1)  # время движения ракеты, год
        l2 = round(v2_hour*t1_hour/1000000)  # путь, пройденный объектом за время движения ракеты
        l2_cent = round(l2*100/orb2)  # процент от длины орбиты объекта, пройденный им

        self.lbl_orb2.text = 'Длина орбиты объекта '+str('{0:,}'.format(orb2).replace(',', ' '))+' км'
        self.lbl_v1_hour.text = str('{0:,}'.format(v1_hour).replace(',', ' '))+' км/ч'
        self.lbl_v1_day.text = str('{0:,}'.format(v1_day).replace(',', ' '))+' км/сут'
        self.lbl_v1_year.text = str('{0:,}'.format(v1_year).replace(',', ' '))+' км/год'
        self.lbl_v2_hour.text = str('{0:,}'.format(v2_hour).replace(',', ' '))+' км/ч'
        self.lbl_v2_day.text = str('{0:,}'.format(v2_day).replace(',', ' '))+' км/сут'
        self.lbl_v2_year.text = str('{0:,}'.format(v2_year).replace(',', ' '))+' км/год'
        self.lbl_t1_hour.text = str('{0:,}'.format(t1_hour).replace(',', ' '))+' час.'
        self.lbl_t1_day.text = str('{0:,}'.format(t1_day).replace(',', ' '))+' сут.'
        self.lbl_t1_year.text = str('{0:,}'.format(t1_year).replace(',', ' '))+' год/лет'
        self.lbl_l2.text = 'За время движения ракеты объект прошёл '+str('{0:,}'.format(l2).replace(',', ' '))+' млн км'
        self.lbl_l2_cent.text = 'Это составляет '+str(l2_cent)+' % от его орбиты'

class OurFlightApp(App):
    def build(self):
        return Container()
        

if __name__ == '__main__':
    OurFlightApp().run()
