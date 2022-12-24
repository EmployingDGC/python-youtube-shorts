def eh_primo(num: int):
    for n in range(2, num):
        if num % n == 0:
            return False
    return True

nums = list(range(1, 1000))

primos = list(filter(eh_primo, nums))

print(primos)
