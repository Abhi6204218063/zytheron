from pdbfixer import PDBFixer
from openmm.app import PDBFile

fixer = PDBFixer(filename="2XKN.pdb")

fixer.findMissingResidues()
fixer.findMissingAtoms()
fixer.addMissingAtoms()
fixer.addMissingHydrogens()

PDBFile.writeFile(fixer.topology, fixer.positions, open("receptor_fixed.pdb", "w"))

print("Protein cleaned successfully")
