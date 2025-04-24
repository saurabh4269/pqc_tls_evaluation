"""
Tests for performance tools (stub).
"""
from src.performance.time_profiler import measure_time
from src.performance.memory_profiler import get_memory_usage
from src.performance.energy_profiler import measure_energy

def test_time_profiler():
    @measure_time
    def f():
        return sum(range(1000))
    _, t = f()
    assert t >= 0

def test_memory_profiler():
    mem = get_memory_usage()
    assert mem > 0

def test_energy_profiler():
    # Only check that the function runs (Linux/powerstat required)
    output = measure_energy("sleep 0.1", 1)
    assert isinstance(output, str)
