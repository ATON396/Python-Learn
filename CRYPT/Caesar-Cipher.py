# CAESESAR CIPHER PROGRAM. 
# Dibujo
#/\  /\  /\  /\  /\  /\  /\  /\  /\  /\  
# \/  \/  \/  \/  \/  \/  \/  \/  \/  \/
#| CAESESAR CIPHER  || CAESESAR CIPHER |
#/\  /\  /\  /\  /\  /\  /\  /\  /\  /\  
#  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/
print('/\  ' * 10)
print('  \/' * 10)
print('| CAESESAR CIPHER  |' * 2)
print('/\  ' * 10)
print('  \/' * 10)

# Parte logica del programa
alfabeto = 'a#bcde!fghijklmnñ&±o*pqrstuvw¿?xy$z'
# Introduce tu clave privada: Usuario dijita numero entro
clave = ((int(input('Introduce tu clave privada: '))) * 9) // 3

nuevoMensaje = ' '
#Por favor, introduce un mensaje: Usuario dijita mensaje alfanumerico
mensaje = input('Por favor, introduce un mensaje: ')
# Condicional para encryptar el mensaje en cesar
for caracter in mensaje:
  if caracter in alfabeto:
    posicion = alfabeto.find(caracter)
    nuevaPosicion = (posicion + clave) % 35
    nuevoCaracter = alfabeto[nuevaPosicion]
    nuevoMensaje += nuevoCaracter
  else:
    nuevoMensaje += caracter
# Imprime por consola el mensaje cifrado en cesar
print('Tu mensaje cifrado es: ', nuevoMensaje)