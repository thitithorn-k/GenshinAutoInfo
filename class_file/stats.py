class Stats:
    def __init__(self):
        self.ATK = 0
        self.ATK_p = 0
        self.CR = 0
        self.CD = 0
        self.EM = 0
        self.HP = 0
        self.HP_p = 0
        self.DEF = 0
        self.DEF_p = 0
        self.PDMG = 0
        self.EDMG = 0
        self.ANEMO_DMG = 0
        self.GEO_DMG = 0
        self.ELECTRO_DMG = 0
        self.HYDRO_DMG = 0
        self.PYRO_DMG = 0
        self.CRYO_DMG = 0
        self.HEAL = 0
        self.SHIELD = 0
        self.ER = 0

        self.mon_res_debuff = 0
        self.mon_def_debuff = 0
        self.reaction_dmg_bonus = 0
        self.max_hp_dmg_bonus = 0
        self.all_dmg_bonus = 0
        self.max_hp_atk_bonus = 0  #
        self.max_er_hydro_bonus = 0  # for Mona

        self.normal_attack_dmg_bonus = 0
        self.charge_attack_dmg_bonus = 0
        self.charge_attack_cr = 0  #
        self.plunging_attack_dmg_bonus = 0
        self.element_skill_dmg_bonus = 0
        self.element_skill_cr = 0  #
        self.element_burst_dmg_bonus = 0
        self.element_burst_cr = 0  #

        self.max_hp_auto_attack_dmg_bonus = 0
        self.max_hp_element_skill_dmg_bonus = 0
        self.max_hp_element_burst_dmg_bonus = 0

        self.overloaded_dmg_bonus = 0  #
        self.electro_charged_dmg_bonus = 0  #
        self.superconduct_dmg_bonus = 0  #
        self.swirl_dmg_bonus = 0  #
        self.vaporize_dmg_bonus = 0  #
        self.melt_dmg_bonus = 0  #
        self.burning_dmg_bonus = 0  #

        self.make_auto_to_element = 0

    def __add__(self, other):
        temp = Stats()
        temp.ATK = self.ATK + other.ATK
        temp.ATK_p = self.ATK_p + other.ATK_p
        temp.CR = self.CR + other.CR
        temp.CD = self.CD + other.CD
        temp.EM = self.EM + other.EM
        temp.HP = self.HP + other.HP
        temp.HP_p = self.HP_p + other.HP_p
        temp.DEF = self.DEF + other.DEF
        temp.DEF_p = self.DEF_p + other.DEF_p
        temp.PDMG = self.PDMG + other.PDMG
        temp.EDMG = self.EDMG + other.EDMG
        temp.ANEMO_DMG = self.ANEMO_DMG + other.ANEMO_DMG
        temp.GEO_DMG = self.GEO_DMG + other.GEO_DMG
        temp.ELECTRO_DMG = self.ELECTRO_DMG + other.ELECTRO_DMG
        temp.HYDRO_DMG = self.HYDRO_DMG + other.HYDRO_DMG
        temp.PYRO_DMG = self.PYRO_DMG + other.PYRO_DMG
        temp.CRYO_DMG = self.CRYO_DMG + other.CRYO_DMG
        temp.HEAL = self.HEAL + other.HEAL
        temp.SHIELD = self.SHIELD + other.SHIELD
        temp.ER = self.ER + other.ER

        temp.mon_res_debuff = self.mon_res_debuff + other.mon_res_debuff
        temp.mon_def_debuff = self.mon_def_debuff + other.mon_def_debuff
        temp.reaction_dmg_bonus = self.reaction_dmg_bonus + other.reaction_dmg_bonus
        temp.max_hp_dmg_bonus = self.max_hp_dmg_bonus + other.max_hp_dmg_bonus
        temp.all_dmg_bonus = self.all_dmg_bonus + other.all_dmg_bonus
        temp.max_hp_atk_bonus = self.max_hp_atk_bonus + other.max_hp_atk_bonus
        temp.max_er_hydro_bonus = self.max_er_hydro_bonus + other.max_er_hydro_bonus

        temp.normal_attack_dmg_bonus = self.normal_attack_dmg_bonus + other.normal_attack_dmg_bonus
        temp.charge_attack_dmg_bonus = self.charge_attack_dmg_bonus + other.charge_attack_dmg_bonus
        temp.charge_attack_cr = self.charge_attack_cr + other.charge_attack_cr
        temp.plunging_attack_dmg_bonus = self.plunging_attack_dmg_bonus + other.plunging_attack_dmg_bonus
        temp.element_skill_dmg_bonus = self.element_skill_dmg_bonus + other.element_skill_dmg_bonus
        temp.element_skill_cr = self.element_skill_cr + other.element_skill_cr
        temp.element_burst_dmg_bonus = self.element_burst_dmg_bonus + other.element_burst_dmg_bonus
        temp.element_burst_cr = self.element_burst_cr + other.element_burst_cr

        temp.max_hp_auto_attack_dmg_bonus = self.max_hp_auto_attack_dmg_bonus + other.max_hp_auto_attack_dmg_bonus
        temp.max_hp_element_skill_dmg_bonus = self.max_hp_element_skill_dmg_bonus + other.max_hp_element_skill_dmg_bonus
        temp.max_hp_element_burst_dmg_bonus = self.max_hp_element_burst_dmg_bonus + other.max_hp_element_burst_dmg_bonus

        temp.overloaded_dmg_bonus = self.overloaded_dmg_bonus + other.overloaded_dmg_bonus
        temp.electro_charged_dmg_bonus = self.electro_charged_dmg_bonus + other.electro_charged_dmg_bonus
        temp.superconduct_dmg_bonus = self.superconduct_dmg_bonus + other.superconduct_dmg_bonus
        temp.swirl_dmg_bonus = self.swirl_dmg_bonus + other.swirl_dmg_bonus
        temp.vaporize_dmg_bonus = self.vaporize_dmg_bonus + other.vaporize_dmg_bonus
        temp.melt_dmg_bonus = self.melt_dmg_bonus + other.melt_dmg_bonus
        temp.burning_dmg_bonus = self.burning_dmg_bonus + other.burning_dmg_bonus

        temp.make_auto_to_element = self.make_auto_to_element + other.make_auto_to_element
        return temp

    def __sub__(self, other):
        temp = Stats()
        temp.ATK = self.ATK - other.ATK
        temp.ATK_p = self.ATK_p - other.ATK_p
        temp.CR = self.CR - other.CR
        temp.CD = self.CD - other.CD
        temp.EM = self.EM - other.EM
        temp.HP = self.HP - other.HP
        temp.HP_p = self.HP_p - other.HP_p
        temp.DEF = self.DEF - other.DEF
        temp.DEF_p = self.DEF_p - other.DEF_p
        temp.PDMG = self.PDMG - other.PDMG
        temp.EDMG = self.EDMG - other.EDMG
        temp.ANEMO_DMG = self.ANEMO_DMG - other.ANEMO_DMG
        temp.GEO_DMG = self.GEO_DMG - other.GEO_DMG
        temp.ELECTRO_DMG = self.ELECTRO_DMG - other.ELECTRO_DMG
        temp.HYDRO_DMG = self.HYDRO_DMG - other.HYDRO_DMG
        temp.PYRO_DMG = self.PYRO_DMG - other.PYRO_DMG
        temp.CRYO_DMG = self.CRYO_DMG - other.CRYO_DMG
        temp.HEAL = self.HEAL - other.HEAL
        temp.SHIELD = self.SHIELD - other.SHIELD
        temp.ER = self.ER - other.ER

        temp.mon_res_debuff = self.mon_res_debuff - other.mon_res_debuff
        temp.mon_def_debuff = self.mon_def_debuff - other.mon_def_debuff
        temp.reaction_dmg_bonus = self.reaction_dmg_bonus - other.reaction_dmg_bonus
        temp.max_hp_dmg_bonus = self.max_hp_dmg_bonus - other.max_hp_dmg_bonus
        temp.all_dmg_bonus = self.all_dmg_bonus - other.all_dmg_bonus
        temp.max_hp_atk_bonus = self.max_hp_atk_bonus - other.max_hp_atk_bonus
        temp.max_er_hydro_bonus = self.max_er_hydro_bonus - other.max_er_hydro_bonus

        temp.normal_attack_dmg_bonus = self.normal_attack_dmg_bonus - other.normal_attack_dmg_bonus
        temp.charge_attack_dmg_bonus = self.charge_attack_dmg_bonus - other.charge_attack_dmg_bonus
        temp.charge_attack_cr = self.charge_attack_cr - other.charge_attack_cr
        temp.plunging_attack_dmg_bonus = self.plunging_attack_dmg_bonus - other.plunging_attack_dmg_bonus
        temp.element_skill_dmg_bonus = self.element_skill_dmg_bonus - other.element_skill_dmg_bonus
        temp.element_skill_cr = self.element_skill_cr - other.element_skill_cr
        temp.element_burst_dmg_bonus = self.element_burst_dmg_bonus - other.element_burst_dmg_bonus
        temp.element_burst_cr = self.element_burst_cr - other.element_burst_cr

        temp.max_hp_auto_attack_dmg_bonus = self.max_hp_auto_attack_dmg_bonus - other.max_hp_auto_attack_dmg_bonus
        temp.max_hp_element_skill_dmg_bonus = self.max_hp_element_skill_dmg_bonus - other.max_hp_element_skill_dmg_bonus
        temp.max_hp_element_burst_dmg_bonus = self.max_hp_element_burst_dmg_bonus - other.max_hp_element_burst_dmg_bonus

        temp.overloaded_dmg_bonus = self.overloaded_dmg_bonus - other.overloaded_dmg_bonus
        temp.electro_charged_dmg_bonus = self.electro_charged_dmg_bonus - other.electro_charged_dmg_bonus
        temp.superconduct_dmg_bonus = self.superconduct_dmg_bonus - other.superconduct_dmg_bonus
        temp.swirl_dmg_bonus = self.swirl_dmg_bonus - other.swirl_dmg_bonus
        temp.vaporize_dmg_bonus = self.vaporize_dmg_bonus - other.vaporize_dmg_bonus
        temp.melt_dmg_bonus = self.melt_dmg_bonus - other.melt_dmg_bonus
        temp.burning_dmg_bonus = self.burning_dmg_bonus - other.burning_dmg_bonus

        temp.make_auto_to_element = self.make_auto_to_element - other.make_auto_to_element
        return temp
