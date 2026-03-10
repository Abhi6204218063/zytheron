from rdkit import Chem
import random

atoms = ["C", "N", "O"]


def generate_molecule():

    length = random.randint(5, 12)

    smi = ""

    for i in range(length):

        smi += random.choice(atoms)

    return smi


def generate_library(n=100):

    mols = []

    while len(mols) < n:

        smi = generate_molecule()

        mol = Chem.MolFromSmiles(smi)

        if mol is not None:

            mols.append(smi)

    return mols
