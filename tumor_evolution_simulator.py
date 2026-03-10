import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def simulate_tumor_evolution(
    sensitive_cells=1000,
    resistant_cells=10,
    growth_rate_sensitive=0.03,
    growth_rate_resistant=0.025,
    mutation_rate=1e-5,
    drug_kill=0.04,
    steps=200,
):

    S = sensitive_cells
    R = resistant_cells

    history = []

    for t in range(steps):

        # growth
        S_growth = growth_rate_sensitive * S
        R_growth = growth_rate_resistant * R

        # mutation (sensitive → resistant)
        mutations = mutation_rate * S

        # drug killing sensitive cells
        drug_effect = drug_kill * S

        # update populations
        S = S + S_growth - drug_effect - mutations
        R = R + R_growth + mutations

        if S < 0:
            S = 0

        history.append((S, R, S + R))

    df = pd.DataFrame(
        history, columns=["Sensitive Cells", "Resistant Cells", "Total Tumor"]
    )

    return df


def plot_tumor_evolution(df):

    plt.figure(figsize=(8, 5))

    plt.plot(df["Sensitive Cells"], label="Sensitive")
    plt.plot(df["Resistant Cells"], label="Resistant")
    plt.plot(df["Total Tumor"], label="Total Tumor")

    plt.xlabel("Time")
    plt.ylabel("Cell Population")

    plt.legend()

    plt.title("Tumor Evolution Simulation")

    plt.show()
