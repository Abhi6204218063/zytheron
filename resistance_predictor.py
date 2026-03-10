import random


def predict_resistance(tumor, drug):

    resistance = random.uniform(0, 1)

    if "EGFR" in tumor:
        resistance += 0.2

    return min(resistance, 1)
