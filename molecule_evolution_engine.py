import random
from rdkit import Chem
from rdkit.Chem import AllChem


# Simple mutation: add atom / replace atom
atoms = ["C", "N", "O", "F"]


def mutate_smiles(smiles):

    pos = random.randint(0, len(smiles) - 1)

    atom = random.choice(atoms)

    new_smiles = smiles[:pos] + atom + smiles[pos + 1 :]

    return new_smiles


def generate_mutations(smiles, num=5):

    mutants = []

    for _ in range(num):

        m = mutate_smiles(smiles)

        try:
            mol = Chem.MolFromSmiles(m)

            if mol is not None:
                mutants.append(m)

        except:
            pass

    return mutants


def evolve_population(best_smiles):

    new_population = []

    for s in best_smiles:

        mutants = generate_mutations(s)

        new_population.extend(mutants)

    return new_population


if __name__ == "__main__":

    seed = ["CCO", "CCN", "CCC"]

    new_molecules = evolve_population(seed)

    print("Generated molecules:")

    for m in new_molecules:
        print(m)
