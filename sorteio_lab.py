import random

pessoas = [ 'Samantha','Leonardo','Leilane', 'Samantha','Leonardo','Leilane' ]
temas = ['1', '3', '4', '5', '7', '10']

print("     SORTEIO DOS BRABOS  \n")
while temas != []:
  while pessoas != []:
    tema_sorteado = temas[random.randrange(len(temas))]
    pessoa_sorteada = pessoas[random.randrange(len(pessoas))]
    
    temas.remove(tema_sorteado)
    pessoas.remove(pessoa_sorteada)
    
    print('O aluno ' + pessoa_sorteada + ' terá o tema ' + tema_sorteado)
print()