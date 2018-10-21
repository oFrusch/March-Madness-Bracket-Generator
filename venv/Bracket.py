# 1 -----
#       | ----
# 16 ----
#
# 9 -----
#       | ----
# 8 ----
#
# 12 -----
#       | ----
# 5 ----
#
# 4 -----
#       | ----
# 13 ----
#
# 6 -----
#       | ----
# 11 ----
#
# 3 -----
#       | ----
# 14 ----
#
# 7 -----
#       | ----
# 10 ----
#
# 2 -----
#       | ----
# 15 ----

from TeamObject import *
import queue
import random


sweet_sixteen = {
    1: 16,
    8: 9,
    5: 12,
    4: 13,
    6: 11,
    3: 14,
    7: 10,
    2: 15
}


# Generates all the teams for one conference
def generate_teams():
    initial_queue = queue.Queue(maxsize=16)
    for i, j in sweet_sixteen.items():
        team1 = make_team(i, "team " + str(i))
        team2 = make_team(j, "team " + str(i))
        initial_queue.put(team1)
        initial_queue.put(team2)
    return initial_queue


# Returns the 8 teams from one conference that will go to Sweet 16
def simulate_round1(teams):
    round2 = queue.Queue(maxsize=8)
    while not teams.empty():
        random_num = random.randint(0, 5) / 5
        team1 = teams.get()
        team2 = teams.get()
        team1_chance = team1.round1_chance * random_num
        team2_chance = team2.round1_chance * random_num
        add_team = team1 if team1_chance > team2_chance else team2
        round2.put(add_team)
    return round2


# Returns the 4 teams from one conference that will go to Elite 8
def simulate_round2(teams):
    sweet_sixteen_queue = queue.Queue(maxsize=4)
    while not teams.empty():
        random_num = random.randint(0, 5) / 5
        team1 = teams.get()
        team2 = teams.get()
        team1_chance = team1.sweet_sixteen_chance * random_num
        team2_chance = team2.sweet_sixteen_chance * random_num
        add_team = team1 if team1_chance > team2_chance else team2
        sweet_sixteen_queue.put(add_team)
    return sweet_sixteen_queue


# Returns the 2 teams from one conference that will go to Final 4
def simulate_16(teams):
    elite_eight_queue = queue.Queue(maxsize=2)
    while not teams.empty():
        random_num = random.randint(0, 5) / 5
        team1 = teams.get()
        team2 = teams.get()
        team1_chance = team1.elite_eight_chance * random_num
        team2_chance = team2.elite_eight_chance * random_num
        add_team = team1 if team1_chance > team2_chance else team2
        elite_eight_queue.put(add_team)
    return elite_eight_queue


# Returns the team from one region that will go to championship
def simulate_8(teams):
    random_num = random.randint(0, 5) / 5
    team1 = teams.get()
    team2 = teams.get()
    team1_chance = team1.final_four_chance * random_num
    team2_chance = team2.final_four_chance * random_num
    return team1 if team1_chance > team2_chance else team2


def simulate_conference():
    teams = generate_teams()
    teams2 = simulate_round1(teams)
    teams16 = simulate_round2(teams2)
    teams8 = simulate_16(teams16)
    conference_winner = simulate_8(teams8)
    return conference_winner


def simulate_region():
    team1 = simulate_conference()
    team2 = simulate_conference()
    random_num = random.randint(0, 5) / 5
    team1_chance = team1.champ_game_chance * random_num
    team2_chance = team2.champ_game_chance * random_num
    return team1 if team1_chance > team2_chance else team2


def simulate_tournament():
    team1 = simulate_region()
    team2 = simulate_region()
    random_num = random.randint(0, 5) / 5
    team1_chance = team1.win_chance * random_num
    team2_chance = team2.win_chance * random_num
    return team1 if team1_chance > team2_chance else team2


winners = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0}
for i in range(0, 100000):
    winners[simulate_tournament().seed] += 1

for i in winners:
    print(i)

