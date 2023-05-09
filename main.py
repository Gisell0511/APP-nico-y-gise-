

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown


class MenuScreen(Screen):
    pass


class CustomScreen(Screen):
    pass


class MenuApp(MDApp):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(MenuScreen(name='menu_screen'))
        screen_manager.add_widget(CustomScreen(name='custom_screen'))
        return screen_manager


class MenuApp2(MDApp):
    def build(self):
        root = BoxLayout(orientation='vertical')

        toolbar = BoxLayout(size_hint=(1, None), height=50)
        menu_button = Button(text='Menu', size_hint=(None, None), size=(100, 50))
        menu_button.bind(on_release=self.show_menu)
        toolbar.add_widget(menu_button)

        self.menu = DropDown()
        menu_items = ['Inicio', 'Perfil', 'Configuración', 'Ayuda']
        for item in menu_items:
            btn = Button(text=item, size_hint_y=None, height=50)
            btn.bind(on_release=lambda btn: self.menu.select(btn.text))
            self.menu.add_widget(btn)

        root.add_widget(toolbar)
        return root

    def show_menu(self, widget):
        self.menu.open(widget)

    def on_stop(self):
        self.menu.dismiss()


if __name__ == "__main__":
    MenuApp().run()
    MenuApp2().run()

