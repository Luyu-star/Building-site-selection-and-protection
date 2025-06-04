import numpy as np
import pandas as pd

data_dict = {
    "Name": [
        "Chapultepec Forest",
        "Museum of Anthropology",
        "Frida Kahlo Museum",
        "Palace of Fine Arts",
        "Chapultepec Zoo",
        "Vasconcelos Library"
    ],
    "History": [1944, 1964, 1958, 1904, 1923, 2006],
    "Floor space": [686, 33000, 800, 8000, 135, 38091],
    "Number of comments": [240000, 73758, 37874, 164683, 63246, 4873],
    "Social evaluation": [4.7, 4.8, 4.5, 4.8, 4.2, 4.7],
    "Disaster factor": [0.049412654, 0.049412654, 0.03729928, 0.03729928, 0.049412654, 0.049412654]
}

df = pd.DataFrame(data_dict)

# 2. Entropy weight method calculation
def entropy_weight(X):
    X_norm = (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0))
    X_norm = X_norm.replace(0, 1e-10)
    p = X_norm.div(X_norm.sum(axis=0), axis=1)
    k = 1.0 / np.log(len(X_norm))
    e = (-k * (p * np.log(p)).sum(axis=0)).values
    d = 1 - e
    w = d / d.sum()
    return w

# 3. Coefficient of variation method calculation
def coeff_variation_weight(X):
    mean_vals = X.mean(axis=0)
    std_vals = X.std(axis=0)
    cv = std_vals / mean_vals
    w = cv / cv.sum()
    return w.values

# 4. Select indicator columns
indicators = ["History", "Floor space", "Number of comments", "Social evaluation", "Disaster factor"]
X = df[indicators]

w_entropy = entropy_weight(X)
w_cv = coeff_variation_weight(X)
w_avg = (w_entropy + w_cv) / 2

# Output weight comparison
weight_df = pd.DataFrame({
    "Entropy Weight": w_entropy,
    "Coefficient of Variation Weight": w_cv,
    "Average Weight": w_avg
}, index=indicators)

print("Weight for each indicator:")
print(weight_df)

X_norm = (X - X.min()) / (X.max() - X.min())

df["CBCI"] = (X_norm * w_avg).sum(axis=1)

df_sorted = df.sort_values(by="CBCI", ascending=False)

print("\nBuilding protection level ranking:")
print(df_sorted[["Name", "CBCI"]].reset_index(drop=True))