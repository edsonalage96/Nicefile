# 📂 Nicefile - Organizador Automático de Ficheiros

O **Nicefile** é um script em Python desenvolvido para automatizar a organização de pastas bagunçadas. Ele varre o diretório onde está localizado, identifica a extensão de cada ficheiro e move-o automaticamente para a sua respetiva pasta categórica (Imagens, Documentos, Áudio, Vídeos, etc.). Ficheiros com extensões desconhecidas são movidos com segurança para uma pasta chamada `Outros`.

---

## Funcionalidades

- **Mapeamento Dinâmico**: As categorias e extensões são configuradas externamente via ficheiro `config.json`.
- **Prevenção de Erros**: O script ignora de forma inteligente a si próprio, o ficheiro de configuração e pastas ocultas do sistema (como a pasta `.git`).
- **Pasta de Segurança**: Ficheiros não identificados vão automaticamente para o diretório `Outros`, evitando a perda de dados.

---

## Tecnologias Utilizadas

- **Python 3.x**
- **Biblioteca `os`** (Manipulação de caminhos e diretórios do sistema)
- **Biblioteca `shutil`** (Movimentação eficiente de ficheiros)
- **Biblioteca `json`** (Integração e leitura de dados de configuração externos)
- **Git & GitHub** (Controlo de versão e armazenamento na nuvem)

---

## 📦 Como Instalar e Usar

1. **Clonar o Repositório** (ou descarregar os ficheiros):
   ```bash
   git clone https://github.com
   cd Nicefile
   ```

2. **Configurar as Extensões**:
   Edite o ficheiro `config.json` para adicionar ou remover extensões e pastas conforme a sua necessidade. Se o ficheiro não existir, o script cria um modelo básico na primeira execução.

3. **Executar o Script**:
   Coloque os ficheiros `nicefile.py` e `config.json` dentro da pasta que deseja organizar, abra o terminal nesse diretório e execute:
   ```bash
   python nicefile.py
   ```

---

## ⚙️ Exemplo de Configuração (`config.json`)

```json
{
    "Imagens": [".jpg", ".jpeg", ".png", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
    "Codigo_Fonte": [".py", ".java", ".js", ".html"]
}
```

---
Desenvolvido com o propósito de praticar lógica de programação, manipulação de sistemas de arquivos e integração de dados em Python.
