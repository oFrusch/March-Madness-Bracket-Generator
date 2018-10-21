# These three dictionaries contain actual data gathered since 1985
final_four_chances = {
    1: 0.41,
    2: 0.212,
    3: 0.114,
    4: 0.1,
    5: 0.045,
    6: 0.023,
    7: 0.023,
    8: 0.038,
    9: 0.008,
    10: 0.008,
    11: 0.023,
    12: (0 / 33) / 4,
    13: (0 / 33) / 4,
    14: (0 / 33) / 4,
    15: (0 / 33) / 4,
    16: (0 / 33) / 4,
}


final_two_chances = {
    1: 0.24,
    2: 0.098,
    3: 0.068,
    4: 0.023,
    5: 0.023,
    6: 0.015,
    7: 0.008,
    8: 0.023,
    9: (0 / 33) / 4,
    10: (0 / 33) / 4,
    11: (0 / 33) / 4,
    12: (0 / 33) / 4,
    13: (0 / 33) / 4,
    14: (0 / 33) / 4,
    15: (0 / 33) / 4,
    16: (0 / 33) / 4,
}


win_chances = {
    1: 0.15,
    2: 0.038,
    3: 0.03,
    4: 0.008,
    5: (0 / 33),
    6: 0.008,
    7: 0.008,
    8: 0.008,
    9: (0 / 33),
    10: (0 / 33),
    11: (0 / 33) / 4,
    12: (0 / 33) / 4,
    13: (0 / 33) / 4,
    14: (0 / 33) / 4,
    15: (0 / 33) / 4,
    16: (0 / 33) / 4,
}


# These 2 dictionaries are my crude conjectures because I was unable to find any data on these rounds
round1_chance = {
    1: 0.999,
    2: 0.95,
    3: 0.93,
    4: 0.80,
    5: 0.75,
    6: 0.67,
    7: 0.60,
    8: 0.51,
    9: 0.49,
    10: 0.40,
    11: 0.33,
    12: 0.26,
    13: 0.20,
    14: 0.10,
    15: 0.05,
    16: 0.001,
}

sweet_sixteen_chance = {
    1: 0.85,
    2: 0.80,
    3: 0.80,
    4: 0.67,
    5: 0.60,
    6: 0.55,
    7: 0.50,
    8: 0.42,
    9: 0.42,
    10: 0.35,
    11: 0.20,
    12: 0.13,
    13: 0.10,
    14: 0.05,
    15: 0.001,
    16: 0.0005,
}

elite_eight_chance = {
    1: 0.70,
    2: 0.46,
    3: 0.40,
    4: 0.25,
    5: 0.06,
    6: 0.10,
    7: 0.076,
    8: 0.061,
    9: 0.015,
    10: 0.061,
    11: 0.023,
    12: 0,
    13: 0,
    14: 0,
    15: 0,
    16: 0,
}


class Team:
    seed = 0
    win_chance = 0.0
    champ_game_chance = 0.0
    final_four_chance = 0.0
    elite_eight_chance = 0.0
    sweet_sixteen_chance = 0.0
    round1_chance = 0.0
    name = "team name"

    def __init__(self, seed, win_chance, champ_game_chance, final_four_chance, elite_eight_chance, sweet_sixteen_chance, round1_chance, name):
        self.seed = seed
        self.win_chance = win_chance
        self.champ_game_chance = champ_game_chance
        self.final_four_chance = final_four_chance
        self.elite_eight_chance = elite_eight_chance
        self.sweet_sixteen_chance = sweet_sixteen_chance
        self.round1_chance = round1_chance
        self.name = name


def make_team(seed, name):
    team = Team(seed, 0, 0, 0, 0, 0, 0, name)
    team.win_chance = calc_win_chance(seed)
    team.champ_game_chance = calc_champ_game_chances(seed)
    team.final_four_chance = calc_final_four_chances(seed)
    team.elite_eight_chance = calc_elite_eight_chances(seed)
    team.sweet_sixteen_chance = calc_sweet_sixteen_chances(seed)
    team.round1_chance = calc_round1_chance(seed)
    return team


# Pass in team seed num
def calc_win_chance(seed):
    return win_chances[seed]


# Pass in team seed num
def calc_champ_game_chances(seed):
    return final_two_chances[seed]


# Pass in team seed num
def calc_final_four_chances(seed):
    return final_four_chances[seed]


# Pass in team seed num
def calc_elite_eight_chances(seed):
    return elite_eight_chance[seed]


# Pass in team seed num
def calc_sweet_sixteen_chances(seed):
    return sweet_sixteen_chance[seed]


# Pass in team seed num
def calc_round1_chance(seed):
    return round1_chance[seed]
