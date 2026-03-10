import os
import subprocess


def run_real_docking(smiles_list, receptor="proteins/protein.pdbqt"):

    print("\nRunning REAL Protein Docking")

    results = []

    for i, smiles in enumerate(smiles_list):

        ligand_file = f"temp_ligand_{i}.pdbqt"
        output_file = f"docking_result_{i}.pdbqt"

        # Dummy ligand file creation (placeholder)
        with open(ligand_file, "w") as f:
            f.write("REMARK ligand placeholder\n")

        cmd = [
            "vina",
            "--receptor",
            receptor,
            "--ligand",
            ligand_file,
            "--center_x",
            "10",
            "--center_y",
            "10",
            "--center_z",
            "10",
            "--size_x",
            "20",
            "--size_y",
            "20",
            "--size_z",
            "20",
            "--out",
            output_file,
        ]

        try:
            subprocess.run(cmd, check=True)
            print("Docked:", smiles)
            results.append((smiles, output_file))

        except Exception as e:
            print("Docking failed:", e)

    return results
