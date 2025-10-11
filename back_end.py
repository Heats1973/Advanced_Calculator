import math


numbers_str = []
last_answer = ""


safe_globals = {
    "__builtins__": None,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "sqrt": math.sqrt,
    "log": math.log,
    "pi": math.pi,
    "e": math.e,
    "abs": abs,
    "round": round,
    "floor": math.floor,
    "ceil": math.ceil,
}


def handle_click(n, ENTRY):
    global last_answer

    def update_entry():
        ENTRY.delete(0, "end")
        ENTRY.insert(0, "".join(numbers_str))

    operators = ["+", "-", "*", "/", "^"]

    if n == "=" and numbers_str:
        try:
            expression = "".join(numbers_str)
            expression = expression.replace("^", "**")

            if last_answer != "":
                expression = expression.replace("ANS", str(last_answer))

            if expression.strip() == "":
                numbers_str.clear()
                numbers_str.append("0")
                update_entry()
                return

            result = eval(expression, safe_globals)

            numbers_str.clear()
            numbers_str.append(str(result))
            last_answer = result

            if isinstance(result, float) and result.is_integer():
                numbers_str[-1] = str(int(result))

            update_entry()

        except ZeroDivisionError:
            numbers_str.clear()
            numbers_str.append("You can't divide by 0")
            update_entry()

        except SyntaxError:
            numbers_str.clear()
            numbers_str.append("Syntax Error")
            update_entry()

        except Exception as e:
            numbers_str.clear()
            numbers_str.append("Error")
            update_entry()

    elif n == "C":
        numbers_str.clear()
        update_entry()

    elif n == "⌫":
        if numbers_str:
            numbers_str.pop()
        update_entry()

    elif numbers_str and numbers_str[-1] in operators and n in operators:
        numbers_str[-1] = n
        update_entry()

    elif n in ["log", "sin", "cos", "tan", "sqrt"]:
        numbers_str.append(n)
        numbers_str.append("(")
        update_entry()

    elif n in ["(", ")"]:
        numbers_str.append(n)
        update_entry()

    else:
        numbers_str.append(n)
        update_entry()
