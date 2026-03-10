import torch
import torch.nn as nn
from rdkit import Chem
from rdkit import RDLogger

RDLogger.DisableLog("rdApp.*")


class GNN(nn.Module):

    def __init__(self):
        super().__init__()

        self.fc1 = nn.Linear(10, 32)
        self.fc2 = nn.Linear(32, 16)
        self.fc3 = nn.Linear(16, 1)

    def forward(self, x):

        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)

        return x


model = GNN()


def featurize(smiles):

    mol = Chem.MolFromSmiles(smiles)

    # invalid molecule check
    if mol is None:
        return torch.zeros(10)

    atoms = [a.GetAtomicNum() for a in mol.GetAtoms()]

    features = atoms[:10]

    while len(features) < 10:
        features.append(0)

    return torch.tensor(features, dtype=torch.float32)


def predict_binding(smiles):

    x = featurize(smiles)

    with torch.no_grad():

        pred = model(x)

    return -abs(float(pred))
