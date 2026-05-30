import os
import shutil
import json

def carregar_configuracao():
    # Caminho do ficheiro de configuração
    caminho_config = "config.json"
    
    # Se o ficheiro JSON não existir, cria um padrão básico
    if not os.path.exists(caminho_config):
        padrao = {"Documentos": [".pdf", ".txt"], "Imagens": [".png", ".jpg"]}
        with open(caminho_config, "w") as f:
            json.dump(padrao, f, indent=4)
        return padrao
        
    # Lê as configurações do JSON
    with open(caminho_config, "r") as f:
        return json.load(f)

def organizar():
    pasta_origem = os.getcwd()
    MAPA_EXTENSOES = carregar_configuracao()
    
    for item in os.listdir(pasta_origem):
        #🔥 Proteção para não mover os ficheiros do próprio script/configuração e Git
        if item in ['nicefile.py', 'config.json'] or item.startswith('.'):
            continue
            
        caminho_item = os.path.join(pasta_origem, item)
        
        if os.path.isfile(caminho_item):
            extensao = os.path.splitext(item)[1].lower()
            categoria_encontrada = False
            
            for categoria, extensoes in MAPA_EXTENSOES.items():
                if extensao in extensoes:
                    pasta_destino = os.path.join(pasta_origem, categoria)
                    if not os.path.exists(pasta_destino):
                        os.makedirs(pasta_destino)
                    shutil.move(caminho_item, pasta_destino)
                    categoria_encontrada = True
                    break
            
            if not categoria_encontrada:
                pasta_destino = os.path.join(pasta_origem, 'Outros')
                if not os.path.exists(pasta_destino):
                    os.makedirs(pasta_destino)
                shutil.move(caminho_item, pasta_destino)
            
            print(f"Ficheiro '{item}' movido para a pasta '{pasta_destino}'")
    
if __name__ == "__main__":
    organizar()
    print("Organização concluída com sucesso!")
