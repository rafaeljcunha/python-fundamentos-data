import pandas as pd

df_paises = pd.read_excel("etl/Paises.xlsx")
df_paises.to_csv("paises.csv",sep=";", index=False)

df_distribuidora = pd.read_excel("etl/DistribuidoraDeFilmes.xlsx")
df_distribuidora.to_csv("distribuidoras.csv",sep=";", index=False)

df_genero = pd.read_excel("etl/Gêneros.xlsx")
df_genero.to_csv("generos.csv",sep=";", index=False)

df_tabela_principal = pd.read_excel("etl/TabelaPrincipal.xlsx")
df_tabela_principal.to_csv("principal.csv",sep=";", index=False)