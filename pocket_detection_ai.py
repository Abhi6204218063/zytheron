import numpy as np
from Bio.PDB import PDBParser


def detect_pocket(pdb_path):

    parser = PDBParser()
    structure = parser.get_structure("protein", pdb_path)

    coords = []

    for model in structure:
        for chain in model:
            for residue in chain:
                for atom in residue:

                    coords.append(atom.coord)

    coords = np.array(coords)

    center = np.mean(coords, axis=0)

    return center
