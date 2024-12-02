{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4b0a1fc7-efaa-404d-9a5c-c5c3aa183527",
   "metadata": {},
   "outputs": [],
   "source": [
    "from fastapi import FastAPI, HTTPException\n",
    "from sqlalchemy import create_engine, text\n",
    "\n",
    "# Configuração da conexão com o banco de dados\n",
    "DATABASE_URL = \"postgresql://diegosindeaux:diego123@localhost:5432/postgres\"\n",
    "engine = create_engine(DATABASE_URL)\n",
    "\n",
    "# Criação do app FastAPI\n",
    "app = FastAPI()\n",
    "\n",
    "@app.get(\"/\")\n",
    "def root():\n",
    "    return {\"message\": \"API para consultar dados do PostgreSQL\"}\n",
    "\n",
    "@app.get(\"/dados\")\n",
    "def consultar_dados():\n",
    "    try:\n",
    "        # Consulta SQL\n",
    "        query = \"SELECT * FROM vinculo_escolas_alunos\"\n",
    "        with engine.connect() as connection:\n",
    "            result = connection.execute(text(query))\n",
    "            # Convertendo os resultados para lista de dicionários\n",
    "            dados = [dict(row) for row in result]\n",
    "        return {\"dados\": dados}\n",
    "    except Exception as e:\n",
    "        raise HTTPException(status_code=500, detail=str(e))\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "",
   "name": ""
  },
  "language_info": {
   "name": ""
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
