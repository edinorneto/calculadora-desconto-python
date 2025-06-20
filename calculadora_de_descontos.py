#Primeiro projeto: Calculadora de Descontos

while True: #enquanto for verdadeiro, ou seja, loop infinito, até o usuário fazer o que eu quero
  valor = input("Digite o valor do produto: ")
  if not valor.strip(): # se nao houver um valor, ao retirar os espaços com o .strip, ele printa o erro e reseta o loop
    print("Erro! Você não digitou o valor.")
    continue

  try: # quando qualquer coisa é digitada, ele tenta passar pra float, caso não seja um valor possível de passar pra float (letra ou espaço em branco), printa o except.
    valor_flt = float(valor)
    break # caso o valor dê certo o loop é quebrado, passando pra verificação do desconto

  except ValueError: #expect que é printado. value error o tipo de dado é correto mas seu valor é errado. não pode ser convertido.
    print("Erro! Você não digitou um valor numérico.")

while True: # segundo passo do programa, loopar agora o percentual, da mesma forma que o anterior
  percentual = input("Digite o percentual de desconto: ")
  if not percentual.strip():
    print("Erro! Você não digitou o desconto.")
    continue

  try:
    percentual_flt = float(percentual)
    break

  except ValueError:
    print("Erro! Você não digitou um valor numérico.")


valor_desconto = (valor_flt * percentual_flt)/100 # funções de cálculo

valor_final = valor_flt - valor_desconto

print(f"O valor do desconto é: {valor_desconto:.2f}")

print(f"O valor final do produto é: {valor_final:.2f}")
