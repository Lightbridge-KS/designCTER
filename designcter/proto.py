# Group `protocol_id` in each `exam_id`
## The order of element in this list appeared in drop down
exam_id_protocols_id_map = {
    "ct_wa": ["ct_wa_routine", 
              "ct_wa_gut_obs",
              "ct_wa_infect",
              "ct_wa_leak_fist_collect",
              "ct_wa_diver",
              "ct_wa_pancrea",
              "ct_wa_free_air",
              "ct_wa_solid_rupture",
              "ct_wa_gi_perforate",
              "ct_wa_hbp_mass",
              "ct_wa_kidney_mass",
              "ct_wa_gi_mass"],
    "ct_upperabd": [
        "ct_upperabd_routine",
        "ct_upperabd_hbp_mass"],
    "ct_lowerabd": [
        "ct_lowerabd_appendix"
    ],
    "cta_wa": ["cta_wa_gi_bleed", 
               "cta_wa_mesenteric_ischemia",
               "cta_wa_aaa_rupture"]
}


# Map `exam_id` to `exam_name`
## The order of this dict appeared in drop down
exam_id_name_map = {
    # exam_id: exam_name
   "ct_wa": "CTWA",
   "ct_upperabd": "CT Upper Abd",
   "ct_lowerabd": "CT Lower Abd",
   "cta_wa": "CTA Whole Abd",
}

# Map `protocol_id` to `protocol_name`
protocols_id_name_map = {
    # CTWA
    "ct_wa_routine": "Routine WA",
    "ct_wa_gut_obs": "Gut Obstruction",
    "ct_wa_infect": "Intra-abdominal infection",
    "ct_wa_leak_fist_collect": "Leak-Fistula-Collection",
    "ct_wa_diver": "Diverticulitis",
    "ct_wa_pancrea": "Pancreatitis",
    "ct_wa_free_air": "Free Air",
    "ct_wa_solid_rupture": "Solid Organ Rupture",
    "ct_wa_gi_perforate": "GI Perforation",
    "ct_wa_hbp_mass": "HBP mass/abscess (CTWA)",
    "ct_wa_kidney_mass": "Kidney mass/abscess",
    "ct_wa_gi_mass": "GI Mass",
    # CT upper abd
    "ct_upperabd_routine": "Routine Upper Abd",
    "ct_upperabd_hbp_mass": "HBP mass/abscess (Upper)",
    # CT Lower Abd
    "ct_lowerabd_appendix": "Appendicitis",
    # CTA WA
    "cta_wa_gi_bleed": "GI Bleed",
    "cta_wa_mesenteric_ischemia": "Mesenteric Ischemia",
    "cta_wa_aaa_rupture": "AAA Rupture"
}


# Actual Protocols
protocols = {
    # by `protocol_id`
    
    # CTWA
    ## Routine WA
    "ct_wa_routine": {
        "protocol_name": protocols_id_name_map["ct_wa_routine"],
        "exam_id": "ct_wa",
        "exam_name": exam_id_name_map["ct_wa"],
        "phase_design_text": """
- Venous (whole)
- Delay (liver)
""",
        "contrast_text": "Oral (limited water), Rectal (water)"
    },
    ## Solid Organ Rupture
    "ct_wa_solid_rupture": {
        "protocol_name": protocols_id_name_map["ct_wa_solid_rupture"],
        "exam_id": "ct_wa",
        "exam_name": exam_id_name_map["ct_wa"],
        "phase_design_text": """
- Plain (whole)
- Late A (upper)
- Venous (whole)
- Delay (upper)
""",
        "contrast_text": "No oral, No rectal"
    },
    ## Free Air
    "ct_wa_free_air": {
        "protocol_name": protocols_id_name_map["ct_wa_free_air"],
        "exam_id": "ct_wa",
        "exam_name": exam_id_name_map["ct_wa"],
        "phase_design_text": """
- Plain
- Venous (may be)
""",
        "contrast_text": "Oral (positive), Rectal (positive) [If not stable -> no oral, no rectal]"
    },
    ## GI Perforate
    "ct_wa_gi_perforate": {
        "protocol_name": protocols_id_name_map["ct_wa_gi_perforate"],
        "exam_id": "ct_wa",
        "exam_name": exam_id_name_map["ct_wa"],
        "phase_design_text": """
- Venous
- Delay (liver)
""",
        "contrast_text": "Oral (limited positive), Rectal (positive)"
    },
    ## Gut Obstruction 
    "ct_wa_gut_obs": {
        "protocol_name": protocols_id_name_map["ct_wa_gut_obs"],
        "exam_id": "ct_wa",
        "exam_name": exam_id_name_map["ct_wa"],
        "phase_design_text": """
- Venous (whole)
- Delay 3 min (liver)
""",
        "contrast_text": "No oral, No rectal"
    },
    ## HBP mass/abscess (CTWA)
    "ct_wa_hbp_mass": {
        "protocol_name": protocols_id_name_map["ct_wa_hbp_mass"],
        "exam_id": "ct_wa",
        "exam_name": exam_id_name_map["ct_wa"],
        "phase_design_text": """
- Plain (upper)
- Late A (upper)
- Venous (whole)
- Delay (upper)
""",
        "contrast_text": "Oral (limited water), No rectal"
    },
    ## Kidney mass/abscess
    "ct_wa_kidney_mass": {
        "protocol_name": protocols_id_name_map["ct_wa_kidney_mass"],
        "exam_id": "ct_wa",
        "exam_name": exam_id_name_map["ct_wa"],
        "phase_design_text": """
- Plain (KUB)
- Late A (upper)
- Venous (100 sec)
- Delay (KUB)
""",
        "contrast_text": "Oral (limited water), No rectal"
    },
    ## GI Mass
    "ct_wa_gi_mass": {
        "protocol_name": protocols_id_name_map["ct_wa_gi_mass"],
        "exam_id": "ct_wa",
        "exam_name": exam_id_name_map["ct_wa"],
        "phase_design_text": """
- Venous (whole)
- Delay (liver)
""",
        "contrast_text": "Oral (full positive), Rectal (water)"
    },
    ## Diverticulitis
    "ct_wa_diver": {
        "protocol_name": protocols_id_name_map["ct_wa_diver"],
        "exam_id": "ct_wa",
        "exam_name": exam_id_name_map["ct_wa"],
        "phase_design_text": """
- Venous (whole)
- Delay (liver)
""",
        "contrast_text": "Oral (limited water), Rectal (1 L, positive CM)"
    },
    ## Pancreatitis
    "ct_wa_pancrea": {
        "protocol_name": protocols_id_name_map["ct_wa_pancrea"],
        "exam_id": "ct_wa",
        "exam_name": exam_id_name_map["ct_wa"],
        "phase_design_text": """
- Plain (upper)
- Late A (upper)
- Venous (whole)
- Delay (upper)
""",
        "contrast_text": "Oral (limited water), No rectal"
    },
    ## Intra-abdominal infection
    "ct_wa_infect": {
        "protocol_name": protocols_id_name_map["ct_wa_infect"],
        "exam_id": "ct_wa",
        "exam_name": exam_id_name_map["ct_wa"],
        "phase_design_text": """
- Plain (whole)
- Late A (upper)
- Venous (whole)
- Delay (upper)
""",
        "contrast_text": "Oral (limited water), Rectal (water)"
    },
    ## Leak-Fistula-Collection
    "ct_wa_leak_fist_collect": {
        "protocol_name": protocols_id_name_map["ct_wa_leak_fist_collect"],
        "exam_id": "ct_wa",
        "exam_name": exam_id_name_map["ct_wa"],
        "phase_design_text": """
- Venous (whole)
- Delay (liver)
""",
        "contrast_text": "Oral (if Hx bowel resect -> full positive; If not -> limited positive), Rectal (positive) ?"
    },
    # "protocol_id": {
    #     "protocol_name": protocols_id_name_map["protocol_id"],
    #     "exam_id": "xxx",
    #     "exam_name": exam_id_name_map["xxx"],
    #     "phase_design_text": """""",
    #     "contrast_text": ""
    # },
    ## Routine Upper Abd
    "ct_upperabd_routine": {
        "protocol_name": protocols_id_name_map["ct_upperabd_routine"],
        "exam_id": "ct_upperabd",
        "exam_name": exam_id_name_map["ct_upperabd"],
        "phase_design_text": """
- Venous (upper)
- Delay (upper)
""",
        "contrast_text": "Oral (limited water), No rectal"
    },
    ## HBP mass/abscess (Upper)
    "ct_upperabd_hbp_mass": {
        "protocol_name": protocols_id_name_map["ct_upperabd_hbp_mass"],
        "exam_id": "ct_upperabd",
        "exam_name": exam_id_name_map["ct_upperabd"],
        "phase_design_text": """
- Plain (upper)
- Late A (upper)
- Venous (upper)
- Delay (upper)
""",
        "contrast_text": "Oral (limited water), No rectal"
    },
    # "protocol_id": {
    #     "protocol_name": protocols_id_name_map["protocol_id"],
    #     "exam_id": "xxx",
    #     "exam_name": exam_id_name_map["xxx"],
    #     "phase_design_text": """""",
    #     "contrast_text": ""
    # },
    # CT lower abd
    "ct_lowerabd_appendix": {
        "protocol_name": protocols_id_name_map["ct_lowerabd_appendix"],
        "exam_id": "ct_lowerabd",
        "exam_name": exam_id_name_map["ct_lowerabd"],
        "phase_design_text": """
- Venous 120 sec (L3 to pubic symphysis)
""",
        "contrast_text": "Rectal (Positive 1 L สวนถึง cecum), No oral"
    },
    # CTA WA
    ## GI Bleed
    "cta_wa_gi_bleed": {
        "protocol_name": protocols_id_name_map["cta_wa_gi_bleed"],
        "exam_id": "cta_wa",
        "exam_name": exam_id_name_map["cta_wa"],
        "phase_design_text": """
- Plain (whole)
- CTA (whole)
- Venous (whole)
- Delay (whole)
""",
        "contrast_text": "No oral, No rectal"
    },
    ## Mesenteric Ischemia
    "cta_wa_mesenteric_ischemia": {
        "protocol_name": protocols_id_name_map["cta_wa_mesenteric_ischemia"],
        "exam_id": "cta_wa",
        "exam_name": exam_id_name_map["cta_wa"],
        "phase_design_text": """
- Plain (whole)
- CTA (whole)
- Venous (whole)
- Delay (whole)
""",
        "contrast_text": "Oral (limited water), Rectal (water)"
    },
    "cta_wa_aaa_rupture": {
        "protocol_name": protocols_id_name_map["cta_wa_aaa_rupture"],
        "exam_id": "cta_wa",
        "exam_name": exam_id_name_map["cta_wa"],
        "phase_design_text": """
- Plain (whole)
- CTA (maybe ถ้ามีเวลา คนไข้ stable)
- Venous (maybe ถ้ามีเวลา คนไข้ stable)
""",
        "contrast_text": "No oral, No rectal"
    },
    # "protocol_id": {
    #     "protocol_name": protocols_id_name_map["protocol_id"],
    #     "exam_id": "xxx",
    #     "exam_name": exam_id_name_map["xxx"],
    #     "phase_design_text": """""",
    #     "contrast_text": ""
    # },
}


# Reverse Mapping

## Map `exam_name` to `exam_id`
exam_name_id_map = {v: k for k, v in exam_id_name_map.items()}

## Map `protocol_name` to `protocol_id`
protocols_name_id_map = {v: k for k, v in protocols_id_name_map.items()}

## Group `protocol_name` in each `exam_id`
exam_id_protocols_name_map = {}

## Loop through each key and list in dict1
for key, value_list in exam_id_protocols_id_map.items():
    # Map each value in the list to its corresponding value in dict2
    mapped_list = [protocols_id_name_map[value] for value in value_list]
    # Store the mapped list in the result dictionary
    exam_id_protocols_name_map[key] = mapped_list
