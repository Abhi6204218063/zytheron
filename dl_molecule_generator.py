import random

atoms = ["C", "N", "O", "S"]


def generate_molecules(n):

    mols = []

    for i in range(n):

        length = random.randint(4, 10)

        sm = ""

        for j in range(length):

            sm += random.choice(atoms)

        mols.append(sm)

    return mols
