from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput

Window.clearcolor = (0, 0, 0.1, 1.0)

class Container(BoxLayout):
    def __init__(self, **kwargs):
        super(Container, self).__init__(**kwargs)

        self.l0 = BoxLayout(orientation='vertical', padding=[20], spacing=10)
        self.l0.add_widget(Label(text='Параметры тел Солнечной системы', font_size=30, halign='center'))

        # ввод радиуса
        self.l1 = BoxLayout()

        self.l1.add_widget(Label(text='Большая\nполуось:', font_size=30, halign='right', valign='bottom')) 

        self.rad = TextInput(multiline='False', halign='center', font_size=30)
        self.l1.add_widget(self.rad)

        self.l1.add_widget(Label(text='км', font_size=30, halign='left', valign='bottom')) 

        # ввод периода обращения
        self.l2 = BoxLayout()

        self.l2.add_widget(Label(text='Период\nобращения:', font_size=30, halign='center', valign='middle'))

        self.period = TextInput(multiline='False', halign='center', font_size=30)
        self.l2.add_widget(self.period)
        
        self.dimention = Spinner(text='размерность', values=('час', 'сут', 'год'), font_size=30, 
                                 halign='center', valign='middle', background_color=(0.9, 0.1, 0.1, 1), background_normal='')
        self.l2.add_widget(self.dimention)

        # кнопка Вычислить
        self.l3 = BoxLayout(padding=30, size_hint=(1, 3))
        self.btn_rad = Button(text='Вычислить', font_size=30, halign='center', valign='middle',
                              background_color=(0.9, 0.1, 0.1, 1), background_normal='', on_press=self.calculate) 
        self.l3.add_widget(self.btn_rad)

        # длина орбиты
        self.l4 = BoxLayout()
        self.lbl_rad = Label(text='Длина орбиты...', font_size=30, halign='center', valign='middle')
        self.l4.add_widget(self.lbl_rad)   

        # размерности периода обращения
        self.l5 = BoxLayout()
        self.lbl_sec = Label(text='Скорость в км/сек...', font_size=30, halign='center', valign='middle')
        self.l5.add_widget(self.lbl_sec)

        self.l6 = BoxLayout()
        self.lbl_hour = Label(text='Скорость в км/час...', font_size=30, halign='center', valign='middle')
        self.l6.add_widget(self.lbl_hour)

        self.l7 = BoxLayout()
        self.lbl_day= Label(text='Скорость в км/сутки...', font_size=30, halign='center', valign='middle')
        self.l7.add_widget(self.lbl_day)

        self.l8 = BoxLayout()
        self.lbl_year= Label(text='Скорость в км/год...', font_size=30, halign='center', valign='middle')
        self.l8.add_widget(self.lbl_year)    

        # вывод всех блоков
        self.add_widget(self.l0)
        self.l0.add_widget(self.l1)
        self.l0.add_widget(self.l2)
        self.l0.add_widget(self.l3)
        self.l0.add_widget(self.l4)
        self.l0.add_widget(self.l5)
        self.l0.add_widget(self.l6)
        self.l0.add_widget(self.l7)
        self.l0.add_widget(self.l8)
        
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


class MainApp(App):
    def build(self):
        return Container()
        

if __name__ == '__main__':
    MainApp().run()