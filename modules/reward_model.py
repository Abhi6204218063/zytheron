def docking_reward(score):

    if score is None:
        return -10

    if score < -9:
        return 10

    if score < -7:
        return 6

    if score < -5:
        return 3

    return -1
