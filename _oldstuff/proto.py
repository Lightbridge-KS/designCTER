# Hierarchical structure Levels
# `category` -> `exam` -> `protocol`
from typing import TypedDict, Dict, List, Annotated

# Level 1 
category = ["Body", "Neuro", "Trauma"]


# Level 2
## Map `exam_id` to `exam_name`
## The order of this dict appeared in drop down

ExamIDToExamName = Annotated[Dict[str, str], "Maps exam_id to exam_name"]

class ExamIDName(TypedDict):
    """
    A TypedDict representing the mapping of exam types to their corresponding exam ID to exam name mappings.
    """
    Body: ExamIDToExamName
    Neuro: ExamIDToExamName
    Trauma: ExamIDToExamName

exam_id_name: ExamIDName = {
    "Body": {
        # exam_id: exam_name
        "ct_wa": "CTWA",
        "cta_wa": "CTA Whole Abd",
        "ct_upperabd": "CT Upper Abd",
        "ct_lowerabd": "CT Lower Abd",
        "ct_kub": "CT KUB",
        "cta_pe": "CTA for PE",
        "ct_chest": "CT Chest",
        "ct_chest_wa": "CT Chest + Whole Abd",
        "cta_chest": "CTA Chest",
        "cta_aorta": "CTA Whole Aorta",
        "cta_runoff": "CTA runoff"
    },
    "Neuro": {
        "ct_brain_nc": "CT Brain (non-contrast)",
        "ct_brain_with_cm": "CT Brain with Contrast",
        "cta_ctv_brain": "CTA/CTV Brain",
        "mri_spine": "MRI Spine"
    },
    "Trauma": {
        "ct_neuro_trauma": "CT Neuro Trauma",
        "ct_body_trauma": "CT Body Trauma"
    }
}

# Level 3
## Group `protocol_id` in each `exam_id`
## The order of element in this list appeared in drop down
exam_id_protocol_id = {
    # Body
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
    "ct_chest_wa": [
        "ct_chest_wa_full"
    ],
    "cta_chest": [
        "cta_chest_hemoptysis",
        "cta_chest_trauma"
    ],
    "cta_aorta": [
        "cta_aorta_first",
        "cta_aorta_dissect",
        "cta_aorta_aaa_postop"
    ],
    "cta_runoff": [
        "cta_runoff_old",
        "cta_runoff_young"
    ],
    # Neuro
    "ct_brain_nc": [
        "ct_brain_nc_routine"
    ],
    "ct_brain_with_cm": [
        "ct_brain_with_cm_routine"
    ],
    "cta_ctv_brain": [
        "cta_brain_aneurysm",
        "ctv_brain_vst"
    ],
    "ct_neuro_trauma": [
        "cta_neck_trauma",
        "ct_facial_trauma",
        "ct_orbit_trauma"
    ],
    "ct_body_trauma": [
        "pan_scan",
        "cta_blunt_abd",
        "cta_penetrate_abd",
        "ct_second_look_abd",
        "cta_chest_trauma"
    ],
    "mri_spine": [
        "mri_screening_whole_spine"
    ]
}


# Map `protocol_id` to `protocol_name`
protocols_id_name = {
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
    # CT Chest + WA
    "ct_chest_wa_full": "Full CT Chest + WA",

    # CTA Chest
    "cta_chest_hemoptysis": "Hemoptysis",
    "cta_chest_trauma": "CTA Chest trauma",
    # CTA Aorta
    "cta_aorta_first": "Aorta first time",
    "cta_aorta_dissect": "Aortic Dissection",
    "cta_aorta_aaa_postop": "AAA Post-op",
    # CTA Runoff
    "cta_runoff_old": "CTA Runoff",
    "cta_runoff_young": "CTA Runoff (< 60 yr)",
    # CT Brain (NC)
    "ct_brain_nc_routine": "CT Brain (non-contrast)",
    # CTA/CTV Brain
    "cta_brain_aneurysm": "Intracranial aneurysm",
    "ctv_brain_vst": "Venous Sinus Thrombosis",
    # CT Brain with CM
    "ct_brain_with_cm_routine": "CT Brain with Contrast",
    # CT Neuro Trauma
    "cta_neck_trauma": "CTA Neck (trauma)",
    "ct_facial_trauma": "CT Facial Bone (trauma)",
    "ct_orbit_trauma": "CT Orbit (trauma)",
    # CT Body Trauma
    "pan_scan": "Pan-Scan Whole body CT (trauma)",
    "cta_blunt_abd": "CTA Blunt Abdomen (trauma)",
    "cta_penetrate_abd": "CTA Penetrating Abd (trauma)",
    "ct_second_look_abd": "CT Second look Abd (trauma)",
    "cta_chest_trauma": "CTA Chest (trauma)",
    # MRI Spine
    "mri_screening_whole_spine": "MRI Screening Whole Spine"
}


# Actual Protocols
protocols = {
    # by `protocol_id`

    # CTWA
    # Routine WA
    "ct_wa_routine": {
        "protocol_name": protocols_id_name["ct_wa_routine"],
        "exam_name": exam_id_name["Body"]["ct_wa"],
        "phase_design_text": """
- Venous (whole)
- Delay (liver)
""",
        "contrast_text": "Oral (limited water), Rectal (water)"
    },
    # Full WA
    "ct_wa_full": {
        "protocol_name": None,
        "exam_name": exam_id_name["Body"]["ct_wa"],
        "phase_design_text": """
- Plain (whole)
- Late A (upper)
- Venous (whole)
- Delay (liver)
""",
        "contrast_text": "Oral (?), Rectal (?)"
    },
    # Solid Organ Rupture
    "ct_wa_solid_rupture": {
        "protocol_name": protocols_id_name["ct_wa_solid_rupture"],
        "exam_name": exam_id_name["Body"]["ct_wa"],
        "phase_design_text": """
- Plain (whole)
- Late A (upper)
- Venous (whole)
- Delay (upper)
""",
        "contrast_text": "No oral, No rectal"
    },
    # Free Air
    "ct_wa_free_air": {
        "protocol_name": protocols_id_name["ct_wa_free_air"],
        "exam_name": exam_id_name["Body"]["ct_wa"],
        "phase_design_text": """
- Plain
- Venous (may be)
""",
        "contrast_text": "Oral (positive), Rectal (positive) [If not stable -> no oral, no rectal]"
    },
    # GI Perforate
    "ct_wa_gi_perforate": {
        "protocol_name": protocols_id_name["ct_wa_gi_perforate"],
        "exam_name": exam_id_name["Body"]["ct_wa"],
        "phase_design_text": """
- Venous
- Delay (liver)
""",
        "contrast_text": "Oral (limited positive), Rectal (positive)"
    },
    # Gut Obstruction
    "ct_wa_gut_obs": {
        "protocol_name": protocols_id_name["ct_wa_gut_obs"],
        "exam_name": exam_id_name["Body"]["ct_wa"],
        "phase_design_text": """
- Venous (whole)
- Delay 3 min (liver)
""",
        "contrast_text": "No oral, No rectal"
    },
    # HBP mass/abscess (CTWA)
    "ct_wa_hbp_mass": {
        "protocol_name": protocols_id_name["ct_wa_hbp_mass"],
        "exam_name": exam_id_name["Body"]["ct_wa"],
        "phase_design_text": """
- Plain (upper)
- Late A (upper)
- Venous (whole)
- Delay (upper)
""",
        "contrast_text": "Oral (limited water), No rectal"
    },
    # Kidney mass/abscess
    "ct_wa_kidney_mass": {
        "protocol_name": protocols_id_name["ct_wa_kidney_mass"],
        "exam_name": exam_id_name["Body"]["ct_wa"],
        "phase_design_text": """
- Plain (KUB)
- Late A (upper)
- Venous (100 sec)
- Delay (KUB)
""",
        "contrast_text": "Oral (limited water), No rectal"
    },
    # GI Mass
    "ct_wa_gi_mass": {
        "protocol_name": protocols_id_name["ct_wa_gi_mass"],
        "exam_name": exam_id_name["Body"]["ct_wa"],
        "phase_design_text": """
- Venous (whole)
- Delay (liver)
""",
        "contrast_text": "Oral (full positive), Rectal (water)"
    },
    # Diverticulitis
    "ct_wa_diver": {
        "protocol_name": protocols_id_name["ct_wa_diver"],
        "exam_name": exam_id_name["Body"]["ct_wa"],
        "phase_design_text": """
- Venous (whole)
- Delay (liver)
""",
        "contrast_text": "Oral (limited water), Rectal (1 L, positive CM)"
    },
    # Pancreatitis
    "ct_wa_pancrea": {
        "protocol_name": protocols_id_name["ct_wa_pancrea"],
        "exam_name": exam_id_name["Body"]["ct_wa"],
        "phase_design_text": """
- Plain (upper)
- Late A (upper)
- Venous (whole)
- Delay (upper)
""",
        "contrast_text": "Oral (limited water), No rectal"
    },
    # Intra-abdominal infection
    "ct_wa_infect": {
        "protocol_name": protocols_id_name["ct_wa_infect"],
        "exam_name": exam_id_name["Body"]["ct_wa"],
        "phase_design_text": """
- Plain (whole)
- Late A (upper)
- Venous (whole)
- Delay (upper)
""",
        "contrast_text": "Oral (limited water), Rectal (water)"
    },
    # Leak-Fistula-Collection
    "ct_wa_leak_fist_collect": {
        "protocol_name": protocols_id_name["ct_wa_leak_fist_collect"],
        "exam_name": exam_id_name["Body"]["ct_wa"],
        "phase_design_text": """
- Venous (whole)
- Delay (liver)
""",
        "contrast_text": "Oral (if Hx bowel resect -> full positive; If not -> limited positive), Rectal (positive) ?"
    },
    # "protocol_id": {
    #     "protocol_name": protocols_id_name["protocol_id"],
    #     "exam_name": exam_id_name["Body"]["xxx"],
    #     "phase_design_text": """""",
    #     "contrast_text": ""
    # },
    # Routine Upper Abd
    "ct_upperabd_routine": {
        "protocol_name": protocols_id_name["ct_upperabd_routine"],
        "exam_name": exam_id_name["Body"]["ct_upperabd"],
        "phase_design_text": """
- Venous (upper)
- Delay (upper)
""",
        "contrast_text": "Oral (limited water), No rectal"
    },
    # HBP mass/abscess (Upper)
    "ct_upperabd_hbp_mass": {
        "protocol_name": protocols_id_name["ct_upperabd_hbp_mass"],
        "exam_name": exam_id_name["Body"]["ct_upperabd"],
        "phase_design_text": """
- Plain (upper)
- Late A (upper)
- Venous (upper)
- Delay (upper)
""",
        "contrast_text": "Oral (limited water), No rectal"
    },
    # Biliary Stone
    "ct_upperabd_biliary_stone": {
        "protocol_name": protocols_id_name["ct_upperabd_biliary_stone"],
        "exam_name": exam_id_name["Body"]["ct_upperabd"],
        "phase_design_text": """
- Plain (upper)
- Late A (upper)
- Venous (upper)
- Delay (liver)
""",
        "contrast_text": "Oral (limited water), No rectal"
    },
    # Adrenal mass/abscess
    "ct_upperabd_adrenal_mass": {
        "protocol_name": protocols_id_name["ct_upperabd_adrenal_mass"],
        "exam_name": exam_id_name["Body"]["ct_upperabd"],
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
    #     "protocol_name": protocols_id_name["protocol_id"],
    #     "exam_name": exam_id_name["Body"]["xxx"],
    #     "phase_design_text": """""",
    #     "contrast_text": ""
    # },
    # CT lower abd
    "ct_lowerabd_appendix": {
        "protocol_name": protocols_id_name["ct_lowerabd_appendix"],
        "exam_name": exam_id_name["Body"]["ct_lowerabd"],
        "phase_design_text": """
- Venous 120 sec (L3 to pubic symphysis)
""",
        "contrast_text": "Rectal (Positive 1 L สวนถึง cecum), No oral"
    },
    # CT KUB
    # CT KUB (non-contrast)
    "ct_kub_nc": {
        "protocol_name": None,
        "exam_name": "CT KUB (non-contrast)",
        "phase_design_text": """
- Plain KUB (kidneys to pubic symphysis)
*** Check ภาพก่อนเลิก
""",
        "contrast_text": "No Oral, No Rectal"
    },
    # KUB Stone (non-contrast)
    "ct_kub_stone": {
        "protocol_name": protocols_id_name["ct_kub_stone"],
        "exam_name": "CT KUB (non-contrast)",
        "phase_design_text": """
- Plain KUB (kidneys to pubic symphysis)
*** Check ภาพก่อนเลิก
""",
        "contrast_text": "No Oral, No Rectal"
    },
    # Hematuria
    "ct_kub_hematuria": {
        "protocol_name": protocols_id_name["ct_kub_hematuria"],
        "exam_name": exam_id_name["Body"]["ct_kub"],
        "phase_design_text": """
- Plain (KUB)
- Late A (Kidney)
- Venous (KUB)
- Delay (KUB)
*** Check ภาพก่อนเลิก
""",
        "contrast_text": "Oral (limited water), No Rectal"
    },
    # Kidney mass/Abscess
    "ct_kub_kidney_mass": {
        "protocol_name": protocols_id_name["ct_kub_kidney_mass"],
        "exam_name": exam_id_name["Body"]["ct_kub"],
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
    #     "protocol_name": protocols_id_name["protocol_id"],
    #     "exam_name": exam_id_name["Body"]["xxx"],
    #     "phase_design_text": """""",
    #     "contrast_text": ""
    # },
    # CTA WA
    # GI Bleed
    "cta_wa_gi_bleed": {
        "protocol_name": protocols_id_name["cta_wa_gi_bleed"],
        "exam_name": exam_id_name["Body"]["cta_wa"],
        "phase_design_text": """
- Plain (whole)
- CTA (whole)
- Venous (whole)
- Delay (whole)
""",
        "contrast_text": "No oral, No rectal"
    },
    # Mesenteric Ischemia
    "cta_wa_mesenteric_ischemia": {
        "protocol_name": protocols_id_name["cta_wa_mesenteric_ischemia"],
        "exam_name": exam_id_name["Body"]["cta_wa"],
        "phase_design_text": """
- Plain (whole)
- CTA (whole)
- Venous (whole)
- Delay (whole)
""",
        "contrast_text": "Oral (limited water), Rectal (water)"
    },
    "cta_wa_aaa_rupture": {
        "protocol_name": protocols_id_name["cta_wa_aaa_rupture"],
        "exam_name": exam_id_name["Body"]["cta_wa"],
        "phase_design_text": """
- Plain (whole)
- CTA (maybe ถ้ามีเวลา คนไข้ stable)
- Venous (maybe ถ้ามีเวลา คนไข้ stable)
""",
        "contrast_text": "No oral, No rectal"
    },
    # CTA for PE
    "cta_pe_no_dvt": {
        "protocol_name": protocols_id_name["cta_pe_no_dvt"],
        "exam_name": exam_id_name["Body"]["cta_pe"],
        "phase_design_text": """
- CTPA (chest)
- Venous (chest)
""",
        "contrast_text": "IV contrast"
    },
    "cta_pe_with_dvt": {
        "protocol_name": protocols_id_name["cta_pe_with_dvt"],
        "exam_name": exam_id_name["Body"]["cta_pe"],
        "phase_design_text": """
- CTPA (chest)
- Venous (chest, legs)
""",
        "contrast_text": "IV contrast"
    },
    # "protocol_id": {
    #     "protocol_name": protocols_id_name["protocol_id"],
    #     "exam_name": exam_id_name["Body"]["xxx"],
    #     "phase_design_text": """""",
    #     "contrast_text": ""
    # },
    # CT Chest
    # Routine Chest
    "ct_chest_routine": {
        "protocol_name": protocols_id_name["ct_chest_routine"],
        "exam_name": exam_id_name["Body"]["ct_chest"],
        "phase_design_text": """
- **maybe** plain (chest)
- Late A (chest)
""",
        "contrast_text": "IV contrast"
    },
    # CT Chest (non-contrast)
    "ct_chest_nc": {
        "protocol_name": None,
        "exam_name": "CT Chest (non-contrast)",
        "phase_design_text": """
- plain (chest)
""",
        "contrast_text": "No IV contrast"
    },
    # Nodule/mass characterization
    "ct_chest_nodule_mass": {
        "protocol_name": protocols_id_name["ct_chest_nodule_mass"],
        "exam_name": exam_id_name["Body"]["ct_chest"],
        "phase_design_text": """
- Plain (chest)
- Late A (chest)
""",
        "contrast_text": "IV contrast"
    },
    # Tracheobronchomalacia
    "ct_chest_tbm": {
        "protocol_name": protocols_id_name["ct_chest_tbm"],
        "exam_name": exam_id_name["Body"]["ct_chest"],
        "phase_design_text": """
- Plain (chest, dynamic expiration)
""",
        "contrast_text": "No IV contrast"
    },
    # Dysphagia
    "ct_chest_dysphagia": {
        "protocol_name": protocols_id_name["ct_chest_dysphagia"],
        "exam_name": exam_id_name["Body"]["ct_chest"],
        "phase_design_text": """
- Plain (chest)
- Venous (chest)
""",
        "contrast_text": "IV contrast, Oral (limited water)"
    },
    # CT esophagogram
    "ct_chest_eso": {
        "protocol_name": protocols_id_name["ct_chest_eso"],
        "exam_name": exam_id_name["Body"]["ct_chest"],
        "phase_design_text": """
- Plain (Chest, reduced dose) ก่อนกิน CM
- จากนั้น กิน CM 1 cup (250 ml) ที่เตียง
- Venous (Chest) หลังกิน CM
""",
        "contrast_text": "Oral (Positive CM)"
    },
    "ct_chest_svc": {
        "protocol_name": protocols_id_name["ct_chest_svc"],
        "exam_name": exam_id_name["Body"]["ct_chest"],
        "phase_design_text": """
- Plain (Chest, reduced dose)
- Late A (Chest)
- Immediate delay (Chest)
""",
        "contrast_text": "IV contrast"
    },
    # CT Chest + WA
    "ct_chest_wa_full": {
        "protocol_name": None,
        "exam_name": exam_id_name["Body"]["ct_chest_wa"],
        "phase_design_text": """
- Plain (Chest + Whole abd)
- Late A (Chest + Upper abd)
- Venous (Whole abd)
- Delay (liver)
""",
        "contrast_text": "Oral (?), Rectal (?)"
    },
    # "protocol_id": {
    #     "protocol_name": protocols_id_name["protocol_id"],
    #     "exam_name": exam_id_name["Body"]["xxx"],
    #     "phase_design_text": """""",
    #     "contrast_text": ""
    # },
    # CTA Chest
    # Hemoptysis
    "cta_chest_hemoptysis": {
        "protocol_name": protocols_id_name["cta_chest_hemoptysis"],
        "exam_name": exam_id_name["Body"]["cta_chest"],
        "phase_design_text": """
- Plain (Chest)
- CTA (Apex to L2) → Systemic arterial phase
- Immediate delay (Chest)
* Note: L2 (Celiac Axis) ให้เห็น renal artery origin
""",
        "contrast_text": "IV contrast"
    },
    # CTA Chest trauma
    "cta_chest_trauma": {
        "protocol_name": protocols_id_name["cta_chest_trauma"],
        "exam_name": exam_id_name["Body"]["cta_chest"],
        "phase_design_text": """
- CTA (chest)
- Venous (chest)
""",
        "contrast_text": "IV Contrast"
    },
    # CTA Aorta
    # Aorta first time
    "cta_aorta_first": {
        "protocol_name": protocols_id_name["cta_aorta_first"],
        "exam_name": exam_id_name["Body"]["cta_aorta"],
        "phase_design_text": """
- Plain (whole aorta)
- CTA (whole aorta)
- Immediate delay (whole aorta)
""",
        "contrast_text": "IV contrast"
    },
    # Aortic Dissection
    "cta_aorta_dissect": {
        "protocol_name": protocols_id_name["cta_aorta_dissect"],
        "exam_name": exam_id_name["Body"]["cta_aorta"],
        "phase_design_text": """
- Plain (whole aorta)
- CTA (whole aorta)
- Immediate delay (whole aorta)
""",
        "contrast_text": "IV contrast"
    },
    # AAA Post-op
    "cta_aorta_aaa_postop": {
        "protocol_name": protocols_id_name["cta_aorta_aaa_postop"],
        "exam_name": exam_id_name["Body"]["cta_aorta"],
        "phase_design_text": """
- Plain (whole aorta)
- CTA (whole aorta)
- Immediate delay (whole aorta)
""",
        "contrast_text": "IV contrast"
    },
    # CTA Runoff
    "cta_runoff_old": {
        "protocol_name": protocols_id_name["cta_runoff_old"],
        "exam_name": exam_id_name["Body"]["cta_runoff"],
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
        "protocol_name": protocols_id_name["cta_runoff_young"],
        "exam_name": exam_id_name["Body"]["cta_runoff"],
        "phase_design_text": """
ขา → Aortic bifurcation to feet
แขน → mid-heart to hands
- CTA
- Immediate delay
""",
        "contrast_text": "IV contrast"
    },
    # Neuro
    # CT Brain
    ## CT Brain 
    "ct_brain_nc_routine": {
        "protocol_name": None,
        "exam_name": exam_id_name["Neuro"]["ct_brain_nc"],
        "phase_design_text": None,
        "contrast_text": "No IV contrast"
    },
    # CTA Brain
    ## Intracranial aneurysm
    "cta_brain_aneurysm": {
        "protocol_name": protocols_id_name["cta_brain_aneurysm"],
        "exam_name": "CTA Brain",
        "phase_design_text": """
- Plain, CTA, post-contrast (Brain)
""",
        "contrast_text": "IV contrast"
    },
    "ctv_brain_vst": {
        "protocol_name": protocols_id_name["ctv_brain_vst"],
        "exam_name": "CTV Brain",
        "phase_design_text": """
- Plain, CTV, post-contrast (Brain)
""",
        "contrast_text": "IV contrast"
    },
    "ct_brain_with_cm_routine": {
        "protocol_name": None,
        "exam_name": exam_id_name["Neuro"]["ct_brain_with_cm"],
        "phase_design_text": """
- Plain, post-contrast (Brain)
""",
        "contrast_text": "IV contrast"
    },
    # Trauma
    ## CTA Neck (trauma)
    "cta_neck_trauma": {
        "protocol_name": protocols_id_name["cta_neck_trauma"],
        "exam_name": "CTA Neck",
        "phase_design_text": """
- CTA (brain, neck) COW to arch
- Post-contrast (brain)
""",
        "contrast_text": "IV contrast"
    },
    ## CT facial bone (trauma)
    "ct_facial_trauma": {
        "protocol_name": protocols_id_name["ct_facial_trauma"],
        "exam_name": "CT Facial Bone (non-contrast)",
        "phase_design_text": """
- CT Facial Bones (plain) with 3D reformats
""",
        "contrast_text": "No IV contrast"
    },
    ## CT Orbit (trauma)
    "ct_orbit_trauma": {
        "protocol_name": protocols_id_name["ct_orbit_trauma"],
        "exam_name": "CT Orbit (non-contrast)",
        "phase_design_text": None,
        "contrast_text": "No IV contrast"
    },
    # CT Body Trauma
    ## Pan-Scan
    "pan_scan": {
        "protocol_name": None,
        "exam_name": protocols_id_name["pan_scan"],
        "phase_design_text": """
- Plain (Brain) [arms down]
- Arterial (COW → pubic symphysis) [arms up]
- Venous (Upper or Whole Abdomen)
- +/- delay kidney, ureter
- +/-  CT cystogram
""",
        "contrast_text": "IV contrast, No oral, No rectal"
    },
    ## CTA Blunt Abdomen (trauma)
    "cta_blunt_abd": {
        "protocol_name": protocols_id_name["cta_blunt_abd"],
        "exam_name": exam_id_name["Body"]["cta_wa"],
        "phase_design_text": """
- CTA (whole)
- Venous (whole)
- may be Delay (in injury site)
""",
        "contrast_text": "IV contrast, No oral, No rectal"
    },
    ## CTA Penetrating Abd (trauma)
    "cta_penetrate_abd": {
        "protocol_name": protocols_id_name["cta_penetrate_abd"],
        "exam_name": exam_id_name["Body"]["cta_wa"],
        "phase_design_text": """
- CTA (whole)
- Venous (whole)
- may be Delay (in injury site)
*** วาง marker ตําแหน่งแผลด้วย
""",
        "contrast_text": "IV contrast, Oral & Rectal full positive (ถ้ามีเวลา)"
    },
    ## CT Second look Abd (trauma)
    "ct_second_look_abd": {
        "protocol_name": protocols_id_name["ct_second_look_abd"],
        "exam_name": exam_id_name["Body"]["ct_wa"],
        "phase_design_text": """
- Venous (whole)
""",
        "contrast_text": "IV contrast, Oral (full positive), Rectal (positive)"
    },
    ## CT Second look Abd (trauma)
    "cta_chest_trauma": {
        "protocol_name": protocols_id_name["cta_chest_trauma"],
        "exam_name": exam_id_name["Body"]["cta_chest"],
        "phase_design_text": """
- CTA (Chest)
- Venous (Chest)
""",
        "contrast_text": "IV contrast, No Oral, No Rectal"
    },
    "mri_screening_whole_spine": {
        "protocol_name": None,
        "exam_name": protocols_id_name["mri_screening_whole_spine"],
        "phase_design_text": """
1. Sagittal T2FS ทำ 3 stacks แยก C-T-LS spine คนละ Series
2. Check ภาพ
  - ถ้าไม่มี cord compression เลิกเคสได้เลย
  - ถ้ามี ให้วาง Plane Axial ใน level ที่สงสัย cord compression 
3. Axial ทำ 3 sequences ได้แก่ T2W, T1W, GRE T2W

If ส่ง neuro -> **ไม่ฉีด Gd ทุกกรณี**; If ส่ง MSK -> consult fellow

Remark:
* ถ้าไม่มี cord compression จะไม่ทำ axial view 
* การวาง plane axial ให้ทำเฉพาะ level ที่สงสัย cord compression โดยวาง coverage ขึ้นข้างบน 2 levels และลงล่าง 2 levels (เช่น lesion T5 ให้วางตั้งแต่ T3-T7)
* ถ้าสงสัย spinal cord infarct ให้ add sag DWI/ADC ด้วย
""",
        "contrast_text": None
    },
    # "protocol_id": {
    #     "protocol_name": protocols_id_name["protocol_id"],
    #     "exam_name": exam_id_name["Neuro"]["xxx"],
    #     "phase_design_text": """""",
    #     "contrast_text": ""
    # },
}


# Reverse Mapping

# Level 2 (reversed)
## Map `exam_name` to `exam_id`
## exam_name_id = {v: k for k, v in exam_id_name.items()}
exam_name_id = {}

for key, value_dict in exam_id_name.items():
    value_dict_inv = {v: k for k, v in value_dict.items()}
    exam_name_id[key] = value_dict_inv

# Map `protocol_name` to `protocol_id`
protocols_name_id = {v: k for k, v in protocols_id_name.items()}

# Level 3 (reversed)
## Group `protocol_name` in each `exam_id`
exam_id_protocol_name = {}

# Loop through each key and list in dict1
for key, value_list in exam_id_protocol_id.items():
    # Map each value in the list to its corresponding value in dict2
    mapped_list = [protocols_id_name[value] for value in value_list]
    # Store the mapped list in the result dictionary
    exam_id_protocol_name[key] = mapped_list
