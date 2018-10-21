# These three dictionaries contain actual data gathered since 1985
final_four_chances = {
    1: (54 / 33) / 4,
    2: (28 / 33) / 4,
    3: (15 / 33) / 4,
    4: (13 / 33) / 4,
    5: (6 / 33) / 4,
    6: (3 / 33) / 4,
    7: (3 / 33) / 4,
    8: (5 / 33) / 4,
    9: (1 / 33) / 4,
    10: (1 / 33) / 4,
    11: (3 / 33) / 4,
    12: (0 / 33) / 4,
    13: (0 / 33) / 4,
    14: (0 / 33) / 4,
    15: (0 / 33) / 4,
    16: (0 / 33) / 4,
}


final_two_chances = {
    1: (32 / 33) / 4,
    2: (12 / 33) / 4,
    3: (10 / 33) / 4,
    4: (3 / 33) / 4,
    5: (3 / 33) / 4,
    6: (2 / 33) / 4,
    7: (1 / 33) / 4,
    8: (3 / 33) / 4,
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
    1: (20 / 33) / 4,
    2: (5 / 33) / 4,
    3: (4 / 33) / 4,
    4: (1 / 33) / 4,
    5: (0 / 33) / 4,
    6: (1 / 33) / 4,
    7: (1 / 33) / 4,
    8: (1 / 33) / 4,
    9: (0 / 33) / 4,
    10: (0 / 33) / 4,
    11: (0 / 33) / 4,
    12: (0 / 33) / 4,
    13: (0 / 33) / 4,
    14: (0 / 33) / 4,
    15: (0 / 33) / 4,
    16: (0 / 33) / 4,
}


# These 2 dictionaries are my crude conjectures because I was unable to find any data on these rounds
sweet_sixteen_chance = {
    1: 0.99,
    2: 0.95,
    3: 0.90,
    4: 0.87,
    5: 0.82,
    6: 0.78,
    7: 0.70,
    8: 0.51,
    9: 0.49,
    10: 0.30,
    11: 0.22,
    12: 0.18,
    13: 0.13,
    14: 0.10,
    15: 0.05,
    16: 0.01,
}

elite_eight_chance = {
    1: 0.80,
    2: 0.40,
    3: 0.22,
    4: 0.20,
    5: 0.10,
    6: 0.05,
    7: 0.05,
    8: 0.08,
    9: 0.015,
    10: 0.015,
    11: 0.05,
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
    name = "team name"

    def __init__(self, seed, win_chance, champ_game_chance, final_four_chance, elite_eight_chance, sweet_sixteen_chance, name):
        self.seed = seed
        self.win_chance = win_chance
        self.champ_game_chance = champ_game_chance
        self.final_four_chance = final_four_chance
        self.elite_eight_chance = elite_eight_chance
        self.sweet_sixteen_chance = sweet_sixteen_chance
        self.name = name


def make_team(seed, name):
    team = Team(seed, 0, 0, 0, 0, 0, name)
    team.win_chance = calc_win_chance(seed)
    team.champ_game_chance = calc_champ_game_chances(seed)
    team.final_four_chance = calc_final_four_chances(seed)
    team.elite_eight_chance = calc_elite_eight_chances(seed)
    team.sweet_sixteen_chance = calc_sweet_sixteen_chances(seed)
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
