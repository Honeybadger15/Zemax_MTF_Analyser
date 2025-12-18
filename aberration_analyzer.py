import matplotlib.pyplot as plt
import pandas as pd

# Read file
df = pd.read_csv(
    r"MTF_Biconvex_data.txt",
    sep=r"\s+",
    header=None,
    names=["Frequency", "Sagittal", "Tangential"],
    encoding="utf-16",
    on_bad_lines='skip',
    skiprows=19
)

# Convert to numeric after reading
df['Frequency'] = pd.to_numeric(df['Frequency'].str.replace(',', '.'), errors='coerce')
df['Sagittal'] = pd.to_numeric(df['Sagittal'].str.replace(',', '.'), errors='coerce')
df['Tangential'] = pd.to_numeric(df['Tangential'].str.replace(',', '.'), errors='coerce')

# Drop any rows with NaN
df = df.dropna(subset=['Frequency','Sagittal','Tangential'])

# Assign numeric arrays
frequency = df['Frequency'].values
sagittal = df['Sagittal'].values
tangential = df['Tangential'].values

# Threshold
threshold = 0.1

# Find failing indices
sagittal_fail_indices = df.index[df.Sagittal < threshold].tolist()
tangential_fail_indices = df.index[df.Tangential < threshold].tolist()

# Print failing ranges safely
if sagittal_fail_indices:
    print(f"Sagittal failure from {frequency[sagittal_fail_indices[0]]:.2f} to {frequency[sagittal_fail_indices[-1]]:.2f} cycles/mm")
if tangential_fail_indices:
    print(f"Tangential failure from {frequency[tangential_fail_indices[0]]:.2f} to {frequency[tangential_fail_indices[-1]]:.2f} cycles/mm")

# Plot
plt.figure(figsize=(8,5))
plt.plot(frequency, sagittal, label='Sagittal MTF', color='blue')
plt.plot(frequency, tangential, label='Tangential MTF', color='orange')

# Highlight failing zones
plt.fill_between(frequency, 0, sagittal, where=sagittal < threshold, color='red', alpha=0.3)
plt.fill_between(frequency, 0, tangential, where=tangential < threshold, color='green', alpha=0.3)

# Threshold line
plt.axhline(threshold, color='grey', linestyle='--', label=f"{threshold*100:.0f}% Threshold", linewidth=1)

# Labels and title
plt.xlabel('Spatial Frequency (cycles/mm)')
plt.ylabel('MTF')
plt.title('Modulation Transfer Function (MTF) Analysis')
plt.ylim(0,1)
plt.legend()
plt.grid()
plt.show()


