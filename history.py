"""
history model
"""
import json


calculation_history = []

def add_to_history(expression, result):

    entry = f"{expression} = {result}"
    calculation_history.append(entry)

def show_history():

    if not calculation_history:
        print("No history yet")
        return

    print("\n========History========")
    for i, entry in enumerate(calculation_history, 1):
        print(f"{i}. {entry}")


def clear_history():

    calculation_history.clear()
    print("History been delete")


def save_history(filename="history.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(calculation_history, f, ensure_ascii=False)

    print(f"History save to {filename}")

def load_history(filename="history.json"):
    global calculation_history
    try:
        with open(filename, "r", encoding="utf-8") as f:
            calculation_history = json.load(f)
        print(f"History upload from {filename}")
    except FileNotFoundError:
        print("File not found in history")
