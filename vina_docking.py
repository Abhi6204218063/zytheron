import subprocess
import os


def run_vina(receptor, ligand_pdbqt):

    config = "vina_config.txt"

    cmd = [
        "vina",
        "--receptor",
        receptor,
        "--ligand",
        ligand_pdbqt,
        "--config",
        config,
        "--out",
        "docked.pdbqt",
    ]

    subprocess.run(cmd)

    score = None

    with open("docked.pdbqt") as f:
        for line in f:
            if "REMARK VINA RESULT" in line:
                score = float(line.split()[3])
                break

    return score
