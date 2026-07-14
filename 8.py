from typing import List

students = ["Komal", "Teja", "Krishna"]
marks = [85, 92, 78]

def get_results(names: List[str], scores: List[int]) -> None:
    """Print each student's result."""
    for index, (name, score) in enumerate(zip(names, scores), start=1):
        status = "Pass" if score >= 35 else "Fail"
        print(f"{index}. {name}: {score} - {status}")

get_results(students, marks)
