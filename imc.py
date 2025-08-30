peso = int(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso / (altura*altura)
if imc < 18.5:
    print("Abaixo do peso, procure um nutricionista.")
elif imc >=18.5 and imc <=24.9:
    print("Peso ideal, continue assim!")
elif imc >=25 and imc <=29.9:
    print("Sobrepeso, procure um nutricionista.")
elif imc >=30 and imc <=39.9:
    print("Obesidade, procure um nutricionista.")
else:
    print("Obesidade mórbida, procure um nutricionista.")
print(f"Seu IMC é {imc:.2f}")