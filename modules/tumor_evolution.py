import random

mutations = ["TP53", "EGFR", "KRAS", "BRAF", "PIK3CA"]


def evolve_tumor():

    tumor = []

    for _ in range(random.randint(2, 5)):
        tumor.append(random.choice(mutations))

    return tumor


def simulate_response(binding):

    growth = random.uniform(0, 1)

    drug_effect = (-binding) / 12

    response = growth - drug_effect

    return max(0, response)
