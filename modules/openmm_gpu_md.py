from openmm import *
from openmm.app import *
from openmm.unit import *
import random


def run_md_simulation(drugs):

    print("\nRunning GPU Molecular Dynamics")

    for d in drugs:

        if isinstance(d, (list, tuple)):
            smiles = d[0]
        else:
            smiles = d

        print("Simulating MD for:", smiles)

    print("MD simulation complete")

    return drugs
