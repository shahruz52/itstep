result = []

def divider(a, b):
    if a < b:
        raise ValueError("a меньше b")
    if b > 100:
        raise IndexError("b больше 100")
    if b == 0:
      raise ZeroDivisionError("Деление на ноль")
    return a / b

data = {10: 2, 2: 5, "123": 4, 18: 0, (): 15, 8: 4} # [] заменено на ()

for key in data:
    try:
        res = divider(key, data[key]) # data[kem] заменено на data[key]
        result.append(res)
    except (ValueError, IndexError, ZeroDivisionError, TypeError) as e:
        print(f"Ошибка с ключом {key}: {e}")
    except Exception as e:
        print(f"Непредвиденная ошибка с ключом {key}: {e}")

print(result)