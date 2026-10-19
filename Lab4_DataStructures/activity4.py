"""
Exercise 1: Engineering Test Data Organizer
Author: Laurence Segundo
Dataset & Analysis Generator
"""

# 1. Generate Individualized Test Records
last_name = "SEGUNDO"
favorite_artist = "TAYLOR SWIFT"

# Generate 5 test sources using Last Name and labels T1-T5
test_sources = [f"T{i}_{last_name}" for i in range(1, 6)]
categories = ["TEMPERATURE", "VOLTAGE", "CURRENT", "PRESSURE", "SPEED"]

# Generate numerical values using character lengths/positions of favorite artist
seed_val = len(favorite_artist)  # 12
base_values = [ord(char) % 50 for char in favorite_artist[:5]] # Derived from TAYLOR

# Initial raw test dataset with a deliberate repeated record and multi-measurements
raw_test_records = [
    {"source": test_sources[0], "category": categories[0], "value": base_values[0] + 25.5},
    {"source": test_sources[1], "category": categories[1], "value": base_values[1] + 12.0},
    {"source": test_sources[2], "category": categories[2], "value": base_values[2] + 5.2},
    # Repeated record (source[0] and category[0])
    {"source": test_sources[0], "category": categories[0], "value": base_values[0] + 25.5},
    {"source": test_sources[3], "category": categories[3], "value": base_values[3] + 101.3},
    {"source": test_sources[4], "category": categories[4], "value": base_values[4] + 60.0},
    # Additional measurement under an existing category
    {"source": test_sources[0], "category": categories[0], "value": base_values[0] + 30.1},
]

print("=== 1. GENERATED TEST DATA ===")
for r in raw_test_records:
    print(r)

# 2. Organize Records by Source and Category
from collections import defaultdict
organized_data = defaultdict(list)
for record in raw_test_records:
    key = (record["source"], record["category"])
    organized_data[key].append(record["value"])

print("\n=== 2. ORGANIZED TEST DATA (Grouped) ===")
for k, v in organized_data.items():
    print(f"Source & Category {k}: Values -> {v}")

# 3. Identify Repeated and Distinct Data
unique_records_set = set((r["source"], r["category"], r["value"]) for r in raw_test_records)
print(f"\n=== 3. REPEATED / DISTINCT DATA ===")
print(f"Total Raw Records: {len(raw_test_records)}")
print(f"Unique Records Count: {len(unique_records_set)}")
print(f"Duplicates Detected: {len(raw_test_records) - len(unique_records_set)}")

# 4. Numerical and Categorical Summaries
all_values = [r["value"] for r in raw_test_records]
summary_stats = {
    "total_records": len(all_values),
    "max_reading": max(all_values),
    "min_reading": min(all_values),
    "average_reading": sum(all_values) / len(all_values)
}

print("\n=== 4. NUMERICAL & CATEGORICAL SUMMARIES ===")
for stat, val in summary_stats.items():
    print(f"{stat.replace('_', ' ').title()}: {val:.2f}")

# 5 & 6. Processed & Ordered Results
sorted_records = sorted(raw_test_records, key=lambda x: x["value"])
print("\n=== 5 & 6. ORDERED RESULTS (Sorted by Value) ===")
for sr in sorted_records:
    print(sr)

# 7. Final Consolidated Summary Report
print("\n=== 7. FINAL CONSOLIDATED SUMMARY ===")
print(f"Dataset processed successfully for {last_name}. Total entries analyzed: {len(raw_test_records)}.")