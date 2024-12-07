import matplotlib.pyplot as plt

import numpy as np

class ComplexityVisualizer:
    def __init__(self, x: np.ndarray, y: np.ndarray, complexity_functions: list):
        """
        Initialize the ComplexityVisualizer.
        :param x: Input sizes.
        :param y: Measured execution times.
        :param complexity_functions: List of complexity functions to evaluate.
        """
        self.x = x
        self.y = y
        self.complexity_functions = complexity_functions

    def plot(self, best_fit_function: str,title: str = "Complexity Function Fit"):
        """
        Plot the data points and complexity functions.
        :param best_fit_function: Name of the best-fitting complexity function.
        """
        plt.figure(figsize=(10, 6))
        
        # Scatter plot of the original data
        plt.scatter(self.x, self.y, color="blue", label="Data points", s=50, zorder=5)
        
        # Plot all complexity functions
        for func in self.complexity_functions:
            y_pred = func.evaluate(self.x)
            plt.plot(self.x, y_pred, label=func.name(), linestyle="--", alpha=0.7)

        # Highlight the best-fitting function
        best_function = next(f for f in self.complexity_functions if f.name() == best_fit_function)
        plt.plot(self.x, best_function.evaluate(self.x), color="red", label=f"Best fit: {best_fit_function}", linewidth=2)

        # Customize the chart
        plt.title(title, fontsize=16)
        plt.xlabel("Input Size (x)", fontsize=14)
        plt.ylabel("Execution Time (y)", fontsize=14)
        plt.grid(alpha=0.3)
        plt.legend(fontsize=12)
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)

        # Show the chart
        plt.tight_layout()
        plt.show()

class ComplexityDashboardVisualizer:
    def __init__(self, grouped_data, complexity_analyzer, feature_to_draw = 'time'):
        """
        Initialize the ComplexityDashboardVisualizer.
        :param grouped_data: Grouped DataFrame containing the benchmark results.
        :param complexity_analyzer: An instance of ComplexityAnalyzer to determine the best fit complexity.
        """
        self.grouped_data = grouped_data
        self.feature_to_draw = feature_to_draw
        self.complexity_analyzer = complexity_analyzer


    def plot_dashboard(self):
        # Define the grid size for the dashboard (adjust rows and columns based on the number of algorithms and data types)
        num_algorithms = len(self.grouped_data['algorithm'].unique())
        num_data_types = len(self.grouped_data['data_type'].unique())
        
        # Create subplots
        fig, axes = plt.subplots(num_algorithms, num_data_types, figsize=(18, 12))
        plt.subplots_adjust(hspace=0.3, wspace=0.3)  # Adjust spacing between plots

        # Loop through each algorithm and data_type to create the respective plots
        for i, (algorithm, group_by_algorithm) in enumerate(self.grouped_data.groupby('algorithm')):
            for j, (data_type, group_by_data_type) in enumerate(group_by_algorithm.groupby('data_type')):
                # Extract the input sizes and time values for fitting
                x = group_by_data_type['size'].values
                y = group_by_data_type[self.feature_to_draw].values

                # Get the best-fit complexity function for time
                best_fit_function_name, best_fit_function = self.complexity_analyzer.get_best_fit(x, y)

                # Plot the data points and complexity functions
                ax = axes[i, j]  # Select the subplot for the current combination
                ax.scatter(x, y, color="blue", label="Data points", s=50)
                
                # Plot all complexity functions
                for func in self.complexity_analyzer.complexity_functions:
                    y_pred = func.evaluate(x)
                    ax.plot(x, y_pred, label=func.name(), linestyle="--", alpha=0.7)

                # Highlight the best-fitting function
                #best_function = next(f for f in self.complexity_analyzer.complexity_functions if f.name() == best_fit_function_name)
                ax.plot(x, best_fit_function.evaluate(x), color="red", label=f"Best fit: {best_fit_function_name}", linewidth=2)

                # Set title and labels
                ax.set_title(f"{algorithm} - {data_type}", fontsize=14)
                ax.set_xlabel("Input Size (n)", fontsize=12)
                ax.set_ylabel(f"Execution {self.feature_to_draw} (s)", fontsize=12)
                ax.grid(alpha=0.3)
                ax.legend(fontsize=10)

        # Show the dashboard with all plots
        plt.show()