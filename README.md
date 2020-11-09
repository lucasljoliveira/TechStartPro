
# Projeto Cadastro de produtos

Desenvolvedor: Lucas João de Oliveira.
Empresa: Olist
Vaga: Desenvolvedor Python Junior

O projeto tem como objetivo criar um programa que realize operações CRUD (criar, ler, atualizar e excluir) em produtos, que estarão alocados dentro de uma ou mais categorias, estas podendo ser importadas via arquivo CSV contendo o nomes das mesmas.


# Instruções de Instalação
Para executar o programa deve-se executar o arquivo “Product Registration.exe” localizado na pasta “Dist”. Caso seja a primeira execução será criado o banco de dados na pasta do executável, arquivo chamado “product.db”.
Para gerar o executável do programa pode ser utilizado o comando pyinstaller --onefile --windowed “Product Registration.py”.


# Instruções de Utilização

Nos campos de busca (search) pode ser utilizado o caractere ‘%’ para buscar por palavras incompletas. 
Exemplos: 

* Name = “Janela%” para produtos que possuem a palavra “Janela” em no início do nome. 
* Description = “%branco%” para produtos que possuem a palavra “Branco” em qualquer parte da descrição. 
* Category= “%brinquedos” para produtos que possuem a palavra “brinquedos” no final do nome.
Ao criar ou alterar um produto, no campo price utilizar o caractere “.” para valores após a vírgula. Não é necessário o caractere “.” para valores de milhar ou maiores.
Exemplo:
* Price= “10123.01” para o preço R$ 10.123,01.

Nenhum dos campos do produto pode estar em branco, inclusive a seleção de categorias, onde deve haver pelo menos uma.


# Instruções de Teste

Não foi desenvolvido o ambiente de testes.


# Ambiente de trabalho

No desenvolvimento do programa foram utilizadas as seguintes configurações:

Notebook
* Core I7
* 16gb memória RAM
* HD 1 Terabyte 
* GTX 1050 TI
* Windows 10
Visual Studio Code Versão: 1.51.0
Qt Designer Versão: 5.11.1
Python Versão: 3.8.5
* sqlite3 - Nativo
* csv - Nativo
* easygui - Versão: 0.98.1
* sys - Nativo
* PySide2 - Versão:  5.15.1
* PyInstaller - Versão: 3.6
* Pip - Versão: 20.2.4
