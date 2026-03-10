import requests


def search_chembl(query):

    url = f"https://www.ebi.ac.uk/chembl/api/data/molecule/search?q={query}&format=json"

    r = requests.get(url)

    if r.status_code != 200:
        return []

    try:
        data = r.json()
    except:
        return []

    results = []

    if "molecules" in data:

        for m in data["molecules"][:10]:

            if "molecule_structures" in m:

                sm = m["molecule_structures"]["canonical_smiles"]

                results.append(sm)

    return results
