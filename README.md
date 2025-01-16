# Projeto Fruteirinha

Bem-vindo ao projeto Fruteirinha, uma aplicação web para gerenciar um marketplace de frutas e verduras. Este projeto permite que os usuários visualizem e cadastrem frutas, além de entrar em contato com o administrador do site.

## Funcionalidades

- **Página Inicial**: Exibe as frutas disponíveis e links para as páginas de produtos e contato.
- **Página de Produtos**: Permite o cadastro de novas frutas e exibe a lista de frutas cadastradas.
- **Página de Contato**: Os usuários podem enviar mensagens ao administrador preenchendo um formulário com nome, email, telefone e mensagem.
- **Painel Admin**: Gerencia as informações de contato e frutas cadastradas.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Django**: Framework web utilizado para o desenvolvimento da aplicação.
- **HTML/CSS**: Para a estrutura e estilização das páginas.

## Estrutura do Projeto

- `fruteirinha/`: Contém as views, modelos, templates e arquivos estáticos do projeto.
- `bdtest/`: Diretório principal do projeto Django, contendo configurações e URLs.

## Como Executar o Projeto

1. **Clone o repositório**:
   ```bash
   git clone <URL-do-repositório>
   cd projeto1
   ```

2. **Crie e ative um ambiente virtual**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use: venv\Scripts\activate
   ```

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute as migrações do banco de dados**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Inicie o servidor**:
   ```bash
   python manage.py runserver
   ```

6. **Acesse a aplicação**:
   Abra o navegador e acesse `http://localhost:8000/`.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
