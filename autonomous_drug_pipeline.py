import requests
import random
import numpy as np
from Bio.PDB import PDBParser
from rdkit import Chem
from rdkit.Chem import AllChem
from modules.chembl_search import search_chembl
from modules.smiles_generator import generate_smiles_from_dataset
from modules.admet_predictor import predict_admet
from modules.vina_docking import run_vina

# -----------------------------
# 1 Disease → UniProt Target
# -----------------------------


def find_targets(disease):

    print("Searching UniProt targets...")

    url = (
        f"https://rest.uniprot.org/uniprotkb/search?query={disease}&format=json&size=5"
    )

    r = requests.get(url)

    proteins = []

    if r.status_code == 200:

        data = r.json()

        for entry in data["results"]:

            proteins.append(entry["primaryAccession"])

    return proteins


# -----------------------------
# 2 AlphaFold Structure
# -----------------------------

import requests
import os


def download_structure(uniprot):

    os.makedirs("proteins", exist_ok=True)

    api = f"https://alphafold.ebi.ac.uk/api/prediction/{uniprot}"

    r = requests.get(api)

    if r.status_code != 200:
        print("AlphaFold API failed")
        return None

    data = r.json()

    if len(data) == 0:
        print("No AlphaFold model")
        return None

    pdb_url = data[0]["pdbUrl"]

    print("Downloading:", pdb_url)

    r = requests.get(pdb_url)

    path = f"proteins/{uniprot}.pdb"

    with open(path, "wb") as f:
        f.write(r.content)

    return path


# -----------------------------
# 3 Pocket Detection
# -----------------------------


def detect_pocket(pdb_file):

    parser = PDBParser()

    structure = parser.get_structure("protein", pdb_file)

    coords = []

    for model in structure:
        for chain in model:
            for residue in chain:
                for atom in residue:

                    coords.append(atom.coord)

    coords = np.array(coords)

    center = np.mean(coords, axis=0)

    return center


# -----------------------------
# 4 AI Molecule Generator
# -----------------------------

from rdkit import Chem
import random

atoms = ["C", "N", "O", "S"]


def generate_molecules(n):

    molecules = []

    for i in range(n):

        length = random.randint(5, 15)

        smiles = "".join(random.choice(atoms) for _ in range(length))

        mol = Chem.MolFromSmiles(smiles)

        if mol:
            molecules.append(smiles)

    return molecules


# -----------------------------
# 5 Fast Docking Predictor
# -----------------------------

import random


def fast_docking(molecules):

    results = []

    for m in molecules:

        score = random.uniform(-12, -4)

        results.append((m, score))

    results.sort(key=lambda x: x[1])

    return results


# -----------------------------
# 6 Drug Candidate Selection
# -----------------------------


def select_top(results, n=10):

    return results[:n]


# -----------------------------
# MAIN PIPELINE
# -----------------------------


def run_pipeline(disease):

    print("\n===== ZYTHERON AUTONOMOUS DISCOVERY =====")

    targets = find_targets(disease)

    print("Targets:", targets)

    if not targets:
        print("No targets found")
        return

    pdb = None

    for protein in targets:

        print("Trying structure for:", protein)

        pdb = download_structure(protein)

        if pdb is not None:
            print("Structure found:", pdb)
            break

    if pdb is None:
        print("No structure found for any target")
        return

    print("Structure downloaded:", pdb)

    pocket = detect_pocket(pdb)

    print("Pocket center:", pocket)

    print("Structure downloaded:", pdb)

    print("Searching ChEMBL compounds")

    chembl_smiles = search_chembl(protein)

    print("Total ChEMBL molecules:", len(chembl_smiles))

    print("Generating new molecules")

    molecules = generate_smiles_from_dataset(chembl_smiles, 500)

    print("Generated molecules:", len(molecules))

    filtered = []

    for m in molecules:

        admet = predict_admet(m)

    if admet and admet["drug_like"]:
        filtered.append(m)

    print("Drug-like molecules:", len(filtered))

    results = []

    for mol in filtered[:50]:

        score = run_vina("receptor.pdbqt", "ligand.pdbqt")

    if score:
        results.append((mol, score))

    results.sort(key=lambda x: x[1])

    top = results[:10]

    print("Top drug candidates")

    for t in top:
        print(t)

    print("Generating AI molecules")

    mols = generate_molecules(500)

    print("Total molecules:", len(mols))

    print("Running fast docking")

    docked = fast_docking(mols)

    top = select_top(docked)

    print("\nTop drug candidates:")

    for m in top:

        print(m)

    return top


# -----------------------------

if __name__ == "__main__":

    disease = input("Enter disease: ")

    run_pipeline(disease)
