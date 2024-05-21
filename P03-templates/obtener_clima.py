def obtener_clima(temp:int) -> str:
  '''
  Requiere: 126 > temp > −273
  Devuelve: el clima del día para ser usado por el bot, donde segun el valor ingresado:
            -Si es menor o igual a 10, devolver 'frio'
            -Si se encuentra entre 10 y 17 grados, devolver 'templado'
            -Si se encuentra entre 17 y 25 grados (inclusive), devolver 'agradable'
            -Si es mayor a 25, devolver 'caluroso'
  '''
  if temp <= 10:
    return ('frio')
  
  elif 10 < temp < 17:
    return ('templado')

  elif 17 <= temp <= 25:
    return ('agradable')
  
  elif  25 < temp:
    return ('caluroso')