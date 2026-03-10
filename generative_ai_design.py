import random

atoms = ["C", "N", "O", "F", "Cl"]


def generate_molecule():
    length = random.randint(4, 10)
    mol = "".join(random.choice(atoms) for _ in range(length))
    return mol
