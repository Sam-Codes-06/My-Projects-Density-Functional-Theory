import numpy as np

# Define high-symmetry points
k_points = np.array([
    [0.000, 0.000, 0.000],  # G
    [0.500, 0.000, 0.500],  # X
    [0.625, 0.250, 0.625],  # U
    [0.375, 0.375, 0.750],  # K
    [0.000, 0.000, 0.000],  # G
    [0.500, 0.500, 0.500],  # L
    [0.500, 0.250, 0.750],  # W
    [0.500, 0.250, 0.750],  # X (repeated)
])

distances = [0.0]

# Calculate distances between consecutive points
for i in range(1, len(k_points)):
    delta_k = k_points[i] - k_points[i - 1]
    dist = np.linalg.norm(delta_k)
    distances.append(distances[-1] + dist)

# Print the cumulative distances
for i, d in enumerate(distances):
    print(f"Point {i + 1}: x = {d:.4f}")