# geo-explorer
Projeto de exploração de trilhas de aprendizagem, desafios de programação e certificados fictícios, com testes automatizados e integração com MCP

🌍 Geo-Explorer

Sobre o projeto

O Geo-Explorer é um projeto desenvolvido em Python com o objetivo de explorar trilhas de aprendizagem, gerar desafios de programação e emitir certificados fictícios de conclusão.

A aplicação foi criada como um projeto educacional para praticar lógica de programação, organização de código, testes automatizados e integração com o Model Context Protocol (MCP).

🚀 Funcionalidades

- Trilhas de aprendizagem: consulta informações sobre tecnologias e conteúdos de estudo.
- Desafios de programação: geração de desafios por tecnologia e nível de dificuldade.
- Certificados: geração de certificados fictícios de conclusão de trilhas.
- Testes automatizados: validação das funcionalidades com pytest.
- Integração com MCP: disponibilização de ferramentas para consulta de trilhas e obtenção de desafios.

🛠️ Tecnologias utilizadas

- Python
- JSON
- Pytest
- Model Context Protocol (MCP)
- Git e GitHub

📁 Estrutura do projeto

geo-explorer/
├── data/
│   └── trilhas.json
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── trilhas.py
│   ├── desafios.py
│   └── certificados.py
├── tests/
│   ├── test_trilhas.py
│   ├── test_desafios.py
│   └── test_certificados.py
├── mcp_server.py
├── requirements.txt
├── .gitignore
└── README.md

⚙️ Instalação

Clone o repositório:

git clone https://github.com/SEU-USUARIO/geo-explorer.git
cd geo-explorer

Instale as dependências:

pip install -r requirements.txt

Substitua "SEU-USUARIO" pelo seu nome de usuário no GitHub.

▶️ Como executar

Consultar uma trilha:

python -m src.main trilha --tecnologia Python

Gerar um desafio:

python -m src.main desafio --tecnologia Python --nivel iniciante

Gerar um certificado fictício:

python -m src.main certificado --nome "Seu Nome" --trilha Python

🧪 Testes

Execute os testes automatizados com:

pytest

🔌 Integração com MCP

O projeto inclui um servidor MCP para disponibilizar ferramentas de consulta de trilhas de aprendizagem e obtenção de desafios de programação para clientes compatíveis.

🎯 Objetivos de aprendizagem

- Praticar Python e modularização.
- Trabalhar com arquivos JSON.
- Implementar tratamento de erros.
- Criar testes automatizados.
- Conhecer o protocolo MCP.
- Utilizar GitHub para versionamento e documentação.

👩‍💻 Autoria

Projeto educacional desenvolvido para o desafio da DIO.

📄 Licença

Este projeto é disponibilizado para fins educacionais.