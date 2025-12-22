## How to Run (For Reviewers)

1. Clone the repository
2. Create a virtual environment
3. Install dependencies from `requirements.txt`
4. Create a `.env` file and add your own `GEMINI_API_KEY`
5. Run the backend with:
   ```bash
   uvicorn backend.main:app --reload
