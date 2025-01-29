import matplotlib.pyplot as plt
import numpy as np

# Grid sizes
grid_sizes = [8, 16, 32, 64, 128, 256, 512]

# Runtimes for each solver (replace with your extracted times)
petsc_times = [0.000037, 0.000037, 0.000066, 0.000181, 0.000655, 0.002643, 0.012645]
sp_direct_times = [0.000440, 0.000932, 0.003591, 0.027801, 0.099943, 0.687767, 5.110570]
cg_solver_times = [0.000702, 0.001586, 0.003798, 0.013081, 1.122691, 1.089890, 6.966102]
dense_direct_times = [0.064091, 0.083768, 0.096388, 0.495240, 30.785260, None, None]  # N/A for larger grids

# Plot
plt.figure(figsize=(8, 6))
plt.loglog(grid_sizes, petsc_times, 'o-', label='PETSc Solver')
plt.loglog(grid_sizes, sp_direct_times, 'o-', label='Sparse Direct Solver (Python)')
plt.loglog(grid_sizes, cg_solver_times, 'o-', label='CG Solver (Python)')
plt.loglog(grid_sizes[:-2], dense_direct_times[:-2], 'o-', label='Dense Direct Solver (Python)')

plt.xlabel('Grid Size (log scale)')
plt.ylabel('Runtime (seconds, log scale)')
plt.title('Performance Benchmark: Runtime vs Grid Size')
plt.legend()
plt.grid(True, which="both", ls="--")
plt.savefig('runtime_comparison_loglog.png')
plt.show()
