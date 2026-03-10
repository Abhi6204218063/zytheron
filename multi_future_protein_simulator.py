import random

AMINO_ACIDS = "ACDEFGHIKLMNPQRSTVWY"


def mutate_sequence(seq):

    seq = list(seq)

    pos = random.randint(0, len(seq) - 1)

    seq[pos] = random.choice(AMINO_ACIDS)

    return "".join(seq)


def structure_shift(original, mutated):

    diff = 0

    for a, b in zip(original, mutated):

        if a != b:
            diff += 1

    return diff / len(original)


def simulate_future_proteins(sequence, n_variants=50):

    print("\nSimulating future protein variants")

    variants = []

    for i in range(n_variants):

        mutated = mutate_sequence(sequence)

        shift = structure_shift(sequence, mutated)

        variants.append({"sequence": mutated, "structure_shift": shift})

    return variants
