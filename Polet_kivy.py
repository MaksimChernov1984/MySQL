from kivy.app import App
from kivy.config import Config
from kivy.graphics import Color
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput


Config.set('graphics', 'width', '250')
Config.set('graphics', 'height', '500')

class MainApp(App):
    def build(self):
        Color(0, .5, 0, 1) 
        layout = BoxLayout(orientation='vertical', padding=[30], spacing=30)

        layout1 = BoxLayout() 
        self.lbl = Label(text='Вас приветствует компания \nПОЛЕТЕЛИ-ПРИЛЕТЕЛИ!', 
                         font_size='20sp', halign='center')        
        layout1.add_widget(self.lbl) 

        #цель
        layout2 = BoxLayout()
        self.destination = Spinner(text='Куда летим?', 
            values=('Луна', 'Меркурий', 'Венера', 'Марс', 'Церера', 'Веста', 
            'Ганимед', 'Ио', 'Европа', 'Каллисто', 'Титан', 'Титания', 'Тритон', 'Плутон', 'Эрида'), 
            background_color=(0.9, 0.1, 0.1, 1), background_normal='')
        layout2.add_widget(self.destination)

        self.destination.bind(text=self.on_destination_select)
        self.destination_select = Label(text='Цель назначения:')
        layout2.add_widget(self.destination_select)

        # тариф
        layout3 = BoxLayout()
        self.tariff = Spinner(text='Выберите тариф', values=('простой', 'быстрый', 'супербыстрый'), 
            background_color=(0.9, 0.1, 0.1, 1), background_normal='')
        layout3.add_widget(self.tariff)

        self.tariff.bind(text=self.on_tariff_select)
        self.tariff_select = Label(text='Тариф:')
        layout3.add_widget(self.tariff_select)

        # кол-во пассажиров
        layout4 = BoxLayout()
        self.lbl = Label(text='Количество пассажиров (не более 20):')
        layout4.add_widget(self.lbl)
        self.passengers = TextInput()
        layout4.add_widget(self.passengers)       

        # кол-во груза
        layout5 = BoxLayout()
        self.lbl = Label(text='Количество тонн груза (не более 100):')
        layout5.add_widget(self.lbl)
        self.cargo = TextInput()
        layout5.add_widget(self.cargo)

        # стоимость
        layout6 = BoxLayout()
        btn_price = Button(text='Стоимость', on_press=self.priced, 
            background_color=(0.9, 0.1, 0.1, 1), background_normal='')
        layout6.add_widget(btn_price)
        self.price_select = Label(text='Стоимость полёта:')
        layout6.add_widget(self.price_select)

        # вывод всех блоков
        layout.add_widget(layout1)
        layout.add_widget(layout2)
        layout.add_widget(layout3)
        layout.add_widget(layout4)
        layout.add_widget(layout5)
        layout.add_widget(layout6)
        return layout


    def on_destination_select(self, spinner, text):
        self.destination_select.text = 'Ваша цель: %s'%self.destination.text    

    def on_tariff_select(self, spinner, text):
        self.tariff_select.text = 'Ваш тариф: %s'%self.tariff.text

    def submit_passengers(self, obj):
        self.passengers_select.text = self.passengers.text

    def submit_cargo(self, obj):
        self.cargo_select.text = self.cargo.text

    def priced(self, obj):
        
        # коэффициенты
        p = int(self.passengers.text)  # количество пассажиров
        c = int(self.cargo.text)  # масса груза в тоннах
        rub = 100_000  # рублей за единичный коэффициент
        
        # коэффициенты цели назначения
        if self.destination.text == 'Луна':
            d = 1
        elif self.destination.text == 'Марс':
            d = 2
        elif self.destination.text == 'Церера':
            d = 2.5
        elif self.destination.text == ('Ганимед') or ('Ио') or ('Калисто') or ('Европа'):
            d = 3
        elif self.destination.text == ('Меркурий') or ('Венера') or ('Титан'):
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

        price = d * p * c * t * rub
        if p <= 20:
            if c <= 100:
                price2 = '{0:,}'.format(price).replace(',', ' ')
            else:
                price2 = 'Слишком много груза.'
        else:
            price2 = 'Слишком много пассажиров.'      
        
        self.price_select.text = price2

if __name__ == '__main__':
    MainApp().run()
