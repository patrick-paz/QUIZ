Quiz App Readme
Este é o repositório do aplicativo de quiz, uma aplicação interativa para testar seus conhecimentos. Abaixo estão as instruções para configurar e executar o aplicativo em seu ambiente local.

Configuração do Ambiente
1. Configurando o Ambiente Virtual (Python)
bash
Copy code
# Criar um ambiente virtual
python -m venv venv

# Ativar o ambiente virtual (Windows)
venv\Scripts\activate

# Ativar o ambiente virtual (Unix ou MacOS)
source venv/bin/activate
2. Instalando Dependências Python
bash
Copy code
pip install -r requirements.txt
3. Configurando e Executando o FastAPI
bash
Copy code
# Ativar o servidor FastAPI
uvicorn main:app --reload
Acesse http://localhost:8000 para visualizar a API do FastAPI.

Configuração do Frontend
1. Instalando Dependências Node.js
Certifique-se de ter o Node.js instalado. Em seguida, execute:

bash
Copy code
# Instalar dependências do projeto Svelte
npm install
2. Iniciando o Aplicativo Frontend (Svelte)
bash
Copy code
# Iniciar o aplicativo Svelte
npm run dev
Acesse http://localhost:5000 para visualizar o aplicativo frontend.

Contribuição
Sinta-se à vontade para contribuir com melhorias, correções de bugs ou novos recursos. Abra uma issue ou envie uma solicitação de pull request.

Divirta-se explorando o mundo do conhecimento com o nosso aplicativo de quiz!






