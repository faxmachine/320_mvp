from kivy.app import App
from kivy.core.window import Window
from kivy.properties import ObjectProperty, NumericProperty, StringProperty, BooleanProperty, ListProperty
from kivy.uix.listview import ListItemButton
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
from kivy.uix.popup import Popup
from kivy.factory import Factory

import inspect, os
import Controller as c


Config.set('input', 'mouse', 'mouse, multitouch_on_demand')
Window.size = (1000,600)


class DownloadList(ListItemButton):
    pass

class DownloadDialog(BoxLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

class MainGUI(BoxLayout):
        #download properties
    download_list = ObjectProperty()
    downloadtext = StringProperty()
    downloadvalid = BooleanProperty()
    downloadcolor = ListProperty()
        #export properties
    exporttext = StringProperty()
    exportvalid = BooleanProperty()
    exportcolor = ListProperty()
    exportlocation = ObjectProperty()
        #style properties
    stylenum = NumericProperty()
    stylename = StringProperty()
    stylecolor = ListProperty()
        #finishing properties
    runvalid = BooleanProperty()
    finished = StringProperty()
    finishname = StringProperty()
    location = ListProperty()

    #constructor
    def __init__(self, **kwargs):
        super(MainGUI, self).__init__(**kwargs)
        self.stylename = "Styles:"
        self.downloadtext = "Download Location Here"
        self.downloadvalid = False
        self.downloadcolor = [0,0,0,1]
        self.exporttext = "Export Location Here"
        self.exportvalid = False
        self.exportcolor = [0,0,0,1]
        self.exportlocation = []
        self.stylenum = 0
        self.stylecolor =  [1,1,1,1]
    #end of constructor

    #get functions
    def getexportpath(self):
        return self.exporttext

    def getstyle(self):
        return self.stylenum

    def getdownloaditem(self):
        return self.downloadtext
    #end of get functions


    #add to finished list
    def addfinished(self,  filename):
        self.download_list.adapter.data.extend([filename])
    #end of add to finish list

    def dismiss_popup(self):
        self._popup.dismiss()



    #download click event
    def download_load(self):
        content = DownloadDialog(load=self.download_location, cancel=self.dismiss_popup)
        self._popup = Popup(title="Select Download Location", content = content, size_hint=(0.9,0.9))
        self._popup.open()

    def download_location(self, path, filename):
        if(len(filename) == 0):
            self.downloadtext = 'Please pick a file'
            self.downloadvalid = False
            self.downloadcolor = [1,0,0,1]
            self.dismiss_popup()
        else:
            self.downloadtext = os.path.join(path,filename[0])
            self.downloadvalid = True
            self.downloadcolor = [0,0,0,1]
            if(self.downloadtext.rfind(".mp3") == -1):
                self.downloadtext = 'NOT A VALID FILE(NEED .mp3 FILE)'
                self.downloadvalid = False
                self.downloadcolor = [1,0,0,1]
            self.dismiss_popup()
    #end of download click event


    #export button click event
    def export_load(self):
        content = DownloadDialog(load=self.export_location, cancel=self.dismiss_popup)
        self._popup = Popup(title="Select Export Location", content = content,size_hint=(0.9,0.9))
        self._popup.open()

    def export_location(self,path,filename):
        if(len(filename) != 0):
            self.exporttext = 'Please do not selected a file'
            self.exportvalid = False
            self.exportcolor = [1,0,0,1]
            self.dismiss_popup()
        else:
            self.exporttext = path
            self.exportvalid = True
            self.stylecolor = [0,0,0,1]
            self.dismiss_popup()
    #end of export button click event


    # style buttons
    def pressstyle1(self):
        self.stylename = "Style 1"
        self.stylenum = 1
        self.stylecolor = [1,1,1,1]

    def pressstyle2(self):
        self.stylename = "Style 2"
        self.stylenum = 2
        self.stylecolor = [1,1,1,1]

    def pressstyle3(self):
        self.stylename = "Style 3"
        self.stylenum = 3
        self.stylecolor = [1,1,1,1]
    #end of style buttons


    #Go button event
    def gopress(self):
        self.runvalid = True
        if(self.stylenum == 0):
            self.stylename = "Please press a style"
            self.stylecolor = [1,0,0,1]
            self.runvalid = False
        if(self.downloadvalid == False):
            self.downloadtext = "Please select a download location"
            self.downloadcolor = [1,0,0,1]
            self.runvalid = False
        #if(self.exportvalid == False):
         #   self.exporttext = "Please selected an export location"
          #  self.exportcolor = [1,0,0,1]
           # self.runvalid = False
        if(self.runvalid == True):
            self.finished = os.path.relpath(self.downloadtext,os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))
            c.go(self.finished,int(self.stylenum))
            self.location = self.downloadtext.split('/')
            self.finishname = self.location[len(self.location)-1]
            self.finishname = self.finishname.split('.')
            self.addFinished(self.finishname)


class MainGUIApp(App):
    def build(self):
        self.load_kv('gui.kv')
        return MainGUI()

Factory.register('DownloadDialog',cls=DownloadDialog)

MGApp = MainGUIApp()
MGApp.run()