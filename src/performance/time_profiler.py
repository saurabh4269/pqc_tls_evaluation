"""
Time measurement utilities for performance evaluation.

Expanded: Add docstring and usage example for measure_time.
"""
import time

def measure_time(func):
    """
    Decorator to measure execution time of a function.
    Returns (result, elapsed_time).
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        elapsed = end - start
        return result, elapsed
    return wrapper

if __name__ == "__main__":
    @measure_time
    def example():
        time.sleep(0.1)
        return "done"
    res, t = example()
    print(f"Result: {res}, Time: {t:.4f}s")
