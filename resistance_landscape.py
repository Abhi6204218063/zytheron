import random


def mutate_protein(seq):

    seq = list(seq)

    pos = random.randint(0, len(seq) - 1)

    aa = [
        "A",
        "V",
        "L",
        "I",
        "F",
        "W",
        "Y",
        "S",
        "T",
        "N",
        "Q",
        "C",
        "G",
        "P",
        "H",
        "R",
        "K",
        "D",
        "E",
    ]

    seq[pos] = random.choice(aa)

    return "".join(seq)


def simulate_resistance_landscape(molecules, future_proteins, predict_binding):

    print("\nMapping resistance landscape\n")

    results = []

    for protein in future_proteins:

        # FIX
        if isinstance(protein, dict):
            protein_seq = protein["sequence"]
        else:
            protein_seq = protein

        mutated_seq = mutate_protein(protein_seq)

        for mol in molecules:

            try:
                score = predict_binding(mol)

                results.append((mol, mutated_seq, score))

            except:
                pass

    print("Resistance simulations:", len(results))

    return results
