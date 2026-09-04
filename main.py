from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

# የወረደው የአማርኛ ፎንት ፋይል ስም (በሪፖዚተሪህ ውስጥ መኖሩን አረጋግጥ)
AMHARIC_FONT = "AbyssinicaSIL-Regular.ttf"

# 1. ዲጂታል የወታደራዊ መታወቂያ ማረጋገጫ ገጽ
class IDVerificationScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # ዋና ርዕስ
        layout.add_widget(Label(
            text="DIGITAL MILITARY ID VERIFICATION\nበዲጂታል ወታደራዊ መታወቂያ ማረጋገጫ",
            font_size=18,
            bold=True,
            halign='center',
            font_name=AMHARIC_FONT,
            color=(0.1, 0.7, 0.8, 1)
        ))
        
        # የስም ማስገቢያ ርዕስ
        layout.add_widget(Label(
            text="የአሠሪው ሙሉ ስም / Operator Full Name:",
            size_hint_y=None,
            height=25,
            font_name=AMHARIC_FONT
        ))
        
        # የስም ማስገቢያ ሣጥን
        self.name_input = TextInput(
            multiline=False,
            size_hint_y=None,
            height=45,
            font_name=AMHARIC_FONT
        )
        layout.add_widget(self.name_input)
        
        # የመታወቂያ ቁጥር ማስገቢያ ርዕስ
        layout.add_widget(Label(
            text="የመታወቂያ ቁጥር / Military ID Number:",
            size_hint_y=None,
            height=25,
            font_name=AMHARIC_FONT
        ))
        
        # የመታወቂያ ቁጥር ማስገቢያ ሣጥን
        self.id_input = TextInput(
            multiline=False,
            size_hint_y=None,
            height=45,
            hint_text="ኮድ ቁጥር ያስገቡ",
            font_name=AMHARIC_FONT
        )
        layout.add_widget(self.id_input)
        
        # የስህተት ወይም የሁኔታ ማሳያ ሌብል
        self.status_label = Label(
            text="",
            color=(1, 0.5, 0, 1),
            size_hint_y=None,
            height=30,
            font_name=AMHARIC_FONT
        )
        layout.add_widget(self.status_label)
        
        # ማረጋገጫ አዝራር
        btn = Button(
            text="VERIFY ID / መታወቂያ አረጋግጥ 🔍",
            size_hint_y=None,
            height=50,
            background_color=(0.1, 0.5, 0.8, 1),
            font_name=AMHARIC_FONT
        )
        btn.bind(on_press=self.verify_id)
        layout.add_widget(btn)
        
        self.add_widget(layout)

    def verify_id(self, instance):
        name = self.name_input.text.strip()
        id_num = self.id_input.text.strip()
        
        if not name or not id_num:
            self.status_label.text = "❌ እባክዎ ስም እና መታወቂያ ቁጥር ያስገቡ!"
            return
            
        # መረጃው ከተሞላ ወደ ሚስጥር ቃል ገጽ ይሻገራል
        self.manager.current = 'password'

# 2. የይለፍ ቃል ገጽ
class PasswordScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        layout.add_widget(Label(
            text="🔑 ENTER MILITARY OTP\nእባክዎ የይለፍ ቃል ያስገቡ",
            font_size=20,
            halign='center',
            font_name=AMHARIC_FONT
        ))
        
        self.password_input = TextInput(
            password=True,
            multiline=False,
            size_hint_y=None,
            height=45,
            font_name=AMHARIC_FONT
        )
        layout.add_widget(self.password_input)
        
        btn = Button(
            text="🔒 LOGIN / ግባ",
            size_hint_y=None,
            height=50,
            background_color=(0, 1, 0, 1),
            font_name=AMHARIC_FONT
        )
        btn.bind(on_press=self.check_password)
        layout.add_widget(btn)
        
        self.error_label = Label(
            text="",
            color=(1, 0, 0, 1),
            size_hint_y=None,
            height=30,
            font_name=AMHARIC_FONT
        )
        layout.add_widget(self.error_label)
        
        self.add_widget(layout)

    def check_password(self, instance):
        if self.password_input.text == "7788":
            self.manager.current = 'main'
        else:
            self.error_label.text = "❌ INVALID PASSWORD! / የተሳሳተ ነው!"

# 3. ዋናው የሰራተኛ ገጽ
class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        scroll = ScrollView()
        layout = BoxLayout(orientation='vertical', padding=15, spacing=10, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))
        
        layout.add_widget(Label(
            text="ሰላም ሰላም እና መታወቂያ ቁጥር አስገብተዋል!",
            size_hint_y=None,
            height=40,
            font_name=AMHARIC_FONT
        ))
        
        layout.add_widget(Label(
            text="ማሳሰቢያ፤ ወደፊት የተለየ ቁጥር መግለጽ ይቻላል::",
            size_hint_y=None,
            height=40,
            font_name=AMHARIC_FONT
        ))
        
        scroll.add_widget(layout)
        self.add_widget(scroll)

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(IDVerificationScreen(name='id_verify'))
        sm.add_widget(PasswordScreen(name='password'))
        sm.add_widget(MainScreen(name='main'))
        return sm

if __name__ == '__main__':
    MyApp().run()
