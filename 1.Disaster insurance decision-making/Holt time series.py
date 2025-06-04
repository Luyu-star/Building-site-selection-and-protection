import numpy as np
import matplotlib.pyplot as plt

# Define CAGR forecast function
def generate_forecast(start_value, cagr, years, growth_rates=None):
    forecasts = []
    value = start_value
    for i, year in enumerate(years):
        if growth_rates and i > 0:
            value *= (1 + growth_rates[i-1])
        elif i > 0:
            value *= (1 + cagr)
        forecasts.append(value)
    return forecasts

# Set years range
years = list(range(2022, 2027))

# Starting values (in billions and millions USD)
mexico_start = 121.1  # billion USD
armenia_start = 130   # million USD

# Mexico CAGR and annual growth rates (slightly higher for 2023-2024)
mexico_cagr = 0.067
mexico_growth_rates = [0.071, 0.068, 0.067, 0.067]  # growth rates for 2023-2026

# Armenia CAGR (uniform growth rate)
armenia_cagr = 0.053

# Generate forecast data
mexico_forecast = generate_forecast(mexico_start, mexico_cagr, years, growth_rates=mexico_growth_rates)
armenia_forecast = generate_forecast(armenia_start, armenia_cagr, years)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(years, mexico_forecast, label='Mexico (Billion USD)', marker='o')
plt.plot(years, armenia_forecast, label='Armenia (Million USD)', marker='x')
plt.title("Figure 5: Forecast of Disaster Losses in Mexico and Armenia (2022–2026) \n"
          "Results based on Holt time series model predictions")
plt.xlabel("Year")
plt.ylabel("Direct Economic Loss")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Print forecast results
print("Mexico (Billion USD):")
for year, value in zip(years, mexico_forecast):
    print(f"{year}: ${value:,.1f}B")

print("\nArmenia (Million USD):")
for year, value in zip(years, armenia_forecast):
    print(f"{year}: ${value:,.1f}M")
    print(f"{year}: ${value:,.1f}M")