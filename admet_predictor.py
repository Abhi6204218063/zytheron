from rdkit import Chem
from rdkit.Chem import Descriptors


def predict_admet(smiles):

    mol = Chem.MolFromSmiles(smiles)

    if mol is None:
        return None

    mw = Descriptors.MolWt(mol)
    logp = Descriptors.MolLogP(mol)
    hbd = Descriptors.NumHDonors(mol)
    hba = Descriptors.NumHAcceptors(mol)

    drug_like = mw < 500 and logp < 5 and hbd <= 5 and hba <= 10

    return {"MW": mw, "logP": logp, "HBD": hbd, "HBA": hba, "drug_like": drug_like}
