import os
import shutil
import pandas as pd

UPLOAD_DIR = "uploads"


def save_uploaded_file(source_path, category):

    os.makedirs(UPLOAD_DIR, exist_ok=True)

    target_dir = os.path.join(UPLOAD_DIR, category)

    os.makedirs(target_dir, exist_ok=True)

    filename = os.path.basename(source_path)

    target_path = os.path.join(target_dir, filename)

    shutil.copy(source_path, target_path)

    print("File saved:", target_path)

    return target_path


def read_fasta(file_path):

    with open(file_path) as f:

        lines = f.readlines()

    sequence = ""

    for line in lines:

        if not line.startswith(">"):

            sequence += line.strip()

    return sequence


def read_smi(file_path):

    with open(file_path) as f:

        smiles = [line.strip() for line in f]

    return smiles


def read_pdb(file_path):

    with open(file_path) as f:

        pdb_data = f.read()

    return pdb_data


def read_csv(file_path):

    df = pd.read_csv(file_path)

    return df
