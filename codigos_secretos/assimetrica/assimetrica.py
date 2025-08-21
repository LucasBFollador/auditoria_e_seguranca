def cifrar_assimetrico(texto, chave_publica):
    resultado = ""
    for letra in texto.upper():
        if letra == " ":
            resultado += " "
        else:
            pos = ord(letra) - ord('A')   #transforma letra em 0..25
            nova_pos = (pos * chave_publica) % 26  #multiplica pela chave
            resultado += chr(nova_pos + ord('A'))
    return resultado

def decifrar_assimetrico(texto, chave_privada):
    resultado = ""
    for letra in texto.upper():
        if letra == " ":
            resultado += " "
        else:
            pos = ord(letra) - ord('A')
            nova_pos = (pos * chave_privada) % 26  #multiplica pela chave privada
            resultado += chr(nova_pos + ord('A'))
    return resultado


mensagem = input("Digite a mensagem: ")

chave_publica = 5
chave_privada = 21  # 5 * 21 = 105 ≡ 1 (mod 26), ou seja, "inverso modular"

cifrada = cifrar_assimetrico(mensagem, chave_publica)
decifrada = decifrar_assimetrico(cifrada, chave_privada)

print("\nMensagem original :", mensagem.upper())
print("Mensagem cifrada  :", cifrada)
