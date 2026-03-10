import random


def select_best_molecules(results, top_k=10):

    results.sort(key=lambda x: x[1])  # lower docking score better

    best = results[:top_k]

    return [m[0] for m in best]


def mutate_smiles(smiles):

    atoms = ["C", "N", "O", "F"]

    pos = random.randint(0, len(smiles) - 1)

    new_atom = random.choice(atoms)

    new_smiles = smiles[:pos] + new_atom + smiles[pos + 1 :]

    return new_smiles
