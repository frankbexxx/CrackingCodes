import cifraTransposicaoEncriptaDesencripta as Cted


# mensagem
mensagem = 'Common sense is not so common.'
mensagem2 = 'Hoje é dia de lasanha bolonhesa.'
mensagem3 = 'Underneath a huge oak tree there was of swine a huge company,'
mensagem4 = 'That grunted as they crunched the mast: For that was ripe and fell full fast.'
mensagem5 = 'Then they trotted away for the wind grew high: One acorn they left, and no more might you spy .'
# chave da mensagem
k = 12

crip = Cted.cifra(k, mensagem)

decrip = Cted.decifra(k, crip)

print(crip)

print(decrip)
