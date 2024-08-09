import csv

def extraer_apellido(archivo_csv, columna_apellido):
  """
  Extrae el apellido de un archivo CSV.

  Args:
    archivo_csv: La ruta completa del archivo CSV.
    columna_apellido: El índice de la columna donde se encuentra el apellido (comenzando desde 0).

  Returns:
    Una lista con los apellidos extraídos.
  """

  apellidos = []
  with open(archivo_csv, 'r') as archivo:
    lector_csv = csv.reader(archivo)
    for fila in lector_csv:
      apellido = fila[columna_apellido]  # Ajusta el índice según tu archivo
      apellidos.append(apellido)

  return apellidos

# Ejemplo de uso:
archivo = 'mis_datos.csv'  # Reemplaza con la ruta de tu archivo
columna_apellido = 1  # Ajusta según el índice de la columna del apellido en tu archivo

todos_los_apellidos = extraer_apellido(archivo, columna_apellido)
print(todos_los_apellidos)
