# Easy Agent
This is the implementation of a personal smart agent with FastAPI. With this example, you will be able to understand the basic aspects of creating an agent with CrewAI and perform queries through API calls.

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

#### 1 - clone project
```bash
  git clone https://github.com/rlbessa/mariza.git && cd mariza
```

#### 2 - init virtual environment:
```bash
  python -m venv .venv
```
OR
```bash
  python3 -m venv .venv
```

#### 3 - join virtual environment:
```bash
  source .venv/bin/activate
```

#### 4 - install uv:
```bash
  pip install uv
```

#### 5 - install dependencies:
```bash
  uv sync
```

#### 6 - install dev depencencies (optional):
```bash
  uv sync --extra dev
```

#### 7 - install ollama:
```bash
  curl -fsSL https://ollama.com/install.sh | sh
```

#### 8 - pull embedding model:
```bash
  ollama pull nomic-embed-text
```

## Running the Project

#### Join Virtual environment
```bash
  .venv\Scripts\activate
```

Argumentos:
- "--host"
  (default: 127.0.0.1)
  (type: str)
    
- "--port"
  (default: 8000)
  (type: int) 
 
- "--reload"
  (action: store_true)
    
- "--workers"
  (default: 1)
  (type: int)

- "--log-level"
  (default: info)
  (choices: ["debug", "info", "warning", "error"])

#### Using script
```bash
  python start_api.py --reload --log-level debug
```

#### Using direct uvicorn (edit host and port)
```bash
  uvicorn upubly.main:app --host 127.0.0.1 --port 8000 
```

#### Using uv run
```bash
  uv run main
```

## Using API

**Add llm's `PLATFORM_API_KEY` into the `.env` file**
The API start listening at `http://localhost:8000`

## cURL map

#### General Agent:

```bash
    curl -X POST "http://localhost:8000/" \
      -H "Content-Type: application/json"
```

```bash
    curl -X POST "http://localhost:8000/process" \
      -H "Content-Type: application/json" \
      -d '{
        "context": "Inserir conteúdo ou dúvida",
        "language": "Portuguese"
      }'
```


## Documentation:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
- TOS: `http://upubly.com/tos`
- Privacy Policy: `http://upubly.com/privacy-policy`
