import random

atoms = ["C", "N", "O", "F", "Cl", "Br"]


def design_drug():

    length = random.randint(6, 14)

    mol = ""

    for _ in range(length):
        mol += random.choice(atoms)

    return mol
