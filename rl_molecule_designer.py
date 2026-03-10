import random


def design_rl_molecules(n=50):

    print("Running RL molecule designer")

    atoms = ["C", "N", "O"]

    molecules = []

    for i in range(n):

        length = random.randint(3, 8)

        smi = ""

        for j in range(length):
            smi += random.choice(atoms)

        molecules.append(smi)

    print("RL molecules generated:", len(molecules))

    return molecules
