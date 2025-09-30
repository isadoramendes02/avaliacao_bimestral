# 2. Média de notas 
# Crie uma função chamada “calcular_media” que receba uma lista de notas e retorne a média. 
# No programa principal (fora da sua função “calcular_media”), peça ao usuário 4 notas e 
# armazene-as em uma lista. 
# Use a função para calcular a média e mostre se o aluno está aprovado (média ≥ 7) ou 
# reprovado (média < 7).

def calcular_media():
    quantidade_notas=int(input("Quantas notas voce quer calcular a media:"))
    total= 0
    for i in range (quantidade_notas):
        nota = float(input(f"Digite {i+1}  nota:"))
        total += nota
    media= total / quantidade_notas
    return media
media = calcular_media()
print(media)
if media > 7:
    print("APROVADO!!!!")
else:
    print("REPROVADO")