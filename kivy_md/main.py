# from kivymd.app import MDApp 
# from kivymd.uix.label import MDLabel 
# from kivy.uix.screenmanager import Screen
# from kivymd.uix.button import MDRectangleFlatButton
# from kivymd.uix.anchorlayout import MDAnchorLayout



# class Demo(MDApp):
#     def build(self):
#        screen = Screen()
#        screen.add_widget(
#            MDRectangleFlatButton(
#                text="Hello, World",
#                pos_hint={"center_x": .5, "center_y": .5},
#            )
#        )
#        return screen

# Demo().run()

# banniere

# from kivy.lang import Builder
# from kivy.factory import Factory

# from kivymd.app import MDApp

# Builder.load_string('''
# <ExampleBanner@Screen>

#     MDBanner:
#         id: banner
#         text: ["One line string text example without actions."]
#         # The widget that is under the banner.
#         # It will be shifted down to the height of the banner.
#         over_widget: screen
#         vertical_pad: toolbar.height

#     MDToolbar:
#         id: toolbar
#         title: "Example Banners"
#         elevation: 10
#         pos_hint: {'top': 1}

#     MDBoxLayout:
#         id: screen
#         orientation: "vertical"
#         size_hint_y: None
#         height: Window.height - toolbar.height

#         OneLineListItem:
#             text: "Banner without actions"
#             on_release: banner.show()

#         Widget:
# ''')


# class Test(MDApp):
#     def build(self):
#         return Factory.ExampleBanner()


# Test().run()

# from kivymd.app import MDApp
# from kivy.lang import Builder


# class Test(MDApp):

#     def build(self):
#         self.theme_cls.primary_palette = "Gray"
#         return Builder.load_string(
#             '''
# BoxLayout:
#     orientation:'vertical'

#     MDToolbar:
#         title: 'Bottom navigation'
#         md_bg_color: .2, .2, .2, 1
#         specific_text_color: 1, 1, 1, 1

#     MDBottomNavigation:
#         panel_color: .2, .2, .2, 1

#         MDBottomNavigationItem:
#             name: 'screen 1'
#             text: 'Python'
#             icon: 'language-python'

#             MDLabel:
#                 text: 'Python'
#                 halign: 'center'

#         MDBottomNavigationItem:
#             name: 'screen 2'
#             text: 'C++'
#             icon: 'language-cpp'

#             MDLabel:
#                 text: 'I programming of C++'
#                 halign: 'center'

#         MDBottomNavigationItem:
#             name: 'screen 3'
#             text: 'JS'
#             icon: 'language-javascript'

#             MDLabel:
#                 text: 'JS'
#                 halign: 'center'
# '''
#         )


# Test().run()


# from kivymd.app import MDApp
# from kivy.lang import Builder 
# from kivy.core.window import Window

# Window.size = (300, 500)

# navigation_helper = '''
# Screen:
#     NavigationLayout:
#     ScreenManager:
#         Screen:
#             BoxLayout:
#                 orientation : 'vertical'
#                 Image:
#                     source : 'bg.jpg'
                
# '''

# class DemoApp(MDApp):
#     def build(self):
#         screen = Builder.load_string(navigation_helper)
        
# DemoApp().run()



# from kivy.lang import Builder

# from kivymd.uix.screen import MDScreen
# from kivymd.app import MDApp

# # Your layouts.
# Builder.load_string(
#     '''
# #:import Window kivy.core.window.Window
# #:import IconLeftWidget kivymd.uix.list.IconLeftWidget


# <ItemBackdropFrontLayer@TwoLineAvatarListItem>
#     icon: "android"

#     IconLeftWidget:
#         icon: root.icon


# <MyBackdropFrontLayer@ItemBackdropFrontLayer>
#     backdrop: None
#     text: "Lower the front layer"
#     secondary_text: " by 50 %"
#     icon: "transfer-down"
#     on_press: root.backdrop.open(-Window.height / 2)
#     pos_hint: {"top": 1}
#     _no_ripple_effect: True


# <MyBackdropBackLayer@Image>
#     size_hint: .8, .8
#     source: "data/logo/kivy-icon-512.png"
#     pos_hint: {"center_x": .5, "center_y": .6}
# '''
# )

# # Usage example of MDBackdrop.
# Builder.load_string(
#     '''
# <ExampleBackdrop>

#     MDBackdrop:
#         id: backdrop
#         left_action_items: [['menu', lambda x: self.open()]]
#         title: "Example Backdrop"
#         radius_left: "25dp"
#         radius_right: "0dp"
#         header_text: "Menu:"

#         MDBackdropBackLayer:
#             MyBackdropBackLayer:
#                 id: backlayer

#         MDBackdropFrontLayer:
#             MyBackdropFrontLayer:
#                 backdrop: backdrop
# '''
# )


# class ExampleBackdrop(MDScreen):
#     pass


# class TestBackdrop(MDApp):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)

#     def build(self):
#         return ExampleBackdrop()


# TestBackdrop().run()



# from kivy.lang import Builder

# from kivymd.toast import toast
# from kivymd.uix.bottomsheet import MDListBottomSheet
# from kivymd.app import MDApp

# KV = '''
# MDScreen:

#     MDToolbar:
#         title: "Example BottomSheet"
#         pos_hint: {"top": 1}
#         elevation: 10

#     MDRaisedButton:
#         text: "Open list bottom sheet"
#         on_release: app.show_example_list_bottom_sheet()
#         pos_hint: {"center_x": .5, "center_y": .5}
# '''


# class Example(MDApp):
#     def build(self):
#         return Builder.load_string(KV)

#     def callback_for_menu_items(self, *args):
#         toast(args[0])

#     def show_example_list_bottom_sheet(self):
#         bottom_sheet_menu = MDListBottomSheet()
#         for i in range(1, 11):
#             bottom_sheet_menu.add_item(
#                 f"Standart Item {i}",
#                 lambda x, y=i: self.callback_for_menu_items(
#                     f"Standart Item {y}"
#                 ),
#             )
#         bottom_sheet_menu.open()


# Example().run() 


# from kivy.lang import Builder

# from kivymd.app import MDApp

# KV = '''
# <MyTile@SmartTileWithLabel>
#     size_hint_y: None
#     height: "240dp"


# ScrollView:

#     MDGridLayout:
#         cols: 3
#         adaptive_height: True
#         padding: dp(4), dp(4)
#         spacing: dp(4)

#         MyTile:
#             source: "bg.jpg"
#             text: "[size=26]Cat 1[/size]\n[size=14]bg.jpg[/size]"

#         MyTile:
#             source: "cat-2.jpg"
#             text: "[size=26]Cat 2[/size]\n[size=14]cat-2.jpg[/size]"
#             tile_text_color: app.theme_cls.accent_color

#         MyTile:
#             source: "cat-3.jpg"
#             text: "[size=26][color=#ffffff]Cat 3[/color][/size]\n[size=14]cat-3.jpg[/size]"
#             tile_text_color: app.theme_cls.accent_color
# '''


# class MyApp(MDApp):
#     def build(self):
#         return Builder.load_string(KV)


# MyApp().run()


# 
# 



from kivy.lang import Builder 
from kivymd.app import MDApp




class MainApp(MDApp):
    def build(self):
        # self.theme_cls.theme_style = "Dark"
        # self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('demo.kv')


MainApp().run()