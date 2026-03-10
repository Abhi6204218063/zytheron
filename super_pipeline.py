import os
from rdkit import RDLogger

RDLogger.DisableLog("rdApp.*")

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

print("====================================")
print("EVOTHERA MASTER DRUG DISCOVERY PIPELINE")
print("====================================")


# ------------------------------------------------
# SAFE IMPORT FUNCTION
# ------------------------------------------------


def safe_import(module, func):

    try:
        mod = __import__(module, fromlist=[func])
        return getattr(mod, func)

    except Exception as e:

        print(f"Skipping {module}.{func} -> {e}")
        return None


# ------------------------------------------------
# IMPORT MODULES
# ------------------------------------------------

read_smi = safe_import("modules.import_manager", "read_smi")
read_fasta = safe_import("modules.import_manager", "read_fasta")

generate_diffusion_molecules = safe_import(
    "modules.diffusion_drug_generator", "generate_diffusion_molecules"
)

massive_screening = safe_import("modules.massive_screening", "massive_screening")

predict_binding = safe_import("modules.ai_binding_predictor", "predict_binding")

simulate_future_proteins = safe_import(
    "modules.future_protein_simulator", "simulate_future_proteins"
)

simulate_resistance_landscape = safe_import(
    "modules.resistance_landscape", "simulate_resistance_landscape"
)

run_evolution_trap = safe_import("modules.evolution_trap_engine", "run_evolution_trap")

tumor_digital_twin = safe_import(
    "modules.tumor_digital_twin", "simulate_tumor_response"
)

detect_active_sites = safe_import("modules.active_site_ai", "detect_active_sites")

gpu_md = safe_import("modules.openmm_gpu_md", "run_md_simulation")

run_real_docking = safe_import("modules.real_docking_engine", "run_real_docking")

export_csv = safe_import("modules.export_manager", "export_csv")

export_txt = safe_import("modules.export_manager", "export_txt")

multi_target_screen = safe_import(
    "modules.multi_target_cancer_engine", "multi_target_screen"
)

autonomous_ai = safe_import(
    "modules.autonomous_drug_discovery", "autonomous_drug_discovery"
)
self_improving_engine = safe_import("modules.self_improving_ai", "self_improving_ai")


# ------------------------------------------------
# HELPER FUNCTIONS
# ------------------------------------------------


def load_protein():

    try:
        with open("proteins/protein.pdb") as f:
            return f.read()
    except:
        print("Protein file not found")
        return None


def rank_drugs(drugs):

    print("Ranking final drugs")

    try:
        return sorted(drugs, key=lambda x: x[1])
    except:
        return drugs


# ------------------------------------------------
# MAIN PIPELINE
# ------------------------------------------------


def run_pipeline():

    print("\nStarting Zytheron AI pipeline")

    # ------------------------------
    # LOAD PROTEIN
    # ------------------------------

    protein = load_protein()

    # ------------------------------
    # LOAD PUBCHEM MOLECULES
    # ------------------------------

    print("\nLoading input molecules")

    from modules.pubchem_real_screening import pubchem_real_screen

    molecules = pubchem_real_screen(300)

    if read_fasta:
        protein_sequence = read_fasta("uploads/proteins/protein.fasta")
    else:
        protein_sequence = "MKTFVLLLCTFTWAS"

    print("Molecules loaded:", len(molecules))
    print("Protein length:", len(protein_sequence))

    # ------------------------------
    # DIFFUSION GENERATOR
    # ------------------------------

    if generate_diffusion_molecules:

        print("\nRunning diffusion molecule generator")

        molecules = generate_diffusion_molecules(500)

        print("Diffusion molecules generated:", len(molecules))

    # ------------------------------
    # MASSIVE SCREENING
    # ------------------------------

    if massive_screening:

        print("\nRunning massive screening")

        molecules = massive_screening(molecules)

        print("Selected molecules:", len(molecules))

    # ------------------------------
    # FIX MOLECULE FORMAT
    # ------------------------------

    clean_molecules = []

    for m in molecules:

        if isinstance(m, tuple):
            clean_molecules.append(m[0])

        elif isinstance(m, list):
            clean_molecules.append(m[0])

        else:
            clean_molecules.append(m)

    molecules = clean_molecules

    # ------------------------------
    # BINDING PREDICTION
    # ------------------------------

    if predict_binding:

        print("\nRunning AI binding predictor")

        scored = predict_binding(molecules)

    else:

        scored = [(m, 0) for m in molecules]

    # ------------------------------
    # SELECT TOP MOLECULES
    # ------------------------------

    print("\nSelecting top molecules")

    top_molecules = sorted(scored, key=lambda x: x[1])[:20]

    print("Top molecules:", len(top_molecules))

    cancer_targets = ["EGFR", "KRAS", "BRAF", "PI3K", "MEK"]

    if multi_target_screen:

        print("\nRunning Multi-Target Cancer Therapy")

        top_molecules = multi_target_screen(top_molecules, cancer_targets)

    # ------------------------------
    # FUTURE PROTEIN MUTATIONS
    # ------------------------------

    if simulate_future_proteins:

        print("\nSimulating future protein variants")

        future_proteins = simulate_future_proteins(protein_sequence)

    else:

        future_proteins = [protein_sequence]

    # ------------------------------
    # RESISTANCE LANDSCAPE
    # ------------------------------

    if simulate_resistance_landscape:

        print("\nMapping resistance landscape")

        simulate_resistance_landscape(top_molecules, future_proteins, predict_binding)

    # ------------------------------
    # EVOLUTION TRAP
    # ------------------------------

    if run_evolution_trap:

        print("\nRunning Evolution Trap Engine")

        final_drugs = run_evolution_trap(
            top_molecules, protein_sequence, predict_binding
        )

    else:

        final_drugs = top_molecules

    # ------------------------------
    # ACTIVE SITE + DOCKING
    # ------------------------------

    print("\nDetecting protein active site")

    if detect_active_sites:
        active_site = detect_active_sites("proteins/protein.pdb")

    print("\nRunning real protein docking")

    if run_real_docking:

        docking_results = run_real_docking([x[0] for x in final_drugs])

    # ------------------------------
    # TUMOR DIGITAL TWIN
    # ------------------------------

    if tumor_digital_twin:

        print("\nRunning Tumor Digital Twin")

        tumor_digital_twin(final_drugs)

    # ------------------------------
    # GPU MOLECULAR DYNAMICS
    # ------------------------------

    if gpu_md:

        print("\nRunning GPU Molecular Dynamics")

        gpu_md(final_drugs)

    # ------------------------------
    # FINAL RANKING
    # ------------------------------

    final_drugs = rank_drugs(final_drugs)

    # ------------------------------
    # EXPORT RESULTS
    # ------------------------------

    print("\nExporting results")

    if export_csv:
        export_csv("results/final_drugs.csv", final_drugs)

    if export_txt:
        export_txt("results/final_drugs.txt", final_drugs)

    print("\nResults saved in:")
    print("results/final_drugs.csv")
    print("results/final_drugs.txt")

    print("\n====================================")
    print("EVOTHERA MASTER PIPELINE COMPLETE")
    print("====================================")

    return final_drugs


# --------------------------------
# AUTONOMOUS AI DRUG DISCOVERY
# --------------------------------

if autonomous_ai:

    print("\nLaunching Autonomous AI Drug Discovery")

    if read_fasta:
        protein_sequence = read_fasta("uploads/proteins/protein.fasta")
    else:
        protein_sequence = "MKTFVLLLCTFTWAS"

    best_drug = autonomous_ai(
        protein_sequence,
        generate_diffusion_molecules,
        massive_screening,
        predict_binding,
        run_real_docking,
        run_evolution_trap,
        tumor_digital_twin,
    )

    print("\nAI Discovered Drug:", best_drug)

    # --------------------------------
# SELF IMPROVING AI ENGINE
# --------------------------------

if self_improving_engine:

    print("\nLaunching Self Improving AI")

    best_drug = self_improving_engine(
        protein_sequence,
        generate_diffusion_molecules,
        massive_screening,
        predict_binding,
        run_real_docking,
        run_evolution_trap,
        tumor_digital_twin,
    )

    print("\nSelf-Improving AI Drug:", best_drug)


# ------------------------------------------------
# RUN DIRECTLY
# ------------------------------------------------

if __name__ == "__main__":

    run_pipeline()
