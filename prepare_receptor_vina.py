import subprocess

print("Preparing receptor for docking...")

input_pdb = "receptor_fixed.pdb"
output_pdbqt = "receptor.pdbqt"

command = ["vina", "--receptor", input_pdb, "--out", output_pdbqt]

subprocess.run(command)

print("Receptor converted to PDBQT successfully")
