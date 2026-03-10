import random
from rdkit import Chem
from rdkit.Chem import AllChem, Descriptors
from rdkit import RDLogger

RDLogger.DisableLog("rdApp.*")

# Allowed atoms for drug-like molecules
ATOM_POOL = ["C", "N", "O", "F", "Cl"]


def is_valid_smiles(smiles):
    try:
        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            return False

        Chem.SanitizeMol(mol)
        return True
    except:
        return False


def drug_like_filter(smiles):
    try:
        mol = Chem.MolFromSmiles(smiles)

        if mol is None:
            return False

        mw = Descriptors.MolWt(mol)
        logp = Descriptors.MolLogP(mol)
        hbd = Descriptors.NumHDonors(mol)
        hba = Descriptors.NumHAcceptors(mol)

        # Lipinski Rule of Five
        if mw > 500:
            return False
        if logp > 5:
            return False
        if hbd > 5:
            return False
        if hba > 10:
            return False

        return True

    except:
        return False


def mutate_smiles(smiles):
    mol = Chem.MolFromSmiles(smiles)

    if mol is None:
        return None

    atoms = mol.GetAtoms()

    if len(atoms) == 0:
        return None

    atom_idx = random.randint(0, len(atoms) - 1)
    new_atom = random.choice(ATOM_POOL)

    atoms[atom_idx].SetAtomicNum(Chem.Atom(new_atom).GetAtomicNum())

    try:
        Chem.SanitizeMol(mol)
        return Chem.MolToSmiles(mol)
    except:
        return None


def generate_mutations(smiles_list, n=20):

    new_population = []

    for s in smiles_list:

        for _ in range(3):

            new_smiles = mutate_smiles(s)

            if new_smiles is None:
                continue

            if not is_valid_smiles(new_smiles):
                continue

            if not drug_like_filter(new_smiles):
                continue

            new_population.append(new_smiles)

            if len(new_population) >= n:
                return new_population

    return new_population
