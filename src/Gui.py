from kivy.app import App
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config

Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
Window.size = (1000,600)

class DownloadList(ListItemButton):
    pass

class MainGUI(BoxLayout):
    download_list = ObjectProperty()
    styleName = ""

    def getStyleName(self):
        return styleName


class MainGUIApp(App):
    def build(self):
        self.load_kv('gui.kv')
        return MainGUI()

MGApp = MainGUIApp()
MGApp.run()