# --- Estágio 1: Builder ---
# Usamos uma imagem base completa do Python que inclui ferramentas de compilação.
FROM python:3.10 as builder

# Instala as dependências de sistema necessárias, como o compilador Rust (cargo).
# Isso é necessário para pacotes como 'pydantic-core'.
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    cargo \
    && rm -rf /var/lib/apt/lists/*

# Define o diretório de trabalho e cria um ambiente virtual.
WORKDIR /app
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copia apenas o arquivo de dependências para aproveitar o cache do Docker.
COPY requirements.txt .

# Instala as dependências no ambiente virtual.
RUN pip install --no-cache-dir -r requirements.txt

# --- Estágio 2: Final ---
# Começamos com a imagem leve para a aplicação final.
FROM python:3.10-slim

# Define o diretório de trabalho.
WORKDIR /app

# Copia o ambiente virtual com as dependências já instaladas do estágio 'builder'.
COPY --from=builder /opt/venv /opt/venv

# Copia o código da aplicação.
COPY . .

# Ativa o ambiente virtual e define o comando de execução.
ENV PATH="/opt/venv/bin:$PATH"
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

