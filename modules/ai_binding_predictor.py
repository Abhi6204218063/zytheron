from rdkit import Chem
import random
from modules.utils_smiles import safe_mol_from_smiles


def featurize(smiles):

    mol = safe_mol_from_smiles(smiles)

    if mol is None:
        return None

    return mol.GetNumAtoms()


def predict_binding(molecules):

    results = []

    for m in molecules:

        # molecule tuple/list ho sakta hai
        if isinstance(m, (list, tuple)):
            smiles = m[0]
        else:
            smiles = m

        smiles = str(smiles)

        try:

            fp = featurize(smiles)

            if fp is None:
                continue

            score = random.uniform(-12, -4)

            results.append((smiles, score))

        except Exception:
            continue

    return results
