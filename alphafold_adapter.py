import requests


def fetch_alphafold_structure(uniprot_id):

    url = f"https://alphafold.ebi.ac.uk/files/AF-{uniprot_id}-F1-model_v4.pdb"

    r = requests.get(url)

    if r.status_code == 200:

        file = f"{uniprot_id}.pdb"

        with open(file, "wb") as f:
            f.write(r.content)

        return file

    return None
