import random
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit import RDLogger

RDLogger.DisableLog("rdApp.*")

# fragments used for generation
FRAGMENTS = ["C", "N", "O", "F", "CC", "CN", "CO", "c1ccccc1", "C(=O)O", "C(=O)N"]


def generate_ai_molecule():

    n = random.randint(2, 5)

    smiles = ""

    for i in range(n):
        frag = random.choice(FRAGMENTS)
        smiles += frag

    try:
        mol = Chem.MolFromSmiles(smiles)

        if mol is None:
            return None

        Chem.SanitizeMol(mol)

        return Chem.MolToSmiles(mol)

    except:
        return None


def generate_ai_population(n=20):

    molecules = []

    attempts = 0

    while len(molecules) < n and attempts < n * 20:

        smi = generate_ai_molecule()

        attempts += 1

        if smi is None:
            continue

        if smi not in molecules:
            molecules.append(smi)

    return molecules
