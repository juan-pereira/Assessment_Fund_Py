import pandas

url = pandas.read_csv("https://sites.google.com/site/dr2fundamentospython/arquivos/Video_Games_Sales_as_at_22_Dec_2016.csv")

filtro_inicial = (url['Genre'] == 'Platform') | (url['Genre'] == 'Action') | (url['Genre'] == 'Shooter')
filtro_de_ano = url['Year_of_Release'] >= 2011

marcas_com_mais_publicacoes = url[filtro_inicial].groupby(['Publisher'])['Publisher'].count().sort_values(ascending=False).head(3)

marcas_com_mais_vendas = url.groupby(['Publisher'])['Global_Sales'].sum().sort_values(ascending=False).head(3)

filtro_marca_action = url[(url['Genre'] == 'Action') & filtro_de_ano].groupby(['Publisher'])['Publisher'].count().sort_values(ascending=False)
filtro_marca_shooter = url[(url['Genre'] == 'Shooter') & filtro_de_ano].groupby(['Publisher'])['Publisher'].count().sort_values(ascending=False)
filtro_marca_platform = url[(url['Genre'] == 'Platform') & filtro_de_ano].groupby(['Publisher'])['Publisher'].count().sort_values(ascending=False)

filtro_mais_vendido_action = url[(url['Genre'] == 'Action') & filtro_de_ano].groupby(['Publisher'])['JP_Sales'].sum().sort_values(ascending=False)
filtro_mais_vendido_shooter = url[(url['Genre'] == 'Shooter') & filtro_de_ano].groupby(['Publisher'])['JP_Sales'].sum().sort_values(ascending=False)
filtro_mais_vendido_platform = url[(url['Genre'] == 'Platform') & filtro_de_ano].groupby(['Publisher'])['JP_Sales'].sum().sort_values(ascending=False)

print("As três marcas que mais publicaram os gêneros de jogos foram: {}".format(marcas_com_mais_publicacoes))
print("As três marcas que mais venderam os gêneros de jogos foram: {}".format(marcas_com_mais_vendas))
print("Mais publicações no gênero Action foi: {}".format(filtro_marca_action.head(1)))
print("Mais publicações no gênero Shooter foi: {}".format(filtro_marca_shooter.head(1)))
print("Mais publicações no gênero Platform foi: {}".format(filtro_marca_platform.head(1)))
print("Mais vendas no gênero Action foi: {}".format(filtro_mais_vendido_action.head(1)))
print("Mais vendas no gênero Shooter foi: {}".format(filtro_mais_vendido_shooter.head(1)))
print("Mais vendas no gênero Platform foi: {}".format(filtro_mais_vendido_platform.head(1)))