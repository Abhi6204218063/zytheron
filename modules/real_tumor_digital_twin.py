import random

mutations = ["TP53", "EGFR", "KRAS", "BRAF", "PIK3CA", "ALK", "BRCA1"]


def generate_patient_tumor():

    profile = []

    for i in range(random.randint(2, 5)):
        profile.append(random.choice(mutations))

    return profile


def simulate_tumor_response(binding):

    growth = random.uniform(0, 1)

    drug_effect = (-binding) / 12

    response = growth - drug_effect

    return max(0, response)
