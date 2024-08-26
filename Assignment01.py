import time

def echo(message):
    start_time = time.perf_counter()
    print(message)
    end_time = time.perf_counter()
    print(f"Execution time: (execution_time) seconds")

    from time import sleep, perf_counter_ns
    timePoint1 = perf_counter_ns()
    sleep(10)
    timePoint2 = perf_counter_ns()
    durationInMS = (timePoint2 - timePoint1) / 1000000
    print(f"Duration: {durationInMS} ms")

echo("Hello, World!")
