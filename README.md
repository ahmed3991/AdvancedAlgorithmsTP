
# Python Project Setup Guide

This guide explains how to set up a Python environment, configure VSCode, and measure time and space complexity for your project. It includes a decorator for automatic time and memory profiling for future use.

## Table of Contents
- [1. Setting Up a Virtual Environment](#1-setting-up-a-virtual-environment)
- [2. Configuring VSCode with the Virtual Environment](#2-configuring-vscode-with-the-virtual-environment)
- [3. Measuring Time and Space Complexity](#3-measuring-time-and-space-complexity)
  - [Time Complexity](#time-complexity)
  - [Space Complexity](#space-complexity)
- [4. Automatic Time and Space Profiling with a Decorator](#4-automatic-time-and-space-profiling-with-a-decorator)

## 1. Setting Up a Virtual Environment

### Step 1: Install `virtualenv`
Install `virtualenv` if it's not already installed:
```bash
pip install virtualenv
```

### Step 2: Create a Virtual Environment
Create a virtual environment for your project:
```bash
virtualenv venv
```

Replace `venv` with the desired name for your environment.

### Step 3: Activate the Virtual Environment
Activate the environment:

- On **Windows**:
  ```bash
  .\venv\Scripts\activate
  ```
- On **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

### Step 4: Deactivate the Environment
When done, deactivate the environment:
```bash
deactivate
```

---

## 2. Configuring VSCode with the Virtual Environment

### Step 1: Open VSCode
Launch VSCode and open your project folder.

### Step 2: Select the Python Interpreter
1. Press `Ctrl + Shift + P` to open the command palette.
2. Type `Python: Select Interpreter` and select the virtual environment you created (`env_name`).

This ensures VSCode uses the correct Python environment for running your code.

---

## 3. Measuring Time and Space Complexity

### Time Complexity
To measure the time complexity of a function, use Python’s `time` module:
```python
import time

def example_function():
    start_time = time.time()
    # A dummy function to simulate processing
    return sum([i ** 2 for i in range(n)])
    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")
```

### Space Complexity
To measure memory usage, use the `memory-profiler` library.

#### Step 1: Install `memory-profiler`
```bash
pip install memory-profiler
```

#### Step 2: Use the `@profile` Decorator
Apply the `@profile` decorator to your function:
```python
from memory_profiler import profile

@profile
def example_function():
    # A dummy function to simulate processing
    return sum([i ** 2 for i in range(n)])
```

#### Step 3: Run the Profiler
Run the script using:
```bash
python -m memory_profiler your_script.py
```

---

## 4. Automatic Time and Space Profiling with a Decorator

To automatically measure time and space complexity in your next project, use this custom decorator:

```python
from memory_profiler import memory_usage
import time

def time_and_space_profiler(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        mem_before = memory_usage()[0]

        result = func(*args, **kwargs)

        mem_after = memory_usage()[0]
        end_time = time.time()

        print(f"Execution time: {end_time - start_time} seconds")
        print(f"Memory usage: {mem_after - mem_before} MiB")

        return result
    return wrapper

# Example usage:
@time_and_space_profiler
def example_function():
    # A dummy function to simulate processing
    return sum([i ** 2 for i in range(n)])

# Test the decorator
example_function(1000000)
```

This decorator can be applied to any function to automatically report time and memory usage when the function is run.

---

### Next Steps
In your upcoming projects, you will use the above setup and tools to work efficiently with Python and measure both time and space complexity of your code. Happy coding!
