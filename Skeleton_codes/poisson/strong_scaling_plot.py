import matplotlib.pyplot as plt
import numpy as np

# Data: Number of processes and corresponding total runtimes
num_processes = [1, 2, 4, 8, 16]
total_runtime = [0.621116, 0.396502, 0.198913, 0.102915, 0.053351]

# Plot the data on a log-log scale
plt.figure(figsize=(8, 6))
plt.loglog(num_processes, total_runtime, marker='o', linestyle='-', color='b', linewidth=2, markersize=8, label="Total Runtime")

# Add labels and title
plt.xlabel("Number of Processes (log scale)", fontsize=12)
plt.ylabel("Total Runtime (seconds, log scale)", fontsize=12)
plt.title("Strong Scaling: Total Runtime vs Number of Processes", fontsize=14)

# Customize the x-axis ticks to display the number of processes
plt.xticks(num_processes, [str(p) for p in num_processes], fontsize=10)
plt.yticks(fontsize=10)

# Add a legend
plt.legend(fontsize=12, loc="upper right")

# Add grid for better visualization
plt.grid(which="both", linestyle="--", linewidth=0.5)

# Add data labels for clarity
for i, txt in enumerate(total_runtime):
    plt.annotate(f"{txt:.3f}", (num_processes[i], total_runtime[i]), textcoords="offset points", xytext=(0, 10), ha='center')

# Save the plot to a file (optional)
plt.savefig("strong_scaling_loglog.png", dpi=300, bbox_inches='tight')

# Show the plot
plt.show()
