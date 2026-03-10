from rdkit import Chem
import random

atoms = ["C", "N", "O", "S"]


def generate_ai_molecules(n=500):

    molecules = []

    while len(molecules) < n:

        length = random.randint(5, 12)

        sm = ""

        for i in range(length):
            sm += random.choice(atoms)

        mol = Chem.MolFromSmiles(sm)

        if mol is not None:

            molecules.append(sm)

    return molecules
