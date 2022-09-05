def quick_sort(items, ini, fin):
  if ini < fin:
      # OBTIENE EL INDICE DE LA PARTICION
      p_indice = partition(items, ini, fin)

      # LLAMA LA FUNCON QUICKSORT DE INI AL PIVOTE Y DEL PIVOTE A FIN
      quick_sort(items, ini, p_indice - 1)
      quick_sort(items, p_indice + 1, fin)

# USO DE LA FUNCION PARTITION
def partition(items, ini, fin):
  # SE DEFINE QUE EL ULTIMO ELEMENTO SEA EL PIVOTE
  pivot = items[fin]
  i = ini
  for j in range(ini, fin):
      # MUEVE EL INDICE IZQ
      if items[j] < pivot:
          items[i], items[j] = items[j], items[i]
          i += 1
    #CAMBIO DE POSICIÓN DEL PIVOTE
  pivot_indice = i
  items[pivot_indice], items[fin] = items[fin], items[pivot_indice]
  return pivot_indice

#Prueba del ejemplo
def ejemplo():
 arrayEjemplo = [8,3,12,4,2,9,7,1]
 ini = 0
 fin = len(arrayEjemplo) - 1
 print("Arreglo original :")
 print(arrayEjemplo)
 quick_sort(arrayEjemplo, ini, fin)
 print("Arreglo ordenado: ")
 print(arrayEjemplo)
  
ejemplo()