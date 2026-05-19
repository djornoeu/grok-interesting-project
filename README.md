**Docker**

### Como rodar com Docker

1. **Build e run com Docker Compose** (recomendado):
   ```bash
   docker compose up --build
   ```

   - Streamlit: http://localhost:8501
   - Jupyter: http://localhost:8888 (token no terminal)

2. **Só Docker (Streamlit)**:
   ```bash
   docker build -t grok-ds .
   docker run -p 8501:8501 grok-ds
   ```

### Arquivos adicionados:
- `Dockerfile` — Imagem otimizada Python slim
- `docker-compose.yml` — Streamlit + Jupyter
- `.dockerignore` — Ignora arquivos desnecessários

