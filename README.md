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

1. Open a terminal.

2. Clone the repository by using the command
        
        git clone https://github.com/Krish-Depani/Decentralized-Voting-System-Using-Ethereum-Blockchain.git

3. Download and install [Ganache](https://trufflesuite.com/ganache/).

4. Create a workspace named <b>developement</b>, in the truffle projects section add `truffle-config.js` by clicking `ADD PROJECT` button.

5. Download [Metamask](https://metamask.io/download/) extension for the browser.

6. Now create wallet (if you don't have one), then import accounts from ganache.

7. Add network to the metamask. ( Network name - Localhost 7575, RPC URl - http://localhost:7545, Chain ID - 1337, Currency symbol - ETH)

8. Open MySQL and create database named <b>voter_db</b>. (DON'T USE XAMPP)

9. In the database created, create new table named <b>voters</b> in the given format and add some values.

           CREATE TABLE voters (
           voter_id VARCHAR(36) PRIMARY KEY NOT NULL,
           role ENUM('admin', 'user') NOT NULL,
           password VARCHAR(255) NOT NULL
           );
   <br>

        +--------------------------------------+-------+-----------+
        | voter_id                             | role  | password  |
        +--------------------------------------+-------+-----------+
        |                                      |       |           |
        +--------------------------------------+-------+-----------+

12. Install truffle globally
    
        npm install -g truffle

14. Go to the root directory of repo and install node modules

        npm install

15. Install python dependencies

        pip install fastapi mysql-connector-python pydantic python-dotenv uvicorn uvicorn[standard] PyJWT

Este projeto possui múltiplos componentes que precisam ser sincronizados. Siga os passos **EXATAMENTE** para evitar erros comuns.

### Fase 1: O "Grande Reset" (Sincronização da Blockchain e Frontend)

**Este passo é CRÍTICO!** Você DEVE executá-lo sempre que:
1.  Clonar o repositório pela primeira vez:
2.  '''bash
3.  git clone [link]
4.  '''
5.  
6.  Modificar o arquivo `blockchain/contracts/Voting.sol`.
7.  O `listener.js` não estiver detectando eventos ou o frontend estiver exibindo `network/artifact mismatch`.

Abra um terminal na **raiz do projeto**:

1.  **Limpar Artefatos Antigos:**
    ```bash
    rm -rf build # Apaga ABIs e informações de deploy antigos do Truffle
    rm -rf src/dist # Apaga o bundle JS do frontend (que pode estar com endereço de contrato obsoleto)
    ```
2.  **Compilar o Contrato:**
    ```bash
    truffle compile # Compila Voting.sol e gera novos ABIs em 'build/'
    ```
3.  **Fazer Deploy do Contrato (Migrar):**
    ```bash
    truffle migrate --reset # Implanta o contrato NOVO no Ganache. ANOTE o endereço do contrato!
    ```
    *Isso gera um novo `Voting.json` em `build/contracts/` com o endereço do contrato recém-deployado.*
4.  **Compilar o Frontend com o Novo Contrato:**
    ```bash
    browserify ./src/js/app.js -o ./src/dist/app.bundle.js
    ```
    *Este comando lê o `Voting.json` recém-gerado e empacota o endereço do contrato e o ABI no `app.bundle.js`. **Este é o passo que evita o `network/artifact mismatch`!***

### Fase 2: Configuração de Banco de Dados e Prompts

1.  **Configurar MySQL:**
    * Acesse o cliente MySQL (`sudo mysql -u root -p`).
    * Crie o banco de dados e a tabela:
        ```sql
        CREATE DATABASE voter_db;
        USE voter_db;
        CREATE TABLE voters (
            id INT AUTO_INCREMENT PRIMARY KEY,
            voter_id VARCHAR(255) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL,
            role VARCHAR(50) NOT NULL DEFAULT 'voter'
        );
        ```
    * **Inserir Usuário Admin Inicial (Obrigatório!):** Sem isso, você não conseguirá logar para configurar a eleição.
        ```sql
        INSERT INTO voters (voter_id, password, role) VALUES ('admin', 'adminpassword', 'admin');
        FLUSH PRIVILEGES;
        EXIT;
        ```
        *Altere 'adminpassword' para uma senha segura.*
    * Crie um arquivo `.env` na raiz do projeto (`SentinelaVote/.env`) com as credenciais do seu MySQL:
        ```env
        MYSQL_HOST=localhost
        MYSQL_USER=root
        MYSQL_PASSWORD=sua_senha_do_root
        MYSQL_DB=voter_db
        ```
        *Adicione `.env` ao seu `.gitignore`.*
2.  **Configurar Prompts da IA:**
    * Crie a pasta `prompts/` na raiz do projeto: `mkdir prompts`.
    * Crie `prompts/system_prompt.txt`:
        ```txt
        You are a blockchain forensic auditor, specializing in detecting
        fraud in decentralized voting systems. Your role is to analyze
        a set of votes in JSON and identify suspicious patterns.

        Be analytical, to the point, and technical in your report.
        ```
    * Crie `prompts/user_prompt_template.txt`:
        ```txt
        Analyze the following voting data. Each record contains:
        - 'voter': The voter's wallet address.
        - 'txCount': The "age" of the wallet (transaction count).
        - 'balance': The ETH balance at the time of voting.
        - 'txHash': The transaction hash.

        TASK:
        **Generate an audit report in Brazilian Portuguese (Português-BR).**
        Focus on identifying:
        1.  **Sybil Attacks:** Look for a large number of votes
            coming from very new wallets (e.g., low 'txCount' like 1, 2, or 3).
            This suggests a single actor created multiple wallets to vote.
        2.  **General Anomalies:** Any other pattern that seems suspicious (e.g., multiple
            votes with identical or very low balances).

        Provide a clear executive summary and, if applicable, a list
        of suspicious wallet addresses, explaining why.

        VOTING DATA (JSON):
        {dados_json}
        ```

### Fase 3: Iniciando os 5 Componentes (Multi-Terminal)

Abra **5 terminais separados** (ou 6, se quiser rodar o auditor de IA em tempo real) na **raiz do projeto**:

1.  **Terminal 1: A Blockchain (Ganache)**
    * Abra o aplicativo **Ganache GUI**.
    * Verifique se ele está rodando na **porta `7545`**.

2.  **Terminal 2: O Backend de Login (Python/FastAPI)**
    ```bash
    cd backend # Navegue para a pasta backend
    uvicorn main:app --reload
    ```

3.  **Terminal 3: O Frontend (Servidor Web)**
    ```bash
    npm run dev # Inicia o lite-server, geralmente em http://localhost:8080
    ```

4.  **Terminal 4: O Coletor de Eventos (Node.js Listener)**
    ```bash
    node listener.js
    ```
    *Você deverá ver: `AUDITOR CONECTADO`, o endereço do contrato e `Escutando eventos 'VoteCast'...`*

5.  **Terminal 5: O Servidor da IA (Ollama)**
    ```bash
    ollama serve
    ```
    *Você também pode usar o aplicativo de desktop do Ollama. Verifique se o modelo `llama3` foi baixado (`ollama pull llama3`).*

### Fase 4: Uso e Geração de Relatório

1.  **Acessar o DApp:** Abra seu navegador em `http://localhost:8080` (ou a porta que seu `npm run dev` indicar).
2.  **Login como Admin:**
    * Use `voter_id: admin` e `password: adminpassword` (ou a que você definiu) em `login.html`.
    * Você será redirecionado para `admin.html`.
    * **IMPORTANTE: Definir as Datas da Eleição!** Este é o **PERRENGUE Comum nº 2**. Se você não definir as datas (`setDates`) no `admin.html`, o contrato não permitirá votos, e o `listener.js` não detectará nada. Cadastre candidatos e defina um período de votação válido.
3.  **Votar como Eleitor (Gerando Dados):**
    * Troque de conta no MetaMask para uma conta diferente do Ganache (ex: Conta 2).
    * Faça um **Hard Refresh (Ctrl+Shift+R ou Cmd+Shift+R)** no navegador para garantir que o DApp carregou o `app.bundle.js` mais recente.
    * Vá para `index.html` e registre um voto.
    * **Verifique o Terminal 4 (Listener):** Você deverá ver o `[VOTO DETECTADO] 🗳️` aparecer com os dados.
    * **Simule Ataque Sybil:** Vote várias vezes com diferentes contas **novas** do Ganache (ex: Conta 3, 4, 5) para gerar dados interessantes para a IA.
4.  **Executar o Auditor de IA:**
    * Abra um **novo terminal (Terminal 6)** na raiz do projeto.
    ```bash
    python auditor_IA.py
    ```
    * **PERRENGUE Comum nº 3 (Lentidão da IA):** Se o auditor estiver muito lento, o Ollama provavelmente está usando a CPU porque o modelo `llama3` é grande demais para sua VRAM.
        * **Solução:** Edite `auditor_IA.py` e mude `MODELO_LLAMA = "llama3"` para `"mistral:7b"` (ou outra versão mais leve como `llama3:8b-instruct-q4_0`). Você pode baixar esses modelos com `ollama pull mistral:7b`.
    * O relatório será impresso no terminal e salvo em `report.txt` na raiz do projeto, em Português-BR e com data/hora.

## ⚠️ Troubleshooting (Perrengues Comuns)

-   **`network/artifact mismatch` no Console do Navegador:** O frontend (`app.bundle.js`) está tentando usar um contrato que não existe ou tem um endereço diferente do deploy atual no Ganache.
    * **Solução:** Execute a **Fase 1: O "Grande Reset"** completa.
-   **`listener.js` está "surdo" (não detecta votos):** O evento `VoteCast` está sendo emitido, mas os requisitos do contrato (`require`) para as datas de votação não foram atendidos.
    * **Solução:** Faça login como admin (`admin.html`) e defina as datas de início e fim da eleição.
-   **`ECONNREFUSED 127.0.0.1:7545` no terminal do Listener:** O `listener.js` não consegue se conectar à blockchain.
    * **Solução:** Verifique se o Ganache está **rodando** e configurado para a **porta `7545`**.
-   **`auditor_IA.py` está muito lento:** O Ollama está executando o Llama 3 primariamente na CPU.
    * **Solução:** Verifique `ollama ps`. Se a `PROCESSOR` mostrar uma divisão `CPU/GPU`, a VRAM é insuficiente. Mude o `MODELO_LLAMA` em `auditor_IA.py` para um modelo menor (ex: `mistral:7b`).

## 🙏 Agradecimentos e Créditos

Este projeto é uma extensão e adaptação de um sistema de votação descentralizado de código aberto. A base fundamental do DApp, incluindo os contratos Solidity iniciais e a interface de votação, foi desenvolvida por **Krish Depani**.

O trabalho dele serviu como um excelente ponto de partida para este projeto. Você pode encontrar o repositório original aqui:

* **Projeto Base:** [https://github.com/Krish-Depani/Decentralized-Voting-System](https://github.com/Krish-Depani/Decentralized-Voting-System)

## 📄 Licença
MIT
