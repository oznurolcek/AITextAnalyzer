# AI Text Analyzer

AI Text Analyzer is a text analysis application powered by Google Gemini.  

The backend is built with FastAPI and the project is designed to run using Docker so that it can be executed on any machine without local Python or dependency issues.

Steps to run the project:

1. Clone the repository

```bash
git clone https://github.com/oznurolcek/AITextAnalyzer.git
cd AITextAnalyzer
```

2. Create a .env file in the root directory and add your Gemini API key

GEMINI_API_KEY=your_gemini_api_key_here

3. Build the Docker images

```
docker compose build
```

4. Run the application

```
docker compose up
```

After the containers start, 

The backend will be available at: http://localhost:8000

The frontend will be available at: http://localhost:8080


Notes:
- .env and .venv files are ignored and not committed.
- The project is intended to be run via Docker.
- Local Python setup is optional and not required.