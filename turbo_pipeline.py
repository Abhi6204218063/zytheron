from modules.diffusion_drug_generator import generate_diffusion_molecules
from modules.ai_binding_predictor import predict_binding


def run_turbo_pipeline():

    print("Running Zytheron Turbo AI Pipeline")

    molecules = generate_diffusion_molecules(30)

    scored = predict_binding(molecules)

    scored.sort(key=lambda x: x[1])

    top = scored[:10]

    print("\nTop AI Drug Candidates\n")

    for m in top:

        print(m)

    return top
