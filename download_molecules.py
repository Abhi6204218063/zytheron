import pubchempy as pcp

compounds = pcp.get_compounds("aspirin", "name")

with open("molecules.smi", "w") as f:
    for c in compounds:
        if c.isomeric_smiles:
            f.write(c.isomeric_smiles + "\n")

print("Molecule library created")
