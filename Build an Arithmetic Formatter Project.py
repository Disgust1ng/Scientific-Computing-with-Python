def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:

        return "Error: Too many problems."

    top_number = []
    bottom_operator_numbers = []
    dashes = []
    answers = []

    for problem in problems:
        parts = problem.split()
        left = parts[0]
        symbol = parts[1]
        right = parts[2]

        if symbol not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."
        
        if not left.isdigit() or not right.isdigit():
            return 'Error: Numbers must only contain digits.'
        
        if len(left) > 4 or len(right) > 4:
            return 'Error: Numbers cannot be more than four digits.'


        length = max(len(left), len(right)) + 2

        top_number.append(left.rjust(length))
        bottom_operator_numbers.append(symbol + right.rjust(length - 1))

        dashes.append('-' * length) 

        if show_answers:
            result = str(eval(left + symbol + right))
            answers.append(result.rjust(length))

    top = "    ".join(top_number)
    bottom = "    ".join(bottom_operator_numbers)
    dash = "    ".join(dashes)

    if show_answers:
        ans = "    ".join(answers)
        return top + '\n' + bottom + '\n' + dash + '\n' +  ans
    else:
        return top + '\n' + bottom + '\n' + dash


print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)}')