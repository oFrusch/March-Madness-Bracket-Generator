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
    initial_queue = queue.Queue(maxsize=16)
    for i,j in sweet_sixteen.items():
        team1 = make_team(i, "team " + str(i))
        team2 = make_team(j, "team " + str(i))
        initial_queue.put(team1)
        initial_queue.put(team2)
    return initial_queue
