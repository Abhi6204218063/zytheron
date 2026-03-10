def extract_best_score(pdbqt_file):

    try:

        with open(pdbqt_file, "r") as f:

            lines = f.readlines()

        for line in lines:

            if line.strip().startswith("REMARK VINA RESULT"):

                parts = line.split()

                score = float(parts[3])

                return score

    except:
        return None

    return None
