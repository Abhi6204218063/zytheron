import os
import subprocess
import pandas as pd
from rdkit import Chem
from rdkit.Chem import AllChem

receptor = "receptor.pdbqt"


def prepare_ligand(smiles, name):

    mol = Chem.MolFromSmiles(smiles)
    mol = Chem.AddHs(mol)

    AllChem.EmbedMolecule(mol)
    AllChem.MMFFOptimizeMolecule(mol)

    pdb_file = f"{name}.pdb"
    pdbqt_file = f"{name}.pdbqt"

    Chem.MolToPDBFile(mol, pdb_file)

    subprocess.run(f"obabel {pdb_file} -O {pdbqt_file}", shell=True)

    return pdbqt_file


def dock_ligand(ligand):

    output = ligand.replace(".pdbqt", "_out.pdbqt")
    log = ligand.replace(".pdbqt", "_log.txt")

    cmd = f"""vina --receptor receptor.pdbqt \
--ligand {ligand} \
--center_x 0 --center_y 0 --center_z 0 \
--size_x 20 --size_y 20 --size_z 20 \
--log {log} \
--out {output}"""

    os.system(cmd)

    score = None

    with open(log) as f:
        for line in f:
            parts = line.split()
            if len(parts) > 1 and parts[0].isdigit():
                score = float(parts[1])
                break

    return score


results = []

with open("molecules.smi") as f:
    for i, smi in enumerate(f):

        smi = smi.strip()

        ligand = prepare_ligand(smi, f"mol{i}")

        score = dock_ligand(ligand)

        results.append([smi, score])

df = pd.DataFrame(results, columns=["SMILES", "BindingEnergy"])

df = df.sort_values("BindingEnergy")

df.to_csv("screening_results.csv", index=False)

print(df.head(10))
