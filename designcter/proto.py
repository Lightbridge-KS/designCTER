# Group `protocol_id` in each `exam_id`
## The order of element in this list appeared in drop down
exam_id_protocols_id_map = {
    "ct_wa": ["ct_wa_routine", 
              "ct_wa_full",
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
    "cta_wa": ["cta_wa_mesenteric_ischemia",
               "cta_wa_gi_bleed", 
               "cta_wa_aaa_rupture"],
    "ct_upperabd": [
        "ct_upperabd_routine",
        "ct_upperabd_biliary_stone",
        "ct_upperabd_hbp_mass",
        "ct_upperabd_adrenal_mass"],
    "ct_lowerabd": [
        "ct_lowerabd_appendix"
    ],
    "ct_kub": [
        "ct_kub_nc",
        "ct_kub_stone",
        "ct_kub_hematuria",
        "ct_kub_kidney_mass"
    ],
    "cta_pe": [
        "cta_pe_no_dvt",
        "cta_pe_with_dvt"
    ],
    "ct_chest": [
        "ct_chest_routine",
        "ct_chest_nc",
        "ct_chest_nodule_mass",
        "ct_chest_tbm",
        "ct_chest_dysphagia",
        "ct_chest_eso",
        "ct_chest_svc"
    ],
    "cta_chest": [
        "cta_chest_hemoptysis", 
        "cta_chest_trauma"
    ],
    "cta_aorta": {
        "cta_aorta_first",
        "cta_aorta_dissect",
        "cta_aorta_aaa_postop"
    },
    "cta_runoff": {
        "cta_runoff_old",
        "cta_runoff_young"
    }
}


# Map `exam_id` to `exam_name`
## The order of this dict appeared in drop down
exam_id_name_map = {
    # exam_id: exam_name
   "ct_wa": "CTWA",
   "cta_wa": "CTA Whole Abd",
   "ct_upperabd": "CT Upper Abd",
   "ct_lowerabd": "CT Lower Abd",
   "ct_kub": "CT KUB",
   "cta_pe": "CTA for PE",
   "ct_chest": "CT Chest",
   "cta_chest": "CTA Chest",
   "cta_aorta": "CTA Whole Aorta",
   "cta_runoff": "CTA runoff"
}

# Map `protocol_id` to `protocol_name`
protocols_id_name_map = {
    # CTWA
    "ct_wa_routine": "Routine WA",
    "ct_wa_full": "Full WA", 
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
    "ct_upperabd_biliary_stone": "Biliary Stone",
    "ct_upperabd_hbp_mass": "HBP mass/abscess (Upper)",
    "ct_upperabd_adrenal_mass": "Adrenal mass/abscess",
    # CT Lower Abd
    "ct_lowerabd_appendix": "Appendicitis",
    # CT KUB
    "ct_kub_nc": "CT KUB (non-contrast)",
    "ct_kub_stone": "KUB Stone", 
    "ct_kub_hematuria": "Hematuria",
    "ct_kub_kidney_mass": "Kidney mass/Abscess",
    # CTA WA
    "cta_wa_gi_bleed": "GI Bleed",
    "cta_wa_mesenteric_ischemia": "Mesenteric Ischemia",
    "cta_wa_aaa_rupture": "AAA Rupture",
    # CTA for PE
    "cta_pe_no_dvt": "CTA for PE (ไม่ลากขา)",
    "cta_pe_with_dvt": "CTA for PE with DVT",
    # CT Chest
    "ct_chest_routine": "Routine CT Chest",
    "ct_chest_nc": "CT Chest (non-contrast)",
    "ct_chest_nodule_mass": "Nodule/mass characterization",
    "ct_chest_tbm": "Tracheobronchomalacia",
    "ct_chest_dysphagia": "Dysphagia",
    "ct_chest_eso": "CT esophagogram",
    "ct_chest_svc": "SVC Obstruction",
    
    # CTA Chest
    "cta_chest_hemoptysis": "Hemoptysis",
    "cta_chest_trauma": "CTA Chest trauma",
    # CTA Aorta
    "cta_aorta_first": "Aorta first time",
    "cta_aorta_dissect": "Aortic Dissection",
    "cta_aorta_aaa_postop": "AAA Post-op",
    # CTA Runoff
    "cta_runoff_old": "CTA Runoff",
    "cta_runoff_young": "CTA Runoff (< 60 yr)"
}


# Actual Protocols
protocols = {
    # by `protocol_id`
    
    # CTWA
    ## Routine WA
    "ct_wa_routine": {
        "protocol_name": protocols_id_name_map["ct_wa_routine"],
        "exam_name": exam_id_name_map["ct_wa"],
        "phase_design_text": """
- Venous (whole)
- Delay (liver)
""",
        "contrast_text": "Oral (limited water), Rectal (water)"
    },
    ## Full WA
    "ct_wa_full": {
        "protocol_name": None,
        "exam_name": exam_id_name_map["ct_wa"],
        "phase_design_text": """
- Plain (whole)
- Late A (upper)
- Venous (whole)
- Delay (liver)
""",
        "contrast_text": "Oral (?), Rectal (?)"
    },  
    ## Solid Organ Rupture
    "ct_wa_solid_rupture": {
        "protocol_name": protocols_id_name_map["ct_wa_solid_rupture"],
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
        "exam_name": exam_id_name_map["ct_wa"],
        "phase_design_text": """
- Venous (whole)
- Delay (liver)
""",
        "contrast_text": "Oral (if Hx bowel resect -> full positive; If not -> limited positive), Rectal (positive) ?"
    },
    # "protocol_id": {
    #     "protocol_name": protocols_id_name_map["protocol_id"],
    #     "exam_name": exam_id_name_map["xxx"],
    #     "phase_design_text": """""",
    #     "contrast_text": ""
    # },
    ## Routine Upper Abd
    "ct_upperabd_routine": {
        "protocol_name": protocols_id_name_map["ct_upperabd_routine"],
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
        "exam_name": exam_id_name_map["ct_upperabd"],
        "phase_design_text": """
- Plain (upper)
- Late A (upper)
- Venous (upper)
- Delay (upper)
""",
        "contrast_text": "Oral (limited water), No rectal"
    },
    ## Biliary Stone
    "ct_upperabd_biliary_stone": {
        "protocol_name": protocols_id_name_map["ct_upperabd_biliary_stone"],
        "exam_name": exam_id_name_map["ct_upperabd"],
        "phase_design_text": """
- Plain (upper)
- Late A (upper)
- Venous (upper)
- Delay (liver)
""",
        "contrast_text": "Oral (limited water), No rectal"
    },
    ## Adrenal mass/abscess
    "ct_upperabd_adrenal_mass": {
        "protocol_name": protocols_id_name_map["ct_upperabd_adrenal_mass"],
        "exam_name": exam_id_name_map["ct_upperabd"],
        "phase_design_text": """
- Plain (upper)
- Late A (upper)
- Venous (upper)
- Delay 3 min (upper)
*** Check ภาพ +/- Delay 15 min (adrenal)
""",
        "contrast_text": "Oral (limited water), No rectal"
    },
    # "protocol_id": {
    #     "protocol_name": protocols_id_name_map["protocol_id"],
    #     "exam_name": exam_id_name_map["xxx"],
    #     "phase_design_text": """""",
    #     "contrast_text": ""
    # },
    # CT lower abd
    "ct_lowerabd_appendix": {
        "protocol_name": protocols_id_name_map["ct_lowerabd_appendix"],
        "exam_name": exam_id_name_map["ct_lowerabd"],
        "phase_design_text": """
- Venous 120 sec (L3 to pubic symphysis)
""",
        "contrast_text": "Rectal (Positive 1 L สวนถึง cecum), No oral"
    },
    # CT KUB
    ## CT KUB (non-contrast)
    "ct_kub_nc": {
        "protocol_name": None,
        "exam_name": "CT KUB (non-contrast)",
        "phase_design_text": """
- Plain KUB (kidneys to pubic symphysis)
*** Check ภาพก่อนเลิก
""",
        "contrast_text": "No Oral, No Rectal"
    },
    ## KUB Stone (non-contrast)
    "ct_kub_stone": {
        "protocol_name": protocols_id_name_map["ct_kub_stone"],
        "exam_name": "CT KUB (non-contrast)",
        "phase_design_text": """
- Plain KUB (kidneys to pubic symphysis)
*** Check ภาพก่อนเลิก
""",
        "contrast_text": "No Oral, No Rectal"
    },
    ## Hematuria
    "ct_kub_hematuria": {
        "protocol_name": protocols_id_name_map["ct_kub_hematuria"],
        "exam_name": exam_id_name_map["ct_kub"],
        "phase_design_text": """
- Plain (KUB)
- Late A (Kidney)
- Venous (KUB)
- Delay (KUB)
*** Check ภาพก่อนเลิก
""",
        "contrast_text": "Oral (limited water), No Rectal"
    },
    ## Kidney mass/Abscess
    "ct_kub_kidney_mass": {
        "protocol_name": protocols_id_name_map["ct_kub_kidney_mass"],
        "exam_name": exam_id_name_map["ct_kub"],
        "phase_design_text": """
*** If suspect renal mass → consider CTWA for staging
- Plain (KUB)
- Late A (Upper)
- Venous (100 sec)
- Delay (KUB)
*** Check ภาพก่อนเลิก
""",
        "contrast_text": "Oral (limited water), No Rectal"
    },
    # "protocol_id": {
    #     "protocol_name": protocols_id_name_map["protocol_id"],
    #     "exam_name": exam_id_name_map["xxx"],
    #     "phase_design_text": """""",
    #     "contrast_text": ""
    # },
    # CTA WA
    ## GI Bleed
    "cta_wa_gi_bleed": {
        "protocol_name": protocols_id_name_map["cta_wa_gi_bleed"],
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
        "exam_name": exam_id_name_map["cta_wa"],
        "phase_design_text": """
- Plain (whole)
- CTA (maybe ถ้ามีเวลา คนไข้ stable)
- Venous (maybe ถ้ามีเวลา คนไข้ stable)
""",
        "contrast_text": "No oral, No rectal"
    },
    # CTA for PE
    "cta_pe_no_dvt": {
        "protocol_name": protocols_id_name_map["cta_pe_no_dvt"],
        "exam_name": exam_id_name_map["cta_pe"],
        "phase_design_text": """
- CTPA (chest)
- Venous (chest)
""",
        "contrast_text": "IV contrast"
    },
    "cta_pe_with_dvt": {
        "protocol_name": protocols_id_name_map["cta_pe_with_dvt"],
        "exam_name": exam_id_name_map["cta_pe"],
        "phase_design_text": """
- CTPA (chest)
- Venous (chest, legs)
""",
        "contrast_text": "IV contrast"
    },
    # "protocol_id": {
    #     "protocol_name": protocols_id_name_map["protocol_id"],
    #     "exam_name": exam_id_name_map["xxx"],
    #     "phase_design_text": """""",
    #     "contrast_text": ""
    # },
    # CT Chest
    ## Routine Chest
    "ct_chest_routine": {
        "protocol_name": protocols_id_name_map["ct_chest_routine"],
        "exam_name": exam_id_name_map["ct_chest"],
        "phase_design_text": """
- **maybe** plain (chest)
- Late A (chest)
""",
        "contrast_text": "IV contrast"
    },   
    ## CT Chest (non-contrast)
    "ct_chest_nc": {
        "protocol_name": None,
        "exam_name": "CT Chest (non-contrast)",
        "phase_design_text": """
- plain (chest)
""",
        "contrast_text": "No IV contrast"
    },
    ## Nodule/mass characterization
    "ct_chest_nodule_mass": {
        "protocol_name": protocols_id_name_map["ct_chest_nodule_mass"],
        "exam_name": exam_id_name_map["ct_chest"],
        "phase_design_text": """
- Plain (chest)
- Late A (chest)
""",
        "contrast_text": "IV contrast"
    },
    ## Tracheobronchomalacia
    "ct_chest_tbm": {
        "protocol_name": protocols_id_name_map["ct_chest_tbm"],
        "exam_name": exam_id_name_map["ct_chest"],
        "phase_design_text": """
- Plain (chest, dynamic expiration)
""",
        "contrast_text": "No IV contrast"
    },
    ## Dysphagia
    "ct_chest_dysphagia": {
        "protocol_name": protocols_id_name_map["ct_chest_dysphagia"],
        "exam_name": exam_id_name_map["ct_chest"],
        "phase_design_text": """
- Plain (chest)
- Venous (chest)
""",
        "contrast_text": "IV contrast, Oral (limited water)"
    },
    ## CT esophagogram
    "ct_chest_eso": {
        "protocol_name": protocols_id_name_map["ct_chest_eso"],
        "exam_name": exam_id_name_map["ct_chest"],
        "phase_design_text": """
- Plain (Chest, reduced dose) ก่อนกิน CM
- จากนั้น กิน CM 1 cup (250 ml) ที่เตียง
- Venous (Chest) หลังกิน CM
""",
        "contrast_text": "Oral (Positive CM)"
    },
    "ct_chest_svc": {
        "protocol_name": protocols_id_name_map["ct_chest_svc"],
        "exam_name": exam_id_name_map["ct_chest"],
        "phase_design_text": """
- Plain (Chest, reduced dose)
- Late A (Chest)
- Immediate delay (Chest)
""",
        "contrast_text": "IV contrast"
    },
    # CTA Chest
    ## Hemoptysis
    "cta_chest_hemoptysis": {
        "protocol_name": protocols_id_name_map["cta_chest_hemoptysis"],
        "exam_name": exam_id_name_map["cta_chest"],
        "phase_design_text": """
- Plain (Chest)
- CTA (Apex to L2) → Systemic arterial phase
- Immediate delay (Chest)
* Note: L2 (Celiac Axis) ให้เห็น renal artery origin
""",
        "contrast_text": "IV contrast"
    },
    ## CTA Chest trauma
    "cta_chest_trauma": {
        "protocol_name": protocols_id_name_map["cta_chest_trauma"],
        "exam_name": exam_id_name_map["cta_chest"],
        "phase_design_text": """
- CTA (chest)
- Venous (chest)
""",
        "contrast_text": "IV Contrast"
    },
    # CTA Aorta
    ## Aorta first time
    "cta_aorta_first": {
        "protocol_name": protocols_id_name_map["cta_aorta_first"],
        "exam_name": exam_id_name_map["cta_aorta"],
        "phase_design_text": """
- Plain (whole aorta)
- CTA (whole aorta)
- Immediate delay (whole aorta)
""",
        "contrast_text": "IV contrast"
    },    
    ## Aortic Dissection
    "cta_aorta_dissect": {
        "protocol_name": protocols_id_name_map["cta_aorta_dissect"],
        "exam_name": exam_id_name_map["cta_aorta"],
        "phase_design_text": """
- Plain (whole aorta)
- CTA (whole aorta)
- Immediate delay (whole aorta)
""",
        "contrast_text": "IV contrast"
    },
    ## AAA Post-op
    "cta_aorta_aaa_postop": {
        "protocol_name": protocols_id_name_map["cta_aorta_aaa_postop"],
        "exam_name": exam_id_name_map["cta_aorta"],
        "phase_design_text": """
- Plain (whole aorta)
- CTA (whole aorta)
- Immediate delay (whole aorta)
""",
        "contrast_text": "IV contrast"
    },
    # CTA Runoff
    "cta_runoff_old": {
        "protocol_name": protocols_id_name_map["cta_runoff_old"],
        "exam_name": exam_id_name_map["cta_runoff"],
        "phase_design_text": """
ขา → Aortic bifurcation to feet
แขน → mid-heart to hands
- Plain
- CTA
- Immediate delay
""",
        "contrast_text": "IV contrast"
    },   
    "cta_runoff_young": {
        "protocol_name": protocols_id_name_map["cta_runoff_young"],
        "exam_name": exam_id_name_map["cta_runoff"],
        "phase_design_text": """
ขา → Aortic bifurcation to feet
แขน → mid-heart to hands
- CTA
- Immediate delay
""",
        "contrast_text": "IV contrast"
    },   
    # "protocol_id": {
    #     "protocol_name": protocols_id_name_map["protocol_id"],
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
