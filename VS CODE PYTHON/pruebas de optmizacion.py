import timeit


def calcular_tiempo():
    lista_completa = list(range(1, 1000001))
    lista_pares = list(range(2, 1000001, 2))

    start_time = timeit.default_timer()

    lista_impares = [x for x in lista_completa if x % 2 != 0]

    end_time = timeit.default_timer()
    tiempo_transcurrido = end_time - start_time

    return lista_impares, tiempo_transcurrido

lista_impares, tiempo = calcular_tiempo()
print(f"Lista de impares: {lista_impares[:10]}...")
print(f"Tiempo transcurrido: {tiempo} segundos")


def calcular_tiempo2():
    lista_completa = list(range(1, 1000001))
    lista_pares = list(range(2, 1000001, 2))

    start_time = timeit.default_timer()

    lista_impares = list(filter(lambda x: x % 2 != 0, lista_completa))

    end_time = timeit.default_timer()
    tiempo_transcurrido = end_time - start_time

    return lista_impares, tiempo_transcurrido

lista_impares, tiempo = calcular_tiempo2()
print(f"Lista de impares: {lista_impares[:10]}...")
print(f"Tiempo transcurrido: {tiempo} segundos")
