import random

# ---------------------------------
# Protein mutation simulator
# ---------------------------------


def generate_mutation_variants(sequence, n=20):

    amino_acids = list("AVLIMFWSTNQKRDEY")

    variants = []

    for i in range(n):

        seq = list(sequence)

        pos = random.randint(0, len(seq) - 1)

        seq[pos] = random.choice(amino_acids)

        variants.append("".join(seq))

    return variants


# ---------------------------------
# Binding prediction wrapper
# ---------------------------------


def binding_score(smiles, predictor):

    try:
        score = predictor(smiles)
        return float(score)
    except:
        return -5.0


# ---------------------------------
# Mutation fitness penalty
# ---------------------------------


def mutation_fitness_penalty():

    return random.uniform(0.5, 5.0)


# ---------------------------------
# Evolution pressure score
# ---------------------------------


def evolution_pressure(binding, penalty):

    pressure = abs(binding) + penalty

    return pressure


# ---------------------------------
# EPDD main evaluation
# ---------------------------------


def run_epdd(molecules, predictor, protein_sequence):

    print("\nRunning Evolution-Pressure Drug Design\n")

    variants = generate_mutation_variants(protein_sequence, 20)

    print("Generated variants:", len(variants))

    results = []

    for mol in molecules:

        try:

            binding = binding_score(mol, predictor)

            penalty = mutation_fitness_penalty()

            pressure = evolution_pressure(binding, penalty)

            results.append((mol, binding, penalty, pressure))

        except:

            continue

    results.sort(key=lambda x: x[3], reverse=True)

    return results
