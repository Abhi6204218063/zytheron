import random


def predict_binding(smiles, target):
    """
    Placeholder binding predictor
    Future: GNN / docking model
    """

    score = random.uniform(-12, -5)

    return score


def multi_target_screen(molecules, targets):

    print("\nRunning Multi-Target Cancer Therapy Engine")

    results = []

    for smiles in molecules:

        target_scores = []

        for target in targets:

            score = predict_binding(smiles, target)

            target_scores.append(score)

        avg_score = sum(target_scores) / len(target_scores)

        results.append((smiles, avg_score, target_scores))

    # best drugs
    results.sort(key=lambda x: x[1])

    print("Multi-target screening complete")

    return results[:20]
