
# API Rest com Flask e Docker

Este é um projeto de uma **API REST** desenvolvida utilizando **Flask**, com a capacidade de ser executada dentro de um **container Docker**. A API foi projetada para gerenciar um sistema escolar com as funcionalidades básicas de cadastro e consulta de **Professores**, **Turmas** e **Alunos**.

## Funcionalidades

A API oferece as seguintes rotas principais:

- **Professores**
  - `GET /professores` - Retorna todos os professores cadastrados.
  - `POST /professores` - Adiciona um novo professor.
  - `GET /professores/{id}` - Retorna um professor específico.
  - `PUT /professores/{id}` - Atualiza as informações de um professor.
  - `DELETE /professores/{id}` - Deleta um professor.

- **Turmas**
  - `GET /turmas` - Retorna todas as turmas.
  - `POST /turmas` - Cria uma nova turma.
  - `GET /turmas/{id}` - Retorna uma turma específica.
  - `PUT /turmas/{id}` - Atualiza as informações de uma turma.
  - `DELETE /turmas/{id}` - Deleta uma turma.

- **Alunos**
  - `GET /alunos` - Retorna todos os alunos cadastrados.
  - `POST /alunos` - Adiciona um novo aluno.
  - `GET /alunos/{id}` - Retorna um aluno específico.
  - `PUT /alunos/{id}` - Atualiza as informações de um aluno.
  - `DELETE /alunos/{id}` - Deleta um aluno.

## Requisitos

Para rodar esse projeto, você precisará ter o seguinte instalado:

- [Python 3.9+](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/get-started)

## Instalando e Configurando o Ambiente

1. **Clonar o repositório**

   Clone o repositório para o seu ambiente local:
   ```bash
   git clone https://github.com/MIH005/Projeto-Flask-Inicial.git
   cd Projeto-Flask-Inicial
   ```

2. **Criar e Ativar a Virtualenv (opcional, caso queira rodar sem o Docker)**

   Se você não quiser usar o Docker e preferir rodar o projeto localmente, crie e ative um ambiente virtual:

   - Para criar a `virtualenv`:
     ```bash
     python -m venv venv
     ```
   
   - Para ativar o ambiente virtual:
     - No **Windows**:
       ```bash
       .\venv\Scripts\activate
       ```
     - No **Linux/macOS**:
       ```bash
       source venv/bin/activate
       ```

3. **Instalar as dependências**

   Se você estiver usando o ambiente virtual, instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```

4. **Rodando com Docker**

   O projeto também pode ser executado diretamente usando o Docker. Para isso, siga os seguintes passos:

   - **Construir a imagem Docker**:
     ```bash
     docker build -t api_escolar .
     ```

   - **Rodar o container**:
     ```bash
     docker run -p 5000:5000 api_escolar
     ```

   A API estará disponível no endereço: `http://localhost:5000`.

## Testando a API

Você pode testar as rotas da API utilizando o **Postman** ou **Insomnia**. Para testar, basta seguir os exemplos das rotas descritas na seção de funcionalidades.

Aqui estão algumas rotas que você pode testar:

- **GET /professores** - Retorna todos os professores.
- **POST /professores** - Cria um novo professor. Exemplo de corpo da requisição:
  ```json
  {
    "nome": "João Silva",
    "email": "joao@escola.com"
  }
  ```
- **GET /turmas** - Retorna todas as turmas.
- **DELETE /alunos/1** - Deleta o aluno com ID 1.

## Estrutura do Projeto

O projeto possui a seguinte estrutura:

```
.
├── app.py            # Código principal da aplicação Flask
├── Dockerfile        # Arquivo para construção da imagem Docker
├── requirements.txt  # Dependências do projeto
└── README.md         # Este arquivo
```

- **app.py**: Contém a implementação da API com Flask e as rotas definidas.
- **Dockerfile**: Arquivo que define a construção da imagem Docker.
- **requirements.txt**: Contém as dependências necessárias para o funcionamento do Flask.

## Contribuindo

Se você quiser contribuir para esse projeto, basta seguir esses passos:

1. Faça um fork deste repositório.
2. Crie uma branch com a sua feature (`git checkout -b minha-nova-feature`).
3. Faça o commit das suas mudanças (`git commit -am 'Adicionando nova feature'`).
4. Envie para o repositório remoto (`git push origin minha-nova-feature`).
5. Crie uma pull request no GitHub.
