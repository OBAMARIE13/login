from kivy.lang import Builder 
from kivymd.app import MDApp


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('login.kv')
    
    
    def clear(self):
        self.root.ids.utilisateur.text = ""
        self.root.ids.password.text = ""
    
    

MainApp().run()