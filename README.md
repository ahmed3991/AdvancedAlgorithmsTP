# Complexity Analysis Library

A Python library for analyzing and visualizing algorithmic complexity. This library helps you determine the time and space complexity of your algorithms through empirical analysis.

Created by Master 1 students at University of El Oued, Algeria (2024/2025) as part of the Advanced Algorithms course.

## Features
- Analyze time complexity of algorithms
- Compare theoretical vs actual performance
- Visualize complexity curves
- Support for common complexity classes:
  - O(1) - Constant
  - O(log n) - Logarithmic
  - O(n) - Linear
  - O(n log n) - Linear-logarithmic
  - O(n²) - Quadratic

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd AdvancedAlgorithmsTP
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Quick Start

### 1. Basic Usage

```python
from complexity.analyser import ComplexityAnalyzer, LinearComplexity, QuadraticComplexity
from complexity.visualizer import ComplexityVisualizer
import numpy as np

# Generate sample data
sizes = np.array([10, 20, 30, 40, 50])
times = np.array([0.1, 0.4, 0.9, 1.6, 2.5])  # Example execution times

# Create analyzer with complexity functions
analyzer = ComplexityAnalyzer([
    LinearComplexity(),
    QuadraticComplexity()
])

# Find best fitting complexity
best_fit, score = analyzer.get_best_fit(sizes, times)
print(f"Best fitting complexity: {best_fit}")

# Visualize results
visualizer = ComplexityVisualizer(sizes, times)
visualizer.plot(best_fit, title="Algorithm Complexity Analysis")
```

### 2. Analyzing Sorting Algorithms

```python
from examples.sort_algos import bubble_sort
import numpy as np

# Generate test data
sizes = [100, 200, 300, 400, 500]
times = []

for n in sizes:
    data = np.random.randint(0, 1000, n)
    start_time = time.time()
    bubble_sort(data)
    times.append(time.time() - start_time)

# Create visualizer
visualizer = ComplexityVisualizer(np.array(sizes), np.array(times))
visualizer.plot(QuadraticComplexity(), title="Bubble Sort Complexity")
```

### 3. Custom Complexity Functions

```python
from complexity.analyser import ComplexityFunction

class CustomComplexity(ComplexityFunction):
    def calculate(self, n):
        return n * np.log(n)  # Example: O(n log n)
    
    def __str__(self):
        return "O(n log n)"

# Use custom complexity in analysis
analyzer = ComplexityAnalyzer([CustomComplexity()])
```

## Project Structure
- `complexity/` - Core library code
  - `analyser.py` - Complexity analysis tools
  - `visualizer.py` - Plotting and visualization
- `examples/` - Example algorithms
  - `search_algos.py` - Search algorithms
  - `sort_algos.py` - Sorting algorithms
- `TPs/` - Jupyter notebooks with analysis

## Contributing
Feel free to submit issues and enhancement requests!

## License
[Your chosen license]
