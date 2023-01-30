from kivy.app import App
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

Window.clearcolor = (0, 0, 0.1, 1.0)

class Container(Widget):

    rad = ObjectProperty(None)
    period = ObjectProperty(None)
    dimention = ObjectProperty(None)
    lbl_rad = ObjectProperty(None)
    lbl_sec = ObjectProperty(None)
    lbl_hour = ObjectProperty(None)
    lbl_day = ObjectProperty(None)
    lbl_year = ObjectProperty(None)

    def calculate(self):
        try:
            r = int(self.rad.text)  # радиус
            p = int(self.period.text)  # период обращения
        except:
            r = 0  # если не введут значения
            p = 1
        circumference = round(r * 3.14 * 2)
        circumference2 = '{0:,}'.format(circumference).replace(',', '  ')  # с разделением на триады

        pp = (r * 3.14 * 2) / p  # скорость без учёта размерности
        if self.dimention.text == 'час':
            speed_sec = round(pp / 3600)
            speed_hour = round(pp)
            speed_day = round(pp * 24)
            speed_year = round(pp * 24 * 365)
        elif self.dimention.text == 'сут':
            speed_sec = round(pp / (3600 * 24))
            speed_hour = round(pp / 24)
            speed_day = round(pp)
            speed_year = round(pp * 365)
        elif self.dimention.text == 'год':
            speed_sec = round(pp / (3600 * 24 * 365))
            speed_hour = round(pp / (24 * 365))
            speed_day = round(pp / 365)
            speed_year = round(pp)
        
        speed2_sec = '{0:,}'.format(speed_sec).replace(',', '  ')  # скорости с триадами
        speed2_hour = '{0:,}'.format(speed_hour).replace(',', '  ')
        speed2_day = '{0:,}'.format(speed_day).replace(',', '  ')
        speed2_year = '{0:,}'.format(speed_year).replace(',', '  ')

        self.lbl_rad.text = 'Длина орбиты  '+circumference2+'  км'
        self.lbl_sec.text = 'Скорость  '+speed2_sec+'  км/сек'
        self.lbl_hour.text = 'Скорость  '+speed2_hour+'  км/час'
        self.lbl_day.text = 'Скорость  '+speed2_day+'  км/сут'
        self.lbl_year.text = 'Скорость  '+speed2_year+'  км/год'


class PlanetOptionsApp(App):
    def build(self):
        return Container()
        

if __name__ == '__main__':
    PlanetOptionsApp().run()