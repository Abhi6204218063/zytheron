def simulate_tumor_response(drugs):

    print("\nRunning Tumor Digital Twin")

    results = []

    for d in drugs:

        # drug tuple ho sakta hai (smiles, score)
        if isinstance(d, (list, tuple)):
            smiles = d[0]
            binding = d[1]
        else:
            smiles = d
            binding = -7

        # agar binding list ho
        if isinstance(binding, list):
            binding = binding[0]

        try:

            response = max(0, 1 + float(binding) / 12)

        except:
            response = 0

        results.append((smiles, binding, response))

    print("Tumor response simulated:", len(results))

    return results
