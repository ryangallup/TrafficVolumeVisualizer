import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV data into a Pandas DataFrame
data = pd.read_csv("Average_Daily_Traffic_Counts.csv")

# Calculate the average daily traffic
average_traffic = data['Total Passing Vehicle Volume'].mean()

# Extract traffic counts
traffic_counts = data['Total Passing Vehicle Volume']

# Create a bar chart
plt.figure(figsize=(10, 6))  # Set the figure size
plt.bar(traffic_counts.index, traffic_counts.values)  # Plot the bars
plt.xlabel("Data Point")
plt.ylabel("Traffic Volume")  # Update label for clarity
plt.title("Daily Traffic Volume")  # Update title for clarity

# Add a horizontal line for the average traffic
plt.axhline(y=average_traffic, color='red', linestyle='--', label=f"Average: {average_traffic:.2f}")
plt.legend()

# Rotate x-axis labels for readability if there are many data points
plt.xticks(rotation=45)

# Display the chart
plt.tight_layout()
plt.show()
