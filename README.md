# AI-Audited Voting System: Sistema de Votação com Auditoria de IA      **ATUALIZAR ESSE README DEPOIS!!!!!!**

![Solidity](https://img.shields.io/badge/Solidity-0.8.0+-363636?logo=solidity)
![Truffle](https://img.shields.io/badge/Truffle-5.x-yellow)
![Node.js](https://img.shields.io/badge/Node.js-18+-green?logo=nodedotjs)
![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.111.0-009688?logo=fastapi)
![Ollama](https://img.shields.io/badge/Ollama-0.1.33+-black?logo=ollama)
![Llama3](https://img.shields.io/badge/Llama3-8B-orange)
![MySQL](https://img.shields.io/badge/MySQL-8.0+-orange?logo=mysql)
![ethers.js](https://img.shields.io/badge/ethers-6.x-253cdd)
![License](https://img.shields.io/badge/License-MIT-green)

Aplicação híbrida (Web 2.5 + Web 3) que combina um sistema de votação descentralizado em Ethereum com um backend de autenticação Python/MySQL e um avançado sistema de auditoria forense off-chain baseado em IA (Llama 3 local via Ollama). Projetado para garantir a integridade da votação e detectar padrões de fraude, como Ataques Sybil, sem comprometer o consenso da blockchain.

## ✨ Objetivos do Projeto
- Implementar um sistema de votação descentralizado transparente e imutável via contratos inteligentes.
- Adicionar uma camada de autenticação tradicional (Web 2.0) com Python/MySQL para gerenciamento de eleitores.
- Desenvolver um coletor de eventos Node.js (`listener.js`) para monitorar a blockchain em tempo real.
- Integrar um LLM local (Llama 3 via Ollama) para análise forense de padrões de votação.
- Gerar relatórios de auditoria detalhados, focando na detecção de fraudes como Ataques Sybil.
- Servir como uma base didática para projetos que mesclam tecnologias Web2 e Web3 com IA local.

## 🧱 Arquitetura do Sistema
O projeto é composto por componentes independentes que interagem para formar um ecossistema robusto.

	├── blockchain-voting-dapp            # Root directory of the project.
		├── build                         # Directory containing compiled contract artifacts.
		|   └── contracts                 
		|       ├── Migrations.json       
		|       └── Voting.json           
		├── contracts                     # Directory containing smart contract source code.
		|   ├── 2_deploy_contracts.js     
		|   ├── Migrations.sol            
		|   └── Voting.sol
		├── data                          # Directory containing database for audit by AI.
		|   └── audit_database.json
		├── Database_API                  # API code for database communication.
		|   └── main.py
		|   └── .env
		├── migrations                    # Ethereum contract deployment scripts.
		|   └── 1_initial_migration.js    
		├── node_modules                  # Node.js modules and dependencies.
		├── prompts                       # System and user prompts for LLM.
		|   └── system_prompt.txt
		|   └── user_prompt.txt
		├── public                        # Public assets.              
		├── src                           
		|   ├── assets                    # Project images.              
		|   ├── css                       # CSS stylesheets.
		|   |   ├── admin.css             
		|   |   ├── index.css             
		|   |   └── login.css             
		|   ├── dist                      # Compiled JavaScript bundles.
		|   |   ├── app.bundle.js               
		|   ├── html                      # HTML templates.
		|   |   ├── admin.html            
		|   |   ├── index.html            
		|   |   └── login.html            
		|   └── js                        # JavaScript logic files.
		|       ├── app.js                
		|       └── login.js              
		├── .env
		├── index.js                      # Main entry point for Node.js application.
		├── listener.js                   # Blockchain events colector for Node.js application.
		├── auditor.py                    # Ai auditor.
		├── package.json                  # Node.js package configuration.
		├── package-lock.json             # Lockfile for package dependencies.
		├── README.md                     # Project documentation.
		└── truffle-config.js             # Truffle configuration file.

**Fluxo de Dados:**
		Usuário (login.html) $\rightarrow$ Backend (FastAPI/MySQL) $\rightarrow$ Frontend (admin/index.html via MetaMask) $\leftrightarrow$ Blockchain (Voting.sol). O Contrato Voting.sol *emite eventos* $\rightarrow$ Coletor (listener.js) *ouve* e *coleta dados* $\rightarrow$ `data/audit_database.json` $\rightarrow$ Auditor de IA (auditor.py) *lê e analisa* com Ollama/Llama 3 $\rightarrow$ `report.txt`.

## 🔧 Requisitos
-   **Sistema Operacional:** Linux, macOS, ou WSL2 (para Windows).
-   **Node.js:** v18+ e `npm` (recomendado usar `nvm`).
-   **Python:** v3.9+ e `pip` (sugestão: usar um ambiente virtual venv ou conda).
-   **MySQL Server:** v8.0+.
-   **Truffle:** Globalmente instalado (`npm install -g truffle`).
-   **Ganache (GUI):** A blockchain pessoal Ethereum (trufflesuite.com/ganache).
-   **MetaMask:** Extensão de navegador.
-   **Ollama:** Servidor local para LLMs (`ollama.com`).
-   **Llama 3:** Modelo baixado no Ollama (`ollama pull llama3`).
-   **Hardware:** GPU NVIDIA com drivers CUDA atualizados é **altamente recomendado** para um bom desempenho da IA.

## 🚀 Guia de Instalação e Execução Local (Crucial para Evitar Erros!)

## Instalação

1. Abra o terminal.

2. Clone o repositório:
        
        git clone LINK CERTO

3. Faça o download e instale o [Ganache](https://trufflesuite.com/ganache/).

4. Crie workspace chamado <b>developement</b>, em truffle projects section adicione `truffle-config.js` clicando em `ADD PROJECT`.

5. Download [Metamask](https://metamask.io/download/) (extensão do navegador).

6. Caso não tenha, crie uma nova carteira, então importe as contas do Ganache.

7. Adicione uma network ao metamask. ( Network name - Localhost 7575, RPC URl - http://localhost:7545, Chain ID - 1337, Currency symbol - ETH)

8. Abra MySQL (**ver fontes externas para instalação e configurações padrão para usar o root como usuário, por exemplo) e crie uma base de dados chamada <b>voter_db</b>. (Não use XAMPP !)
		sudo mysql -u root -p
		CREATE DATABASE voter_db;

8.1. Caso abra um novo terminal para reconectar no mysql, lembresse de entrar na BD.
		USE voter_db; 

9. Com a BD criada, crie uma nova tabela chamada de <b>voters</b> no seguinte formato e adicione alguns valores.


           CREATE TABLE voters (
           voter_id VARCHAR(50) PRIMARY KEY NOT NULL,
           role ENUM('admin', 'user') NOT NULL,
           password VARCHAR(255) NOT NULL
           );
   <br>

        +--------------------------------------+-------+-----------+
        | voter_id                             | role  | password  |
        +--------------------------------------+-------+-----------+
        |                                      |       |           |
        +--------------------------------------+-------+-----------+

9.1. **IMPORTANTE:** Aqui é necessário adicionar pelo menos um "admin" e um "user" na tabela para que possa-se testar a aplicação (exemplo a seguir), pois é nesta tabela que serão armazenados os dados de login tanto para votantes quanto para quem realiza cadastros.


           INSERT INTO voters (voter_id, role, password) VALUES ('adress_1_from_metamask', 'password_1_from_metamask', 'admin');
           INSERT INTO voters (voter_id, role, password) VALUES ('adress_2_from_metamask', 'password_2_from_metamask', 'user');
   <br>

        +--------------------------------------+-------+--------------------------+
        | voter_id                             | role  | password                 |
        +--------------------------------------+-------+--------------------------+
        |adress_1_from_metamask                |admin  |password_1_from_metamask  |
        +--------------------------------------+-------+--------------------------+
        |adress_2_from_metamask                |user   |password_1_from_metamask  |
        +--------------------------------------+-------+--------------------------+

12. Instale o truffle globalmente.
    
        npm install -g truffle
        
13. Instale o browserfy globalmente.
    
        npm install -g browserify

14. Vá para raiz do repositório do projeto e instale os node modules.

        npm install

15. Instale as dependências do python.

        pip install fastapi mysql-connector-python pydantic python-dotenv uvicorn uvicorn[standard] PyJWT



## Usabilidade

#### Nota 1: Atualize as credênciais do banco de dados no arquivo `./Database_API/.env`.

### IMPORTANTE: Este projeto possui múltiplos componentes que precisam ser sincronizados. Siga os passos **EXATAMENTE** para evitar erros.

1. Abra um terminal no diretório do projeto.

2. Execute o Ganache e workspace <b>development</b>.

3. **IMPORTANTE:** Excute os seguinte comandos na raíz do projeto para limpar todo cache local e excluir dados e credenciais antigos que farão o projeto não funionar.

        rm -rf build          # Apaga ABIs e informações de deploy antigos do Truffle
        rm -rf src/dist       # Apaga o bundle JS do frontend (que pode estar com endereço de contrato obsoleto)

4. Excute o seguinte comando na raíz do projeto.

        truffle compile       # Compila Voting.sol e gera novos ABIs em 'build/'

5. Em um novo terminal, façamos o deploy do contrato para a blockchain local.
    
        truffle migrate       # ou use o comando: truffle migrate --reset
    **Recomendação:** Por precaução, rode o comando acima com a flag [--reset].
    Isso implanta o contrato NOVO no Ganache (é bom ANOTAR o endereço do contrato), ou seja, geram novos `Voting.json` e `Migrations.json` em `build/contracts/` com o endereço dos contratos recém-deployados.
    
6. "Empacote" o app.js com o browserify.
    
        browserify ./src/js/app.js -o ./src/dist/app.bundle.js

7. Inicialize o servidor node.
    
        node index.js

8. Vá para o diretório `Database_API` em outro terminal
    
        cd Database_API
    then start the database server by following command

        uvicorn main:app --reload --host 127.0.0.1

Agora todo sistema de votação está configurado! A aplicação estará rodando em http://localhost:8080/.<br>.
Para uma melhor demonstração da votação, veja o vídeo de apresentação do projeto no [YouTube video](LINK AQUI).

9. Comecemos a parte de auditoria via IA: abra um novo terminal na raiz do projeto e incialize outro servidor node para o coletor de dados da votação.
    
        node listener.js
        
10. Por fim, abra um último terminal na raiz do projeto e pode colocar a LLM para trabalhar e gerar nosso relatório (lembresse de veriifcar se o Ollama está rodando e se o ambiente virtual está ativo, se for o caso).
    
        python auditor.py      	
        


## ⚠️ Troubleshooting (Perrengues Comuns)

-   **`network/artifact mismatch` no Console do Navegador:** O frontend (`app.bundle.js`) está tentando usar um contrato que não existe ou tem um endereço diferente do deploy atual no Ganache.
    * **Solução:** Execute a **Fase 1: O "Grande Reset"** completa.
-   **`listener.js` está "surdo" (não detecta votos):** O evento `VoteCast` está sendo emitido, mas os requisitos do contrato (`require`) para as datas de votação não foram atendidos.
    * **Solução:** Faça login como admin (`admin.html`) e defina as datas de início e fim da eleição.
-   **`ECONNREFUSED 127.0.0.1:7545` no terminal do Listener:** O `listener.js` não consegue se conectar à blockchain.
    * **Solução:** Verifique se o Ganache está **rodando** e configurado para a **porta `7545`**.
-   **`auditoR.py` está muito lento:** O Ollama está executando o Llama 3 primariamente na CPU.
    * **Solução:** Verifique `ollama ps`. Se a `PROCESSOR` mostrar uma divisão `CPU/GPU`, a VRAM é insuficiente. Mude o `MODELO_LLAMA` em `auditor.py` para um modelo menor (ex: `mistral:7b`).
-   **"SINUCA DE BICO"** Realizou todas as orientações até aqui e simplesmente a aplicação não conecta com o MetaMask, seja login, seja cadastro, seja votação.
    * **Solução:** Limpe o cache do navegador com um hard refresh (Ctrl + Shift + R) como recurso final.

## 🙏 Agradecimentos e Créditos

Este projeto é uma extensão e adaptação de um sistema de votação descentralizado de código aberto. A base fundamental do DApp, incluindo os contratos Solidity iniciais e a interface de votação, foi desenvolvida por **Krish Depani**.

O trabalho dele serviu como um excelente ponto de partida para este projeto. Você pode encontrar o repositório original aqui:

* **Projeto Base:** [https://github.com/Krish-Depani/Decentralized-Voting-System](https://github.com/Krish-Depani/Decentralized-Voting-System)

## 📄 Licença
MIT
