class Character:
    def __init__(self, name, HP, ATK, DEF, CR, CD, ATK_p, EM, HP_p, DEF_p,
                 HEAL, PDMG, EDMG, BSCONDUCT, BOVERLOAD, BELECTROCH, BSWIRL,
                 BSHATTER, BCRYSTALIZE, ER, WEAPON_TYPE, ELEMENTAL, lv):
        self.name = name
        self.HP = HP  # 0
        self.ATK = ATK  # 1
        self.DEF = DEF  # 2
        self.CR = CR  # 3
        self.CD = CD  # 4
        self.ATK_p = ATK_p  # 5
        self.EM = EM  # 6
        self.HP_p = HP_p  # 7
        self.DEF_p = DEF_p  # 8
        self.HEAL = HEAL  # 9
        self.PDMG = PDMG  # 10
        self.EDMG = EDMG  # 11
        self.BSCONDUCT = BSCONDUCT  # 12
        self.BOVERLOAD = BOVERLOAD  # 13
        self.BELECTROCH = BELECTROCH  # 14
        self.BSWIRL = BSWIRL  # 15
        self.BSHATTER = BSHATTER  # 16
        self.BCRYSTALIZE = BCRYSTALIZE  # 17
        self.ER = ER  # 18
        self.WEAPON_TYPE = WEAPON_TYPE  # 19
        self.ELEMENTAL = ELEMENTAL  # 20
        self.level = lv  # 21