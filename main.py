from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Color, Rectangle
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout

class InputScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

            # set background color
        with self.canvas.before:
            Color(0.53, 0.81, 0.92, 1) # set sky blue color
            self.rect = Rectangle(size=self.size, pos=self.pos)

            # create image widget for PNG file
        png_image = Image(source='logo.png', size_hint=(1, None), size=(200, 100))

        # create input widgets
        self.name_input = TextInput(multiline=False, hint_text='Enter your Full Name')
        self.class_input = TextInput(multiline=False,hint_text='Enter your Class between 6 to 9')
        self.marks1_input = TextInput(multiline=False, hint_text='Enter maths marks 25 or below 25')
        self.marks2_input = TextInput(multiline=False, hint_text='Enter Physics Marks 25 or below 25')
        self.marks3_input = TextInput(multiline=False, hint_text='Enter Chemistry Marks 25 or below 25')
        self.marks4_input = TextInput(multiline=False, hint_text='Enter Biology Marks 25 or below 25')
        self.marks5_input = TextInput(multiline=False, hint_text='Enter English Marks 20 or below 20')
        self.marks6_input = TextInput(multiline=False, hint_text='Enter Telugu Marks 20 or below 20')
        self.marks7_input = TextInput(multiline=False, hint_text='Enter Hindi Marks 20 or below 20')
        self.marks8_input = TextInput(multiline=False, hint_text='Enter Social Marks 20 or below 20')
        self.calculate_button = Button(text='Calculate',color=(1, 1, 0, 1))

        # create layout for input widgets
        input_layout = GridLayout(cols=2,row_force_default=True,row_default_height=30,padding=100,spacing=60)
        input_layout.add_widget(png_image)

       # create horizontal layout for the first two input fields
        first_row_layout = BoxLayout(orientation='horizontal',spacing=10,size_hint=(None, 1), width=300)
        first_row_layout.add_widget(self.name_input)
        first_row_layout.add_widget(self.class_input)
        input_layout.add_widget(first_row_layout)

        # create horizontal layout for the next two input fields
        second_row_layout = BoxLayout(orientation='horizontal',spacing=10,size_hint=(None, 1), width=300)
        second_row_layout.add_widget(self.marks1_input)
        second_row_layout.add_widget(self.marks2_input)
        input_layout.add_widget(second_row_layout)

         # create horizontal layout for the third two input fields
        third_row_layout = BoxLayout(orientation='horizontal',spacing=10, size_hint=(None, 1), width=300)
        third_row_layout.add_widget(self.marks3_input)
        third_row_layout.add_widget(self.marks4_input)
        input_layout.add_widget(third_row_layout)

         # create horizontal layout for the fourth two input fields
        fourth_row_layout = BoxLayout(orientation='horizontal',spacing=10, size_hint=(None, 1), width=300)
        fourth_row_layout.add_widget(self.marks5_input)
        fourth_row_layout.add_widget(self.marks6_input)
        input_layout.add_widget(fourth_row_layout)

         # create horizontal layout for the fifth two input fields
        fifth_row_layout = BoxLayout(orientation='horizontal',spacing=10, size_hint=(None, 1), width=300)
        fifth_row_layout.add_widget(self.marks7_input)
        fifth_row_layout.add_widget(self.marks8_input)
        input_layout.add_widget(fifth_row_layout)
        input_layout.add_widget(self.calculate_button)

       
        # add layout to screen
        self.add_widget(input_layout)

        # bind button press to method
        self.calculate_button.bind(on_press=self.calculate_marks)

    def on_size(self, *args):
        # update background rectangle size when screen size changes
        self.rect.size = self.size

    def on_pos(self, *args):
        # update background rectangle position when screen position changes
        self.rect.pos = self.pos

    def calculate_marks(self, instance):
        try:
            # get input values
            name = self.name_input.text
            classs = int(self.class_input.text)
            marks1 = float(self.marks1_input.text)
            marks2 = float(self.marks2_input.text)
            marks3 = float(self.marks3_input.text)
            marks4 = float(self.marks4_input.text)
            marks5 = float(self.marks5_input.text)
            marks6 = float(self.marks6_input.text)
            marks7 = float(self.marks7_input.text)
            marks8 = float(self.marks8_input.text)

            # validate marks
            if marks1 > 26 or marks2 > 26 or marks3 > 26 or marks4 > 26 or marks5 > 21 or marks6 > 21 or marks7 > 21:
                raise ValueError
            
            if 6 <= classs >=10:
                raise ValueError

            # calculate total marks and percentage
            total_marks = marks1 + marks2 + marks3 + marks4 + marks5 + marks6 + marks7 + marks8
            if total_marks>180:
                total_mark="Please enter valid marks"
            else:
                total_mark=total_marks
            percentage = (total_marks / 180)*100

            if percentage>101:
                percentages=("Please enter valid marks")
            else:
                percentages=f"{percentage:.2f}%"

            # calculate grade

            if percentage > 100:
                grade="Please enter valid marks"
            elif percentage > 90.99 and percentage<=100:
                grade = "A1"
            elif percentage > 80.99:
                grade = "A2"
            elif percentage > 70.99:
                grade = "B1"
            elif percentage > 60.99:
                grade = "B2"
            elif percentage > 50.99:
                grade = "C1"
            elif percentage > 40.99:
                grade = "C2"
            elif percentage > 34.99:
                grade = "D1"
            elif percentage >=0 and percentage < 35:
                grade = "D2"
            else:
                grade="Please enter valid marks"
        
       

            # update output label text
            output_label.text = f'Name: {name} \n Class: {classs} \n Maths: {marks1} \n Physics: {marks2} \n Chemistry: {marks3} \n Biology: {marks4} \n English: {marks5} \n Telugu: {marks6} \n Hindi: {marks7} \n Social: {marks8} \n Total Marks: {total_mark} \n Percentage: {percentages} \n Grade:{grade}'
        except ValueError:
            output_label.text = 'Please enter valid marks'
            # self.percentage_label.text = ''
            # self.grade_label.text=''
        # switch to output screen
        sm.current = 'output'

        # clear input fields
        self.name_input.text = ''
        self.class_input.text = ''
        self.marks1_input.text = ''
        self.marks2_input.text = ''
        self.marks3_input.text = ''
        self.marks4_input.text = ''
        self.marks5_input.text = ''
        self.marks6_input.text = ''
        self.marks7_input.text = ''
        self.marks8_input.text = ''


class OutputScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

            # set background color
        with self.canvas.before:
            Color(0.53, 0.81, 0.92, 1) # set sky blue color
            self.rect = Rectangle(size=self.size, pos=self.pos)

        # create back button
        self.back_button = Button(text='Back',size_hint=(None, None),color=(1, 1, 0, 1),size=(100, 50), padding=(20, 10))

         # create image widget for PNG file
        png_image = Image(source='logo.png', size_hint=(1, None), size=(200, 200))

        # create output label
        global output_label
        output_label = Label(text='', font_size='69sp', color=(1, 0, 0, 1)) # set font size to 20 and color to red


        # create layout for back button and output label
        layout = BoxLayout(orientation='vertical',spacing=10, padding=50)
        layout.add_widget(png_image)
        layout.add_widget(output_label)
        layout.add_widget(self.back_button)

        # add layout to screen
        self.add_widget(layout)

        # bind button press to method
        self.back_button.bind(on_press=self.go_to_input_screen)

    def on_size(self, *args):
        # update background rectangle size when screen size changes
        self.rect.size = self.size

    def on_pos(self, *args):
        # update background rectangle position when screen position changes
        self.rect.pos = self.pos

    def go_to_input_screen(self, instance):
        # switch to input screen
        sm.current = 'input'

class MarksApp(App):
    def build(self):
        # create screen manager
        global sm
        sm = ScreenManager()

        # create input screen
        input_screen = InputScreen(name='input')
        sm.add_widget(input_screen)

        # create output screen
        global output_screen
        output_screen = OutputScreen(name='output')
        sm.add_widget(output_screen)

        return sm


if __name__ == '__main__':
    MarksApp().run()