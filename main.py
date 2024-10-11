import math
import algos
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import threading
import time
import asyncio

sizes = [10, 100, 1000, 10000]
samples = 30
sem_df = threading.Semaphore()
c_dataframe = pd.DataFrame()
t_dataframe = pd.DataFrame()
m_dataframe = pd.DataFrame()

def runner(func, arrays, xs):
    comparisons = []
    times = []
    memory = []
    for i in range(samples):
        result = func(arrays[i], xs[i])
        comparisons.append(result[0])
        times.append(result[1])
        memory.append(result[2])
    sem_df.acquire()
    c_dataframe[f"{func.__name__}_{len(arrays[0])}"] = comparisons
    t_dataframe[f"{func.__name__}_{len(arrays[0])}"] = times
    m_dataframe[f"{func.__name__}_{len(arrays[0])}"] = memory
    sem_df.release()

def main():
    fig, axs = plt.subplots(3)
    plots = []
    for size in sizes:
        lists = []
        xs = []
        for _ in range(samples):
            lists.append(
               np.sort(np.random.randint(0, size * 10, size)).tolist()
            )
            xs.append(np.random.randint(-2 * math.log2(size), 10 * size + 2 * math.log2(size)))

        threads = []
        for func in [algos.SequentialSearch, algos.SequentialSearchOptimized, algos.BinarySearch, algos.BinarySearchRecursive]:
            thread = threading.Thread(target=runner, args=(func, lists, xs))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    for func in [algos.SequentialSearch, algos.SequentialSearchOptimized, algos.BinarySearch, algos.BinarySearchRecursive]:
        # axs[0].set_yscale('log', base=10)
        yc_arr = []
        yt_arr = []
        ym_arr = []
        for i, s in enumerate(sizes):
            yc_arr.append(np.log10(c_dataframe[f"{func.__name__}_{s}"].mean()))
            yt_arr.append(t_dataframe[f"{func.__name__}_{s}"].mean())
            ym_arr.append(m_dataframe[f"{func.__name__}_{s}"].mean())
        plot_t, = axs[0].plot(range(4), yc_arr, label=func.__name__)
        axs[1].plot(range(4), np.multiply(yt_arr, 1000), label=func.__name__)
        axs[2].plot(range(4), np.multiply(ym_arr, 1000), label=func.__name__)
        plots.append(plot_t)
    # axs[0].set_yticks(np.geomspace(c_dataframe.min().min(), c_dataframe.max().max(), 6))
    axs[0].autoscale(axis='y')
    axs[1].autoscale(axis='y')
    axs[2].autoscale(axis='y')
    axs[0].set_title("Comparisons")
    axs[1].set_title("Time (ms)")
    axs[2].set_title("Memory (KB)")
    plt.legend(plots, [p.get_label() for p in plots], loc="upper right")
    for ax in axs.flat:
        ax.set_xticks(range(4))  # Set the positions for the major ticks
        ax.set_xticklabels(['a', 'b', 'a', 'z'])  # Set the labels for the major ticks
        ax.minorticks_off()  # Disable minor ticks completely

        # Optionally: Use MaxNLocator to force integer major ticks (no fractions)
        ax.xaxis.set_major_locator(plt.MaxNLocator(integer=True))

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()