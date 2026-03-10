import os
import csv


# Results directory
RESULT_DIR = "results"


def ensure_result_dir():
    """
    Create results folder if it does not exist
    """
    if not os.path.exists(RESULT_DIR):
        os.makedirs(RESULT_DIR)


def export_csv(filename, data):
    """
    Export results to CSV file
    """

    ensure_result_dir()

    path = os.path.join(RESULT_DIR, filename)

    with open(path, "w", newline="", encoding="utf-8") as f:

        writer = csv.writer(f)

        for row in data:

            if isinstance(row, (list, tuple)):
                writer.writerow(row)
            else:
                writer.writerow([row])

    print(f"Exported: {path}")


def export_txt(filename, data):
    """
    Export results to TXT file
    """

    ensure_result_dir()

    path = os.path.join(RESULT_DIR, filename)

    with open(path, "w", encoding="utf-8") as f:

        for row in data:

            if isinstance(row, (list, tuple)):
                f.write(", ".join(map(str, row)) + "\n")
            else:
                f.write(str(row) + "\n")

    print(f"Exported: {path}")
