# Kindle to Anki Flashcard Automator / Automatizador de Flashcards Kindle-Anki

<!-- Português -->
## 🇧🇷 Português (Portuguese)
[Todo o conteúdo em português aqui...]

Transforma palavras que você clicou/inspencionou no Kindle em cartões do Anki **automaticamente**, no modelo de cartões do Eliezer Piano (YouTuber de aprendizado de idiomas).  

👉 **Vídeo do método do Eliezer Piano**: [Como Usar Anki para Vocabulário](https://www.youtube.com/watch?v=akYH2dafutY&list=PLBb4O15oYCV2PkmQwk9dsGstU4ios7yHl&index=2)  

---  

### 🔥 **O que o projeto faz?**  
1. Pega todas as palavras que você clicou/inspencionou no Kindle (salvas automaticamente no arquivo `vocab.db`).  
2. Busca:  
   - **Definição em inglês** (usando a API gratuita [DictionaryAPI](https://dictionaryapi.dev/)).  
   - **Tradução em português** (usando a API do Google Translate).  
3. Cria cartões no Anki iguais aos do Eliezer Piano:  
   - **Frente**: Palavra em inglês (ex: "restless") + setence (ex: "Do you often feel restless and unable to focus on the task at hand?").  
   - **Verso**: Definição em português(ex: "Não permitir ou proporcionar descanso.") + pronúncia(ex: "/ˈɹɛstləs/") + tradução(ex: "Não permitir ou proporcionar descanso.").  

---  

### ⚡ **Como usar?**  

#### **Passo 1: Instalar o necessário**  
- Tenha Python instalado.  
- Conecte seu Kindle no PC e ache o arquivo `vocab.db` (geralmente em `Kindle/documents/system/vocab.db`).  

#### **Passo 2: Configurar o projeto**  
1. Clone o repositório:  
   ```bash
   git clone https://github.com/seu-usuario/kindle-to-anki.git
   cd kindle-to-anki
2. Instale as dependências:
    ```bash
    pip install -r requirements.txt 
3. Crie um arquivo `.env` e coloque sua chave da Google Translate API (veja como obter abaixo):
    ```bash
    API_KEY = "sua chave de API do google aqui"
([Como pegar sua chave de API do google](https://www.youtube.com/watch?v=zkJlZHsZbTQ))


#### **Passo 3: Rodar o programa**
1. Conecte o Kindle ao PC.
2. Copie o arquivo `vocab.db` (geralmente em `Kindle/documents/system/vocab.db`) para a pasta do projeto asseguirando que o nome `vocab.db` seja mantido.
3. Execute:
    ```bash
    python main.py
4. Os cartões serão gerados em um arquivo csv chamado de saida. Assim é só ir no anki e exportar para qualquer baralho.
---

<!-- English -->
## 🇺🇸 English (Inglês)

Transforms words you've looked up on your Kindle into Anki flashcards **automatically**, following Eliezer Piano's card model (a language learning YouTuber).  

👉 **Eliezer Piano's method video**: [How to Use Anki for Vocabulary](https://www.youtube.com/watch?v=akYH2dafutY&list=PLBb4O15oYCV2PkmQwk9dsGstU4ios7yHl&index=2)  

---  

### 🔥 **What does this project do?**  
1. Extracts all words you've looked up on your Kindle (automatically saved in the `vocab.db` file).  
2. Fetches:  
   - **English definition** (using the free [DictionaryAPI](https://dictionaryapi.dev/)).  
   - **Portuguese translation** (using Google Translate API).  
3. Creates Anki cards following Eliezer Piano's model:  
   - **Front**: English word (e.g., "restless") + example sentence (e.g., "Do you often feel restless and unable to focus on the task at hand?").  
   - **Back**: Portuguese definition (e.g., "Não permitir ou proporcionar descanso.") + pronunciation (e.g., "/ˈɹɛstləs/") + translation (e.g., "Não permitir ou proporcionar descanso.").  

---  

### ⚡ **How to use?**  

#### **Step 1: Install requirements**  
- Have Python installed.  
- Connect your Kindle to PC and locate the `vocab.db` file (usually in `Kindle/documents/system/vocab.db`).  

#### **Step 2: Configure the project**  
1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/kindle-to-anki.git
   cd kindle-to-anki
2. Install dependencies:
    ```bash
    pip install -r requirements.txt 
3. Create a `.env` file and add your Google Translate API key (see how to get it below):
    ```bash
    API_KEY = "your google API key here"
([How to get your Google API key](https://www.youtube.com/watch?v=zkJlZHsZbTQ))


#### **Step 3: Run the program**
1. Connect your Kindle to PC.
2. Copy the `vocab.db` file (usually in `Kindle/documents/system/vocab.db`) to the project folder, making sure to keep the filename as `vocab.db`.
3. Run:
    ```bash
    python main.py
4. Flashcards will be generated in a CSV file named "saida" (output). Just import this into Anki to any deck you want.
