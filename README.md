# API REST BIBLIOTECA 
Uma API simples de gerenciamento de livros com Flask + MySQL.

## Tecnologias
- Python
- Flask
- MySQL
- Postman

## Como usar
1. Clone o repositório
2. Instale as dependências com `pip install -r requirements.txt`
3. Configure o banco de dados MySQL com o script abaixo
4. Mude o usuario e a senha de acordo com o seu MySQL
5. Rode o servidor com `python app.py`

## Funcionalidades
- Criar livro
- Listar todos os livros
- Buscar livro por ID
- Atualizar livro
- Deletar livro

## Script do Banco de Dados (MySQL)

```sql
CREATE DATABASE biblioteca;

USE biblioteca;

CREATE TABLE livros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    autor VARCHAR(255) NOT NULL
);

INSERT INTO livros (titulo, autor) VALUES 
("O Senhor dos Anéis", "J.R.R. Tolkien"),
("Harry Potter e a Pedra Filosofal", "J.K. Rowling"),
("Hábitos Atômicos", "James Clear");

SELECT * FROM livros;

