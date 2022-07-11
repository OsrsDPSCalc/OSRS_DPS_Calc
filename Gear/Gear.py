class Equipment:
    def __init__(self, stab_bonus, slash_bonus, crush_bonus, magic_bonus, ranged_bonus, stab_def_bonus, slash_def_bonus, crush_def_bonus, magic_def_bonus, ranged_def_bonus, str_bonus, ranged_str_bonus, magic_dmg_bonus, prayer_bonus):
        self.stab_bonus = stab_bonus
        self.slash_bonus = slash_bonus
        self.crush_bonus = crush_bonus
        self.magic_bonus = magic_bonus
        self.ranged_bonus = ranged_bonus
        self.stab_def_bonus = stab_def_bonus
        self.slash_def_bonus = slash_def_bonus
        self.crush_def_bonus = crush_def_bonus
        self.magic_def_bonus = magic_def_bonus
        self.ranged_def_bonus = ranged_def_bonus
        self.str_bonus = str_bonus
        self.ranged_str_bonus = ranged_str_bonus
        self.magic_dmg_bonus = magic_dmg_bonus
        self.prayer_bonus = prayer_bonus


Bandos_chestplate = Equipment(0, 0, 0, -15, -10, 98, 93, 105, -6, 133, 4, 0, 0, 1)
Infernal_cape = Equipment(4, 4, 4, 1, 1, 12, 12, 12, 12, 12, 8, 0, 0, 2)
Torva_full_helm = Equipment(0, 0, 0, -5, -5, 59, 60, 62, -2, 57, 8, 0, 0, 1)

