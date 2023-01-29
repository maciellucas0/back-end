
Sobre o desafio
Você recebeu um arquivo CNAB com os dados das movimentações financeiras de várias lojas. Precisamos criar uma maneira para que estes dados sejam importados para um banco de dados.
Sua tarefa é criar uma interface web que aceite upload do arquivo CNAB, normalize os dados e armazene-os em um banco de dados relacional e exiba essas informações em tela.

Instruções:

Crie seu ambiente virtual:
python -m venv venv
Ative seu venv:
# linux:
source venv/bin/activate

# windows:
.\venv\Scripts\activate
Atualize o pip
 pip install --upgrade pip
Instale as dependências
pip install -r requirements.txt
Execute as migrações
python manage.py migrate
