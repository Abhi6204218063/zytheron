import subprocess
from rdkit import Chem
from rdkit.Chem import AllChem

from pubchem_screening import get_pubchem_molecules
from ai_binding_predictor import predict_binding


RECEPTOR = "receptor.pdbqt"


def smiles_to_pdb(smiles, filename):

    mol = Chem.MolFromSmiles(smiles)

    mol = Chem.AddHs(mol)

    AllChem.EmbedMolecule(mol)

    AllChem.MMFFOptimizeMolecule(mol)

    Chem.MolToPDBFile(mol, filename)


def pdb_to_pdbqt(pdb_file, pdbqt_file):

    command = ["obabel", pdb_file, "-O", pdbqt_file]

    subprocess.run(command)


def run_vina(ligand):

    command = [
        "vina",
        "--receptor",
        RECEPTOR,
        "--ligand",
        ligand,
        "--center_x",
        "10",
        "--center_y",
        "10",
        "--center_z",
        "10",
        "--size_x",
        "20",
        "--size_y",
        "20",
        "--size_z",
        "20",
        "--exhaustiveness",
        "8",
    ]

    subprocess.run(command)


def main():

    print("Downloading molecules...")

    molecules = get_pubchem_molecules(50)

    print("AI screening...")

    scored = []

    for m in molecules:

        score = predict_binding(m)

        scored.append((m, score))

    scored.sort(key=lambda x: x[1], reverse=True)

    top = scored[:5]

    print("\nTop molecules for docking:")

    for i, (smiles, score) in enumerate(top):

        print(i, smiles, score)

        pdb = f"ligand_{i}.pdb"

        pdbqt = f"ligand_{i}.pdbqt"

        smiles_to_pdb(smiles, pdb)

        pdb_to_pdbqt(pdb, pdbqt)

        run_vina(pdbqt)


if __name__ == "__main__":
    main()
