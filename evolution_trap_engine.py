import random

AMINO_ACIDS = "ACDEFGHIKLMNPQRSTVWY"


def mutate_protein(sequence):

    seq = list(sequence)

    pos = random.randint(0, len(seq) - 1)

    seq[pos] = random.choice(AMINO_ACIDS)

    return "".join(seq)


def protein_stability_score(sequence):

    # simple proxy stability model

    hydrophobic = "AILMFWYV"

    score = 0

    for aa in sequence:

        if aa in hydrophobic:
            score += 1

    return score / len(sequence)


def run_evolution_trap(molecules, protein_sequence, predict_binding):

    print("\nRunning Evolution Trap Drug Engine")

    results = []

    for mol in molecules:

        base_binding = predict_binding(mol)

        if base_binding is None:
            continue

        mutation_penalty = []

        for i in range(10):

            mutated = mutate_protein(protein_sequence)

            stability = protein_stability_score(mutated)

            mutated_binding = predict_binding(mol)

            if mutated_binding is None:
                continue

            base_binding = (
                base_binding[0][1] if isinstance(base_binding, list) else base_binding
            )
            mutated_binding = (
                mutated_binding[0][1]
                if isinstance(mutated_binding, list)
                else mutated_binding
            )

            penalty = abs(mutated_binding - base_binding)

            mutation_penalty.append((penalty, stability))

        if len(mutation_penalty) == 0:
            continue

        avg_penalty = sum([p[0] for p in mutation_penalty]) / len(mutation_penalty)

        avg_stability = sum([p[1] for p in mutation_penalty]) / len(mutation_penalty)

        trap_score = avg_penalty * (1 - avg_stability)

        results.append((mol, trap_score))

    results.sort(key=lambda x: x[1], reverse=True)

    return results
