def f2c(fahr: float) -> float:
    cel: float = (fahr - 32) * 5 / 9
    return cel

fahr: float = 150
cel = f2c(fahr)
print (cel)