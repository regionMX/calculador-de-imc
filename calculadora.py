####### bienvenida 
print('Hola buen dia ')
print('ingrese los siguientes datos que se te pidan')
input()
########aqui pide que intridusca los datos 
nombre = input("porfavor introdusca su nombre: ")
apellido = input("porfavor introdusca su apellido paterno y materno: ")
edad = int(input("porfavor introdusca su edad: "))
masa = float(input("porfavor introdusca su masa en (kg): "))
altura = float(input("porfavor introdusca su altura en (m): "))
estatura = altura
#calculo del imc
IMC = masa / estatura**2
          
print("Nombre: " + nombre)
print("Apellido: " + apellido)
print("Tiene: " + str(edad) + "años")
print("altura: " + str(altura) )
print("IMC: " + str(IMC))

if IMC >= 0 and IMC <= 18.9:
  print("Peso bajo")
elif IMC >= 18.50 and IMC <= 24.99:
   print("peso normal ")
elif IMC >= 25.00 and IMC <= 29.99:
   print(" sobrepeso ")
elif IMC >= 30.00 and IMC <= 34.99:
   print("obesidad leve ")
elif IMC >= 35.00 and IMC <= 39.99:
   print("obesidad media ")
elif IMC >= 40.00:
   print("obesidad morbida ")



    







