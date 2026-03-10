from rdkit import Chem
from rdkit.Chem import AllChem

# example molecule (ethanol)
smiles = "CCO"

mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)

# generate 3D structure
AllChem.EmbedMolecule(mol)
AllChem.MMFFOptimizeMolecule(mol)

Chem.MolToMolFile(mol, "ligand.mol")

print("3D ligand created successfully")
