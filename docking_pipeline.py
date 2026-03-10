# =====================================
# EVOTHERA Molecular Docking Pipeline
# RDKit + Meeko + AutoDock Vina
# =====================================

from rdkit import Chem
from rdkit.Chem import AllChem
from meeko import MoleculePreparation, PDBQTWriterLegacy
import subprocess

# -------------------------------------
# 1 SMILES input
# -------------------------------------

print("Creating molecule from SMILES...")

smiles = "CCO"

mol = Chem.MolFromSmiles(smiles)
mol = Chem.AddHs(mol)

# -------------------------------------
# 2 Generate 3D structure
# -------------------------------------

print("Generating 3D structure...")

AllChem.EmbedMolecule(mol)
AllChem.MMFFOptimizeMolecule(mol)

Chem.MolToMolFile(mol, "ligand.mol")

print("3D ligand generated")

# -------------------------------------
# 3 Reload molecule
# -------------------------------------

mol = Chem.MolFromMolFile("ligand.mol", removeHs=False)

# -------------------------------------
# 4 Convert to PDBQT
# -------------------------------------

print("Converting ligand to PDBQT...")

prep = MoleculePreparation()

setups = prep.prepare(mol)

pdbqt_string = PDBQTWriterLegacy.write_string(setups[0])[0]

with open("ligand.pdbqt", "w") as f:
    f.write(pdbqt_string)

print("Ligand converted to PDBQT")

# -------------------------------------
# 5 Run docking
# -------------------------------------

print("Running docking...")

vina_command = [
    r"C:\vina\vina.exe",
    "--receptor",
    "receptor.pdbqt",
    "--ligand",
    "ligand.pdbqt",
    "--center_x",
    "0",
    "--center_y",
    "0",
    "--center_z",
    "0",
    "--size_x",
    "20",
    "--size_y",
    "20",
    "--size_z",
    "20",
    "--out",
    "docked.pdbqt",
]

subprocess.run(vina_command)

print("Docking finished")
