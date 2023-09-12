# Função para calcular o valor da chave
def calcular_chave(chave_texto):
    soma = 0
    for letra in chave_texto:
        soma += ord(letra) - ord('a') + 1  # Transforma a letra em um valor de 1 a 26
    return soma % 26

def codificar_mensagem(mensagem, chave):
    mensagem_codificada = ""
    for letra in mensagem:
        if letra.isalpha():  
            if letra.islower():  
                codigo_letra = ord(letra) - ord('a')
                codigo_letra = (codigo_letra + chave) % 26
                letra_codificada = chr(codigo_letra + ord('a'))
            else:
                codigo_letra = ord(letra) - ord('A')
                codigo_letra = (codigo_letra + chave) % 26
                letra_codificada = chr(codigo_letra + ord('A'))
            mensagem_codificada += letra_codificada
        else:
            mensagem_codificada += letra  
    return mensagem_codificada

chave_texto = input("Digite a chave: ")

chave = calcular_chave(chave_texto)

mensagem = input("Digite a mensagem: ")

mensagem_codificada = codificar_mensagem(mensagem, chave)

print("Mensagem codificada:", mensagem_codificada)
