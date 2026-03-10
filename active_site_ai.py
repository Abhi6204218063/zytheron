import numpy as np
from Bio.PDB import PDBParser


def detect_active_sites(pdb_file="proteins/protein.pdb"):

    print("\nRunning AI Active Site Discovery Engine")

    parser = PDBParser(QUIET=True)
    structure = parser.get_structure("protein", pdb_file)

    coords = []

    for atom in structure.get_atoms():
        coords.append(atom.get_coord())

    coords = np.array(coords)

    # Simple clustering-based pocket detection
    center = coords.mean(axis=0)

    distances = np.linalg.norm(coords - center, axis=1)

    pocket_atoms = coords[distances < np.percentile(distances, 40)]

    pocket_center = pocket_atoms.mean(axis=0)

    result = {
        "center_x": float(pocket_center[0]),
        "center_y": float(pocket_center[1]),
        "center_z": float(pocket_center[2]),
        "pocket_size": len(pocket_atoms),
    }

    print("Active site detected at:")
    print(result)

    return result
