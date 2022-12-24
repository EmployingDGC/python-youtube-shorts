"""
Convertendo:
    Celcius para Farenheit;
    Farenheit para Celcius.
"""

def celcius_farenheit(celcius: float) -> str:
    farenheit = (celcius * 9 / 5) + 32
    
    return f"{celcius:.2f}°C = {farenheit:.2f}°F"


def farenheit_celcius(farenheit: float) -> str:
    celcius = (farenheit - 32) * 5 / 9
    
    return f"{farenheit}°F = {celcius:.2f}°C"


opcoes = {
    "1": celcius_farenheit,
    "2": farenheit_celcius,
    "0": None
}

while True:
    print("1 - Celcius para Farenheit")
    print("2 - Farenheit para Celcius")
    print("0 - Sair")

    op = input()
    
    if op not in opcoes:
        print("\nOpção Inválida\n")
        continue
    
    if op == "0":
        break
    
    graus = float(input("\nDigite a temperatura: "))
    
    print(f"\n{opcoes.get(op)(graus)}\n")
