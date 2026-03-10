from pubchem_screening import get_pubchem_molecules
from drug_like_mutation_engine import generate_mutations
from ai_binding_predictor import predict_binding


def score_population(smiles_list):

    scored = []

    for s in smiles_list:
        try:
            score = predict_binding(s)
            scored.append((s, score))
        except:
            continue

    scored.sort(key=lambda x: x[1], reverse=True)

    return scored


def evolution_loop():

    print("Downloading initial molecules...")

    population = get_pubchem_molecules(50)

    generations = 3

    for g in range(generations):

        print("\nGeneration:", g + 1)

        scored = score_population(population)

        top = scored[:5]

        print("\nTop molecules:")

        for m in top:
            print(m)

        best_smiles = [x[0] for x in top]

        new_molecules = generate_mutations(best_smiles, 20)

        print("\nNew molecules generated:", len(new_molecules))

        population = best_smiles + new_molecules


if __name__ == "__main__":
    evolution_loop()
