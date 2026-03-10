import random


def evaluate_future_proof(molecules, variants):

    results = {}

    print("\nRunning future-proof evaluation...")

    for mol in molecules:

        scores = []

        print("\nTesting molecule:", mol)

        for v in variants:

            # simulated docking score
            score = random.uniform(-8.0, -3.0)

            scores.append(score)

        print("Variant scores:", scores)

        results[mol] = scores

    print("\nCollected results:", results)

    return results


def compute_robustness(results):

    ranked = []

    for mol, scores in results.items():

        avg_score = sum(scores) / len(scores)
        worst_case = max(scores)
        best_case = min(scores)

        robustness = abs(avg_score) + abs(best_case)

        ranked.append((mol, avg_score, worst_case, robustness))

    ranked.sort(key=lambda x: x[3], reverse=True)

    # fallback candidate (important)
    if len(ranked) == 0:

        ranked.append(("NO_MOLECULE_FOUND", 0, 0, 0))

    return ranked
