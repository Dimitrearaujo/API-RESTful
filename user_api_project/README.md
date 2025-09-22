
# API de Cadastro de Usuários

Este projeto é uma API RESTful simples desenvolvida com **Flask** para o cadastro, atualização, remoção e visualização de usuários.

## Funcionalidades
- **GET /users**: Retorna todos os usuários cadastrados.
- **GET /users/{id}**: Retorna um usuário específico pelo ID.
- **POST /users**: Cria um novo usuário.
- **PUT /users/{id}**: Atualiza um usuário existente.
- **DELETE /users/{id}**: Exclui um usuário pelo ID.

## Como Rodar o Projeto

1. Clone este repositório para seu computador:
   ```bash
   git clone https://github.com/SEU_USUARIO/user-api.git
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd user-api
   ```

3. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use venv\Scripts\activate
   ```

4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

5. Execute a API:
   ```bash
   python app/user_api.py
   ```

A API estará disponível em `http://127.0.0.1:5000`.

## Testando a API

- **Criar usuário**: Envie uma solicitação POST para `http://127.0.0.1:5000/users` com um corpo JSON:
  ```json
  {
    "name": "João Silva",
    "email": "joao.silva@example.com"
  }
  ```
- **Listar usuários**: Envie uma solicitação GET para `http://127.0.0.1:5000/users`.
- **Atualizar usuário**: Envie uma solicitação PUT para `http://127.0.0.1:5000/users/1` com os dados que deseja atualizar.
- **Deletar usuário**: Envie uma solicitação DELETE para `http://127.0.0.1:5000/users/1`.

## Contribuindo

1. Fork o repositório.
2. Crie uma nova branch (`git checkout -b feature-nome-da-feature`).
3. Faça suas alterações e commit (`git commit -am 'Adiciona nova feature'`).
4. Faça push para a branch (`git push origin feature-nome-da-feature`).
5. Abra um pull request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
