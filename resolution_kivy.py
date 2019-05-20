from kivy.app import App

from kivy.uix.screenmanager import ScreenManager, NoTransition, Screen
from kivy.uix.popup import Popup

from kivy.uix.boxlayout import BoxLayout

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import CoreImage
from io import BytesIO

from resolution import Resolution
import traceback


class Enlarge(Popup, Resolution):
    def __init__(self, picture_location, *args, **kwargs):
        super(Enlarge, self).__init__(picture_location=picture_location,*args,**kwargs)
        self.picture.save(f"{picture_location}_to_display.jpg")
        self.picture_to_display.texture = CoreImage(f"{picture_location}_to_display.jpg").texture
    
    def enlarge(self, how_many_times_to_enlarge):
        how_many_times_to_enlarge = int(how_many_times_to_enlarge)
        picture_enlarged = self.change_resolution(how_many_times_to_enlarge)
        picture_enlarged.save('enlarged_picture.bmp')

class FileChooser(Screen):
    def __init__(self, **kwargs):
        super(FileChooser, self).__init__(**kwargs)
    
    def load_picture(self, picture_location):
        try:
            self.popup = Enlarge(picture_location=picture_location[0], title="Enlarger",
                                size_hint=(1,1))
            self.popup.open()
        except:
            print('wrong format')

class MainApp(App):
    def build(self):
        self.title = "Paveikslu skyros (angl. resolution) didinimo priemone"
        manager = ScreenManager()
        manager.transition=NoTransition()
        manager.add_widget(FileChooser(name='FileChooser'))
        return manager

if __name__ == '__main__':
    try:
        app = MainApp()
        app.run()
    except Exception as e:
        print(e)
        traceback.print_exc()
        app.get_running_app().stop()