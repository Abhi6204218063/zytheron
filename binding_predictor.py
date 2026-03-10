import random


def predict_binding(drug):

    score = -random.uniform(6, 12)

    if "N" in drug:
        score -= 0.3

    if "O" in drug:
        score -= 0.3

    return score
