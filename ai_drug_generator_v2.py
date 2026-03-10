from rdkit import Chem
from rdkit.Chem import Descriptors
import random

# drug-like fragments
FRAGMENTS = [
    "C",
    "N",
    "O",
    "F",
    "CC",
    "CN",
    "CO",
    "c1ccccc1",
    "C(=O)O",
    "C(=O)N",
    "CCN",
    "CCO",
]


def drug_likeness(smiles):

    mol = Chem.MolFromSmiles(smiles)

    if mol is None:
        return False

    mw = Descriptors.MolWt(mol)
    logp = Descriptors.MolLogP(mol)
    hbd = Descriptors.NumHDonors(mol)
    hba = Descriptors.NumHAcceptors(mol)

    if mw > 500:
        return False

    if logp > 5:
        return False

    if hbd > 5:
        return False

    if hba > 10:
        return False

    return True


def generate_candidate():

    length = random.randint(3, 6)

    smiles = ""

    for i in range(length):
        smiles += random.choice(FRAGMENTS)

    mol = Chem.MolFromSmiles(smiles)

    if mol is None:
        return None

    try:
        Chem.SanitizeMol(mol)
        smiles = Chem.MolToSmiles(mol)
    except:
        return None

    if not drug_likeness(smiles):
        return None

    return smiles


def generate_ai_molecules(n=20):

    molecules = []

    attempts = 0

    while len(molecules) < n and attempts < 1000:

        m = generate_candidate()

        attempts += 1

        if m is None:
            continue

        if m not in molecules:
            molecules.append(m)

    return molecules


from rdkit import Chem
from rdkit.Chem import Descriptors
import random

# drug-like fragments
FRAGMENTS = [
    "C",
    "N",
    "O",
    "F",
    "CC",
    "CN",
    "CO",
    "c1ccccc1",
    "C(=O)O",
    "C(=O)N",
    "CCN",
    "CCO",
]


def drug_likeness(smiles):

    mol = Chem.MolFromSmiles(smiles)

    if mol is None:
        return False

    mw = Descriptors.MolWt(mol)
    logp = Descriptors.MolLogP(mol)
    hbd = Descriptors.NumHDonors(mol)
    hba = Descriptors.NumHAcceptors(mol)

    if mw > 500:
        return False

    if logp > 5:
        return False

    if hbd > 5:
        return False

    if hba > 10:
        return False

    return True


def generate_candidate():

    length = random.randint(3, 6)

    smiles = ""

    for i in range(length):
        smiles += random.choice(FRAGMENTS)

    mol = Chem.MolFromSmiles(smiles)

    if mol is None:
        return None

    try:
        Chem.SanitizeMol(mol)
        smiles = Chem.MolToSmiles(mol)
    except:
        return None

    if not drug_likeness(smiles):
        return None

    return smiles


def generate_ai_molecules(n=20):

    molecules = []

    attempts = 0

    while len(molecules) < n and attempts < 1000:

        m = generate_candidate()

        attempts += 1

        if m is None:
            continue

        if m not in molecules:
            molecules.append(m)

    return molecules
