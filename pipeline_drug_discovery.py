import subprocess

from import_manager import read_smi, read_fasta
from export_manager import export_csv, export_txt

from ai_binding_predictor import predict_binding
from multi_future_protein_simulator import simulate_future_proteins
from evolution_steering_engine import run_evolution_steering


RECEPTOR = "receptor.pdbqt"


def run_pipeline():

    print("\nEVOTHERA Drug Discovery Pipeline\n")

    # -------------------------
    # Import molecules
    # -------------------------

    molecules = read_smi("uploads/molecules/drug.smi")

    print("Molecules loaded:", len(molecules))

    # -------------------------
    # Import protein
    # -------------------------

    protein_sequence = read_fasta("uploads/proteins/protein.fasta")

    print("Protein length:", len(protein_sequence))

    # -------------------------
    # AI Binding Prediction
    # -------------------------

    print("\nRunning AI binding predictor")

    scores = []

    for mol in molecules:

        try:

            score = predict_binding(mol)

            scores.append((mol, score))

        except:

            continue

    scores.sort(key=lambda x: x[1], reverse=True)

    top_molecules = scores[:10]

    print("\nTop AI molecules")

    for m in top_molecules:

        print(m)

    # -------------------------
    # Multi Future Protein Simulation
    # -------------------------

    print("\nSimulating future protein mutations")

    variants = simulate_future_proteins(protein_sequence, 20)

    for v in variants[:5]:

        print(v)

    # -------------------------
    # Evolution Steering
    # -------------------------

    print("\nRunning Evolution Steering Engine")

    best_molecules = [m[0] for m in top_molecules]

    steering_results = run_evolution_steering(
        best_molecules, protein_sequence, predict_binding
    )

    print("\nTop Evolution Resistant Drugs")

    for r in steering_results[:5]:

        print(r)

    # -------------------------
    # Export Results
    # -------------------------

    export_csv(steering_results, "evolution_scores.csv")

    export_txt(steering_results, "evolution_scores.txt")

    print("\nPipeline completed\n")


if __name__ == "__main__":

    run_pipeline()
