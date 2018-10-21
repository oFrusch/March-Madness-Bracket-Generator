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


def generate_teams():
    teams = []
    for i in range(1, 17):
        team = make_team(i, "team " + str(i))
        teams.append(team)
    return teams

