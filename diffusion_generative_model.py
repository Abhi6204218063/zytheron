import random

atoms = ["C", "N", "O", "F", "Cl", "Br"]


def diffusion_generate(num=1000):

    molecules = []

    for _ in range(num):

        length = random.randint(5, 15)

        mol = ""

        for i in range(length):
            mol += random.choice(atoms)

        molecules.append(mol)

    return molecules
