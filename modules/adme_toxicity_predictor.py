import random


def predict_adme(smiles):

    logp = random.uniform(0, 5)

    solubility = random.uniform(-6, 0)

    permeability = random.uniform(0, 1)

    return {"logP": logp, "solubility": solubility, "permeability": permeability}


def predict_toxicity(smiles):

    return random.uniform(0, 1)
