import time


def max_number(lista):
    start_time = time.time()
    max_value = lista[0]
    for i in lista[1:]:
        if i > max_value:
            max_value = i
    end_time = time.time()
    exec_time = end_time - start_time
    print(f"Execution time: {exec_time} seconds")
    return max_value

if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    max_value = max_number(lista)
    print(f"Max value: {max_value}")