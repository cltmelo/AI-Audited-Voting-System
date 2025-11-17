const ethers = require("ethers");
const fs = require('fs');
const path = require('path');


const contractJsonPath = path.resolve(__dirname, './build/contracts/Voting.json');

function getContractData() {
    try {
        console.log(`[DEBUG] Lendo contrato de: ${contractJsonPath}`);
        
        const data = fs.readFileSync(contractJsonPath, 'utf8');
        const contractJson = JSON.parse(data);
        const CONTRACT_ABI = contractJson.abi;
        
        const networkId = "5777"; // Confirmado pela sua imagem
        
        if (!contractJson.networks || !contractJson.networks[networkId]) {
            throw new Error(`Contrato não encontrado. Verifique se o 'Voting.json' contém dados da rede "5777".`);
        }
        
        const CONTRACT_ADDRESS = contractJson.networks[networkId].address;

        if (!CONTRACT_ABI || !CONTRACT_ADDRESS) {
            throw new Error("Não foi possível encontrar ABI ou Endereço no JSON.");
        }
        
        return { CONTRACT_ABI, CONTRACT_ADDRESS };

    } catch (err) {
        console.error("--- ERRO AO CARREGAR CONTRATO ---");
        console.error(err.message);
        console.error("Você rodou 'truffle migrate --reset'?");
        console.error("-----------------------------------");
        process.exit(1);
    }
}

const { CONTRACT_ABI, CONTRACT_ADDRESS } = getContractData();

const PROVIDER_URL_WS = "ws://127.0.0.1:7545"; // WebSocket (para eventos)
const PROVIDER_URL_HTTP = "http://127.0.0.1:7545"; // HTTP (para buscas)



async function main() {
    console.log("Iniciando o Auditor Forense (Listener)...");
    
    const wsProvider = new ethers.WebSocketProvider(PROVIDER_URL_WS);
    const httpProvider = new ethers.JsonRpcProvider(PROVIDER_URL_HTTP);

    const contract = new ethers.Contract(CONTRACT_ADDRESS, CONTRACT_ABI, wsProvider);

    console.log("----------------------------------------");
    console.log(` AUDITOR CONECTADO `);
    console.log(` > Contrato: ${contract.target}`); // AGORA VAI FUNCIONAR, DIABO
    console.log(` > Escutando eventos 'VoteCast'...`);
    console.log("----------------------------------------");

    contract.on("VoteCast", async (voter, proposalId, eventPayload) => {
        try {
            console.log(`[VOTO DETECTADO] 🗳️: ${voter} -> Proposta ${proposalId.toString()}`);

            const txCount = await httpProvider.getTransactionCount(voter);
            console.log(`  > Contagem de Tx (Idade): ${txCount}`);

            const txHash = eventPayload.log.transactionHash;
            const receipt = await eventPayload.getTransactionReceipt();
            const tx = await eventPayload.getTransaction();

            if (tx.gasPrice && receipt.gasUsed) {
                const gasCost = tx.gasPrice * receipt.gasUsed; 
                console.log(`  > Custo do Gás: ${ethers.formatEther(gasCost)} ETH`);
            }
            
            const balance = await httpProvider.getBalance(voter);
            const formattedBalance = ethers.formatEther(balance); 
            console.log(`  > Saldo Atual: ${formattedBalance} ETH`);

            const data = {
                voter: voter,
                proposal: proposalId.toString(),
                txCount: txCount,
                txHash: txHash,
                balance: formattedBalance,
                timestamp: new Date().toISOString()
            };

            saveDataForAI(data);
            console.log("----------------------------------------");

        } catch (err) {
            console.error("Erro ao processar evento 'VoteCast':", err);
            console.log("----------------------------------------");
        }
    });
}


const DATA_DIR = path.resolve(__dirname, 'data');
const DB_FILE = path.resolve(DATA_DIR, 'audit_database.json');

function saveDataForAI(data) {
    console.log(`  > Salvando dados para o LLM em ${DB_FILE}...`);
    
    if (!fs.existsSync(DATA_DIR)) {
        fs.mkdirSync(DATA_DIR);
        console.log(`  > Pasta 'data' criada.`);
    }

    let database = [];
    if (fs.existsSync(DB_FILE)) {
        try {
            database = JSON.parse(fs.readFileSync(DB_FILE));
        } catch (err) {
            database = [];
        }
    }
    database.push(data);
    fs.writeFileSync(DB_FILE, JSON.stringify(database, null, 2));
}



main().catch((error) => {
    // Este erro 'ECONNREFUSED' pode ser pego aqui se o wsProvider falhar na inicialização
    if (error.code === 'ECONNREFUSED') {
        console.error("-----------------------------------");
        console.error("ERRO FATAL: Conexão recusada.");
        console.error("Verifique se o Ganache está rodando na porta 7545.");
        console.error("-----------------------------------");
    } else {
        console.error("Erro fatal no listener:", error);
    }
    process.exit(1);
});