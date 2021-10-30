class ArtifactStat:
    def __init__(self):
        self.ATK = []
        self.ATK_p = []
        self.CR = []
        self.CD = []
        self.EM = []
        self.HP = []
        self.HP_p = []
        self.DEF = []
        self.DEF_p = []
        self.PDMG = []
        self.ANEMO_DMG = []
        self.GEO_DMG = []
        self.ELECTRO_DMG = []
        self.HYDRO_DMG = []
        self.PYRO_DMG = []
        self.CRYO_DMG = []
        self.HEAL = []
        self.SHIELD = []
        self.ER = []

    def print_log(self):
        print(f'ATK={self.ATK}\n'
              f'ATK_p={self.ATK_p}\n'
              f'CR={self.CR}\n'
              f'CD={self.CD}\n'
              f'EM={self.EM}\n'
              f'HP={self.HP}\n'
              f'HP_p={self.HP_p}\n'
              f'DEF={self.DEF}\n'
              f'DEF_p={self.DEF_p}\n'
              f'PDMG_p={self.PDMG}\n'
              f'ANEMO_DMG={self.ANEMO_DMG}\n'
              f'GEO_DMG={self.GEO_DMG}\n'
              f'ELECTRO_DMG={self.ELECTRO_DMG}\n'
              f'HYDRO_DMG={self.HYDRPO_DMG}\n'
              f'PYRO_DMG={self.PYRO_DMG}\n'
              f'CRYO_DMG={self.CRYO_DMG}\n'
              f'HEAL={self.HEAL}\n'
              f'SHIELD={self.SHIELD}\n'
              f'ER={self.ER}')