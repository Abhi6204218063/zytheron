import subprocess


def run_gpu_docking(receptor, ligands):

    results = []

    for lig in ligands:

        cmd = [
            "vina",
            "--receptor",
            receptor,
            "--ligand",
            lig,
            "--out",
            f"dock_{lig}.pdbqt",
        ]

        subprocess.run(cmd)

        results.append(f"dock_{lig}.pdbqt")

    return results
