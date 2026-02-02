# nota_definitiva
# Programa #2: Nota definitiva

Programa en Python para calcular la nota definitiva de una asignatura del Colegio Guanentá, a partir de diferentes tipos de evaluación y sus respectivos porcentajes.

# Instrucciones:
 - Ingrese el nombre de la asignatura.
 - Ingrese las notas solicitadas usando valores enteros entre 10 y 50.
 - No utilice números decimales, ya que el programa solo acepta valores enteros.

## Análisis

# Diagrama de flujo
![alt text](diagrama.png)

### Variables de entrada
 - asignatura: Nombre de la asignatura
 - Nc: Nota cognitiva
 - Np: Nota procedimental
 - Na: Nota actitudinal
 - Au: Nota de autoevaluación
 - Bi: Nota bimestral

### Procesamiento
 - Nd: Nota definitiva
 - pasar: Variable lógica que indica si el estudiante aprueba la asignatura

 - Nd = (Nc * 0.3) + (Np * 0.3) + (Na * 0.1) + (Au * 0.1) + (Bi * 0.2)
 - Nd = int(Nd)
 - pasar = Nd > 29

## Diseño

![diagrama de flujo](diagrama.png)

## Construcción
 - Código implementado en el archivo "nota_definitiva.py"
