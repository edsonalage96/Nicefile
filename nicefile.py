import os
import shutil


MAPA_EXTENSOES = {
    'Imagens': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Documentos': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov'],
    'Arquivos_Compactados': ['.zip', '.rar', '.7z', '.tar.gz'],
    'Codigo_Fonte': ['.py', '.java', '.cpp', '.js', '.html', '.css'],
    'Outros': []
}

def organizar():
    pasta_origem = os.getcwd()

    
    for item in os.listdir(pasta_origem):

        if item == 'nicefile.py':
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
            
            print(f"Arquivo '{item}' movido para a pasta '{pasta_destino}'")
    
if __name__ == "__main__":
    organizar()
    print("Organização concluída!")
