# 7. Par ou Ímpar (Condicional + Função) 
# Crie uma função que receba um número inteiro e retorne se ele é par ou ímpar.
def par_ou_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"
resultado= par_ou_impar(6)
print(f"O numero é {resultado}")
  
    