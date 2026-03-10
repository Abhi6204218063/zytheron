def rank_candidates(results):

    ranked = sorted(results, key=lambda x: x["score"], reverse=True)

    return ranked[:20]
