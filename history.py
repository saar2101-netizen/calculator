"""
history model
"""

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
