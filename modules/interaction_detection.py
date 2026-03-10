from rdkit import Chem


def detect_interactions(smiles):

    mol = Chem.MolFromSmiles(smiles)

    h_bond_donors = 0
    h_bond_acceptors = 0

    for atom in mol.GetAtoms():

        if atom.GetAtomicNum() == 7 or atom.GetAtomicNum() == 8:

            h_bond_acceptors += 1

    return {"Hbond_acceptors": h_bond_acceptors, "Hbond_donors": h_bond_donors}
