import subprocess
import pathlib
import csv
import config

from llm_generate import generate_code
from llm_optimize_prompt import optimize_prompt
from run_benchmark import benchmark

PROMPT = "Improve the performance of this code using parallelism."
prev_time = None

with open("results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["iteration", "avg_time_ns", "prompt"])

    for i in range(config.MAX_ITERATIONS):
        print(f"ITERATION {i}")

        cpp = f"gen_{i}.cpp"
        exe = f"gen_{i}.exe"

        # 1. Generate code (cached)
        generate_code(PROMPT, i)

        # 2. Compile
        subprocess.run(
            ["cl", "/O2", "/openmp", cpp, "/Fe:" + exe],
            check=True
        )

        # 3. Benchmark
        avg_time = benchmark(exe)
        writer.writerow([i, avg_time, PROMPT])
        f.flush()

        # 4. Early stop
        if prev_time is not None:
            improvement = (prev_time - avg_time) / prev_time
            if improvement < config.IMPROVEMENT_THRESHOLD:
                print("EARLY STOP: no significant improvement")
                break

        prev_time = avg_time

        # 5. Prompt optimization (1 call)
        PROMPT = optimize_prompt(PROMPT, f"avg_time={avg_time}", i)
