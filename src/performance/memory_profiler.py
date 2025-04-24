"""
Memory usage tracking using psutil.

Expanded: Add docstring and usage example for get_memory_usage.
"""
import psutil

def get_memory_usage():
    """
    Get current process memory usage (RSS in bytes).
    """
    process = psutil.Process()
    mem_info = process.memory_info()
    return mem_info.rss  # Resident Set Size in bytes

if __name__ == "__main__":
    print(f"Current memory usage: {get_memory_usage()} bytes")
