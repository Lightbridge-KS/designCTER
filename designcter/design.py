import datetime
from ._designTemp import design_template
from .proto import protocols
from ._utils import bool_yesno



def design_ct(protocol_id: str, 
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
    
    protocol = protocols[protocol_id]
    ptc_nm = protocol['protocol_name']
    protocol_name_line = "" if ptc_nm is None else f"\nProtocol name: {ptc_nm}"
    
    str_design = design_template["cter_gen"].format(
        exam_name = protocol["exam_name"],
        protocol_name_line = protocol_name_line,
        phase_design_text = protocol["phase_design_text"].strip(),
        contrast_text = protocol["contrast_text"],
        NPO_time_text = NPO_time,
        eGFR_date_text = eGFR_date,
        eGFR_value_text = eGFR_value,
        renal_premed_text = renal_premed,
        allergy_premed_text = allergy_premed,
        pregnancy_text = bool_yesno(pregnancy),
        ETT_text = bool_yesno(ETT),
        C1_text = bool_yesno(C1),
        precaution_text = precaution,
        special_inst_text = special_inst,
        ref_phy_name_text = ref_phy_name,
        ref_phy_tel_text = ref_phy_tel
    )
    
    return str_design