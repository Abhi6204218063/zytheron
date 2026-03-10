import random


def simulate_cell_response(smiles):

    return {
        "toxicity": random.random(),
        "growth_inhibition": random.random(),
        "metabolism_score": random.random(),
    }
