# Chat Multiusuário em Python

Este é um sistema de chat multiusuário síncrono desenvolvido em Python, utilizando a arquitetura cliente/servidor com comunicação via socket. A aplicação permite que múltiplos usuários conversem em tempo real e mantém um histórico de mensagens.

## Funcionalidades

- **Cliente com Interface Gráfica**: Interface utilizando React.
- **Conexão ao Servidor**: O cliente solicita ao usuário um nome e uma porta, e se conecta ao servidor.
- **Histórico de Mensagens**: Cada cliente mantém um histórico de mensagens exibido em sua interface.
- **Notificações de Entrada/Saída**: O servidor notifica todos os clientes quando um novo usuário entra ou sai do chat.
- **Sincronização de Mensagens**: Todas as mensagens são transmitidas para todos os clientes conectados.
- **Verificação de Disponibilidade do Servidor**: O cliente verifica se o servidor está ativo antes de tentar se conectar.

## Pré-requisitos

- Python 3.x
- Tkinter (incluído no Python por padrão)
- Docker

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/larissamato/client-server.git
   cd client-server
   ```
## Como Usar

### Iniciar o Servidor

1. Entre na pasta e adicione as variáveis de ambiente:
   ```bash
   cd server
   cp .env.example .env
   ```
2. Execute o servidor:
   ```bash
   docker-compose up -d
   ```
### Iniciar o Cliente

1. Entre na pasta client e instale as dependências  
   ```bash
   cd client
   npm install
   ```
2. Adicione as variáveis de ambiente:
   ```bash
   cp .env.example .env
   ```
3. Depois execute:
   ```bash
   npm run dev
   ```
4. Abra duas janelas do browser 
   ```bash
   http://localhost:5173/
   ```
