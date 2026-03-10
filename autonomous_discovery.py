from molecule_generator import generate_molecule
from ai_binding_predictor import predict_binding

print("Generating molecules...")

molecules = []

for i in range(50):

    sm = generate_molecule()

    if sm:
        molecules.append(sm)

results = []

for sm in molecules:

    score = predict_binding(sm)

    if score is not None:
        results.append((sm, score))

results = sorted(results, key=lambda x: x[1])

print("\nTop molecules:")

for r in results[:5]:
    print(r)
