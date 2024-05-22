
import time
print("\tBanco Pichincha\n")
nombre=input("Ingrese su nombre porfavor: ")
print("Tipos de tarjeta:\n")
print("Tipos 1\n")
print("Tipos 2\n")
print("Tipos 3\n")
print("Tipos cualquier otro numero\n")
tipo=int(input("Ingrese el tipo de Tarjeta:"))
saldo=float(input("Ingrese su credito anterior: "))
print ("PROCESANDO......")
time.sleep(3)
if(tipo==1):
    aumento=saldo*0.25
    saldo=saldo*1.25
    
elif(tipo==2):
    aumento=saldo*0.35
    saldo=saldo*1.35
elif(tipo==3):
    aumento=saldo*0.4
    saldo=saldo*1.4
else:
    aumento=saldo*0.25
    saldo=saldo*1.5

print(f"{nombre} se le aumento su credito a {aumento}$ y su Saldo Actual {saldo}$ ")
