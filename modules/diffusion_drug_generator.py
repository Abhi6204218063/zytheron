import random


def generate_diffusion_molecules(n=50):

    print("Running diffusion drug generator")

    atoms = ["C", "N", "O"]

    molecules = []

    for i in range(n):

        length = random.randint(3, 8)

        smi = ""

        for j in range(length):
            smi += random.choice(atoms)

        molecules.append(smi)

    print("Diffusion molecules generated:", len(molecules))

    return molecules
