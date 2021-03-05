def arithmetic_arranger(problems, show_results=False):

    operands1 = []
    operands2 = []
    operators = []
    dashes = []
    results = []

    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        operand1 = problem.split()[0]
        operator = problem.split()[1]
        operand2 = problem.split()[2]
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        if not (operand1.isdigit() and operand2.isdigit()):
            return "Error: Numbers must only contain digits."
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = len(max([operand1, operand2], key=len)) + 2
        operands1.append(operand1.rjust(width))
        operands2.append(operator + operand2.rjust(width - 1))
        operators.append(operator)
        dashes.append("-" * width)
        results.append(str(eval(f"{int(operand1)} {operator} {int(operand2)}")).rjust(width))

    combined = ["    ".join(x) for x in [operands1, operands2, dashes]]

    if show_results:
        return "\n".join(combined) + "\n" + "    ".join(results)
    return "\n".join(combined)