# AI Text Analyzer

AI Text Analyzer is a backend service built with FastAPI and powered by Google Gemini.

Requirements:
- Docker
- Docker Compose

Python or a virtual environment is NOT required when running the project with Docker.

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
The forend will be available at: http://localhost:8080


Notes:
- .env and .venv files are ignored and not committed.
- The project is intended to be run via Docker.
- Local Python setup is optional and not required.