"""
Script to analyze and plot performance results.
"""
import pandas as pd
import matplotlib.pyplot as plt
import os

def plot_metric(csv_file, metric_name):
    if not os.path.exists(csv_file):
        print(f"{csv_file} not found.")
        return
    df = pd.read_csv(csv_file)
    df.plot(x='algorithm', y=metric_name, kind='bar', legend=False)
    plt.title(f'{metric_name} by Algorithm')
    plt.ylabel(metric_name)
    plt.xlabel('Algorithm')
    plt.tight_layout()
    plt.show()

def main():
    plot_metric('../results/time_results.csv', 'time')
    plot_metric('../results/energy_results.csv', 'energy')
    plot_metric('../results/memory_results.csv', 'memory')

if __name__ == '__main__':
    main()
