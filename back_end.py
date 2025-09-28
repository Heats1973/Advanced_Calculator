numbers_str = []
ENTRY = None

#back_end part
#n - button value / user input
#number_str - list to store user inputs

def handle_click(n, ENTRY):
    def update_entry():
        ENTRY.delete(0, "end")
        ENTRY.insert(0, "".join(numbers_str))

    operators = ["+", "-", "*", "/"]
    if n == "=" and numbers_str:
        try:
            expression = "".join(numbers_str)
            result = eval(expression)
            numbers_str.clear()
            numbers_str.append(str(result))
            if isinstance(result, float) and result.is_integer():
                numbers_str[-1] = str(int(result))

            update_entry()

        except ZeroDivisionError:  # ловимо ділення на 0
            numbers_str.clear()
            numbers_str.append("ти гей?")
            update_entry()

        except Exception:  # всі інші помилки
            numbers_str.clear()
            numbers_str.append("Чоза хуйня?")
            update_entry()


    elif n == "C":
        numbers_str.clear()
        update_entry()

    elif n == "⌫":
        numbers_str.pop()
        update_entry()

    elif numbers_str and numbers_str[-1] in operators and n in operators:
        numbers_str[-1] = n
        update_entry()

    else:
        numbers_str.append(n)
        update_entry()
