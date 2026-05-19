FROM python:3.11-slim

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Criar usuário não-root
RUN useradd -m -u 1000 appuser
WORKDIR /app

# Copiar requirements primeiro para cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o resto do código
COPY . .

# Mudar para usuário não-root
USER appuser

# Expor porta para Streamlit (8501)
EXPOSE 8501

# Comando padrão
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
