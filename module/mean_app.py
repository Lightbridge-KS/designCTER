import flet as ft
from flet import Container, Column, Row, ResponsiveRow
import pyperclip

from calc.mean import calc_mean
from calc._utils import parse_str_to_num_or_list
from module.man import Manual

class AppMean(ft.UserControl):
    def __init__(self):
        super().__init__()
        
        ## Input Text of numbers
        self.input_numbers_text = ft.TextField(
            label="Numbers to calculate", hint_text="e.g. 1.1 1.2"
        )
        
        # Button
        self.btn = ft.ElevatedButton(text="Generate", on_click=self.button_gen_clicked)
        self.btn_copy = ft.IconButton(icon=ft.icons.CONTENT_COPY, icon_size=20, tooltip="Copy output", on_click=self.button_cp_clicked)
        
        # Output text
        txt_size = 14 # 14
        self.output_text_field = ft.TextField(label="Mean", value="", multiline=True, read_only=False, text_size=txt_size) 
    
    def button_cp_clicked(self, e):
        pyperclip.copy(self.output_text_field.value)
        
    def build(self):
        rr = ResponsiveRow(
            controls=[
                ft.Text("Mean Calculator",  theme_style=ft.TextThemeStyle.TITLE_LARGE),
                Column(col={"sm": 6},
                    controls = [
                        self.input_numbers_text,
                        # Manual
                        ft.Text(Manual.mean_app, theme_style = ft.TextThemeStyle.BODY_SMALL, color=ft.colors.GREY),
                        # ft.Markdown(Manual.mean_app, selectable=True)
                    ], alignment=ft.MainAxisAlignment.START),
                Column(col={"sm": 6},
                       controls = [
                        self.output_text_field,
                        Row([self.btn, self.btn_copy], alignment=ft.MainAxisAlignment.START), 
                ], alignment=ft.MainAxisAlignment.START)
            ]
        )
        lv = ft.ListView(controls=[rr], expand=1, spacing=5, padding=10, auto_scroll=False)
        return lv
    
    def button_gen_clicked(self, e):
        self._log()
        self.output_text_field.value = self.calc()
        self.output_text_field.focus()
        self.output_text_field.update()
        
    def _log(self):
        print("Btn clicked")
        print(f"Input: {self.input_numbers_text.value}")
        print(self.calc())
        
    def calc(self):
        numbers = parse_str_to_num_or_list(self.input_numbers_text.value)
        mean = calc_mean(numbers)
        return mean

# if __name__ == "__main__":
#     def main(page: ft.Page):
#         page.title = "MyMeanApp"
#         app1 = AppMean()
        
#         page.add(app1)
        
#     ft.app(target=main)