from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from instructions import txt_instruction, txt_test1, txt_test2, txt_test3, txt_sits
from ruffier import test 
from seconds import Seconds
from sits import Sits
from runner import Runner


main_color = (0, 255, 0, 1)
btn_color = (0, 0, 1, 1)

Window.clearcolor = main_color

age = 7
name = ""
p1, p2, p3 = 0, 0, 0

def check_int(str_num):
    try:
        return int(str_num)
    except:
        return False

class InstrScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        instr = Label(text=txt_instruction)
        
        lbl1 = Label(text='Введите имя:', halign="right")
        self.in_name = TextInput(multiline='False')
        
        lbl2 = Label(text='Введите возраст:', halign='right')
        self.in_age = TextInput(text='7', multiline=False)
        
        self.btn = Button(text='Начать', size_hint=(0.5, 0.35), pos_hint={'center_x': 0.5})
        self.btn.background_color = btn_color
        self.btn.on_press = self.next

        line1 = BoxLayout(size_hint=(1, None), height='40sp')
        line2 = BoxLayout(size_hint=(1, None), height='40sp')
        line1.add_widget(lbl1)
        line1.add_widget(self.in_name)
        line2.add_widget(lbl2)
        line2.add_widget(self.in_age)

        outer = BoxLayout(orientation = 'vertical', padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)

        self.add_widget(outer)
    
    def next(self):
            global age, name 
            name = self.in_name.text
            age = check_int(self.in_age.text)
            if age == False or age < 7:
                age = 7
                self.in_age.text = str(age)
            else:
                print("Отлично, идём дальше!")
                self.manager.current = 'pulse1'
                

class PulseScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = False 

        instr = Label(text=txt_test1)

        lbl1 = Label(text = 'Считайте пульс')
        self.lbl_sec = Seconds(15)
        self.lbl_sec.bind(done = self.sec_finished)

        line1 = BoxLayout()
        vlay = BoxLayout(orientation='vertical')
        vlay.add_widget(lbl1)
        vlay.add_widget(self.lbl_sec)
        #line1.add_widget(instr)
        line1.add_widget(vlay)

        line2 = BoxLayout(size_hint=(0.8, None), height='30sp')
        lbl_result = Label(text='Введите результат:', halign='right')
        self.in_result = TextInput(text='0', multiline='False')
        self.in_result.set_disabled(True)

        line2.add_widget(lbl_result)
        line2.add_widget(self.in_result)

        self.btn = Button(text='Начать', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.background_color = btn_color
        self.btn.on_press = self.next

        outer = BoxLayout(orientation = 'vertical', padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)

        self.add_widget(outer)

    def sec_finished(self, *args):
        self.in_result.set_disabled(False)
        self.btn.set_disabled(False)
        self.btn.text = 'Продолжить'
        self.next_screen = True

    def next(self):
            if not self.next_screen:
                self.btn.set_disabled(True)
                self.lbl_sec.start()
            else:    
                global p1
                p1 = check_int(self.in_result.text)  
                if p1 == False or p1 <= 0:
                    p1 = 0
                    self.in_result.text = str(p1)
                    print("Пульс не может быть нулём, дробью, не целым числом, отрицательным числом или словом.")   
                else:
                    print("Отлично, идём дальше!")
                    self.manager.current = 'sits'
            

            #if p1 < 15:
            #    print("Пульс не может быть меньше 15 или быть отрицательным числом")   
            #else:
            #    print("Отлично, идём дальше!")
            #self.manager.current = 'sits'

class ThirdScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  
        self.next_screen = False   

        instr = Label(text=txt_sits, size_hint=(0.5, 1))
        #self.lbl_sits = Sits(30)
        #self.run = Runner(total = 30, steptime = 1.5, size_hint=(0.4, 1))
        #self.run.bind(finished = self.run_finished)

        line = BoxLayout()
        vlay = BoxLayout(orientation = 'vertical', size_hint=(0.3, 1))
        #vlay.add_widget(self.lbl_sits)
        line.add_widget(instr)
        line.add_widget(vlay)
        #line.add_widget(self.run)

        self.btn = Button(text='Продолжить', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.background_color = btn_color
        self.btn.on_press = self.next

        outer = BoxLayout(orientation = 'vertical', padding=8, spacing=8)
        outer.add_widget(self.btn)

        self.add_widget(outer)
        self.add_widget(vlay)

    #def run_finished(self, instance, value):
        self.btn.set_disabled(False)
        self.btn.text = 'продолжить'
        self.next_screen = True

    def next(self):
        #if not self.next_screen:
            #self.btn.set_disabled(True)
            #self.run.start()
            #self.run.bind(value=self.lbl_sits.next)
        #else:
        self.manager.current = '1'

class FourthScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        instr = Label(text=txt_test3)
        
        lbl1 = Label(text='Введите результат(1):', halign="right")
        self.in_resul = TextInput(multiline='False')
        
        lbl2 = Label(text='Введите результат(2):', halign='right')
        self.in_resul1 = TextInput(multiline=False)
        
        self.btn = Button(text='Подсчитать результат', size_hint=(0.5, 0.35), pos_hint={'center_x': 0.5})
        self.btn.background_color = btn_color
        self.btn.on_press = self.next

        line1 = BoxLayout(size_hint=(1, None), height='40sp')
        line2 = BoxLayout(size_hint=(1, None), height='40sp')
        line1.add_widget(lbl1)
        line1.add_widget(self.in_resul)
        line2.add_widget(lbl2)
        line2.add_widget(self.in_resul1)

        outer = BoxLayout(orientation = 'vertical', padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)

        self.add_widget(outer)
    
    def next(self):
            global p2, p3
            p2 = check_int(self.in_resul.text) 
            p3 = check_int(self.in_resul1.text)
            if p2 == False or p3 == False or p2 <= 0 or p3 <= 0:
                p2 = 0
                self.in_resul.text = str(p2)
                p3 = 0
                self.in_resul1.text = str(p3)
                print("Пульс не может быть нулём, дробью, не целым числом, отрицательным числом или словом.")
            elif p2 == False or p2 <= 0:
                p2 = 0
                self.in_resul.text = str(p2)
                print("Пульс не может быть нулём, дробью, не целым числом, отрицательным числом или словом.")
            elif p3 == False or p2 <= 0:
                p3 = 0
                self.in_resul1.text = str(p3)
                print("Пульс не может быть нулём, дробью, не целым числом, отрицательным числом или словом.")
            else:
                print("Отлично, идём дальше!")
                self.manager.current = '2'

class FifthScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.outer = BoxLayout(orientation = 'vertical', padding=8, spacing=8)
        self.instr = Label(text = '')
        self.outer.add_widget(self.instr)

        self.add_widget(self.outer)
        self.on_enter = self.before

    def before(self):
        global name 
        self.instr.text = name + '\n' + test(p1, p2, p3, age)


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstrScr(name="instr"))
        sm.add_widget(PulseScr(name="pulse1"))
        sm.add_widget(ThirdScr(name="sits"))
        sm.add_widget(FourthScr(name="1"))
        sm.add_widget(FifthScr(name="2"))

        return sm

MyApp().run()


