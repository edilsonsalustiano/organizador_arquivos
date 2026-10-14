import shutil
from pathlib import Path


caminho = Path.home() /"Downloads"
pdf = caminho / "PDF"
word = caminho / "WORD"
excel = caminho / "EXCEL"
jpeg = caminho / "JPEG"
avulso = caminho / "AVULSO"

for arquivo in caminho.iterdir():
    if arquivo.is_file():
        if arquivo.suffix == ".pdf":
            print(arquivo.name)
            print(arquivo.suffix)
            destino = shutil.move(arquivo, pdf)
            print(f'Arquivo{arquivo.name} movido para {destino} com sucesso!')

        elif arquivo.suffix in (".xlsx", ".xls", ".csv"):
            print(arquivo.name)
            print(arquivo.suffix)
            destino = shutil.move(arquivo, excel)
            print(f'Arquivo{arquivo.name} movido para {destino} com sucesso!')

        elif arquivo.suffix in (".docx", ".odt", ".doc"):
            print(arquivo.name)
            print(arquivo.suffix)
            destino = shutil.move(arquivo, word)
            print(f'Arquivo{arquivo.name} movido para {destino} com sucesso!')

        elif arquivo.suffix in (".jpeg", ".png", ".jpg"):
            print(arquivo.name)
            print(arquivo.suffix)
            destino = shutil.move(arquivo, jpeg)
            print(f'Arquivo{arquivo.name} movido para {destino} com sucesso!')
        else:
            print(arquivo.name)
            print(arquivo.suffix)
            destino = shutil.move(arquivo, avulso)
            print(f'Arquivo{arquivo.name} movido para {destino} com sucesso!')
        
    else:
        print('Não é um arquivo')