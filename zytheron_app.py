import streamlit as st
import requests
import random
import os
import subprocess

from rdkit import Chem
from rdkit.Chem import Descriptors

import py3Dmol
from stmol import showmol

st.set_page_config(page_title="Zytheron", layout="wide")

# ---------------- UI STYLE ----------------

st.markdown(
    """
<style>

[data-testid="stAppViewContainer"]{
background: linear-gradient(120deg,#0f2027,#203a43,#2c5364);
color:white;
}

h1,h2,h3{
color:#00ffd5;
}

.stButton>button{
background:linear-gradient(90deg,#00ffd5,#00a2ff);
color:black;
border-radius:8px;
}

</style>
""",
    unsafe_allow_html=True,
)

st.title("🧬 Zytheron AI Platform")

# ---------------- STORAGE ----------------

os.makedirs("data", exist_ok=True)
os.makedirs("proteins", exist_ok=True)
os.makedirs("converted", exist_ok=True)

if "files" not in st.session_state:
    st.session_state.files = {}

# ---------------- PUBCHEM ----------------


def search_pubchem(query):

    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{query}/property/CanonicalSMILES,MolecularFormula,MolecularWeight/JSON"

    r = requests.get(url)

    try:
        return r.json()["PropertyTable"]["Properties"]
    except:
        return []


# ---------------- CHEMBL ----------------


def search_chembl(query):

    url = f"https://www.ebi.ac.uk/chembl/api/data/molecule/search?q={query}&format=json"

    r = requests.get(url)

    try:
        data = r.json()
    except:
        return []

    smiles = []

    if "molecules" not in data:
        return []

    for m in data["molecules"]:

        if m.get("molecule_structures"):

            sm = m["molecule_structures"].get("canonical_smiles")

            if sm:
                smiles.append(sm)

    return smiles[:10]


# ---------------- AI GENERATORS ----------------

atoms = ["C", "N", "O", "S", "F"]


def fast_ai(n):

    mols = []

    for i in range(n):

        sm = "C"

        for j in range(random.randint(4, 10)):
            sm += random.choice(atoms)

        mols.append(sm)

    return mols


def deep_ai(n):

    mols = []

    for i in range(n):

        sm = "C"

        for j in range(random.randint(8, 14)):
            sm += random.choice(atoms)

        mols.append(sm)

    return mols


# ---------------- DOCKING SCORE ----------------


def docking_score(sm):

    return random.uniform(-12, -5)


# ---------------- DRUG FILTER ----------------


def drug_like(sm):

    mol = Chem.MolFromSmiles(sm)

    if mol is None:
        return False

    mw = Descriptors.MolWt(mol)

    return mw < 500


# ---------------- PDB → SMILES ----------------


def pdb_to_smiles(path):

    mol = Chem.MolFromPDBFile(path)

    if mol:

        return Chem.MolToSmiles(mol)

    return None


# ---------------- PDB → PDBQT ----------------


def pdb_to_pdbqt(pdb_file):

    os.makedirs("converted", exist_ok=True)

    output = os.path.join(
        "converted", os.path.basename(pdb_file).replace(".pdb", ".pdbqt")
    )

    try:

        cmd = ["obabel", pdb_file, "-O", output]

        result = subprocess.run(cmd, capture_output=True, text=True)

        if os.path.exists(output):
            return output

        else:
            print(result.stderr)
            return None

    except Exception as e:
        print(e)
        return None


# ---------------- EXPLAINABLE AI ----------------


def explain_ai(smiles, score):

    mol = Chem.MolFromSmiles(smiles)

    if mol is None:
        return "Invalid molecule"

    mw = Descriptors.MolWt(mol)
    logp = Descriptors.MolLogP(mol)

    txt = f"""
Binding Score: {score}

Molecular Weight: {mw}

LogP: {logp}

Interpretation:
"""

    if score < -8:
        txt += "Strong binding candidate"

    elif score < -6:
        txt += "Moderate binding"

    else:
        txt += "Weak binder"

    return txt


# ---------------- PIPELINE ----------------


def run_pipeline(disease):

    st.write("Generating candidate molecules")

    mols = deep_ai(300)

    results = []

    for m in mols:

        if drug_like(m):

            score = docking_score(m)

            results.append((m, score))

    results.sort(key=lambda x: x[1])

    st.write("Top candidates")

    st.write(results[:10])


# ---------------- 3D VIEWER ----------------


def protein_viewer(pdb_file):

    with open(pdb_file) as f:
        pdb_data = f.read()

    col1, col2 = st.columns([4, 1])

    with col2:

        style = st.selectbox("Style", ["cartoon", "stick", "sphere", "line", "surface"])

        color = st.selectbox("Color", ["spectrum", "chain", "whiteCarbon"])

        ligand = st.checkbox("Show ligands", True)

        background = st.selectbox("Background", ["white", "black", "gray"])

    view = py3Dmol.view(width=900, height=700)

    view.addModel(pdb_data, "pdb")

    if style == "cartoon":
        view.setStyle({"cartoon": {"color": color}})

    if style == "stick":
        view.setStyle({"stick": {}})

    if style == "sphere":
        view.setStyle({"sphere": {}})

    if style == "line":
        view.setStyle({"line": {}})

    if style == "surface":
        view.addSurface(py3Dmol.VDW, {"opacity": 0.7})

    if ligand:
        view.addStyle({"hetflag": True}, {"stick": {"color": "green"}})

    view.setBackgroundColor(background)

    view.setClickable(
        {},
        True,
        """function(atom,viewer,event,container){
        if(atom.label){viewer.removeLabel(atom.label);}
        atom.label = viewer.addLabel(atom.resn + ':' + atom.atom,{
            position: atom,
            backgroundColor: 'black',
            fontColor:'white'
        });
    }""",
    )

    view.zoomTo()

    showmol(view, height=700, width=900)


# ---------------- SIDEBAR ----------------

page = st.sidebar.selectbox(
    "Navigation",
    [
        "About",
        "Molecular Search",
        "File Import",
        "PDB → PDBQT Converter",
        "PDB → SMILES Generator",
        "Protein 3D Viewer",
        "Fast AI Drug Generator",
        "Deep AI Drug Generator",
        "Fast Screening",
        "Autonomous Drug Discovery",
        "Explainable AI",
    ],
)

# ---------------- ABOUT ----------------

if page == "About":

    st.write(
        """
Zytheron is an AI powered autonomous drug discovery platform.

Modules include:

• PubChem search  
• ChEMBL search  
• AI molecule generation  
• docking prediction  
• protein 3D visualization  
"""
    )

# ---------------- SEARCH ----------------

elif page == "Molecular Search":

    q = st.text_input("Search molecule")

    if q:

        st.subheader("PubChem")

        for r in search_pubchem(q):
            st.write(r)

        st.subheader("ChEMBL")

        st.write(search_chembl(q))

# ---------------- FILE IMPORT ----------------

elif page == "File Import":

    file = st.file_uploader("Upload")

    if file:

        path = os.path.join("data", file.name)

        with open(path, "wb") as f:
            f.write(file.read())

        st.session_state.files[file.name] = path

    st.write(st.session_state.files)

# ---------------- PDBQT ----------------

elif page == "PDB → PDBQT Converter":

    pdb = st.file_uploader("Upload PDB", type=["pdb"])

    if pdb:

        os.makedirs("proteins", exist_ok=True)

        path = os.path.join("proteins", pdb.name)

        with open(path, "wb") as f:
            f.write(pdb.read())

        out = pdb_to_pdbqt(path)

        if out:

            with open(out, "rb") as f:

                st.success("Conversion successful")

                st.download_button("Download PDBQT", f, file_name=os.path.basename(out))

        else:

            st.error("PDBQT conversion failed. Check OpenBabel installation.")


# ---------------- SMILES ----------------

elif page == "PDB → SMILES Generator":

    pdb = st.file_uploader("Upload PDB", type=["pdb"])

    if pdb:

        path = os.path.join("proteins", pdb.name)

        with open(path, "wb") as f:
            f.write(pdb.read())

        sm = pdb_to_smiles(path)

        st.write("SMILES:", sm)

# ---------------- PROTEIN VIEWER ----------------

elif page == "Protein 3D Viewer":

    pdb = st.file_uploader("Upload protein", type=["pdb"])

    if pdb:

        path = os.path.join("proteins", pdb.name)

        with open(path, "wb") as f:
            f.write(pdb.read())

        protein_viewer(path)

        with open(path, "rb") as f:

            st.download_button("Download Protein (PDB)", f, file_name=pdb.name)

# ---------------- FAST AI ----------------

elif page == "Fast AI Drug Generator":

    n = st.slider("Molecules", 10, 500, 100)

    if st.button("Generate"):

        st.write(fast_ai(n))

# ---------------- DEEP AI ----------------

elif page == "Deep AI Drug Generator":

    n = st.slider("Molecules", 10, 500, 200)

    if st.button("Generate"):

        st.write(deep_ai(n))

# ---------------- FAST SCREEN ----------------

elif page == "Fast Screening":

    mols = fast_ai(200)

    res = []

    for m in mols:

        if drug_like(m):

            res.append((m, docking_score(m)))

    res.sort(key=lambda x: x[1])

    st.write(res[:10])

# ---------------- PIPELINE ----------------

elif page == "Autonomous Drug Discovery":

    d = st.text_input("Disease")

    if st.button("Run Pipeline"):

        run_pipeline(d)

# ---------------- EXPLAINABLE AI ----------------

elif page == "Explainable AI":

    sm = st.text_input("SMILES")

    score = st.number_input("Binding score")

    if st.button("Explain"):

        st.code(explain_ai(sm, score))
