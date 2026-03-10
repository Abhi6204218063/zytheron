import random


def dock(smiles):

    score = random.uniform(-12, -6)

    pose = "predicted_binding_pose"

    return {"score": score, "pose": pose}
