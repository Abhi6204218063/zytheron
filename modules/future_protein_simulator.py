import random

AMINO_ACIDS = list("ACDEFGHIKLMNPQRSTVWY")


def mutate_protein(sequence, mutation_rate=0.05):

    seq = list(sequence)

    for i in range(len(seq)):

        if random.random() < mutation_rate:
            seq[i] = random.choice(AMINO_ACIDS)

    return "".join(seq)


def generate_future_variants(sequence, n=20):

    variants = []

    for _ in range(n):

        mutated = mutate_protein(sequence)

        variants.append(mutated)

    return variants


def predict_structure_shift(original, mutated):

    diff = sum(1 for a, b in zip(original, mutated) if a != b)

    structural_shift = diff / len(original)

    return structural_shift


def simulate_future_proteins(sequence, variants=20):

    future_proteins = generate_future_variants(sequence, variants)

    results = []

    for v in future_proteins:

        shift = predict_structure_shift(sequence, v)

        results.append({"sequence": v, "structure_shift": shift})

    return results


if __name__ == "__main__":

    protein = "MKTFFVLLLCTFTVVAS"

    sims = simulate_future_proteins(protein, 10)

    for s in sims:

        print(s)
