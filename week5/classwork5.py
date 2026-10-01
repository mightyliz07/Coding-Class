students = [
{"name": "Amina", "score": 85},
{"name": "David", "score": 94},
{"name": "Chidi", "score": 78},
{"name": "Fatima", "score": 91}
]
top = max(students, key=lambda s: s["score"])
print(f"{top['name']}: {top['score']}")
