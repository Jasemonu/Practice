from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MainApp(App):
    def build(self):
        self.operators = ["/", "*", "+", "-"]

        # Create the main layout
        main_layout = BoxLayout(orientation="vertical")

        # Create a TextInput widget for input
        self.text_input = TextInput(font_size=32, readonly=True, halign="right", multiline=False)
        main_layout.add_widget(self.text_input)

        # Create a grid layout for buttons
        button_grid = GridLayout(cols=4, spacing=5)

        # Create number buttons (0-9)
        for i in range(1, 10):
            button = Button(text=str(i), pos_hint={"center_x": 0.5, "center_y": 0.5})
            button.bind(on_press=self.on_button_press)
            button_grid.add_widget(button)

        # Create operator buttons (+, -, *, /)
        for operator in self.operators:
            button = Button(text=operator, pos_hint={"center_x": 0.5, "center_y": 0.5})
            button.bind(on_press=self.on_button_press)
            button_grid.add_widget(button)

        # Create the equals button
        equals_button = Button(text="=", pos_hint={"center_x": 0.5, "center_y": 0.5})
        equals_button.bind(on_press=self.on_solution)
        button_grid.add_widget(equals_button)

        # Create the clear button
        clear_button = Button(text="C", pos_hint={"center_x": 0.5, "center_y": 0.5})
        clear_button.bind(on_press=self.on_clear)
        button_grid.add_widget(clear_button)

        # Add the button grid to the main layout
        main_layout.add_widget(button_grid)

        return main_layout

    def on_button_press(self, instance):
        # Handle button press (append the button's text to the TextInput)
        current_text = self.text_input.text
        button_text = instance.text
        new_text = current_text + button_text
        self.text_input.text = new_text

    def on_solution(self, instance):
        # Calculate the result and display it
        try:
            current_text = self.text_input.text
            result = str(eval(current_text))
            self.text_input.text = result
        except Exception:
            self.text_input.text = "Error"

    def on_clear(self, instance):
        # Clear the TextInput
        self.text_input.text = ""

if __name__ == "__main__":
    app = MainApp()
    app.run()

