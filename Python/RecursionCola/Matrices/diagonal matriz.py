def diagonal(matriz):
   if isinstance(matriz, list) and (len(matriz) == len(matriz[0])):
      return diagonal_aux(matriz, len(matriz), len(matriz[0]), 0, 0, 0)
   else:
      return -1

def diagonal_aux(matriz, numf, numc, fila, columna, suma):
   if (fila == numf):
      return suma
   else:
      return diagonal_aux(matriz, numf, numc, fila + 1, columna + 1, suma + matriz[fila][columna])
