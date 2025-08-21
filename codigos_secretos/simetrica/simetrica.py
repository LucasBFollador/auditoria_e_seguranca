def cifrar_simetrico(texto, chave):
    resultado = ""
    for letra in texto.upper():  #deixa tudo maiúsculo
        if letra == " ":  #mantém espaços
            resultado += " "
        else:
            #transforma a letra em número de 0 a 25 (A=0, B=1,..., Z=25)
            pos = ord(letra) - ord('A')
            #Da letra Z volta para a letra A
            nova_pos = (pos + chave) % 26
            #converte de volta para letra
            resultado += chr(nova_pos + ord('A'))
    return resultado

def decifrar_simetrico(texto, chave):
    resultado = ""
    for letra in texto:
        resultado += chr(ord(letra) - chave)
    return resultado

mensagem = input("Digite a mensagem: ")
chave = int(input("Digite a chave (número): "))

cifrada = cifrar_simetrico(mensagem, chave)
decifrada = decifrar_simetrico(cifrada, chave)

print("Mensagem original:", mensagem)
print("Mensagem cifrada :", cifrada)
