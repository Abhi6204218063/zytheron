import random

mutations = ["EGFR", "KRAS", "TP53", "BRAF", "PIK3CA"]


def evolve_tumor():

    tumor_profile = []

    for _ in range(random.randint(1, 4)):
        tumor_profile.append(random.choice(mutations))

    return tumor_profile
