from rdkit import Chem


def pdb_to_smiles(pdb_file):

    mol = Chem.MolFromPDBFile(pdb_file)

    if mol:
        return Chem.MolToSmiles(mol)

    return None
