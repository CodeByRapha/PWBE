# PWBE - Formativa
# GUIA DE EXECUÇÃO DO PROJETO


# REQUISITOS INICIAIS:

-O sistema deve ser executado em um servidor com Windows para garantir que todos os comandos funcionem conforme esperado. 
-Em outros sistemas operacionais, pode ser necessário adaptar alguns comandos.

-É fundamental ter o Python instalado na máquina;
-O Visual Studio Code também deve estar configurado para reconhecer o Python;
-O MySQL Workbench precisa estar previamente instalado, pois será utilizado para a criação do banco de dados.

# CONFIGURAÇÃO DO BANCO DE DADOS:

- Inicie o MySQL Workbench;
- Abra o banco de dados correspondente ao projeto no aplicativo;
- No arquivo settings.py, entre as linhas 99 e 108, insira os dados corretos da conexão para que a aplicação funcione corretamente.

# EXECUÇÃO DA APLICAÇÃO:

- Siga os passos abaixo para rodar o sistema:

- Abra o projeto no Visual Studio Code;
- Pressione CTRL + J para abrir o terminal (ou abra manualmente);

- Crie o ambiente virtual com o comando:
    python -m venv env

- Ative o ambiente virtual:
    .\env\Scripts\activate

- Instale os pacotes necessários usando o arquivo requirements.txt:
    pip install -r requirements.txt

- No Workbench, crie o banco de dados e o deixe ativo;
- Retorne ao terminal do projeto

- Faça as migrações:
    python manage.py makemigrations

- Aplique as migrações no banco:
    python manage.py migrate

- Crie um superuser com o comando:
    python manage.py createsuperuser

- Por fim, rode o projeto:
    python manage.py runserver






