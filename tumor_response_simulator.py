import random


def simulate_response(binding, resistance):

    response = (-binding) / 12

    response = response * (1 - resistance)

    noise = random.uniform(-0.05, 0.05)

    return max(0, response + noise)
