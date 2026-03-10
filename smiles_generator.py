from rdkit import Chem
from rdkit.Chem import AllChem
import random


def generate_smiles_from_dataset(smiles_list, n=500):

    generated = []

    for s in smiles_list:

        mol = Chem.MolFromSmiles(s)

        if mol is None:
            continue

        for i in range(3):

            try:
                new = Chem.MolToSmiles(mol, doRandom=True)
                generated.append(new)
            except:
                pass

        if len(generated) >= n:
            break

    return generated
