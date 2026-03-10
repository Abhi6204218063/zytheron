import random

from multi_future_protein_simulator import simulate_future_proteins


def run_evolution_steering(molecules, protein_sequence, predict_binding):

    print("\nRunning Evolution Steering Engine")

    future_proteins = simulate_future_proteins(protein_sequence, 30)

    results = []

    for mol in molecules:

        base_binding = predict_binding(mol)

        if base_binding is None:
            continue

        penalties = []

        for variant in future_proteins:

            mutated_seq = variant["sequence"]

            mutated_binding = predict_binding(mol)

            if mutated_binding is None:
                continue

            penalty = abs(mutated_binding - base_binding)

            penalties.append(penalty)

        if len(penalties) == 0:
            continue

        steering_score = sum(penalties) / len(penalties)

        results.append((mol, steering_score))

    results.sort(key=lambda x: x[1], reverse=True)

    return results
