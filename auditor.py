import json
import ollama
import os
import sys
import locale
from datetime import datetime

DATA_DIR = "data"
PROMPT_DIR = "prompts"
DATABASE_FILE = os.path.join(DATA_DIR, "audit_database.json") 
SYSTEM_PROMPT_FILE = os.path.join(PROMPT_DIR, "system_prompt.txt")
USER_PROMPT_FILE = os.path.join(PROMPT_DIR, "user_prompt.txt")


REPORT_FILE = "report.txt" 

# Configuração do Modelo
# Para escopos menores, com de teste, sugiro usar modelos mais rapidos que usem o máximo de GPU. "mistral:7b" ou "gemma:2b".
MODELO_LLAMA = "llama3:8b" 
# MODELO_LLAMA = "mistral:7b" 
# MODELO_LLAMA = "gemma:2b" 

# Carregamento dos Dados de Votação 
def carregar_dados_auditoria():
    """Carrega os dados de votação do arquivo JSON."""
    try:
        filepath = os.path.join(os.path.dirname(__file__), DATABASE_FILE)
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if not data:
                print(f"O arquivo '{DATABASE_FILE}' está vazio. Vote primeiro.")
                return None
            return data
    except FileNotFoundError:
        print(f"Erro: Arquivo '{DATABASE_FILE}' não encontrado.")
        print("Certifique-se de que o 'listener.js' rodou e salvou alguns votos.")
        return None
    except Exception as e:
        print(f"Um erro inesperado ocorreu ao ler o arquivo: {e}")
        return None

def carregar_prompt(nome_arquivo):
    """Lê um arquivo de prompt de texto."""
    try:
        filepath = os.path.join(os.path.dirname(__file__), nome_arquivo)
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Erro Crítico: Arquivo de prompt não encontrado: {nome_arquivo}")
        sys.exit(1)
    except Exception as e:
        print(f"Erro ao ler o prompt {nome_arquivo}: {e}")
        sys.exit(1)


# LLM prompt
def gerar_relatorio_auditoria(dados_de_voto):
    """Formata os dados e envia para o LLM local para análise."""
    
    print(f"Iniciando auditoria local para {len(dados_de_voto)} votos...")

    prompt_sistema_template = carregar_prompt(SYSTEM_PROMPT_FILE)
    prompt_usuario_template = carregar_prompt(USER_PROMPT_FILE)

    # Formata o user prompt com os dados de votação
    dados_formatados_json = json.dumps(dados_de_voto, indent=2)
    prompt_usuario_final = prompt_usuario_template.format(dados_json=dados_formatados_json)

    # Monta o prompt completo no formato Llama 3
    prompt_completo = (
        f"<|begin_of_text|><|start_system_prompt|>"
        f"{prompt_sistema_template}"
        f"<|end_system_prompt|><|start_user_prompt|>"
        f"{prompt_usuario_final}"
        f"<|end_user_prompt|><|start_assistant_prompt|>"
    )

    try:
        print("Enviando dados para IA...")
        
        response = ollama.generate(
            model=MODELO_LLAMA,
            prompt=prompt_completo
        )
        
        return response['response'] # Pega o texto da resposta
    
    except Exception as e:
        print(f"Erro ao chamar o Ollama: {e}")
        print("\n--- VERIFICAÇÃO ---")
        print("1. O Ollama está rodando? (Rode 'ollama serve' em outro terminal)")
        print(f"2. O modelo '{MODELO_LLAMA}' está baixado? (Rode 'ollama pull {MODELO_LLAMA}')")
        return None



def salvar_relatorio(relatorio_texto):
    """Salva o relatório final com data e hora em um arquivo .txt na raiz."""
    try:
        # --- Configuração de Data/Hora em ptbr ---
        try:
            # Tenta configurar o locale para Português do Brasil (Linux)
            locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
        except locale.Error:
            try:
                # Tenta configurar para Windows
                locale.setlocale(locale.LC_TIME, 'Portuguese_Brazil.1252')
            except locale.Error:
                # Fallback se o locale não estiver instalado no sistema
                print("Aviso: Locale 'pt_BR' não encontrado. Usando o padrão do sistema.")
        
        now = datetime.now()
        # Formato: sábado, 15 de novembro de 2025 - 21:58:48
        timestamp_str = now.strftime("%A, %d de %B de %Y - %H:%M:%S")
        
        # --- Montagem do Relatório Final ---
        relatorio_completo = (
            f"--- RELATÓRIO DE AUDITORIA ---\n"
            f"Gerado em: {timestamp_str}\n"
            f"----------------------------------\n\n"
            f"{relatorio_texto}"
        )

        filepath = os.path.join(os.path.dirname(__file__), REPORT_FILE)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(relatorio_completo)
            
        print(f"\nRelatório salvo com sucesso em: {filepath}")
    
    except Exception as e:
        print(f"Erro ao salvar o relatório em '{REPORT_FILE}': {e}")

def main():
    dados = carregar_dados_auditoria()
    
    if dados:
        relatorio = gerar_relatorio_auditoria(dados)
        if relatorio:
            print("\n--- 📜 RELATÓRIO DE AUDITORIA (Llama 3) 📜 ---") #obg gpt por deixar bonitinho
            print(relatorio)
            print("---------------------------------------------")
            
            salvar_relatorio(relatorio)

if __name__ == "__main__":
    main()