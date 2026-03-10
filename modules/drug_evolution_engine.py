import random

atoms = ["C", "N", "O", "F", "Cl", "Br"]


def evolve_drug(drug):

    drug = list(drug)

    pos = random.randint(0, len(drug) - 1)

    drug[pos] = random.choice(atoms)

    return "".join(drug)
