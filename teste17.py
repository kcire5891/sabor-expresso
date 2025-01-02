idades.append(27)
idades.remove(27)
print(idades)

[(idade) for idade in idades if idade > 21]

[idade + 1 for idade in idades if idade > 21]

idades_no_ano_que_vem = []
for idade in idades:
  idades_no_ano_que_vem.append(idade+1)

def proximo ano(idade):
  return idade+1

[proximo_ano(idade) for idade in idades if idade > 21]