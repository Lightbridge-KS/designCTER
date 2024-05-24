body_id_exam_protocols = {
    "ct_wa": ["ct_wa_routine"],
    "ct_kub": ["ct_kub_nc", "ct_kub_stone"]
}

body_exam_id_name = {
   "ct_wa": "CTWA",
   "ct_kub": "CT KUB",
}

body_protocols_id_name = {
    "ct_wa_routine": "Routine WA",
    "ct_kub_nc": "CT KUB NC",
    "ct_kub_stone": "KUB Stone"
}


body_protocols = {
    "ct_wa_routine": {
        "protocol_name": body_exam_id_name["ct_wa_routine"],
        "exam_name": body_protocols_id_name["ct_wa"],
        "phase_design_text": """
- Venous (whole)
- Delay (liver)
""",
        "contrast_text": "Oral (limited water), Rectal (water)"
    },
    "ct_kub_nc": {
        "protocol_name": None,
        "exam_name": "CT KUB (non-contrast)",
        "phase_design_text": """
- Plain KUB (kidneys to pubic symphysis)
*** Check ภาพก่อนเลิก
""",
        "contrast_text": "No Oral, No Rectal"
    },
    "ct_kub_stone": {
        "protocol_name": body_exam_id_name["ct_kub_stone"],
        "exam_name": "CT KUB (non-contrast)",
        "phase_design_text": """
- Plain KUB (kidneys to pubic symphysis)
*** Check ภาพก่อนเลิก
""",
        "contrast_text": "No Oral, No Rectal"
    },
}