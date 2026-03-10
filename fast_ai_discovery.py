import random


def screen(molecules):

    results = []

    for m in molecules:

        score = random.uniform(-12, -5)

        results.append((m, score))

    results.sort(key=lambda x: x[1])

    return results
