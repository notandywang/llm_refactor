import subprocess
import time

THREADS = [1, 2, 4, 8]
INPUT = 20_000_000
REPEATS = 2

def benchmark(exe):
    times = []
    for t in THREADS:
        for _ in range(REPEATS):
            start = time.time_ns()
            subprocess.run([exe, str(INPUT)], stdout=subprocess.DEVNULL)
            end = time.time_ns()
            times.append(end - start)
    return sum(times) / len(times)
