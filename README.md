# Gerencia-Oficina

Este projeto consiste em um sistema de gerenciamento de oficina, facilitando o controle de ordens de serviço e produtos em estoque. Ele foi desenvolvido para atender às necessidades dos donos de oficinas, proporcionando uma maneira eficiente de gerenciar seus serviços, clientes e inventários.

## Tecnologias Utilizadas

- **Python**: Usado para a lógica de backend e processamento dos dados.
- **Django**: Framework web utilizado para construir e manter o backend do projeto.
- **HTML**: Utilizado para estruturar e exibir o conteúdo das páginas web.
- **Tailwind CSS**: Framework de CSS utilizado para estilizar as páginas web de forma eficiente e responsiva.

## Funcionalidades

- **Cadastro de Clientes**: Permite o registro e gerenciamento de informações dos clientes da oficina.
- **Cadastro de Veículos**: Facilita o registro de veículos associados aos clientes.
- **Gerenciamento de Serviços**: Controle completo de serviços realizados na oficina, incluindo datas e descrições dos serviços.
- **Gerenciamento de Estoque**: Controle e monitoramento de produtos em estoque, permitindo atualizações em tempo real.

## Como Executar

1. Clone o repositório:
```
git clone https://github.com/gusluz/Gerencia-Oficina.git
```

2. Navegue até o diretório do projeto:
```
cd Gerencia-Oficina
```

3. Crie um ambiente virtual para evitar a instalação global das dependências:
```
python -m venv venv
```

4. Ative o ambiente virtual:
- No Windows:
```
venv\Scripts\activate
```
- No macOS e Linux:
```
source venv/bin/activate
```

5. Instale as dependências necessárias:
```
pip install -r requirements.txt
```

6. Navege para 'oficina' e execute as migrações do banco de dados:
```
cd oficina
python manage.py migrate
```

7. Inicie o servidor:
```
python manage.py runserver
```

8. Crie um usuario:
- teste@teste.com
- Tt123456

