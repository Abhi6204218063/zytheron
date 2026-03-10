from meeko import MoleculePreparation
from rdkit import Chem

print("Loading receptor...")

mol = Chem.MolFromPDBFile("receptor_fixed.pdb", removeHs=False)

prep = MoleculePreparation()
prep.prepare(mol)

pdbqt_string = prep.write_pdbqt_string()

with open("receptor.pdbqt", "w") as f:
    f.write(pdbqt_string)

print("Receptor converted to PDBQT successfully")
