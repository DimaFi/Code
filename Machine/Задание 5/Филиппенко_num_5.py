import csv
import sys

def parse_input_parameters():
    params = {
        "file": "input.csv",
        "rows": None,
        "cols": None,
        "n": None,
        "m": None,
        "pigeons": []
    }

    print("Введите параметры (например, file=my_csv.csv, rows=2, cols=2 и т.д.):")
    while True:
        try:
            user_input = input().strip()
            if not user_input:
                break

            if "=" not in user_input:
                raise ValueError(f"Некорректный параметр: {user_input}")

            key, value = user_input.split("=", 1)
            key = key.strip()
            value = value.strip()

            if key == "file":
                params["file"] = value
            elif key == "rows":
                params["rows"] = int(value)
            elif key == "cols":
                params["cols"] = int(value)
            elif key == "n":
                params["n"] = int(value)
            elif key == "m":
                params["m"] = int(value)
            elif key == "pigeons":
                params["pigeons"] = [item.strip() for item in value.split(",")]
            else:
                raise ValueError(f"Неизвестный параметр: {key}")

        except ValueError as e:
            print(f"Ошибка: {e}")

    return params

def validate_parameters(params):
    errors = []

    if params["rows"] is None or params["cols"] is None:
        errors.append("Не указаны размеры стеллажа (rows и cols).")

    if params["n"] is None or params["m"] is None:
        errors.append("Не указаны количество ящиков (n) или количество предметов (m).")

    if len(params["pigeons"]) != params["m"]:
        errors.append("Число предметов не соответствует указанному m.")

    if params["rows"] * params["cols"] < params["n"]:
        errors.append("Размеры стеллажа меньше количества ящиков.")

    if errors:
        raise ValueError("\n".join(errors))

def write_to_csv(file_name, params):
    with open(file_name, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["rows", "cols", "n", "m", "pigeons"])
        writer.writerow([params["rows"], params["cols"], params["n"], params["m"], ", ".join(params["pigeons"])])

def apply_dirichlet_principle(params):
    n = params["n"]
    m = params["m"]

    if m > n:
        print(f"Принцип Дирихле: хотя бы в одном ящике лежит не менее {m // n + 1} предметов.")
    else:
        print(f"Принцип Дирихле: пустых ящиков как минимум {n - m}.")

def main():
    try:
        params = parse_input_parameters()
        validate_parameters(params)
        write_to_csv(params["file"], params)
        apply_dirichlet_principle(params)
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()