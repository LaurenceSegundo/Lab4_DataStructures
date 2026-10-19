"""
Exercise 2: Student Performance Data Analyzer
Author: Laurence Segundo
"""
last_name = "SEGUNDO"
favorite_artist = "TAYLOR SWIFT"

# 1. Generate Student Performance Records
student_names = [f"Student_{i}_{last_name}" for i in range(1, 6)]
subjects = ["PROGRAMMING", "MATHEMATICS", "ELECTRONICS", "PHYSICS", "ENGLISH"]

# Base score derived from favorite artist character positions
base_score = len(favorite_artist) * 7  # 84

raw_records = [
    {"name": student_names[0], "subject": subjects[0], "score": 92},
    {"name": student_names[1], "subject": subjects[1], "score": 78},
    {"name": student_names[2], "subject": subjects[2], "score": 85},
    # Repeated record
    {"name": student_names[0], "subject": subjects[0], "score": 92},
    {"name": student_names[3], "subject": subjects[3], "score": 65},
    # Incomplete record (missing score represented as None)
    {"name": student_names[4], "subject": subjects[4], "score": None}
]

print("=== 1. GENERATED PERFORMANCE RECORDS ===")
for r in raw_records:
    print(r)

# 2 & 3. Organize & Handle Incomplete/Repeated Records
valid_records = [r for r in raw_records if r["score"] is not None]
unique_records = [dict(t) for t in {tuple(d.items()) for d in valid_records}]

print("\n=== 3. REPEATED/INCOMPLETE RECORDS HANDLED ===")
print(f"Valid Records Count: {len(valid_records)}, Unique Records Count: {len(unique_records)}")

# 4. Performance Categories
def get_category(score):
    if score >= 90: return "Distinction"
    elif score >= 80: return "Merit"
    elif score >= 75: return "Pass"
    else: return "Needs Improvement"

print("\n=== 4. PERFORMANCE CATEGORIES ===")
for r in unique_records:
    print(f"{r['name']} ({r['subject']}): {r['score']} -> {get_category(r['score'])}")

# 5. Student and Subject Summaries
from collections import defaultdict
student_totals = defaultdict(list)
for r in unique_records:
    student_totals[r["name"]].append(r["score"])

print("\n=== 5. STUDENT SUMMARIES ===")
for student, scores in student_totals.items():
    print(f"{student} Average: {sum(scores)/len(scores):.2f}")

# 6. Ordered Results
ordered_records = sorted(unique_records, key=lambda x: x["score"], reverse=True)
print("\n=== 6. ORDERED RESULTS (Highest to Lowest Score) ===")
for r in ordered_records:
    print(r)