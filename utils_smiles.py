def extract_smiles(m):

    # tuple case  ('CCO', -7.3)
    if isinstance(m, tuple):
        return str(m[0])

    # list case ['CCO', -7.3]
    if isinstance(m, list):
        return str(m[0])

    # direct smiles
    return str(m)


from rdkit import Chem


def safe_mol_from_smiles(m):

    smiles = extract_smiles(m)

    mol = Chem.MolFromSmiles(smiles)

    if mol is None:
        return None

    return mol
