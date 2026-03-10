import numpy as np
from Bio.PDB import PDBParser


def detect_active_site(pdb_file):

    parser = PDBParser(QUIET=True)
    structure = parser.get_structure("protein", pdb_file)

    coords = []

    for atom in structure.get_atoms():
        coords.append(atom.get_coord())

    coords = np.array(coords)

    center = coords.mean(axis=0)

    dist = np.linalg.norm(coords - center, axis=1)

    pocket_atoms = coords[dist < np.percentile(dist, 40)]

    pocket_center = pocket_atoms.mean(axis=0)

    return pocket_center, pocket_atoms


def simulate_mutation_effect(pocket_atoms, mutation_strength=0.5):

    noise = np.random.normal(0, mutation_strength, pocket_atoms.shape)

    mutated_atoms = pocket_atoms + noise

    mutated_center = mutated_atoms.mean(axis=0)

    return mutated_center


def mutation_aware_active_site(pdb_file="proteins/protein.pdb", simulations=10):

    print("\nRunning Mutation-Aware Active Site AI")

    center, pocket_atoms = detect_active_site(pdb_file)

    print("Original Active Site Center:", center)

    future_sites = []

    for i in range(simulations):

        new_center = simulate_mutation_effect(pocket_atoms)

        future_sites.append(new_center)

        print(f"Mutation Simulation {i+1} →", new_center)

    future_sites = np.array(future_sites)

    avg_future_site = future_sites.mean(axis=0)

    print("\nPredicted Future Active Site:", avg_future_site)

    return {
        "original": center,
        "future_sites": future_sites,
        "predicted_future": avg_future_site,
    }
