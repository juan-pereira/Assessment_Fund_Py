import pandas as pd

url = pd.read_csv("https://sites.google.com/site/dr2fundamentospython/arquivos/Winter_Olympics_Medals.csv")

ano = url['Year'] >= 2001

esportes = (url['Sport'] == 'Skating') | (url['Sport'] == 'Ice Hockey') | (url['Sport'] == 'Skiing') | \
                (url['Sport'] == 'Curling')

medalhas_ouro = url['Medal'] == 'Gold'

total_ouro_NOR = url[(url['NOC'] == 'NOR') & esportes & medalhas_ouro & ano]

total_ouro_SWE = url[(url['NOC'] == 'SWE') & esportes & medalhas_ouro & ano]

total_ouro_DEN = url[(url['NOC'] == 'DEN') & esportes & medalhas_ouro & ano]

lista = list(total_ouro_NOR.shape)
conquer_gold_NOR = lista[0]
lista = list(total_ouro_SWE.shape)
conquer_gold_SWE = lista[0]
lista = list(total_ouro_DEN.shape)
conquer_gold_DEN = lista[0]

if conquer_gold_NOR > conquer_gold_SWE and conquer_gold_NOR > conquer_gold_DEN:
    print(f"Noruega é o país nordico que mais conquistou medalhas de ouro, com {conquer_gold_NOR} medalhas")
elif conquer_gold_SWE > conquer_gold_NOR and conquer_gold_SWE > conquer_gold_DEN:
    print(f"Suéçia é o país nordico que mais conquistou medalhas de ouro, com {conquer_gold_SWE} medalhas")
else:
    print(f"Dinamarca é o país nordico que mais conquistou medalhas de ouro, com {conquer_gold_DEN} medalhas")