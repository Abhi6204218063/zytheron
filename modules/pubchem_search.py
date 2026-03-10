import requests


def search_pubchem(query):

    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{query}/property/MolecularFormula,MolecularWeight,CanonicalSMILES/JSON"

    r = requests.get(url)

    if r.status_code != 200:
        return None

    data = r.json()

    results = []

    try:

        for item in data["PropertyTable"]["Properties"]:

            results.append(
                {
                    "formula": item["MolecularFormula"],
                    "weight": item["MolecularWeight"],
                    "smiles": item["CanonicalSMILES"],
                }
            )

    except:
        return None

    return results
