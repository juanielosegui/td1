def f2c(fahr: float, x: float) -> float:
    x: float = (fahr - 32) * 5 / 9
    return x

fahr: float
print(input(f2c('Inserte fahrenheit: ')))