import time
import sys

print("\n==============================")
print(" EVOTHERA AUTONOMOUS AI LAB ")
print("==============================\n")

print("Initializing system...\n")

time.sleep(1)

try:

    from pipeline_drug_discovery import run_pipeline

except Exception as e:

    print("Error loading pipeline:")
    print(e)
    sys.exit()


def run_autonomous_lab():

    print("Starting autonomous drug discovery...\n")

    start_time = time.time()

    try:

        run_pipeline()

    except Exception as e:

        print("Pipeline failed:")
        print(e)
        return

    end_time = time.time()

    print("\n================================")
    print(" AUTONOMOUS LAB COMPLETED ")
    print("================================")

    print("Total runtime:", round(end_time - start_time, 2), "seconds")

    print("\nResults saved in:")
    print("results/evolution_scores.csv")
    print("results/evolution_scores.txt")


if __name__ == "__main__":

    run_autonomous_lab()
