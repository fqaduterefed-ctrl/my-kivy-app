import sys import os
import sys
import os
import subprocess
የKivy አስፈላጊ ፓኬጆችን ማምጣት
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
🔐 የወታደራዊ ምስጢር ቁልፍ እና የአማርኛ ፊደላት መዝገበ-ቃላት
ANABABBI_ENC = {"ግዕዝ": "+1", "ካዕብ": "2", "ሣልስ": "-3", "ራብዕ": "/4", "ኃምስ": "+5", "ሳድስ": "-6", "ሳብዕ": "7", "ዲቃላ": "/8"}
ANABABBI_DEC = {v: k for k, v in ANABABBI_ENC.items()}
TENEBABBI_ENC = {
    "ሀ": "90", "ለ": "51", "ሐ": "42", "መ": "33", "ሠ": "74", "ረ": "25", "ሰ": "86", "ሸ": "17", "ቀ": "08", "በ": "69",
    "ተ": "11", "ቸ": "22", "ኀ": "33", "ነ": "44", "ኘ": "55", "አ": "66", "ከ": "77", "ኸ": "88", "ወ": "99", "ዐ": "12",
    "ዘ": "23", "ዠ": "34", "የ": "45", "ደ": "56", "ጀ": "67", "ገ": "78", "ጠ": "89", "ጨ": "91", "ጰ": "52", "ጸ": "43",
    "ፀ": "32", "ፈ": "21", "ፐ": "10"
}
TENEBABBI_DEC = {v: k for k, v in TENEBABBI_ENC.items()}
FIDEL_MAP = {
    "ሀ": ("ሀ", "ግዕዝ"), "ሁ": ("ሀ", "ካዕብ"), "ሂ": ("ሀ", "ሣልስ"), "ሃ": ("ሀ", "ራብዕ"), "ሄ": ("ሀ", "ኃምስ"), "ህ": ("ሀ", "ሳድስ"), "ሆ": ("ሀ", "ሳብዕ"),
    "ለ": ("ለ", "ግዕዝ"), "ሉ": ("ለ", "ካዕብ"), "ሊ": ("ለ", "ሣልስ"), "ላ": ("ለ", "ራብዕ"), "ሌ": ("ለ", "ኃምስ"), "ል": ("ለ", "ሳድስ"), "ሎ": ("ለ", "ሳብዕ"), "ሏ": ("ለ", "ዲቃላ"),
    "ሐ": ("ሐ", "ግዕዝ"), "ሑ": ("ሐ", "ካዕብ"), "ሒ": ("ሐ", "ሣልስ"), "ሓ": ("ሐ", "ራብዕ"), "ሔ": ("ሐ", "ኃምስ"), "ሕ": ("ሐ", "ሳድስ"), "ሖ": ("ሐ", "ሳብዕ"), "ሗ": ("ሐ", "ዲቃላ"),
    "መ": ("መ", "ግዕዝ"), "ሙ": ("መ", "ካዕብ"), "ሚ": ("መ", "ሣልስ"), "ማ": ("መ", "ራብዕ"), "ሜ": ("መ", "ኃምስ"), "ም": ("መ", "ሳድስ"), "ሞ": ("መ", "ሳብዕ"), "ሟ": ("መ", "ዲቃላ"),
    "ሠ": ("ሠ", "ግዕዝ"), "ሡ": ("ሠ", "ካዕብ"), "ሢ": ("ሠ", "ሣልስ"), "ሣ": ("ሠ", "ራብዕ"), "ሤ": ("ሠ", "ኃምስ"), "ሥ": ("ሠ", "ሳድስ"), "ሦ": ("ሠ", "ሳብዕ"), "ሧ": ("ሠ", "ዲቃላ"),
    "ረ": ("ረ", "ግዕዝ"), "ሩ": ("ረ", "ካዕብ"), "ሪ": ("ረ", "ሣልስ"), "ራ": ("ረ", "ራብዕ"), "ሬ": ("ረ", "ኃምስ"), "ር": ("ረ", "ሳድስ"), "ሮ": ("ረ", "ሳብዕ"), "ሯ": ("ረ", "ዲቃላ"),
    "ሰ": ("ሰ", "ግዕዝ"), "ሱ": ("ሰ", "ካዕብ"), "ሲ": ("ሰ", "ሣልስ"), "ሳ": ("ሰ", "ራብዕ"), "ሴ": ("ሰ", "ኃምስ"), "ስ": ("ሰ", "ሳድስ"), "ሶ": ("ሰ", "ሳብዕ"), "ሷ": ("ሰ", "ዲቃላ"),
    "ሸ": ("ሸ", "ግዕዝ"), "ሹ": ("ሸ", "ካዕብ"), "ሺ": ("ሸ", "ሣልስ"), "ሻ": ("ሸ", "ራብዕ"), "ሼ": ("ሸ", "ኃምስ"), "ሽ": ("ሸ", "ሳድስ"), "ሾ": ("ሸ", "ሳብዕ"), "ሿ": ("ሸ", "ዲቃላ"),
    "ቀ": ("ቀ", "ግዕዝ"), "ቁ": ("ቀ", "ካዕብ"), "ቂ": ("ቀ", "ሣልስ"), "ቃ": ("ቀ", "ራብዕ"), "ቄ": ("ቀ", "ኃምስ"), "ቅ": ("ቀ", "ሳድስ"), "ቆ": ("ቀ", "ሳብዕ"), "ቋ": ("ቀ", "ዲቃላ"),
    "በ": ("በ", "ግዕዝ"), "ቡ": ("በ", "ካዕብ"), "ቢ": ("በ", "ሣልስ"), "ባ": ("በ", "ራብዕ"), "ቤ": ("በ", "ኃምስ"), "ብ": ("በ", "ሳድስ"), "ቦ": ("በ", "ሳብዕ"), "ቧ": ("በ", "ዲቃላ"),
    "ተ": ("ተ", "ግዕዝ"), "ቱ": ("ተ", "ካዕብ"), "ቲ": ("ተ", "ሣልስ"), "ታ": ("ተ", "ራብዕ"), "ቴ": ("ተ", "ኃምስ"), "ት": ("ተ", "ሳድስ"), "ቶ": ("ተ", "ሳብዕ"), "ቷ": ("ተ", "ዲቃላ"),
    "ቸ": ("ቸ", "ግዕዝ"), "ቹ": ("ቸ", "ካዕብ"), "ቺ": ("ቸ", "ሣልስ"), "ቻ": ("ቸ", "ራብዕ"), "ቼ": ("ቸ", "ኃምስ"), "ች": ("ቸ", "ሳድስ"), "ቾ": ("ቸ", "ሳብዕ"), "ቿ": ("ቸ", "ዲቃላ"),
    "ኀ": ("ኀ", "ግዕዝ"), "ኁ": ("ኀ", "ካዕብ"), "ኂ": ("ኀ", "ሣልስ"), "ኃ": ("ኀ", "ራብዕ"), "ኄ": ("ኀ", "ኃምስ"), "ኅ": ("ኀ", "ሳድስ"), "ኆ": ("ኀ", "ሳብዕ"), "ኋ": ("ኀ", "ዲቃላ"),
    "ነ": ("ነ", "ግዕዝ"), "ኑ": ("ነ", "ካዕብ"), "ኒ": ("ነ", "ሣልስ"), "ና": ("ነ", "ራብዕ"), "ኔ": ("ነ", "ኃምስ"), "ን": ("ነ", "ሳድስ"), "ኖ": ("ነ", "ሳብዕ"), "ኗ": ("ነ", "ዲቃላ"),
    "ኘ": ("ኘ", "ግዕዝ"), "ኙ": ("ኘ", "ካዕብ"), "ኚ": ("ኘ", "ሣልስ"), "ኛ": ("ኘ", "ራብዕ"), "ኜ": ("ኘ", "ኃምስ"), "ኝ": ("ኘ", "ሳድስ"), "ኞ": ("ኘ", "ሳብዕ"), "ጟ": ("ኘ", "ዲቃላ"),
    "አ": ("አ", "ግዕዝ"), "ኡ": ("አ", "ካዕብ"), "ኢ": ("አ", "ሣልስ"), "ኣ": ("አ", "ራብዕ"), "ኤ": ("አ", "ኃምስ"), "እ": ("አ", "ሳድስ"), "ኦ": ("አ", "ሳብዕ"), "ኧ": ("አ", "ዲቃላ"),
    "ከ": ("ከ", "ግዕዝ"), "ኩ": ("ከ", "ካዕብ"), "ኪ": ("ከ", "ሣልስ"), "ካ": ("ከ", "ራብዕ"), "ኬ": ("ከ", "ኃምስ"), "ክ": ("ከ", "ሳድስ"), "ኮ": ("ከ", "ሳብዕ"), "ኳ": ("ከ", "ዲቃላ"),
    "ኸ": ("ኸ", "ግዕዝ"), "ኹ": ("ኸ", "ካዕብ"), "ኺ": ("ኸ", "ሣልስ"), "ኻ": ("ኸ", "ራብዕ"), "ኼ": ("ኸ", "ኃምስ"), "ኽ": ("ኸ", "ሳድስ"), "ኾ": ("ኸ", "ሳብዕ"),
    "ወ": ("ወ", "ግዕዝ"), "ዉ": ("ወ", "ካዕብ"), "ዊ": ("ወ", "ሣልስ"), "ዋ": ("ወ", "ራብዕ"), "ዌ": ("ወ", "ኃምስ"), "ው": ("ወ", "ሳድስ"), "ዎ": ("ወ", "ሳብዕ"),
    "ዐ": ("ዐ", "ግዕዝ"), "ዑ": ("ዐ", "ካዕብ"), "ዒ": ("ዐ", "ሣልስ"), "ዓ": ("ዐ", "ራብዕ"), "ዔ": ("ዐ", "ኃምስ"), "ዕ": ("ዐ", "ሳድስ"), "ዖ": ("ዐ", "ሳብዕ"),
    "ዘ": ("ዘ", "ግዕዝ"), "ዙ": ("ዘ", "ካዕብ"), "ዚ": ("ዘ", "ሣልስ"), "ዛ": ("ዘ", "ራብዕ"), "ዜ": ("ዘ", "ኃምስ"), "ዝ": ("ዘ", "ሳድስ"), "ዞ": ("ዘ", "ሳብዕ"), "ዟ": ("ዘ", "ዲቃላ"),
    "ዠ": ("ዠ", "ግዕዝ"), "ዡ": ("ዠ", "ካዕብ"), "ዢ": ("ዠ", "ሣልስ"), "ዣ": ("ዠ", "ራብዕ"), "ዤ": ("ዠ", "ኃምስ"), "ዥ": ("ዠ", "ሳድስ"), "ዦ": ("ዠ", "ሳብዕ"), "ዧ": ("ዠ", "ዲቃላ"),
    "የ": ("የ", "ግዕዝ"), "ዩ": ("የ", "ካዕብ"), "ዪ": ("የ", "ሣልስ"), "ያ": ("የ", "ራብዕ"), "ዬ": ("የ", "ኃምስ"), "ይ": ("የ", "ሳድስ"), "ዮ": ("የ", "ሳብዕ"),
    "ደ": ("ደ", "ግዕዝ"), "ዱ": ("ደ", "ካዕብ"), "ዲ": ("ደ", "ሣልስ"), "ዳ": ("ደ", "ራብዕ"), "ዴ": ("ደ", "ኃምስ"), "ድ": ("ደ", "ሳድስ"), "ዶ": ("ደ", "ሳብዕ"), "ዷ": ("ደ", "ዲቃላ"),
    "ጀ": ("ጀ", "ግዕዝ"), "ጁ": ("ጀ", "ካዕብ"), "ጂ": ("ጀ", "ሣልስ"), "ጃ": ("ጀ", "ራብዕ"), "ጄ": ("ጀ", "ኃምስ"), "ጅ": ("ጀ", "ሳድስ"), "ጆ": ("ጀ", "ሳብዕ"), "ጇ": ("ጀ", "ዲቃላ"),
    "ገ": ("ገ", "ግዕዝ"), "ጉ": ("ገ", "ካዕብ"), "ጊ": ("ገ", "ሣልስ"), "ጋ": ("ገ", "ራብዕ"), "ጌ": ("ገ", "ኃምስ"), "ግ": ("ገ", "ሳድስ"), "ጎ": ("ገ", "ሳብዕ"), "ጓ": ("ገ", "ዲቃላ"),
    "ጠ": ("ጠ", "ግዕዝ"), "ጡ": ("ጠ", "ካዕብ"), "ጢ": ("ጠ", "ሣልስ"), "ጣ": ("ጠ", "ራብዕ"), "ጤ": ("ጠ", "ኃምስ"), "ጥ": ("ጠ", "ሳድስ"), "ጦ": ("ጠ", "ሳብዕ"), "ጧ": ("ጠ", "ዲቃላ"),
    "ጨ": ("ጨ", "ግዕዝ"), "ጩ": ("ጨ", "ካዕብ"), "ጪ": ("ጨ", "ሣልስ"), "ጫ": ("ጨ", "ራብዕ"), "ጬ": ("ጨ", "ኃምስ"), "ጭ": ("ጨ", "ሳድስ"), "ጮ": ("ጨ", "ሳብዕ"), "ጯ": ("ጨ", "ዲቃላ"),
    "ጰ": ("ጰ", "ግዕዝ"), "ጱ": ("ጰ", "ካዕብ"), "ጲ": ("ጰ", "ሣልስ"), "ጳ": ("ጰ", "ራብዕ"), "ጴ": ("ጰ", "ኃምስ"), "ጵ": ("ጰ", "ሳድስ"), "ጶ": ("ጰ", "ሳብዕ"), "ጷ": ("ጰ", "ዲቃላ"),
    "ጸ": ("ጸ", "ግዕዝ"), "ጹ": ("ጸ", "ካዕብ"), "ጺ": ("ጸ", "ሣልስ"), "ጻ": ("ጸ", "ራብዕ"), "ጼ": ("ጸ", "ኃምስ"), "ጽ": ("ጸ", "ሳድስ"), "ጾ": ("ጸ", "ሳብዕ"), "ጿ": ("ጸ", "ዲቃላ"),
    "ፀ": ("ፀ", "ግዕዝ"), "ፁ": ("ፀ", "ካዕብ"), "ፂ": ("ፀ", "ሣልስ"), "ፃ": ("ፀ", "ራብዕ"), "ፄ": ("ፀ", "ኃምስ"), "ፅ": ("ፀ", "ሳድስ"), "ፆ": ("ፀ", "ሳብዕ"),
    "ፈ": ("ፈ", "ግዕዝ"), "ፉ": ("ፈ", "ካዕብ"), "ፊ": ("ፈ", "ሣልስ"), "ፋ": ("ፈ", "ራብዕ"), "ፌ": ("ፈ", "ኃምስ"), "ፍ": ("ፈ", "ሳድስ"), "ፎ": ("ፈ", "ሳብዕ"), "ፏ": ("ፈ", "ዲቃላ"),
    "ፐ": ("ፐ", "ግዕዝ"), "ፑ": ("ፐ", "ካዕብ"), "ፒ": ("ፐ", "ሣልስ"), "ፓ": ("ፐ", "ራብዕ"), "ፔ": ("ፐ", "ኃምስ"), "ፕ": ("ፐ", "ሳድስ"), "ፖ": ("ፐ", "ሳብዕ"), "ፗ": ("ፐ", "ዲቃላ")
}
REV_FIDEL_MAP = {f"{TENEBABBI_ENC.get(v)}{ANABABBI_ENC.get(v)}": k for k, v in FIDEL_MAP.items() if TENEBABBI_ENC.get(v) and ANABABBI_ENC.get(v)}
def encrypt(text):
    result = []
    for char in text:
        if char in FIDEL_MAP:
            teneb, anab = FIDEL_MAP[char]
            result.append(f"{TENEBABBI_ENC[teneb]}{ANABABBI_ENC[anab]}")
        else:
            result.append(char)
    return " ".join(result)
def decrypt(cipher):
    parts = cipher.split()
    return "".join(REV_FIDEL_MAP.get(p, p) for p in parts)
def send_sms_via_termux(phone, msg):
    try:
        subprocess.run(["termux-sms-send", "-n", phone, msg], check=True)
        return True
    except:
        return False
1️⃣ አዲሱ የወታደራዊ መታወቂያ ማረጋገጫ ገጽ (Military ID Verification Screen)
class IDVerificationScreen(Screen):
    def init(self, **kwargs):
        super().init(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        layout.add_widget(Label(
            text="🪪 DIGITAL MILITARY ID VERIFICATION\nየዲጂታል ወታደራዊ መታወቂያ ማረጋገጫ", 
            font_size=18, 
            bold=True,
            halign='center',
            color=(0.1, 0.7, 0.8, 1)
        ))
        layout.add_widget(Label(text="የኦፕሬተር ሙሉ ስም / Operator Full Name:", size_hint_y=None, height=25))
        self.name_input = TextInput(multiline=False, size_hint_y=None, height=45)
        layout.add_widget(self.name_input)
        layout.add_widget(Label(text="የመታወቂያ ቁጥር / Military ID Number:", size_hint_y=None, height=25))
        self.id_input = TextInput(multiline=False, size_hint_y=None, height=45, hint_text="ኮድ ቁጥር ያስገቡ")
        layout.add_widget(self.id_input)
        self.status_label = Label(text="", color=(1, 0.5, 0, 1), size_hint_y=None, height=30)
        layout.add_widget(self.status_label)
        btn = Button(text="VERIFY ID / መታወቂያ አረጋግጥ 🔍", size_hint_y=None, height=50, background_color=(0.1, 0.5, 0.8, 1))
        btn.bind(on_press=self.verify_id)
        layout.add_widget(btn)
        self.add_widget(layout)
    def verify_id(self, instance):
        name = self.name_input.text.strip()
        id_num = self.id_input.text.strip()
        if not name or not id_num:
            self.status_label.text = "❌ እባክዎ ስም እና መታወቂያ ቁጥር ያስገቡ!"
            return
እዚህ ጋር እንደ ምሳሌ ማንኛውም መታወቂያ እንዲያሳልፍ አድርጌዋለሁ፤ ወደፊት የተለየ ቁጥር መገደብ ይቻላል።
        self.manager.current = 'password'
2️⃣ የይለፍ ቃል ገጽ (PasswordScreen)
class PasswordScreen(Screen):
    def init(self, **kwargs):
        super().init(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout.add_widget(Label(
            text="🔑 ENTER MILITARY OTP\nየይለፍ ቃል ያስገቡ", 
            font_size=20, 
            halign='center'
        ))
        self.password_input = TextInput(password=True, multiline=False, size_hint_y=None, height=50)
        layout.add_widget(self.password_input)
        btn = Button(text="🔒 LOGIN / ግባ", size_hint_y=None, height=50, background_color=(0, 0.7, 0, 1))
        btn.bind(on_press=self.check_password)
        layout.add_widget(btn)
        self.error_label = Label(text="", color=(1, 0, 0, 1), size_hint_y=None, height=30)
        layout.add_widget(self.error_label)
        self.add_widget(layout)
    def check_password(self, instance):
        if self.password_input.text == "7788":
            self.manager.current = 'main'
        else:
            self.error_label.text = "❌ INVALID PASSWORD! / የተሳሳተ ነው!"
3️⃣ ዋናው የስራ ገጽ (MainScreen)
class MainScreen(Screen):
    def init(self, **kwargs):
        super().init(**kwargs)
        scroll = ScrollView()
        layout = BoxLayout(orientation='vertical', padding=15, spacing=10, size_hint_y=None)