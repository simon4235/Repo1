# mi_primer_script.py
print("¡Hola, GitHub!")
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Generar lista de números primos entre 1 y 1000
primos = [num for num in range(1, 1001) if es_primo(num)]

print("Números primos entre 1 y 1000:")
print(primos)
