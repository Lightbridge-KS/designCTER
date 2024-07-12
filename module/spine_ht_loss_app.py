import flet as ft
from flet import Container, Column, Row, ResponsiveRow
import pyperclip

from calc.spine import spine_ht_loss
from calc._utils import parse_str_to_num_or_list, read_markdown_file
from module.man import Manual

# Spine Ht Loss App
class AppSpineHtLoss(ft.UserControl):
    def __init__(self):
        super().__init__()
        ## Normal Height (cm)
        self.input_ht_normal = ft.TextField(
            label="Normal height (cm)", hint_text="Normal height in cm", on_submit=self.button_gen_clicked
        )
        ## Collapsed Height (cm)
        self.input_ht_bad = ft.TextField(
            label="Collapsed height (cm)", hint_text="Collapsed height in cm", on_submit=self.button_gen_clicked
        )
        # Button
        self.btn = ft.ElevatedButton(text="Generate", on_click=self.button_gen_clicked)
        self.btn_copy = ft.IconButton(icon=ft.icons.CONTENT_COPY, icon_size=20, tooltip="Copy output", on_click=self.button_cp_clicked)

        # Output text
        txt_size = 14 # 14
        self.output_text_field = ft.TextField(label="Height loss", value="", multiline=True, read_only=False, text_size=txt_size) 
    
    def button_cp_clicked(self, e):
        pyperclip.copy(self.output_text_field.value)
        
    def build(self):
        rr = ResponsiveRow(
            controls=[
                ft.Text("Spine Height Loss",  theme_style=ft.TextThemeStyle.TITLE_LARGE),
                Column(col={"sm": 6},
                    controls = [
                        self.input_ht_normal,
                        self.input_ht_bad,
                        # Manual
                        ft.Text(Manual.spine_ht_loss_app, theme_style = ft.TextThemeStyle.BODY_SMALL, color=ft.colors.GREY),
                        ft.Text(Manual.spine_ht_loss_app_ref, theme_style = ft.TextThemeStyle.BODY_SMALL, color=ft.colors.GREY),
                        # ft.Markdown(Manual.spine_ht_loss_app, selectable=True)
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
        print(f"Normal: {self.input_ht_normal.value}")
        print(f"Bad: {self.input_ht_bad.value}")
        print(self.calc())
        
    def calc(self):
        normal_cm = parse_str_to_num_or_list(self.input_ht_normal.value)
        bad_cm = parse_str_to_num_or_list(self.input_ht_bad.value)
        ht_loss_str = spine_ht_loss(normal_cm=normal_cm, bad_cm=bad_cm)
        return ht_loss_str

# if __name__ == "__main__":
#     def main(page: ft.Page):
#         page.title = "MyAppSpineHtLoss"
#         app1 = AppSpineHtLoss()
        
#         page.add(app1)
        
#     ft.app(target=main)