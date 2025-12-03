---
title: "Sprint 8"
description: "Finalizacao do MVP e Deploy"
date: 2025-10-22
draft: false
---

# Sprint 8 - Finalizacao do MVP

**Periodo:** 17/10/2025 a 22/10/2025

## Objetivos da Sprint

- Configurar pipeline de CI/CD automatizada
- Implementar deploy automatico (Vercel + Railway)
- Realizar testes finais de integracao
- Criar documentacao completa do projeto
- Preparar apresentacao final do MVP

## Resultados Esperados

- Pipeline de build funcionando no GitHub Actions
- Deploy automatico em producao
- Documentacao GitPages completa
- MVP pronto para entrega final

## Issues da Sprint

### Issue #68 - Fazer a pipeline da build
**Objetivo:** Configurar pipeline de CI/CD automatizada

**O que fazer:**
- Configurar GitHub Actions para lint e build
- Adicionar validacao de TypeScript no frontend
- Adicionar validacao de Python (Ruff) no backend
- Criar workflow de deploy automatico

**Por que fazer:**
- Automatizar deploy e testes
- Garantir qualidade do codigo
- Reduzir erros em producao

**Pronto quando:**
- ✅ Pipeline configurada no GitHub Actions
- ✅ Testes automatizados rodando
- ✅ Deploy automatico funcionando

**Tamanho:** Media

**Responsavel:** Paulo (Pirata2040)

**Status:** ✅ Concluido

---

### Issue #67 - Fazer a simulacao de dashboard
**Objetivo:** Criar prototipo definitivo do dashboard

**Status:** ✅ Concluido na Sprint 8

---

### Issue #66 - Prototipo definitivo
**Objetivo:** Finalizar prototipo no Figma

**Status:** ✅ Concluido na Sprint 8

---

## Entregas da Sprint

| Item | Status |
|------|--------|
| Pipeline de CI/CD | ✅ Completo |
| Deploy automatico | ✅ Completo |
| Documentacao GitPages | ✅ Completo |
| Testes de integracao | ✅ Completo |
| Apresentacao do MVP | ✅ Completo |

## Tecnologias Implementadas

### GitHub Actions
```yaml
# .github/workflows/ci.yml
name: CI Pipeline
on: [push, pull_request]

jobs:
  lint-frontend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Node
        uses: actions/setup-node@v3
      - name: Install deps
        run: cd frontend && npm install
      - name: Lint
        run: cd frontend && npm run lint
      
  lint-backend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Python
        uses: actions/setup-python@v4
      - name: Install deps
        run: cd backend && pip install -r requirements.txt
      - name: Lint
        run: cd backend && ruff check .
```

### Deploy Configuration

**Frontend (Vercel):**
- Root Directory: `frontend`
- Framework: Next.js
- Build Command: `npm run build`
- Output Directory: `.next`

**Backend (Railway):**
- Root Directory: `backend`
- Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
- Environment: `GEMINI_API_KEY`

## Metricas da Sprint

- **Velocity:** 10 story points
- **Issues fechadas:** 3
- **Commits:** 15+
- **PRs merged:** 8
- **Deploy time:** < 5 minutos

## Documentacao

- [Reunioes](./reunioes)
- [Issues](./issues)

