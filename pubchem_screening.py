import pubchempy as pcp
from ai_binding_predictor import predict_binding


# -------------------------------
# Download molecules from PubChem
# -------------------------------


def get_pubchem_molecules(num=50):

    smiles_list = []

    print("Downloading molecules from PubChem...")

    for cid in range(1, 10000):

        try:
            compound = pcp.Compound.from_cid(cid)

            if compound is not None and compound.smiles is not None:
                smiles_list.append(compound.smiles)

        except:
            continue

        if len(smiles_list) >= num:
            break

    print("Downloaded molecules:", len(smiles_list))

    return smiles_list


# -------------------------------
# AI Screening
# -------------------------------


def screen_molecules():

    molecules = get_pubchem_molecules(50)

    results = []

    for m in molecules:

        score = predict_binding(m)

        results.append((m, score))

    results.sort(key=lambda x: x[1], reverse=True)

    print("\nTop molecules:")

    for r in results[:5]:
        print(r)


# -------------------------------
# Run
# -------------------------------

if __name__ == "__main__":

    screen_molecules()
