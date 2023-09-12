def calcular_chave(chave_texto):
    soma = 0
    for letra in chave_texto:
        soma += ord(letra) - ord('a') + 1
    return soma % 26
def decodificar_mensagem(mensagem_codificada, chave):
    mensagem_decodificada = ""
    for letra in mensagem_codificada:
        if letra.isalpha():
            if letra.islower():
                codigo_letra = ord(letra) - ord('a')
                codigo_letra = (codigo_letra - chave) % 26  
                letra_decodificada = chr(codigo_letra + ord('a'))
            else:
                codigo_letra = ord(letra) - ord('A')
                codigo_letra = (codigo_letra - chave) % 26
                letra_decodificada = chr(codigo_letra + ord('A'))
            mensagem_decodificada += letra_decodificada
        else:
            mensagem_decodificada += letra
    return mensagem_decodificada

chave_texto = input("Digite a chave: ")

chave = calcular_chave(chave_texto)

mensagem_codificada = input("Digite a mensagem codificada: ")

mensagem_decodificada = decodificar_mensagem(mensagem_codificada, chave)

print("Mensagem decodificada:", mensagem_decodificada)
