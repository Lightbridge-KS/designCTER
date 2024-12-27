import datetime
from ._designTemp import design_template
from .proto import protocols
from ._utils import bool_yesno, bool_yesdash, newlineFormatOS


class Design:
    def __init__(self, protocol_id: str, **kwarg):
        
        self.protocol = protocols[protocol_id]
        # Protocol Name Line
        self.ptc_nm = self.protocol['protocol_name']
        self.protocol_name_line = "" if self.ptc_nm is None else f"\nProtocol name: {self.ptc_nm}"
        # Phase Design Line
        self.pdt = self.protocol["phase_design_text"]
        self.phase_design_line = "" if self.pdt is None else f"\n{self.pdt.strip()}"
        
        if protocol_id in ["mri_screening_whole_spine"]:
            self.result = self.design_mr(protocol_id = protocol_id) 
        else:
            self.result = self.design_ct(protocol_id = protocol_id, **kwarg)
    
    def __str__(self):
        return self.result

    def __repr__(self):
        return self.result
    
    def design_ct(self, 
                  protocol_id: str, 
                  NPO_time: str = "-",
                  eGFR_value: str = "-", 
                  eGFR_date: str = datetime.date.today().strftime('%d/%m/%Y'),
                  renal_premed: str = "-",
                  allergy_premed: str = "-",
                  pregnancy: bool = False,
                  ETT: bool = False,
                  C1: bool = False,
                  precaution: str = "-",
                  special_inst: str = "-",
                  ref_phy_name: str = "-",
                  ref_phy_tel: str = "-"
                  ):
        
        str_design = design_template["cter_gen"].format(
            exam_name = self.protocol["exam_name"],
            protocol_name_line = self.protocol_name_line,
            phase_design_line = self.phase_design_line,
            contrast_text = self.protocol["contrast_text"],
            NPO_time_text = NPO_time,
            eGFR_date_text = eGFR_date,
            eGFR_value_text = eGFR_value,
            renal_premed_text = renal_premed,
            allergy_premed_text = allergy_premed,
            pregnancy_text = bool_yesdash(pregnancy),
            ETT_text = bool_yesdash(ETT),
            C1_text = bool_yesdash(C1),
            precaution_text = precaution,
            special_inst_text = special_inst,
            ref_phy_name_text = ref_phy_name,
            ref_phy_tel_text = ref_phy_tel
        )
        # Format newline for macOS or Windows
        str_design_fmt = newlineFormatOS(str_design)
        
        return str_design_fmt
    
    def design_mr(self, 
                  protocol_id: str):
        str_design = design_template["mri_gen"].format(
            exam_name = self.protocol["exam_name"],
            protocol_name_line = self.protocol_name_line,
            phase_design_line = self.phase_design_line,
            contrast_text = self.protocol["contrast_text"]
        )
        
        # Format newline for macOS or Windows
        str_design_fmt = newlineFormatOS(str_design)
        
        return str_design_fmt
