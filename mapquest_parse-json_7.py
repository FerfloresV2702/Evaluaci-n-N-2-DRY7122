import requests

def calcular_distancia(ciudad_origen, ciudad_destino):
    # Obtener los datos de ruta desde la API de MapQuest
    url = f"http://www.mapquestapi.com/directions/v2/route?key=E4tdpz5fFyizkvtYh5Cj9fMVA153f2Cv&from={ciudad_origen}&to={ciudad_destino}"
    response = requests.get(url)
    data = response.json()

    # Extraer la distancia en kilómetros y la duración en segundos
    distancia_km = data["route"]["distance"] * 1.60934
    duracion_seg = data["route"]["time"]

    # Calcular la duración en horas, minutos y segundos
    duracion_horas = duracion_seg // 3600
    duracion_minutos = (duracion_seg % 3600) // 60
    duracion_segundos = duracion_seg % 60

    # Calcular el combustible requerido en litros (suponiendo un consumo promedio de 10 km/litro)
    combustible_litros = distancia_km / 10

    # Imprimir los resultados con dos decimales
    print(f"Distancia: {distancia_km:.2f} km")
    print(f"Duración: {int(duracion_horas)} horas, {int(duracion_minutos)} minutos, {int(duracion_segundos)} segundos")
    print(f"Combustible requerido: {combustible_litros:.2f} litros")

    # Imprimir la narrativa del viaje
    print(f"Viaje desde {ciudad_origen} hasta {ciudad_destino}")

# Pedir al usuario las ciudades de origen y destino
ciudad_origen = input("Ciudad de Origen: ")
ciudad_destino = input("Ciudad de Destino: ")

# Calcular la distancia y mostrar los resultados
calcular_distancia(ciudad_origen, ciudad_destino)

while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break