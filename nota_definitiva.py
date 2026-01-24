#input
asignatura = input("digite la asignatura: ")
Nc = input ("digite la nota cognitiva: ")
Np = input("digite la nota procedimental: ")
Na = input("digite la nota actitudinal: ")
Au = input("digite la nota de auto evaluación: ")
Bi = input("digite la nota bimestral: ")

#proceso
Nc = int(Nc)
Np = int(Np)
Na = int(Na)
Au = int(Au)
Bi = int(Bi)

Nd = Nc * 0.3 + Np * 0.3 + Na * 0.1 + Au * 0.1 + Bi * 0.2
Nd = int(Nd)
pasar = Nd > 29

#output
print(asignatura)
print(Nd)
if pasar: print("pasaste la asignatura")
else: print("perdiste la asignatura")