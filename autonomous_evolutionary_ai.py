from modules.tumor_evolution_engine import evolve_tumor
from modules.drug_design_ai import design_drug
from modules.binding_predictor import predict_binding
from modules.resistance_predictor import predict_resistance
from modules.drug_evolution_engine import evolve_drug
from modules.tumor_response_simulator import simulate_response
from modules.explainable_ai import explain
from modules.compound_ranking import rank_drugs

results = []

for generation in range(200):

    tumor = evolve_tumor()

    drug = design_drug()

    drug = evolve_drug(drug)

    binding = predict_binding(drug)

    resistance = predict_resistance(tumor, drug)

    response = simulate_response(binding, resistance)

    explanation = explain(drug, tumor)

    score = (-binding) + response - resistance

    results.append(
        {
            "drug": drug,
            "tumor_profile": tumor,
            "binding": binding,
            "resistance": resistance,
            "tumor_response": response,
            "score": score,
            "explanation": explanation,
        }
    )


top = rank_drugs(results)

print("\nEvolution-Resistant Drug Candidates\n")

for r in top:
    print(r)
