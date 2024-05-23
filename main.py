import flet as ft
import pyperclip
import datetime
from flet import (
    Container,
    Column,
    Row,
    ResponsiveRow,
    Page
)
import designcter
from designcter.proto import (
    exam_id_name_map, 
    exam_name_id_map, 
    protocols_name_id_map,
    exam_id_protocols_name_map
)

# Input Component
class InputDesign(ft.UserControl):
    def __init__(self):
        super().__init__()
        ## Input: Exam Name
        self.input_exam_name = ft.Dropdown(
            label="Exam", hint_text="Type of Study",
            options=[ft.dropdown.Option(x) for x in exam_id_name_map.values()],
            on_change=self.input_exam_name_changed
        )
        ## Input: Protocol Name
        self.input_protocol_name = ft.Dropdown(
            label="Protocol", hint_text="Protocol Name",
            on_change=self.input_protocol_name_changed
        )
        
    def input_exam_name_changed(self, e):
        print(f"Dropdown Exam: {self.input_exam_name.value}")
        self.input_exam_name.update()
        
        # Value of `input_protocol_name` depend on `input_exam_name`
        exam_id = exam_name_id_map[self.input_exam_name.value]
        protocol_names = exam_id_protocols_name_map[exam_id]
        self.input_protocol_name.options = [ft.dropdown.Option(x) for x in protocol_names]
        self.input_protocol_name.update()
        
    def input_protocol_name_changed(self, e):
        print(f"Dropdown Protocol: {self.input_protocol_name.value}")
        self.input_protocol_name.update()
        
    ## Build Input UI
    def build(self):
        return Container(
            content=Column(
                [self.input_exam_name,
                 self.input_protocol_name]
            )
        )
    ## Get All Selected Input Values
    def get(self):
        out = {
            "protocol_id": protocols_name_id_map[self.input_protocol_name.value],
            "NPO_time": "-",
            "eGFR_value": "-", 
            "eGFR_date": datetime.date.today(),
            "renal_premed": "-",
            "allergy_premed": "-",
            "pregnancy": False,
            "ETT":  False,
            "C1": False,
            "precaution": "-",
            "special_inst": "-",
            "ref_phy_name": "-",
            "ref_phy_tel":"-"
        }
        return out
    ## Log
    def _log(self):
        return f"get(): {self.get()}"
        

def main(page: ft.Page):
    # Input Group
    input_design = InputDesign()
    ## Calculation
    def get_text_output():
        input_dict = input_design.get()
        # Design CT as String
        text_output = designcter.design_ct(**input_dict)
        return text_output
    def _log():
        print("Btn clicked")
        print(input_design._log())
        print(get_text_output())
    ## Button Clicked 
    def button_gen_clicked(e):
        _log()
        output_text_field.value = get_text_output()
        output_text_field.focus()
        output_text_field.update()     
    
    # Title & App Bar
    page.title = "Design CTER Protocol"
    
    # Button
    btn = ft.ElevatedButton(text="Generate", on_click=button_gen_clicked)
    
    # Output Text Field
    txt_size = 14 # 14
    output_text_field = ft.TextField(value="\n"*txt_size, multiline=True, read_only=False, text_size=txt_size,
                                     min_lines=txt_size+1, max_lines=txt_size+1) 
    
    # UI
    rr = ResponsiveRow(
            controls=[
                Column(col={"sm": 6},
                       controls=[
                        input_design,
                        Row([btn], alignment=ft.MainAxisAlignment.START)
                        ], 
                       alignment=ft.MainAxisAlignment.START
                ),
                Column(col={"sm": 6}, 
                       controls=[output_text_field],
                       alignment=ft.MainAxisAlignment.START
                )
            ]
        )
    lv = ft.ListView(controls=[rr], 
                     expand=1, spacing=5, padding=10, auto_scroll=False)
    
    page.add(lv)


if __name__ == "__main__":
    ft.app(target=main)