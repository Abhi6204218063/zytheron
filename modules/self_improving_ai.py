import random


def self_improving_ai(
    protein_sequence, generator, screening, binding, docking, evolution, tumor, cycles=6
):

    print("\n=================================")
    print("ZYTHERON SELF IMPROVING AI ENGINE")
    print("=================================")

    best_drug = None
    best_score = 999

    memory = []

    for cycle in range(cycles):

        print(f"\nAI Learning Cycle {cycle+1}")

        # -------------------------
        # Generate molecules
        # -------------------------

        molecules = generator(300)

        print("Generated:", len(molecules))

        # -------------------------
        # Screening
        # -------------------------

        molecules = screening(molecules)

        print("After screening:", len(molecules))

        # -------------------------
        # Binding prediction
        # -------------------------

        scored = binding(molecules)

        # -------------------------
        # Docking
        # -------------------------

        docking_results = docking([x[0] for x in scored])

        # -------------------------
        # Evolution resistance
        # -------------------------

        resistant = evolution(docking_results, protein_sequence, binding)

        # -------------------------
        # Tumor simulation
        # -------------------------

        tumor_scores = tumor(resistant)

        # -------------------------
        # Learning step
        # -------------------------

        for drug, score in tumor_scores:

            memory.append((drug, score))

            if score < best_score:

                best_score = score
                best_drug = drug

        print("Best score so far:", best_score)

        # -------------------------
        # AI improvement
        # -------------------------

        memory = sorted(memory, key=lambda x: x[1])[:50]

    print("\nFinal Best Drug:", best_drug)

    return best_drug
