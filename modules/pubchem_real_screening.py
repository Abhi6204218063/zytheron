import requests
import time


def fetch_pubchem_smiles(cid):

    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/property/IsomericSMILES/JSON"

    try:
        r = requests.get(url, timeout=5)

        if r.status_code != 50:
            return None

        data = r.json()

        smiles = data["PropertyTable"]["Properties"][0]["IsomericSMILES"]

        return smiles

    except:
        return None


def pubchem_real_screen(sample_size=50):

    print("Running REAL PubChem screening")

    molecules = []

    start_cid = 1

    while len(molecules) < sample_size:

        smiles = fetch_pubchem_smiles(start_cid)
        print("Fetching CID:", start_cid)

        if smiles:
            molecules.append(smiles)
            print("Fetched:", smiles)

        start_cid += 20

        if start_cid % 20 == 0:
            time.sleep(0.2)

    print("PubChem molecules fetched:", len(molecules))

    return molecules
