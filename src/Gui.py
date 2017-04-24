from kivy.app import App
from kivy.core.window import Window
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivy.uix.listview import ListItemButton
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
from kivy.uix.popup import Popup
from kivy.factory import Factory

import os


Config.set('input', 'mouse', 'mouse, multitouch_on_demand')
Window.size = (1000,600)


class DownloadList(ListItemButton):
    pass

class DownloadDialog(BoxLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

class MainGUI(BoxLayout):
    download_list = ObjectProperty()
    stylename = StringProperty()
    downloadtext = StringProperty()
    exporttext = StringProperty()
    stylenum = NumericProperty()

    def __init__(self, **kwargs):
        super(MainGUI, self).__init__(**kwargs)
        self.stylename = "Styles:"
        self.downloadtext = "Download Location Here"
        self.exporttext = "Export Location Here"
        self.stylenum = 0

    def dismiss_popup(self):
        self._popup.dismiss()

    def download_load(self):
        content = DownloadDialog(load=self.download_location, cancel=self.dismiss_popup)
        self._popup = Popup(title="Select Download Location", content = content, size_hint=(0.9,0.9))
        self._popup.open()

    def download_location(self, path, filename):
        if(len(filename) == 0):
            self.downloadtext = 'Please pick a file'
            self.dismiss_popup()
        else:
            self.downloadtext = os.path.join(path,filename[0])
            if(self.downloadtext.rfind("/mp4") == -1):
                self.downloadtext = 'NOT A VALID FILE(NEED .mp3 FILE)'
            self.dismiss_popup()

    def export_load(self):
        content = DownloadDialog(load=self.export_location, cancel=self.dismiss_popup)
        self._popup = Popup(title="Select Export Location", content = content,size_hint=(0.9,0.9))
        self._popup.open()

    def export_location(self,path,file):
        self.exporttext = path
        self.dismiss_popup()

    def pressstyle1(self):
        self.stylename = "Style 1"
        self.stylenum = 1

    def pressstyle2(self):
        self.stylename = "Style 2"
        self.stylenum = 2

    def pressstyle3(self):
        self.stylename = "Style 3"
        self.stylenum = 3


class MainGUIApp(App):
    def build(self):
        self.load_kv('gui.kv')
        return MainGUI()

Factory.register('DownloadDialog',cls=DownloadDialog)

MGApp = MainGUIApp()
MGApp.run()