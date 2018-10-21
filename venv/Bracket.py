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
    sweet_sixteen_queue = queue.Queue(maxsize=8)
    while not teams.empty():
        random_num = random.randint(0, 5) / 5
        team1 = teams.get()
        team2 = teams.get()
        team1_chance = team1.sweet_sixteen_chance * random_num
        team2_chance = team2.sweet_sixteen_chance * random_num
        add_team = team1 if team1_chance > team2_chance else team2
        sweet_sixteen_queue.put(add_team)
    return sweet_sixteen_queue


# Returns the 4 teams from one conference that will go to Elite 8
def simulate_16(teams):
    elite_eight_queue = queue.Queue(maxsize=4)
    while not teams.empty():
        random_num = random.randint(0, 5) / 5
        team1 = teams.get()
        team2 = teams.get()
        team1_chance = team1.elite_eight_chance * random_num
        team2_chance = team2.elite_eight_chance * random_num
        add_team = team1 if team1_chance > team2_chance else team2
        elite_eight_queue.put(add_team)
    return elite_eight_queue


# Returns the 2 teams from one conference that will go to Final 4
def simulate_8(teams):
    final_four_queue = queue.Queue(maxsize=2)
    while not teams.empty():
        random_num = random.randint(0, 5) / 5
        team1 = teams.get()
        team2 = teams.get()
        team1_chance = team1.final_four_chance * random_num
        team2_chance = team2.final_four_chance * random_num
        add_team = team1 if team1_chance > team2_chance else team2
        final_four_queue.put(add_team)
    return final_four_queue


# Returns the team from one region that will go to championship
def simulate_4(teams):
    random_num = random.randint(0, 5) / 5
    team1 = teams.get()
    team2 = teams.get()
    team1_chance = team1.champ_game_chance * random_num
    team2_chance = team2.champ_game_chance * random_num
    return team1 if team1_chance > team2_chance else team2


def simulate_conference():
    teams = generate_teams()
    teams16 = simulate_round1(teams)
    teams8 = simulate_16(teams16)
    teams4 = simulate_8(teams8)
    conference_winner = simulate_4(teams4)
    return conference_winner


for i in range(0, 100):
    winner = simulate_conference()
    print(winner.seed)

