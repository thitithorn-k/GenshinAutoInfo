import condition_option
from class_file.stats import Stats
from class_file.character import Character
from class_file.weapon import Weapon
from class_file.stats import Stats


def update_stat(character, weapon, artifacts, stats):
    condition_option.reset_all_option()

    stats = Stats()
    stats = process_weapon(weapon, character, stats)
    stats = process_artifact(artifacts, character, stats)
    return stats


def process_weapon(weapon, character, stats):
    weapon_type = character.WEAPON_TYPE
    weapon_name = weapon.name
    temp_stats = Stats()
    if weapon_type == 'Sword':
        if weapon_name == 'Cool Steel':
            temp_stats.all_dmg_bonus += 0.12
            condition = 'Increases DMG against opponents affected by Hydro or Cryo by 12%.'
            condition_option.add_option(weapon_name, condition, temp_stats)
        elif weapon_name == 'Dark Iron Sword':
            temp_stats.ATK_p += 0.2
            condition = 'Upon causing an Overloaded, Superconduct, Electro-Charged, or an Electro-infused Swirl reaction, ATK is increased by 20% for 12s.'
            condition_option.add_option(weapon_name, condition, temp_stats)
        elif weapon_name == 'Harbinger of Dawn':
            temp_stats.CR += 0.14
            condition = 'When HP is above 90%, increases CRIT Rate by 14%.'
            condition_option.add_option(weapon_name, condition, temp_stats)
        elif weapon_name == 'Blackcliff Longsword':
            temp_stats = [Stats(), Stats(), Stats()]
            temp_stats[0].ATK_p += 0.12
            temp_stats[1].ATK_p += 0.24
            temp_stats[2].ATK_p += 0.36
            condition = 'After defeating an opponent, ATK is increased by 12% for 30s. Max 3 stacks.'
            condition_option.add_option(weapon_name, condition, temp_stats)
        elif weapon_name == 'Iron Sting':
            temp_stats = [Stats(), Stats()]
            temp_stats[0].all_dmg_bonus += 0.06
            temp_stats[1].all_dmg_bonus += 0.12
            condition = 'Dealing Elemental DMG increases all DMG by 6% for 6s. Max 2 stacks.'
            condition_option.add_option(weapon_name, condition, temp_stats)
        elif weapon_name == 'Lion\'s Roar':
            temp_stats.all_dmg_bonus += 0.2
            condition = 'Increases DMG against opponents affected by Pyro or Electro by 20%.'
            condition_option.add_option(weapon_name, condition, temp_stats)
        elif weapon_name == 'Prototype Rancour':
            temp_stats = [Stats(), Stats(), Stats(), Stats()]
            temp_stats[0].normal_attack_dmg_bonus += 0.04
            temp_stats[0].charge_attack_dmg_bonus += 0.04
            temp_stats[0].DEF_p += 0.04
            temp_stats[1].normal_attack_dmg_bonus += 0.08
            temp_stats[1].charge_attack_dmg_bonus += 0.08
            temp_stats[1].DEF_p += 0.088
            temp_stats[2].normal_attack_dmg_bonus += 0.12
            temp_stats[2].charge_attack_dmg_bonus += 0.12
            temp_stats[2].DEF_p += 0.12
            temp_stats[3].normal_attack_dmg_bonus += 0.16
            temp_stats[3].charge_attack_dmg_bonus += 0.16
            temp_stats[3].DEF_p += 0.16
            condition = 'On hit, Normal or Charged Attacks increase ATK and DEF by 4% for 6s. Max 4 stacks.'
            condition_option.add_option(weapon_name, condition, temp_stats)
        elif weapon_name == 'Royal Longsword':
            temp_stats = [Stats(), Stats(), Stats(), Stats(), Stats()]
            temp_stats[0].CR += 0.08
            temp_stats[1].CR += 0.16
            temp_stats[2].CR += 0.24
            temp_stats[3].CR += 0.32
            temp_stats[4].CR += 0.40
            condition = 'Upon damaging an opponent, increases CRIT Rate by 8%. Max 5 stacks.'
            condition_option.add_option(weapon_name, condition, temp_stats)
        elif weapon_name == 'The Alley Flash':
            stats.all_dmg_bonus += 0.12
        elif weapon_name == 'The Black Sword':
            stats.normal_attack_dmg_bonus += 0.2
            stats.charge_attack_dmg_bonus += 0.2
        elif weapon_name == 'Festering Desire':
            stats.element_skill_dmg_bonus += 0.16
            stats.element_skill_cr += 0.06
        elif weapon_name == 'Aquila Favonia':
            stats.ATK_p += 0.2
        elif weapon_name == 'Skyward Blade':
            stats.CR += 0.04
        elif weapon_name == 'Summit Shaper':
            stats.SHIELD += 0.2
            temp_stats = [Stats(), Stats(), Stats(), Stats(), Stats()]
            temp_stats[0].ATK_p += 0.04
            temp_stats[1].ATK_p += 0.08
            temp_stats[2].ATK_p += 0.12
            temp_stats[3].ATK_p += 0.16
            temp_stats[4].ATK_p += 0.2
            condition = 'While not protected by a shield, Scoring hits on opponents increases ATK by 4% for 8s. Max 5 stacks.'
            condition_option.add_option(weapon_name, condition, temp_stats)

            temp_stats = [Stats(), Stats(), Stats(), Stats(), Stats()]
            temp_stats[0].ATK_p += 0.08
            temp_stats[1].ATK_p += 0.16
            temp_stats[2].ATK_p += 0.24
            temp_stats[3].ATK_p += 0.32
            temp_stats[4].ATK_p += 0.4
            condition = 'While protected by a shield, Scoring hits on opponents increases ATK by 8% for 8s. Max 5 stacks.'
            condition_option.add_option(weapon_name, condition, temp_stats)
        elif weapon_name == 'Primordial Jade Cutter':
            stats.HP += 0.2
            stats.max_hp_atk_bonus += 0.012
        elif weapon_name == 'Freedom-Sworn':
            stats.all_dmg_bonus += 0.1
            temp_stats.normal_attack_dmg_bonus += 0.16
            temp_stats.charge_attack_dmg_bonus += 0.16
            temp_stats.plunging_attack_dmg_bonus += 0.16
            temp_stats.ATK_p += 0.2
            condition = '"Millennial Movement: Song of Resistance" increases Normal, Charged and Plunging Attack DMG by 16% and increases ATK by 20%.'
            condition_option.add_option(weapon_name, condition, temp_stats)
        elif weapon_name == 'Mistsplitter Reforged':
            stats.EDMG += 0.12
            temp_stats = [Stats(), Stats(), Stats()]
            if character.ELEMENTAL == 'Anemo':
                temp_stats[0].ANEMO_DMG += 0.08
                temp_stats[1].ANEMO_DMG += 0.16
                temp_stats[2].ANEMO_DMG += 0.28
            elif character.ELEMENTAL == 'Geo':
                temp_stats[0].GEO_DMG += 0.08
                temp_stats[1].GEO_DMG += 0.16
                temp_stats[2].GEO_DMG += 0.28
            elif character.ELEMENTAL == 'Electro':
                temp_stats[0].ELECTRO_DMG += 0.08
                temp_stats[1].ELECTRO_DMG += 0.16
                temp_stats[2].ELECTRO_DMG += 0.28
            elif character.ELEMENTAL == 'Hydro':
                temp_stats[0].HYDRO_DMG += 0.08
                temp_stats[1].HYDRO_DMG += 0.16
                temp_stats[2].HYDRO_DMG += 0.28
            elif character.ELEMENTAL == 'Pyro':
                temp_stats[0].PYRO_DMG += 0.08
                temp_stats[1].PYRO_DMG += 0.16
                temp_stats[2].PYRO_DMG += 0.28
            elif character.ELEMENTAL == 'Cryo':
                temp_stats[0].CRYO_DMG += 0.08
                temp_stats[1].CRYO_DMG += 0.16
                temp_stats[2].CRYO_DMG += 0.28
            condition = 'At stack levels 1/2/3, the Mistsplitter\'s Emblem provides a 8/16/28% Elemental DMG Bonus for the character\'s Elemental Type.'
            condition_option.add_option(weapon_name, condition, temp_stats)
    elif weapon_type == 'Claymore':
        if weapon_name == 'Bloodtainted Greatsword':
            temp_stats.all_dmg_bonus += 0.12
            condition = 'Increases DMG dealt against opponents affected by Pyro or Electro by 12%.'
            condition_option.add_option(weapon_name, condition, temp_stats)
        elif weapon_name == 'Debate Club':
            # TODO deal additional DMG equal to 60% of ATK
            pass
        elif weapon_name == 'Ferrous Shadow':
            temp_stats.charge_attack_dmg_bonus += 0.3
            condition = 'When HP falls below 70%, increases Charged Attack DMG by 30%'
            condition_option.add_option(weapon_name, condition, temp_stats)
        elif weapon_name == 'Skyrider Greatsword':
            temp_stats = [Stats(), Stats(), Stats(), Stats()]
            temp_stats[0].ATK_p += 0.06
            temp_stats[1].ATK_p += 0.12
            temp_stats[2].ATK_p += 0.18
            temp_stats[3].ATK_p += 0.24
            condition = 'On hit, Normal or Charged Attacks increase ATK by 6% for 6s. Max 4 stacks.'
            condition_option.add_option(weapon_name, condition, temp_stats)
        elif weapon_name == 'Blackcliff Slasher':
            temp_stats = [Stats(), Stats(), Stats()]
            temp_stats[0].ATK_p += 0.12
            temp_stats[1].ATK_p += 0.24
            temp_stats[2].ATK_p += 0.36
            condition = 'After defeating an opponent, ATK is increased by 12% for 30s. Max 3 stacks'
            condition_option.add_option(weapon_name, condition, temp_stats)
        elif weapon_name == 'Lithic Blade':
            temp_stats = [Stats(), Stats(), Stats(), Stats()]
            temp_stats[0].ATK_p += 0.07
            temp_stats[0].CR += 0.03
            temp_stats[1].ATK_p += 0.14
            temp_stats[1].CR += 0.06
            temp_stats[2].ATK_p += 0.21
            temp_stats[2].CR += 0.09
            temp_stats[3].ATK_p += 0.28
            temp_stats[3].CR += 0.12
            condition = 'For every character in the party who hails from Liyue, the character who equips this weapon gains a 7% ATK increase and a 3% CRIT Rate increase. Max 4 stacks.'
            condition_option.add_option(weapon_name, condition, temp_stats)
        elif weapon_name == 'Rainslasher':
            temp_stats.all_dmg_bonus += 0.2
            condition = 'Increases DMG against opponents affected by Hydro or Electro by 20%.'
            condition_option.add_option(weapon_name, condition, temp_stats)
        elif weapon_name == 'Royal Greatsword':
            temp_stats = [Stats(), Stats(), Stats(), Stats(), Stats()]
            temp_stats[0].CR += 0.08
            temp_stats[1].CR += 0.16
            temp_stats[2].CR += 0.24
            temp_stats[3].CR += 0.32
            temp_stats[4].CR += 0.40
            condition = 'Upon damaging an opponent, increases CRIT Rate by 8%. Max 5 stacks.'
            condition_option.add_option(weapon_name, condition, temp_stats)
        elif weapon_name == 'Serpent Spine':
            temp_stats = [Stats(), Stats(), Stats(), Stats(), Stats()]
            temp_stats[0].all_dmg_bonus += 0.06
            temp_stats[1].all_dmg_bonus += 0.12
            temp_stats[2].all_dmg_bonus += 0.18
            temp_stats[3].all_dmg_bonus += 0.24
            temp_stats[4].all_dmg_bonus += 0.3
            condition = 'Every 4s a character is on the field, they will deal 6% more DMG and take 3% more DMG. Max 5 stacks'
            condition_option.add_option(weapon_name, condition, temp_stats)
        elif weapon_name == 'The Bell':
            temp_stats.all_dmg_bonus += 0.12
            condition = 'While protected by a shield, the character gains 12% increased DMG.'
            condition_option.add_option(weapon_name, condition, temp_stats)
        elif weapon_name == 'Whiteblind':
            temp_stats = [Stats(), Stats(), Stats(), Stats()]
            temp_stats[0].ATK_p += 0.06
            temp_stats[0].DEF_p += 0.06
            temp_stats[1].ATK_p += 0.12
            temp_stats[1].DEF_p += 0.12
            temp_stats[2].ATK_p += 0.18
            temp_stats[2].DEF_p += 0.18
            temp_stats[3].ATK_p += 0.24
            temp_stats[3].DEF_p += 0.24
            condition = 'On hit, Normal or Charged Attacks increase ATK and DEF by 6% for 6s. Max 4 stacks.'
            condition_option.add_option(weapon_name, condition, temp_stats)
        elif weapon_name == 'Katsuragikiri Nagamasa':
            stats.element_skill_dmg_bonus += 0.06
        elif weapon_name == 'Luxurious Sea-Lord':
            stats.element_burst_dmg_bonus += 0.12
        elif weapon_name == 'Skyward Pride':
            stats.all_dmg_bonus += 0.08
        elif weapon_name == 'Wolf\'s Gravestone':
            stats.ATK_p += 0.2
            temp_stats.ATK_p += 0.4
            condition = 'On hit, attacks against opponents with less than 30% HP increase all party members\' ATK by 40% for 12s.'
            condition_option.add_option(weapon_name, condition, temp_stats)
        elif weapon_name == 'The Unforged':
            stats.SHIELD += 0.2
            temp_stats = [Stats(), Stats(), Stats(), Stats(), Stats()]
            temp_stats[0].ATK_p += 0.04
            temp_stats[1].ATK_p += 0.08
            temp_stats[2].ATK_p += 0.12
            temp_stats[3].ATK_p += 0.16
            temp_stats[4].ATK_p += 0.2
            condition = 'While not protected by a shield, Scoring hits on opponents increases ATK by 4% for 8s. Max 5 stacks.'
            condition_option.add_option(weapon_name, condition, temp_stats)

            temp_stats = [Stats(), Stats(), Stats(), Stats(), Stats()]
            temp_stats[0].ATK_p += 0.08
            temp_stats[1].ATK_p += 0.16
            temp_stats[2].ATK_p += 0.24
            temp_stats[3].ATK_p += 0.32
            temp_stats[4].ATK_p += 0.4
            condition = 'While protected by a shield, Scoring hits on opponents increases ATK by 8% for 8s. Max 5 stacks.'
            condition_option.add_option(weapon_name, condition, temp_stats)
        elif weapon_name == 'Song of Broken Pines':
            stats.ATK_p += 0.16
            temp_stats.ATK_p += 0.2
            condition = '"Millennial Movement: Banner-Hymn" increases Normal ATK SPD by 12% and increases ATK by 20%.'
            condition_option.add_option(weapon_name, condition, temp_stats)
    elif weapon_type == 'Polearm':
        if weapon_name == 'Black Tassel':
            temp_stats.all_dmg_bonus += 0.4
            condition = 'Increases DMG against slimes by 40%.'
            condition_option.add_option(weapon_name, condition, temp_stats)
        elif weapon_name == 'White Tassel':
            stats.normal_attack_dmg_bonus += 0.24
        elif weapon_name == 'Blackcliff Pole':
            temp_stats = [Stats(), Stats(), Stats()]
            temp_stats[0].ATK_p += 0.12
            temp_stats[1].ATK_p += 0.24
            temp_stats[2].ATK_p += 0.36
            condition = 'After defeating an enemy, ATK is increased by 12% for 30s. Max 3 stacks.'
            condition_option.add_option(weapon_name, condition, temp_stats)
        elif weapon_name == 'Crescent Pike':
            # Normal and Charged Attacks deal additional DMG equal to 20% of ATK
            pass
        elif weapon_name == 'Deathmatch':
            temp_stats.ATK_p += 0.16
            temp_stats.DEF_p += 0.16
            condition = 'If there are at least 2 opponents nearby, ATK is increased by 16% and DEF is increased by 16%.'
            condition_option.add_option(weapon_name, condition, temp_stats)

            temp_stats = Stats()
            temp_stats.ATK_p += 0.24
            condition = 'If there are fewer than 2 opponents nearby, ATK is increased by 24%.'
            condition_option.add_option(weapon_name, condition, temp_stats)
        elif weapon_name == 'Dragon\'s Bane':
            temp_stats.all_dmg_bonus += 0.2
            condition = 'Increases DMG against opponents affected by Hydro or Pyro by 20%.'
            condition_option.add_option(weapon_name, condition, temp_stats)
        elif weapon_name == 'Lithic Spear':
            temp_stats = [Stats(), Stats(), Stats(), Stats()]
            temp_stats[0].ATK_p += 0.07
            temp_stats[0].CR += 0.03
            temp_stats[1].ATK_p += 0.07
            temp_stats[1].CR += 0.03
            temp_stats[2].ATK_p += 0.07
            temp_stats[2].CR += 0.03
            temp_stats[3].ATK_p += 0.07
            temp_stats[3].CR += 0.03
            condition = 'For every character in the party who hails from Liyue, the character who equips this weapon gains a 7% ATK increase and a 3% CRIT Rate increase. Max 4 stacks.'
            condition_option.add_option(weapon_name, condition, temp_stats)
        elif weapon_name == 'Prototype Starglitter':
            temp_stats = [Stats(), Stats()]
            temp_stats[0].normal_attack_dmg_bonus += 0.08
            temp_stats[0].charge_attack_dmg_bonus += 0.08
            temp_stats[1].normal_attack_dmg_bonus += 0.16
            temp_stats[1].charge_attack_dmg_bonus += 0.16
            condition = 'After using an Elemental Skill, increases Normal and Charged Attack DMG by 8% for 12s. Max 2 stacks.'
            condition_option.add_option(weapon_name, condition, temp_stats)
        elif weapon_name == 'Royal Spear':
            temp_stats = [Stats(), Stats(), Stats(), Stats(), Stats()]
            temp_stats[0].CR += 0.08
            temp_stats[1].CR += 0.16
            temp_stats[2].CR += 0.24
            temp_stats[3].CR += 0.32
            temp_stats[4].CR += 0.4
            condition = 'Upon damaging an opponent, increases CRIT Rate by 8%. Max 5 stacks.'
            condition_option.add_option(weapon_name, condition, temp_stats)
        elif weapon_name == 'Kitain Cross Spear':
            stats.element_skill_dmg_bonus += 0.06
        elif weapon_name == 'Vortex Vanquisher':
            stats.SHIELD += 0.2
            temp_stats = [Stats(), Stats(), Stats(), Stats(), Stats()]
            temp_stats[0].ATK_p += 0.04
            temp_stats[1].ATK_p += 0.08
            temp_stats[2].ATK_p += 0.12
            temp_stats[3].ATK_p += 0.16
            temp_stats[4].ATK_p += 0.2
            condition = 'While not protected by a shield, Scoring hits on opponents increases ATK by 4% for 8s. Max 5 stacks.'
            condition_option.add_option(weapon_name, condition, temp_stats)

            temp_stats = [Stats(), Stats(), Stats(), Stats(), Stats()]
            temp_stats[0].ATK_p += 0.08
            temp_stats[1].ATK_p += 0.16
            temp_stats[2].ATK_p += 0.24
            temp_stats[3].ATK_p += 0.32
            temp_stats[4].ATK_p += 0.4
            condition = 'While protected by a shield, Scoring hits on opponents increases ATK by 8% for 8s. Max 5 stacks.'
            condition_option.add_option(weapon_name, condition, temp_stats)
        elif weapon_name == 'Primordial Jade Winged-Spear':
            temp_stats = [Stats(), Stats(), Stats(), Stats(), Stats(), Stats(), Stats()]
            temp_stats[0].ATK_p += 0.032
            temp_stats[1].ATK_p += 0.064
            temp_stats[2].ATK_p += 0.096
            temp_stats[3].ATK_p += 0.128
            temp_stats[4].ATK_p += 0.160
            temp_stats[5].ATK_p += 0.192
            temp_stats[6].ATK_p += 0.224
            temp_stats[6].all_dmg_bonus += 0.12
            condition = 'On hit, increases ATK by 3.2% for 6s. Max 7 stacks. While in possession of the maximum possible stacks, DMG dealt is increased by 12%.'
            condition_option.add_option(weapon_name, condition, temp_stats)
        elif weapon_name == 'Skyward Spine':
            stats.CR += 0.08
        elif weapon_name == 'Staff of Homa':
            stats.HP_p += 0.2
            stats.max_hp_atk_bonus += 0.008
            # condition = 'Provides an ATK Bonus based on 0.8% of the wielder\'s Max HP.'
            # condition_option.add_option(weapon_name, condition, temp_stats)

            temp_stats.max_hp_atk_bonus += 0.01
            condition = 'When the wielder\'s HP is less than 50%, this ATK Bonus is increased by an additional 1% of Max HP.'
            condition_option.add_option(weapon_name, condition, temp_stats)
        elif weapon_name == 'The Catch':
            stats.element_burst_dmg_bonus += 0.16
            stats.element_burst_cr += 0.06
        elif weapon_name == 'Engulfing Lightning':
            # TODO make 'Engulfing Lightning' works
            condition = 'Under develop'
            condition_option.add_option(weapon_name, condition, temp_stats)
    elif weapon_type == 'Bow':
        if weapon_name == 'Raven Bow':
            temp_stats.all_dmg_bonus += 0.12
            condition = 'Increases DMG against opponents affected by Hydro or Pyro by 12%.'
            condition_option.add_option(weapon_name, condition, temp_stats)
        elif weapon_name == 'Sharpshooter\'s Oath':
            temp_stats.all_dmg_bonus += 0.24
            condition = 'Increases DMG against weak spots by 24%.'
            condition_option.add_option(weapon_name, condition, temp_stats)
        elif weapon_name == 'Slingshot':
            temp_stats.all_dmg_bonus += 0.36
            condition = 'If a Normal or Charged Attack hits a target within 0.3s of being fired, increases DMG by 36%.'
            condition_option.add_option(weapon_name, condition, temp_stats)

            temp_stats = Stats()
            temp_stats.all_dmg_bonus -= 0.1
            condition = 'If a Normal or Charged Attack hits a target after 0.3s of being fired, decreases DMG by 10%.'
            condition_option.add_option(weapon_name, condition, temp_stats)
        elif weapon_name == 'The Stringless':
            stats.element_skill_dmg_bonus += 0.24
            stats.element_burst_dmg_bonus += 0.24
        elif weapon_name == 'Alley Hunter':
            temp_stats = [Stats(), Stats(), Stats(), Stats(), Stats(),
                          Stats(), Stats(), Stats(), Stats(), Stats()]
            temp_stats[0].all_dmg_bonus += 0.02
            temp_stats[1].all_dmg_bonus += 0.04
            temp_stats[2].all_dmg_bonus += 0.06
            temp_stats[3].all_dmg_bonus += 0.08
            temp_stats[4].all_dmg_bonus += 0.10
            temp_stats[5].all_dmg_bonus += 0.12
            temp_stats[6].all_dmg_bonus += 0.14
            temp_stats[7].all_dmg_bonus += 0.16
            temp_stats[8].all_dmg_bonus += 0.18
            temp_stats[9].all_dmg_bonus += 0.20
            condition = 'While the character equipped with this weapon is in the party but not on the field, their DMG increases by 2% every second up to a max of 20%.'
            condition_option.add_option(weapon_name, condition, temp_stats)
        elif weapon_name == 'Blackcliff Warbow':
            temp_stats = [Stats(), Stats(), Stats()]
            temp_stats[0].ATK_p += 0.12
            temp_stats[1].ATK_p += 0.24
            temp_stats[2].ATK_p += 0.36
            condition = 'After defeating an enemy, ATK is increased by 12% for 30s. Max of 3 stacks.'
            condition_option.add_option(weapon_name, condition, temp_stats)
        elif weapon_name == 'Compound Bow':
            temp_stats = [Stats(), Stats(), Stats(), Stats()]
            temp_stats[0].ATK_p += 0.04
            temp_stats[1].ATK_p += 0.08
            temp_stats[2].ATK_p += 0.12
            temp_stats[3].ATK_p += 0.16
            condition = 'Normal Attack and Charged Attack hits increase ATK by 4% for 6s. Max 4 stacks.'
            condition_option.add_option(weapon_name, condition, temp_stats)
        elif weapon_name == 'Prototype Crescent':
            temp_stats.ATK_p = 0.36
            condition = 'Charged Attack hits on weak points increase Movement SPD by 10% and ATK by 36% for 10s.'
            condition_option.add_option(weapon_name, condition, temp_stats)
        elif weapon_name == 'Royal Bow':
            temp_stats = [Stats(), Stats(), Stats(), Stats(), Stats()]
            temp_stats[0].CR += 0.08
            temp_stats[1].CR += 0.08
            temp_stats[2].CR += 0.08
            temp_stats[3].CR += 0.08
            temp_stats[4].CR += 0.08
            condition = 'Upon damaging an opponent, increases CRIT Rate by 8%. Max 5 stacks.'
            condition_option.add_option(weapon_name, condition, temp_stats)
        elif weapon_name == 'Rust':
            stats.normal_attack_dmg_bonus += 0.4
            stats.charge_attack_dmg_bonus -= 0.1
        elif weapon_name == 'Windblume Ode':
            temp_stats.ATK_p += 0.16
            condition = 'After using an Elemental Skill, receive a boon from the ancient wish of the Windblume, increasing ATK by 16% for 6s.'
            condition_option.add_option(weapon_name, condition, temp_stats)
        elif weapon_name == 'Mitternachts Waltz':
            temp_stats.element_skill_dmg_bonus += 0.2
            condition = 'Normal Attack hits on opponents increase Elemental Skill DMG by 20% for 5s.'
            condition_option.add_option(weapon_name, condition, temp_stats)

            temp_stats = Stats()
            temp_stats.normal_attack_dmg_bonus += 0.2
            condition = 'Elemental Skill hits on opponents increase Normal Attack DMG by 20% for 5s.'
            condition_option.add_option(weapon_name, condition, temp_stats)
        elif weapon_name == 'Hamayumi':
            stats.normal_attack_dmg_bonus += 0.16
            stats.charge_attack_dmg_bonus += 0.12
            temp_stats.normal_attack_dmg_bonus += 0.16
            temp_stats.charge_attack_dmg_bonus += 0.12
            condition = 'When the equipping character\'s Energy reaches 100%, this effect is increased by 100%.'
            condition_option.add_option(weapon_name, condition, temp_stats)
        elif weapon_name == 'Skyward Harp':
            stats.CD += 0.2
        elif weapon_name == 'Amos\' Bow':
            stats.normal_attack_dmg_bonus += 0.12
            stats.charge_attack_dmg_bonus += 0.12
            temp_stats = [Stats(), Stats(), Stats(), Stats(), Stats()]
            temp_stats[0].all_dmg_bonus += 0.08
            temp_stats[1].all_dmg_bonus += 0.16
            temp_stats[2].all_dmg_bonus += 0.24
            temp_stats[3].all_dmg_bonus += 0.32
            temp_stats[4].all_dmg_bonus += 0.4
            condition = 'After a Normal or Charged Attack is fired, DMG dealt increases by a further 8% every 0.1s the arrow is in the air for up to 5 times.'
            condition_option.add_option(weapon_name, condition, temp_stats)
        elif weapon_name == 'Elegy for the End':
            stats.EM += 60
            temp_stats.EM += 100
            temp_stats.ATK_p += 0.2
            condition = '"Millennial Movement: Farewell Song" increases Elemental Mastery by 100 and increases ATK by 20%.'
            condition_option.add_option(weapon_name, condition, temp_stats)
        elif weapon_name == 'Thundering Pulse':
            stats.ATK_p += 0.2
            temp_stats = [Stats(), Stats(), Stats()]
            temp_stats[0].normal_attack_dmg_bonus += 0.12
            temp_stats[1].normal_attack_dmg_bonus += 0.24
            temp_stats[2].normal_attack_dmg_bonus += 0.4
            condition = 'At stack levels 1/2/3, the Thunder Emblem increases Normal Attack DMG by 12/24/40%.'
            condition_option.add_option(weapon_name, condition, temp_stats)
        elif weapon_name == 'Polar Star':
            stats.element_skill_dmg_bonus += 0.12
            stats.element_burst_dmg_bonus += 0.12
            temp_stats = [Stats(), Stats(), Stats(), Stats()]
            temp_stats[0].ATK_p += 0.1
            temp_stats[1].ATK_p += 0.2
            temp_stats[2].ATK_p += 0.3
            temp_stats[3].ATK_p += 0.48
            condition = 'When 1/2/3/4 stacks of Ashen Nightstar are present, ATK is increased by 10/20/30/48%.'
            condition_option.add_option(weapon_name, condition, temp_stats)
    elif weapon_type == 'Catalyst':
        if weapon_name == 'Emerald Orb':
            temp_stats.ATK_p += 0.2
            condition = 'Upon causing a Vaporize, Electro-Charged, Frozen, or a Hydro-infused Swirl reaction, increases ATK by 20% for 12s.'
            condition_option.add_option(weapon_name, condition, temp_stats)
        elif weapon_name == 'Magic Guide':
            temp_stats.all_dmg_bonus += 0.12
            condition = 'Increases DMG against opponents affected by Hydro or Electro by 12%.'
            condition_option.add_option(weapon_name, condition, temp_stats)
        elif weapon_name == 'Twin Nephrite':
            temp_stats.ATK_p += 0.12
            condition = 'Defeating an opponent increases Movement SPD and ATK by 12% for 15s.'
            condition_option.add_option(weapon_name, condition, temp_stats)
        elif weapon_name == 'Blackcliff Agate':
            temp_stats = [Stats(), Stats(), Stats()]
            temp_stats[0].ATK_p += 0.12
            temp_stats[1].ATK_p += 0.24
            temp_stats[2].ATK_p += 0.36
            condition = 'After defeating an enemy, ATK is increased by 12% for 30s. Max 3 stacks.'
            condition_option.add_option(weapon_name, condition, temp_stats)
        elif weapon_name == 'Mappa Mare':
            temp_stats = [Stats(), Stats()]
            temp_stats[0].EM += 0.08
            temp_stats[1].EM += 0.16
            condition = 'Triggering an Elemental reaction grants a 8% Elemental DMG Bonus for 10s. Max 2 stacks.'
            condition_option.add_option(weapon_name, condition, temp_stats)
        elif weapon_name == 'Royal Grimoire':
            temp_stats = [Stats(), Stats(), Stats(), Stats(), Stats()]
            temp_stats[0].CR += 0.08
            temp_stats[1].CR += 0.16
            temp_stats[2].CR += 0.24
            temp_stats[3].CR += 0.32
            temp_stats[4].CR += 0.4
            condition = 'Upon damaging an opponent, increases CRIT Rate by 8%. Max 5 stacks.'
            condition_option.add_option(weapon_name, condition, temp_stats)
        elif weapon_name == 'Solar Pearl':
            temp_stats.element_skill_dmg_bonus += 0.2
            temp_stats.element_burst_dmg_bonus += 0.2
            condition = 'Normal Attack hits increase Elemental Skill and Elemental Burst DMG by 20% for 6s.'
            condition_option.add_option(weapon_name, condition, temp_stats)

            temp_stats = Stats()
            temp_stats.normal_attack_dmg_bonus += 0.2
            condition = 'Elemental Skill or Elemental Burst hits increase Normal Attack DMG by 20% for 6s.'
            condition_option.add_option(weapon_name, condition, temp_stats)
        elif weapon_name == 'The Widsith':
            temp_stats.ATK_p += 0.6
            condition = 'Recitative: ATK is increased by 60%.'
            condition_option.add_option(weapon_name, condition, temp_stats)

            temp_stats = Stats()
            temp_stats.EDMG += 0.48
            condition = 'Aria: Increases all Elemental DMG by 48%.'
            condition_option.add_option(weapon_name, condition, temp_stats)

            temp_stats = Stats()
            temp_stats.EM += 240
            condition = 'Interlude: Elemental Mastery is increased by 240.'
            condition_option.add_option(weapon_name, condition, temp_stats)
        elif weapon_name == 'Wine and Song':
            temp_stats.ATK_p += 0.2
            condition = 'Using a Sprint or Alternate Sprint ability increases ATK by 20% for 5s.'
            condition_option.add_option(weapon_name, condition, temp_stats)
        elif weapon_name == 'Dodoco Tales':
            temp_stats.charge_attack_dmg_bonus += 0.16
            condition = 'Normal Attack hits on opponents increase Charged Attack DMG by 16% for 6s.'
            condition_option.add_option(weapon_name, condition, temp_stats)

            temp_stats = Stats()
            temp_stats.ATK_p += 0.08
            condition = 'Charged Attack hits on opponents increase ATK by 8% for 6s.'
            condition_option.add_option(weapon_name, condition, temp_stats)
        elif weapon_name == 'Lost Prayer to the Sacred Winds':
            temp_stats = [Stats(), Stats(), Stats(), Stats()]
            temp_stats[0].EDMG += 0.08
            temp_stats[1].EDMG += 0.16
            temp_stats[2].EDMG += 0.24
            temp_stats[3].EDMG += 0.32
            condition = 'When in battle, gain an 8% Elemental DMG Bonus every 4s. Max 4 stacks.'
            condition_option.add_option(weapon_name, condition, temp_stats)
        elif weapon_name == 'Skyward Atlas':
            stats.EDMG += 0.12
        elif weapon_name == 'Memory of Dust':
            stats.SHIELD += 0.2
            temp_stats = [Stats(), Stats(), Stats(), Stats(), Stats()]
            temp_stats[0].ATK_p += 0.04
            temp_stats[1].ATK_p += 0.08
            temp_stats[2].ATK_p += 0.12
            temp_stats[3].ATK_p += 0.16
            temp_stats[4].ATK_p += 0.2
            condition = 'While not protected by a shield, Scoring hits on opponents increases ATK by 4% for 8s.'
            condition_option.add_option(weapon_name, condition, temp_stats)

            temp_stats = [Stats(), Stats(), Stats(), Stats(), Stats()]
            temp_stats[0].ATK_p += 0.08
            temp_stats[1].ATK_p += 0.16
            temp_stats[2].ATK_p += 0.24
            temp_stats[3].ATK_p += 0.32
            temp_stats[4].ATK_p += 0.4
            condition = 'While protected by a shield, Scoring hits on opponents increases ATK by 8% for 8s.'
            condition_option.add_option(weapon_name, condition, temp_stats)
    return stats


def process_artifact(artifacts, character, stats):
    atf_name = []
    for each_atf in artifacts:
        if each_atf is not None:
            atf_name.append(each_atf.get('asn_name'))

    atf_result = []
    already_add = []
    for each_atf_name in atf_name:
        if each_atf_name in already_add:
            continue
        already_add.append(each_atf_name)
        same_name_count = atf_name.count(each_atf_name)
        atf_result.append((each_atf_name, same_name_count))

    for each_atf_result in atf_result:
        name = each_atf_result[0]
        piece = each_atf_result[1]
        if name == 'Adventurer':
            if piece >= 2:
                stats.HP += 1000
        elif name == 'Traveling Doctor':
            if piece >= 2:
                stats.HEAL += 0.2
        elif name == 'Resolution of Sojourner':
            if piece >= 2:
                stats.ATK_p += 0.18
            if piece >= 4:
                stats.charge_attack_cr += 0.3
        elif name == 'Brave Heart':
            if piece >= 2:
                stats.ATK_p += 0.18
            if piece >= 4:
                temp_stats = Stats()
                temp_stats.all_dmg_bonus += 0.3
                condition = 'Increases DMG by 30% against opponents with more than 50% HP.'
                condition_option.add_option(name, condition, temp_stats)
        elif name == 'Martial Artist':
            if piece >= 2:
                stats.normal_attack_dmg_bonus += 0.15
                stats.charge_attack_dmg_bonus += 00.15
            if piece >= 4:
                temp_stats = Stats()
                temp_stats.normal_attack_dmg_bonus += 0.25
                temp_stats.charge_attack_dmg_bonus += 0.25
                condition = 'After using Elemental Skill, increases Normal Attack and Charged Attack DMG by 25% for 8s.'
                condition_option.add_option(name, condition, temp_stats)
        elif name == 'Berserker':
            if piece >= 2:
                stats.CR += 0.12
            if piece >= 4:
                temp_stats = Stats()
                temp_stats.CR += 0.24
                condition = 'When HP is below 70%, CRIT Rate increases by an additional 24%.'
                condition_option.add_option(name, condition, temp_stats)
        elif name == 'Bloodstained Chivalry':
            if piece >= 2:
                stats.PDMG += 0.25
            if piece >= 4:
                temp_stats = Stats()
                temp_stats.charge_attack_dmg_bonus += 0.5
                condition = 'After defeating an opponent, increases Charged Attack DMG by 50%, and reduces its Stamina cost to 0 for 10s.'
                condition_option.add_option(name, condition, temp_stats)
        elif name == 'Gladiator\'s Finale':
            if piece >= 2:
                stats.ATK_p += 0.18
            if piece >= 4:
                if character.WEAPON_TYPE in ['Sword', 'Claymore', 'Polearm']:
                    stats.normal_attack_dmg_bonus += 0.35
        elif name == 'Wanderer\'s Troupe':
            if piece >= 2:
                stats.EM += 80
            if piece >= 4:
                if character.WEAPON_TYPE in ['Catalyst', 'Bow']:
                    stats.charge_attack_dmg_bonus += 0.35
        elif name == 'Pale Flame':
            if piece >= 2:
                stats.PDMG += 0.25
            if piece >= 4:
                temp_stats = [Stats(), Stats()]
                temp_stats[0].ATK_p += 0.9
                temp_stats[1].ATK_p += 1.8
                temp_stats[1].PDMG += 0.25
                condition = 'When an Elemental Skill hits an opponent, ATK is increased by 9% for 7s. This effect stacks up to 2 times and can be triggered once every 0.3s. Once 2 stacks are reached, the 2-set effect is increased by 100%.'
                condition_option.add_option(name, condition, temp_stats)
        elif name == 'Gambler':
            if piece >= 2:
                stats.element_skill_dmg_bonus += 0.2
        elif name == 'Thundering Fury':
            if piece >= 2:
                # TODO not sure electro dmg bonus is all dmg bonus?
                stats.ELECTRO_DMG += 0.15
            if piece >= 4:
                stats.overloaded_dmg_bonus += 0.4
                stats.electro_charged_dmg_bonus += 0.4
                stats.superconduct_dmg_bonus += 0.4
        elif name == 'Viridescent Venerer':
            if piece >= 2:
                stats.ANEMO_DMG += 0.15
            if piece >= 4:
                stats.swirl_dmg_bonus += 0.6
                # condition effect
                # Decreases opponent's Elemental RES to the element infused in the Swirl by 40% for 10s.
                # stats.mon_res_debuff += 0.4
        elif name == 'Archaic Petra':
            if piece >= 2:
                stats.GEO_DMG += 0.15
            if piece >= 4:
                temp_stats = Stats()
                # TODO is this all_dmg_bonus?
                temp_stats.all_dmg_bonus += 0.35
                condition = 'Upon obtaining an Elemental Shard created through a Crystallize Reaction, all party members gain a 35% DMG Bonus for that particular element for 10s. Only one form of Elemental DMG Bonus can be gained in this manner at any one time.'
                condition_option.add_option(name, condition, temp_stats)
                pass
        elif name == 'Crimson Witch of Flames':
            if piece >= 2:
                stats.PYRO_DMG += 0.15
            if piece >= 4:
                stats.overloaded_dmg_bonus += 0.4
                stats.vaporize_dmg_bonus += 0.15
                stats.melt_dmg_bonus += 0.15
                temp_stats = [Stats(), Stats(), Stats()]
                stacks_1 = 0.15
                stacks_2 = stacks_1 + (stacks_1/2)
                stacks_3 = stacks_2 + (stacks_2/2)
                temp_stats[0].PYRO_DMG += stacks_1
                temp_stats[1].PYRO_DMG += stacks_2
                temp_stats[2].PYRO_DMG += stacks_3
                condition = 'Using Elemental Skill increases the 2-Piece Set Bonus by 50% of its starting value for 10s. Max 3 stacks.'
                condition_option.add_option(name, condition, temp_stats)
        elif name == 'Noblesse Oblige':
            if piece >= 2:
                stats.element_burst_dmg_bonus += 0.2
            if piece >= 4:
                temp_stats = Stats()
                temp_stats.ATK_p += 0.2
                condition = 'Using an Elemental Burst increases all party members\' ATK by 20% for 12s.'
                condition_option.add_option(name, condition, temp_stats)
        elif name == 'Blizzard Strayer':
            if piece >= 2:
                stats.CRYO_DMG += 0.15
            if piece >= 4:
                temp_stats = Stats()
                temp_stats.CR += 0.2
                condition = 'When a character attacks an opponent affected by Cryo, their CRIT Rate is increased by 20%.'
                condition_option.add_option(name, condition, temp_stats)

                temp_stats = Stats()
                temp_stats.CR += 0.2
                condition = 'If the opponent is Frozen, CRIT Rate is increased by an additional 20%.'
                condition_option.add_option(name, condition, temp_stats)
        elif name == 'Heart of Depth':
            if piece >= 2:
                stats.HYDRO_DMG += 0.15
            if piece >= 4:
                temp_stats = Stats()
                temp_stats.normal_attack_dmg_bonus += 0.3
                temp_stats.charge_attack_dmg_bonus += 0.3
                condition = 'After using Elemental Skill, increases Normal Attack and Charged Attack DMG by 30% for 15s.'
                condition_option.add_option(name, condition, temp_stats)
        elif name == 'Glacier and Snowfield':
            if piece >= 2:
                stats.CRYO_DMG += 0.15
            if piece >= 4:
                stats.superconduct_dmg_bonus += 1
                stats.melt_dmg_bonus += 0.15

                temp_stats = Stats()
                temp_stats.CRYO_DMG += 0.3
                condition = 'Using an Elemental Burst increases Cryo DMG Bonus by 30% for 10s.'
                condition_option.add_option(name, condition, temp_stats)
        elif name == 'Shimenawa\'s Reminiscence':
            if piece >= 2:
                stats.ATK_p += 0.18
            if piece >= 4:
                temp_stats = Stats()
                temp_stats.normal_attack_dmg_bonus += 0.5
                temp_stats.charge_attack_dmg_bonus += 0.5
                temp_stats.plunging_attack_dmg_bonus += 0.5
                condition = 'When casting an Elemental Skill, if the character has 15 or more Energy,they lose 15 Energy and Normal/Charged/Plunging Attack DMG isincreased by 50% for 10s.'
                condition_option.add_option(name, condition, temp_stats)
        elif name == 'Lucky Dog':
            if piece >= 2:
                stats.DEF += 100
        elif name == 'Defender\'s Will':
            if piece >= 2:
                stats.DEF_p += 0.3
            if piece >= 4:
                # For each different element present in your own party,
                # the wearer's Elemental RES to that corresponding element is
                # increased by 30%.
                pass
        elif name == 'Retracing Bolide':
            if piece >= 2:
                stats.SHIELD += 0.3
            if piece >= 4:
                temp_stats = Stats()
                temp_stats.normal_attack_dmg_bonus += 0.4
                temp_stats.charge_attack_dmg_bonus += 0.4
                condition = 'While protected by a shield, gain an additional 40% Normal and Charged Attack DMG.'
                condition_option.add_option(name, condition, temp_stats)
        elif name == 'Tiny Miracle':
            if piece >= 2:
                # Electro RES increased by 40%.
                pass
            if piece >= 4:
                temp_stats = Stats()
                temp_stats.all_dmg_bonus += 0.35
                condition = 'Increases DMG against opponents affected by Electro by 35%.'
                condition_option.add_option(name, condition, temp_stats)
        elif name == 'Lavawalker':
            if piece >= 2:
                # Pyro RES increased by 40%.
                pass
            if piece >= 4:
                temp_stats = Stats()
                temp_stats.all_dmg_bonus += 0.35
                condition = 'Increases DMG against opponents affected by Pyro by 35%.'
                condition_option.add_option(name, condition, temp_stats)
        elif name == 'Scholar':
            if piece >= 2:
                stats.ER += 0.2
            if piece >= 4:
                # Gaining Elemental Particles or Orbs
                pass
        elif name == 'Instructor':
            if piece >= 2:
                stats.EM += 80
            if piece >= 4:
                temp_stats = Stats()
                temp_stats.EM += 120
                condition = 'Upon triggering an Elemental Reaction, increases all party members\' Elemental Mastery by 120 for 8s.'
                condition_option.add_option(name, condition, temp_stats)
        elif name == 'The Exile':
            if piece >= 2:
                stats.ER += 0.2
            if piece >= 4:
                # Using an Elemental Burst regenerates 2 Energy
                pass
        elif name == 'Maiden Beloved':
            if piece >= 2:
                stats.HEAL += 0.15
            if piece >= 4:
                temp_stats = Stats()
                temp_stats.HEAL += 0.2
                condition = 'Using an Elemental Skill or Burst increases healing received by all party members by 20% for 10s.'
                condition_option.add_option(name, condition, temp_stats)
        elif name == 'Tenacity of the Millelith':
            if piece >= 2:
                stats.HP_p += 0.2
            if piece >= 4:
                temp_stats = Stats()
                temp_stats.ATK_p += 0.2
                temp_stats.SHIELD += 0.3
                condition = 'When an Elemental Skill hits an opponent, the ATK of all nearby party members is increased by 20% and their Shield Strength is increased by 30% for 3s.'
                condition_option.add_option(name, condition, temp_stats)
        elif name == 'Emblem of Severed Fate':
            if piece >= 2:
                stats.ER += 0.2
            if piece >= 4:
                # TODO calculate emblem effect
                # emblem effect
                pass
        elif name == 'Prayers for Illumination':
            # decreed elemental affected time
            pass

    print(stats.__dict__)
    return stats
