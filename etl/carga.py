# Importações
import pandas as pd
import pyodbc


# Conexão com o banco de dados
driver = "ODBC Driver 18 for SQL Server"
server = "localhost"
database = "ETL_STAGE"
username = "sa"
password = "Admin@123"

connectionString = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};Encrypt=No;'
connection = pyodbc.connect(connectionString)

cursor = connection.cursor() 

# ETL Distribuidoras
try:
  df_distribuidora = pd.read_excel("etl/DistribuidoraDeFilmes.xlsx")
  cursor.execute("DELETE FROM [DistribuidoraFilmes]")
  df_distribuidora.rename(columns={'Distribuidora de Filmes': 'DescricaoDistribuidora'}, inplace = True)
  for index, row in df_distribuidora.iterrows():
    cursor.execute("Insert into [DistribuidoraFilmes](IdDistribuidora,DescricaoDistribuidora)values(?,?)", int(row.name + 1), row.DescricaoDistribuidora)
  cursor.commit()
except Exception as e:
    cursor.rollback()
    print("Houve um erro ao inserir na tabela 'DistribuidoraFilmes'")
    raise e
finally:
  print("Dados inseridos na tabela 'DistribuidoraFilmes'")
  
#  ETL Gêneros
try:
  df_genero = pd.read_excel("etl/Gêneros.xlsx")
  cursor.execute("DELETE FROM [GeneroFilmes]")
  df_genero.rename(columns={'Gênero': 'DescricaoGenero'}, inplace = True)
  for index, row in df_genero.iterrows():
    cursor.execute("Insert into [GeneroFilmes](IdGenero,DescricaoGenero)values(?,?)", int(index + 1), row.DescricaoGenero)
  cursor.commit()
except Exception as e:
    cursor.rollback()
    print("Houve um erro ao inserir na tabela 'GeneroFilmes'")
    raise e
finally:
  print("Dados inseridos na tabela 'GeneroFilmes'")

# ETL Paises
try:
  df_pais = pd.read_excel("etl/Paises.xlsx")
  df_pais.rename(columns={'País(es) produtor(es) da obra': 'DescricaoPaises'}, inplace = True)
  cursor.execute("DELETE FROM [Paises]")
  for index, row in df_pais.iterrows():
    cursor.execute("Insert into [Paises](IdPaises,DescricaoPaises)values(?,?)", int(index + 1), row.DescricaoPaises)
  cursor.commit()
except Exception as e:
    cursor.rollback()
    print("Houve um erro ao inserir na tabela 'Paises'")
    raise e
finally:
  print("Dados inseridos na tabela 'Paises'")
  
# ETL Tabela Principal
try:
  df_tabela_principal = pd.read_excel("etl/TabelaPrincipal.xlsx")
  df_tabela_principal.drop(columns={"Ano de exibição", "CPB/ROE", "Origem da empresa distribuidora"}, inplace=True)
  df_tabela_principal.rename(columns={
    "Título da obra": "TituloFilme",
    "Gênero": "GeneroFilme",
    "País(es) produtor(es) da obra": "PaisFilme",
    "Nacionalidade da obra": "NacionalidadeFilme",
    "Data de lançamento": "DatadeLancamento",
    "Distribuidora": "DistribuidoraFilme",
    "Público no ano de exibição": "PublicoAnoExibicao",
    "Renda (R$) no ano de exibição": "RendaAnoExibicao"}, inplace=True)
  df_tabela_principal["DatadeLancamento"] = pd.to_datetime(df_tabela_principal["DatadeLancamento"], format=f'%d/%m/%Y', errors="coerce").dt.date
  cursor.execute("DELETE FROM [FilmesLancados]")
  for index, row in df_tabela_principal.iterrows():
    TituloFilme, GeneroFilme, PaisFilme, NacionalidadeFilme, DatadeLancamento, DistribuidoraFilme, PublicoAnoExibicao, RendaAnoExibicao = row
    cursor.execute(
      "Insert into [FilmesLancados](IdFilmesLancados,TituloFilme,GeneroFilme,PaisFilme,NacionalidadeFilme,DatadeLancamento,DistribuidoraFilme,PublicoAnoExibicao,RendaAnoExibicao)values(?,?,?,?,?,?,?,?,?)",
        int(index + 1), TituloFilme, GeneroFilme, PaisFilme, NacionalidadeFilme, DatadeLancamento, DistribuidoraFilme, PublicoAnoExibicao, RendaAnoExibicao)

  cursor.commit()
except Exception as e:
  cursor.rollback()
  print("Houve um erro ao inserir na tabela 'FilmesLancados'")
  raise e
finally:
  print("Dados inseridos na tabela 'FilmesLancados'")


# Encerrando conexão com o banco
cursor.close()
connection.close()