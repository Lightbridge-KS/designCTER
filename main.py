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
from designcter._utils import dash_if_blank

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
        ## CheckBox: ETT, C1, Pregnancy
        self.input_ETT = ft.CupertinoCheckbox(label="ETT", value=False, on_change=self._log_input_checkboxes)
        self.input_C1 = ft.CupertinoCheckbox(label="C1", value=False, on_change=self._log_input_checkboxes)
        self.input_pregnancy = ft.CupertinoCheckbox(label="Pregnancy", value=False, on_change=self._log_input_checkboxes)
        # NPO Time
        self.input_NPO_time = ft.TextField(label="NPO time", hint_text="NPO time")
        # eGFR
        ## TextField: eGFR_value
        self.input_eGFR_value = ft.TextField(label="eGFR", expand=1, hint_text="eGFR Value")
        ## Date TextField eGFR_date
        self.input_eGFR_date = ft.TextField(label="eGFR Date", expand=1, value=datetime.date.today().strftime('%d/%m/%Y'))
        # Premed
        self.input_renal_premed = ft.TextField(label="Renal Premed", expand=1, hint_text="Renal Premed")
        self.input_allergy_premed = ft.TextField(label="Allergy Premed", expand=1, hint_text="Allergy Premed")
        # Precaution & Special Inst
        self.input_precaution = ft.TextField(label="Precaution", expand=1, hint_text="Precaution")
        self.input_special_inst = ft.TextField(label="Special Instruction", expand=1, hint_text="Special Instr.")
        ## TextField: ref_phy_name
        self.input_ref_phy_name = ft.TextField(label="Ref physician name", hint_text="Name of Ref physician")
        ## TextField: ref_phy_tel
        self.input_ref_phy_tel = ft.TextField(label="Ref physician tel", hint_text="PCT of Ref physician")
        
        
        
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
                 self.input_protocol_name,
                 Row([self.input_ETT, self.input_C1, self.input_pregnancy], alignment=ft.MainAxisAlignment.START),
                 Row([self.input_eGFR_value, self.input_eGFR_date], alignment=ft.MainAxisAlignment.START),
                 Row([self.input_renal_premed, self.input_allergy_premed], alignment=ft.MainAxisAlignment.START),                             
                 self.input_NPO_time,
                 Row([self.input_precaution, self.input_special_inst], alignment=ft.MainAxisAlignment.START),                                           
                 self.input_ref_phy_name,
                 self.input_ref_phy_tel]
            )
        )
    ## Get All Selected Input Values
    def get(self):
        out = {
            "protocol_id": protocols_name_id_map[self.input_protocol_name.value],
            "NPO_time": dash_if_blank(self.input_NPO_time.value),
            "eGFR_value": dash_if_blank(self.input_eGFR_value.value), 
            "eGFR_date": self.input_eGFR_date.value,
            "renal_premed": dash_if_blank(self.input_renal_premed.value),
            "allergy_premed": dash_if_blank(self.input_allergy_premed.value),
            "pregnancy": self.input_pregnancy.value,
            "ETT":  self.input_ETT.value,
            "C1": self.input_C1.value,
            "precaution": dash_if_blank(self.input_precaution.value),
            "special_inst": dash_if_blank(self.input_special_inst.value),
            "ref_phy_name": self.input_ref_phy_name.value,
            "ref_phy_tel": self.input_ref_phy_tel.value
        }
        return out
    ## reset Input
    def reset(self):
        ## CheckBox
        self.input_ETT.value = False; self.input_ETT.update()
        self.input_C1.value = False; self.input_C1.update()
        self.input_pregnancy.value = False; self.input_pregnancy.update()
        ## TextField
        self.input_eGFR_value.value = ""; self.input_eGFR_value.update()
        self.input_eGFR_date.value = datetime.date.today().strftime('%d/%m/%Y'); self.input_eGFR_date.update()
        self.input_NPO_time.value = ""; self.input_NPO_time.update()
        self.input_renal_premed.value = ""; self.input_renal_premed.update()
        self.input_allergy_premed.value = ""; self.input_allergy_premed.update()
        self.input_ref_phy_name.value = ""; self.input_ref_phy_name.update()
        self.input_ref_phy_tel.value = ""; self.input_ref_phy_tel.update()
        self.input_precaution.value = ""; self.input_precaution.update()
        self.input_special_inst.value = ""; self.input_special_inst.update()
        
        
        
        
    ## Log
    def _log(self):
        return f"get(): {self.get()}"
    
    def _log_input_checkboxes(self, e):
        print(f"ETT: {self.input_ETT.value}, CT: {self.input_C1.value}, pregnancy: {self.input_pregnancy.value}")
    def _log_input_textfield(self, e):
        print(f"""ref_phy_name: {self.input_ref_phy_name.value}
                  ref_phy_tel: {self.input_ref_phy_tel.value}
                  eGFR_value: {self.input_eGFR_value.value}
                  input_NPO_time: {self.input_NPO_time.value}
              """)
        
        

def main(page: ft.Page):
    # Input Group
    input_design = InputDesign()
    ## Calculation
    def get_text_output():
        input_dict = input_design.get()
        # Design CT as String
        text_output = designcter.design_ct(**input_dict)
        return text_output
    ## Reset
    def button_reset_clicked(e):
        input_design.reset()
    def _log():
        print("btn_gen clicked")
        print(input_design._log())
        print(get_text_output())
    ## Button Generate Clicked 
    def button_gen_clicked(e):
        _log()
        output_text_field.value = get_text_output()
        output_text_field.focus()
        output_text_field.update()     
    ## Copy Clicked 
    def button_cp_clicked(e):
        pyperclip.copy(output_text_field.value)
    ## Theme
    def theme_changed(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
        page.update()
    
    # Title & App Bar
    page.title = "Design CTER Protocol"
    # Page Size
    page.window_min_width = 780
    page.window_width = 780
    page.window_min_height = 725
    page.window_height = 725
    # App Bar
    page.appbar = ft.CupertinoAppBar(
        leading=ft.Icon(ft.icons.PALETTE),
        bgcolor=ft.colors.SURFACE_VARIANT,
        middle=ft.Text("Design CTER Protocol", weight=ft.FontWeight.BOLD),
        trailing=ft.IconButton(icon=ft.icons.BRIGHTNESS_2_OUTLINED,
                               tooltip="Toggle theme",
                               on_click=theme_changed)
    )
    
    # Button
    btn_gen = ft.ElevatedButton(text="Generate", on_click=button_gen_clicked)
    btn_reset = ft.ElevatedButton(text="Reset", on_click=button_reset_clicked)
    btn_copy = ft.IconButton(
                    icon=ft.icons.CONTENT_COPY,
                    icon_size=20,
                    tooltip="Copy output",
                    on_click=button_cp_clicked
                    )
    
    # Output Text Field
    txt_size = 14 # 14
    output_text_field = ft.TextField(value="\n"*txt_size, multiline=True, read_only=False, text_size=txt_size,
                                     min_lines=txt_size+12, max_lines=txt_size+1) 
    
    # UI
    rr = ResponsiveRow(
            controls=[
                Column(col={"sm": 6},
                       controls=[
                        input_design,
                        Row([Column([Row([btn_gen, btn_copy])]), Column([btn_reset])], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
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