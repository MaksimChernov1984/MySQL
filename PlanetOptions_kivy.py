from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.config import Config

Window.clearcolor = (0, 0, 0.1, 1.0)
Window.size = (480, 853)
Config.set('kivy', 'keyboard_mode', 'systemanddoc')


class PlanetoptionsApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        layout1 = BoxLayout() 
        self.lbl = Label(text='Параметры тел Солнечной системы', font_size=20, halign='center', valign='middle')        
        layout1.add_widget(self.lbl) 

        # ввод радиуса
        layout2 = BoxLayout()
        self.lbl = Label(text='Большая\nполуось:', font_size=20, halign='center', valign='bottom')
        layout2.add_widget(self.lbl) 
        self.rad = TextInput(multiline='False', halign='center', font_size=20)
        layout2.add_widget(self.rad)
        self.lbl = Label(text='км', font_size=20, halign='left', valign='bottom')
        layout2.add_widget(self.lbl) 

        # ввод периода обращения
        layout3 = BoxLayout()
        self.lbl = Label(text='Период\nобращения:', font_size=20, halign='center', valign='middle')
        layout3.add_widget(self.lbl)
        self.period = TextInput(multiline='False', halign='center', font_size=20)
        layout3.add_widget(self.period)
        self.dimention = Spinner(text='размерность', values=('км/сек', 'км/час', 'км/сут', 'км/год'), font_size=20, 
            halign='center', valign='middle', background_color=(0.9, 0.1, 0.1, 1), background_normal='')
        layout3.add_widget(self.dimention)

        # кнопка Вычислить
        layout4 = BoxLayout(padding=20, size_hint=(1, 3))
        self.btn_rad = Button(text='Вычислить', font_size=20, halign='center', valign='middle',
            background_color=(0.9, 0.1, 0.1, 1), background_normal='', on_press=self.calculate) 
        layout4.add_widget(self.btn_rad)

        # длина орбиты
        layout5 = BoxLayout()
        self.lbl_rad = Label(text='Длина орбиты...', font_size=20, halign='center', valign='middle')
        layout5.add_widget(self.lbl_rad)   

        # размерности периода обращения
        layout6 = BoxLayout()
        self.lbl_sec = Label(text='Скорость в км/сек...', font_size=20, halign='center', valign='middle')
        layout6.add_widget(self.lbl_sec)
        layout7 = BoxLayout()
        self.lbl_hour = Label(text='Скорость в км/час...', font_size=20, halign='center', valign='middle')
        layout7.add_widget(self.lbl_hour)
        layout8 = BoxLayout()
        self.lbl_day= Label(text='Скорость в км/сутки...', font_size=20, halign='center', valign='middle')
        layout8.add_widget(self.lbl_day)
        layout9 = BoxLayout()
        self.lbl_year= Label(text='Скорость в км/год...', font_size=20, halign='center', valign='middle')
        layout9.add_widget(self.lbl_year)    

        # вывод всех блоков
        layout.add_widget(layout1)
        layout.add_widget(layout2)
        layout.add_widget(layout3)
        layout.add_widget(layout4)
        layout.add_widget(layout5)
        layout.add_widget(layout6)
        layout.add_widget(layout7)
        layout.add_widget(layout8)
        layout.add_widget(layout9)
        return layout
        
    def calculate(self, obj):
        try:
            r = int(self.rad.text)  # радиус
            p = int(self.period.text)  # период обращения
        except:
            r = 0  # если не введут значения
            p = 1
        circumference = round(r * 3.14 * 2)
        circumference2 = '{0:,}'.format(circumference).replace(',', '  ')  # с разделением на триады

        pp = (r * 3.14 * 2) / p  # скорость без учёта размерности
        if self.dimention.text == 'км/сек':
            speed_sec = round(pp)
            speed_hour = round(pp * 3600)
            speed_day = round(pp * 3600 * 24)
            speed_year = round(pp * 3600 *24 * 365)
        elif self.dimention.text == 'км/час':
            speed_sec = round(pp / 3600)
            speed_hour = round(pp)
            speed_day = round(pp * 24)
            speed_year = round(pp * 24 * 365)
        elif self.dimention.text == 'км/сут':
            speed_sec = round(pp / (3600 * 24))
            speed_hour = round(pp / 24)
            speed_day = round(pp)
            speed_year = round(pp * 365)
        elif self.dimention.text == 'км/год':
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


if __name__ == '__main__':
    PlanetoptionsApp().run()