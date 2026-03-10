import subprocess


def run_docking():

    command = [
        "vina",
        "--receptor",
        "receptor.pdbqt",
        "--ligand",
        "ligand.pdbqt",
        "--center_x",
        "0",
        "--center_y",
        "0",
        "--center_z",
        "0",
        "--size_x",
        "20",
        "--size_y",
        "20",
        "--size_z",
        "20",
    ]

    subprocess.run(command)
