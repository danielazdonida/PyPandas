import pandas as pd
import functions

arquivo = functions.Functions()

arquivo.readFileExcel('C:/Users/ddonida/Documents/Curso/ReadingExcelFile/example.xlsx')

print(arquivo.lerArquivo())          #mostra o arquivo lido na saída

print('')

print(arquivo.filterColumn('Letras'))         #filtra a tabela: mostra apenas os dados da coluna 'Letras'

print('')

print(arquivo.describe())                    #descrição dos dados da tabela

print('')

print(arquivo.shape())                       #tamanho da tabela (linhasxcolunas)