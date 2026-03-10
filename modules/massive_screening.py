import random


def massive_screening(molecules, threshold=0.3):
    """
    Simulates large scale screening of molecules.
    Filters molecules based on a fake probability score.
    """

    print("\nRunning Massive Screening Engine\n")

    screened = []

    for m in molecules:

        score = random.random()

        if score > threshold:
            screened.append(m)

    print("Input molecules:", len(molecules))
    print("Selected molecules:", len(screened))

    return screened


def run_massive_screening(molecules):
    """
    Wrapper function so pipeline can call either name
    """

    return massive_screening(molecules)
