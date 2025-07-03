import flet as ft
import pyperclip
import datetime
from flet import Container, Column, Row, ResponsiveRow, Page
import designcter
from designcter.proto import (
    category,
    exam_id_name, exam_name_id,
    exam_id_protocol_name,
    protocols_name_id, 
)
from designcter._utils import dash_if_blank

class InputDesign(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.input_category = ft.Dropdown(
            label="Category", hint_text="Category",
            options=[ft.dropdown.Option(x) for x in category],
            on_change=self.input_category_changed
        )
        self.input_exam_name = ft.Dropdown(
            label="Exam", hint_text="Type of Study",
            on_change=self.input_exam_name_changed
        )
        self.input_protocol_name = ft.Dropdown(
            label="Protocol", hint_text="Protocol Name",
            on_change=self.input_protocol_name_changed
        )
        self.input_ETT = ft.CupertinoCheckbox(label="ETT", value=False, on_change=self._log_input_checkboxes)
        self.input_C1 = ft.CupertinoCheckbox(label="C1", value=False, on_change=self._log_input_checkboxes)
        self.input_pregnancy = ft.CupertinoCheckbox(label="Pregnancy", value=False, on_change=self._log_input_checkboxes)
        self.input_NPO_time = ft.TextField(label="NPO time", hint_text="NPO time")
        self.input_eGFR_value = ft.TextField(label="eGFR", expand=1, hint_text="eGFR Value")
        self.input_eGFR_date = ft.TextField(label="eGFR Date", expand=1, value=datetime.date.today().strftime('%d/%m/%Y'))
        self.input_renal_premed = ft.TextField(label="Renal Premed", expand=1, hint_text="Renal Premed")
        self.input_allergy_premed = ft.TextField(label="Allergy Premed", expand=1, hint_text="Allergy Premed")
        self.input_precaution = ft.TextField(label="Precaution", expand=1, hint_text="Precaution")
        self.input_special_inst = ft.TextField(label="Special Instruction", expand=1, hint_text="Special Instr.")
        self.input_ref_phy_name = ft.TextField(label="Ref physician name", hint_text="Name of Ref physician")
        self.input_ref_phy_tel = ft.TextField(label="Ref physician tel", hint_text="PCT of Ref physician")

    def input_category_changed(self, e):
        print(f"Dropdown Category: {self.input_category.value}")
        exam_id_name_selected = exam_id_name[self.input_category.value]
        self.input_exam_name.options = [ft.dropdown.Option(x) for x in exam_id_name_selected.values()]
        self.input_exam_name.update()

    def input_exam_name_changed(self, e):
        print(f"Dropdown Exam: {self.input_exam_name.value}")
        exam_id_selected = exam_name_id[self.input_category.value][self.input_exam_name.value]
        protocol_names_selected = exam_id_protocol_name[exam_id_selected]
        self.input_protocol_name.options = [ft.dropdown.Option(x) for x in protocol_names_selected]
        self.input_protocol_name.update()

    def input_protocol_name_changed(self, e):
        print(f"Dropdown Protocol: {self.input_protocol_name.value}")

    def build(self):
        return Container(
            content=Column([
                self.input_category,
                self.input_exam_name,
                self.input_protocol_name,
                Row([self.input_ETT, self.input_C1, self.input_pregnancy], alignment=ft.MainAxisAlignment.START),
                Row([self.input_eGFR_value, self.input_eGFR_date], alignment=ft.MainAxisAlignment.START),
                Row([self.input_renal_premed, self.input_allergy_premed], alignment=ft.MainAxisAlignment.START),
                self.input_NPO_time,
                Row([self.input_precaution, self.input_special_inst], alignment=ft.MainAxisAlignment.START),
                self.input_ref_phy_name,
                self.input_ref_phy_tel
            ])
        )

    def get(self):
        out = {
            "protocol_id": protocols_name_id[self.input_protocol_name.value],
            "NPO_time": dash_if_blank(self.input_NPO_time.value),
            "eGFR_value": dash_if_blank(self.input_eGFR_value.value),
            "eGFR_date": self.input_eGFR_date.value,
            "renal_premed": dash_if_blank(self.input_renal_premed.value),
            "allergy_premed": dash_if_blank(self.input_allergy_premed.value),
            "pregnancy": self.input_pregnancy.value,
            "ETT": self.input_ETT.value,
            "C1": self.input_C1.value,
            "precaution": dash_if_blank(self.input_precaution.value),
            "special_inst": dash_if_blank(self.input_special_inst.value),
            "ref_phy_name": self.input_ref_phy_name.value,
            "ref_phy_tel": self.input_ref_phy_tel.value
        }
        return out

    def reset(self):
        self.input_ETT.value = False; self.input_ETT.update()
        self.input_C1.value = False; self.input_C1.update()
        self.input_pregnancy.value = False; self.input_pregnancy.update()
        self.input_eGFR_value.value = ""; self.input_eGFR_value.update()
        self.input_eGFR_date.value = datetime.date.today().strftime('%d/%m/%Y'); self.input_eGFR_date.update()
        self.input_NPO_time.value = ""; self.input_NPO_time.update()
        self.input_renal_premed.value = ""; self.input_renal_premed.update()
        self.input_allergy_premed.value = ""; self.input_allergy_premed.update()
        self.input_ref_phy_name.value = ""; self.input_ref_phy_name.update()
        self.input_ref_phy_tel.value = ""; self.input_ref_phy_tel.update()
        self.input_precaution.value = ""; self.input_precaution.update()
        self.input_special_inst.value = ""; self.input_special_inst.update()

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

class AppDesignCT(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.input_design = InputDesign()
        self.txt_size = 14
        self.output_text_field = ft.TextField(value="\n"*self.txt_size, multiline=True, read_only=False, text_size=self.txt_size, min_lines=self.txt_size+12)
        self.btn_gen = ft.ElevatedButton(text="    Generate    ", on_click=self.button_gen_clicked)
        self.btn_reset = ft.ElevatedButton(text="Reset", on_click=self.button_reset_clicked)
        self.btn_copy = ft.IconButton(icon=ft.icons.CONTENT_COPY, icon_size=20, tooltip="Copy output", on_click=self.button_cp_clicked)

    def get_text_output(self):
        input_dict = self.input_design.get()
        text_output = designcter.Design(**input_dict)
        return text_output

    def button_reset_clicked(self, e):
        self.input_design.reset()

    def _log(self):
        print("btn_gen clicked")
        print(self.input_design._log())
        print(self.get_text_output())

    def button_gen_clicked(self, e):
        self._log()
        self.output_text_field.value = self.get_text_output()
        self.output_text_field.focus()
        self.output_text_field.update()

    def button_cp_clicked(self, e):
        pyperclip.copy(self.output_text_field.value)

    def build(self):
        rr = ResponsiveRow(
            controls=[
                Column(col={"sm": 6}, controls=[
                    self.input_design,
                    
                ], alignment=ft.MainAxisAlignment.START),
                Column(col={"sm": 6}, 
                       controls=[self.output_text_field,
                                 Row([Column([Row([self.btn_gen, self.btn_copy])]), Column([self.btn_reset])], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),], 
                       alignment=ft.MainAxisAlignment.START)
            ]
        )
        lv = ft.ListView(controls=[rr], expand=1, spacing=5, padding=10, auto_scroll=False)
        return lv
