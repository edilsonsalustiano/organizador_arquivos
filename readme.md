📂 Organizador de Arquivos com Python

Projeto desenvolvido em Python para automatizar a organização de arquivos da pasta Downloads, separando-os em pastas de acordo com suas extensões.

🎯 Objetivo

Praticar conceitos de Python e desenvolver uma solução simples para automatizar tarefas do dia a dia, utilizando manipulação de caminhos, estruturas condicionais e movimentação de arquivos.

⚙️ Tecnologias utilizadas

Python 3

pathlib — manipulação de caminhos e identificação de arquivos.

shutil — movimentação de arquivos entre pastas.

📁 Como funciona

O programa percorre os arquivos da pasta Downloads e os organiza conforme suas extensões:

Pasta de destino

Extensões

PDF

.pdf

WORD

.docx, .odt, .doc

EXCEL

.xlsx, .xls, .csv

JPEG

.jpeg, .png, .jpg

AVULSO

Outras extensões

Arquivos que não correspondem às categorias definidas são direcionados para a pasta AVULSO.

🚀 Como executar

Instale o Python.

Clone este repositório:

git clone https://github.com/SEU-USUARIO/organizador-arquivos.git

Entre na pasta do projeto:

cd organizador-arquivos

Execute o programa:

python organizador.py

⚠️ Observações

As pastas de destino precisam existir antes da execução.

O programa movimenta os arquivos de verdade; eles deixam de ficar na pasta de origem.

Arquivos com extensões não contempladas pelas categorias são movidos para AVULSO.

Recomenda-se conferir as pastas de destino antes de executar o programa.

📚 Aprendizados

Este projeto foi desenvolvido para praticar:

Path.home() e Path.iterdir();

identificação de arquivos com is_file();

verificação de extensões com suffix;

estruturas condicionais if, elif e else;

movimentação de arquivos com shutil.move().

👨‍💻 Autor

Edilson Salustiano Lima Neto

