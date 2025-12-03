---
title: "Reunioes da Sprint 9"
description: "Registro das reunioes realizadas durante a Sprint 9"
date: 2025-10-28
draft: false
---

# Reunioes da Sprint 9

## Relatorio da Reuniao
23 de Outubro de 2025

**Data:** 23/10/25  
**Formato:** Reuniao online  
**Tema:** Automacao de infraestrutura e qualidade de software

---

## 1. Sumario

* Configuracao da API do Querido Diario para ranking
* Implementacao de Docker e Docker Compose
* Setup de Integracao Continua (CI)
* Configuracao de ferramentas de qualidade (Black, Flake8)
* Implementacao de testes automatizados com pytest
* Criacao de scripts de automacao
* Padronizacao de envio de dados para API

---

## 2. Topicos Abordados

**Infraestrutura e DevOps:**

A equipe priorizou a automacao completa da infraestrutura e processos de desenvolvimento. As principais iniciativas foram:

1. **Containerizacao com Docker:** Criacao de Dockerfiles para frontend (Next.js) e backend (FastAPI), com Docker Compose orquestrando ambos os servicos. Isso eliminou problemas de "funciona na minha maquina" e padronizou o ambiente de desenvolvimento

2. **Pipeline de CI/CD:** Configuracao completa de GitHub Actions com workflows para:
   - Lint automatico (ESLint para frontend, Ruff para backend)
   - Testes automatizados (pytest)
   - Build e validacao
   - Deploy automatico

3. **Qualidade de codigo:** Implementacao de Black (formatador) e Flake8 (linter) para garantir consistencia e aderencia ao PEP 8. Pre-commit hooks instalados para validacao antes de cada commit

**Testes e Validacao:**

* Suite completa de testes com pytest cobrindo:
  - Testes unitarios para logica de negocios
  - Testes de integracao para APIs externas
  - Testes de endpoints da API
  - Cobertura de 60%+ alcancada

**Novas Funcionalidades:**

* API de ranking integrada com Querido Diario para mostrar top 3 subcategorias
* Schemas Pydantic para validacao automatica de dados
* Scripts utilitarios para tarefas comuns (setup, clean, backup, deploy)

---

## 3. Issues da Sprint 9

* **#75 - Configurar a API do querido diario para a pagina de ranking** - backend / DevOps
  * Integrar API do Querido Diario
  * Processar dados de ranking
  * Retornar top 3 subcategorias

* **#73 - Fazer o script de tarefa** - Automatizacao / backend / DevOps
  * Criar scripts de setup e deploy
  * Automatizar tarefas repetitivas
  * Documentar uso dos scripts

* **#72 - Automacao da Infraestrutura - Docker e YamL** - Automatizacao / DevOps / documentation
  * Dockerfiles para frontend e backend
  * Docker Compose para orquestracao
  * Documentar processo de containerizacao

* **#71 - Integracao Continua(CI) - Fazer automatizacao** - Automatizacao / backend / DevOps
  * GitHub Actions workflows
  * Validacao automatica de PRs
  * Deploy automatico em producao

* **#70 - Qualidade de Software - Blacks/flacke8** - Arquitetura / DevOps / Requisitos
  * Configurar Black e Flake8
  * Pre-commit hooks
  * Formatar codigo existente

* **#69 - Testes Automatizados (Pyteste e outros)** - Automatizacao / DevOps / testing
  * Suite de testes com pytest
  * Cobertura de 60%+
  * Testes unitarios e de integracao

* **#65 - Configuracao do envio de dados para API** - Automatizacao / backend
  * Schemas Pydantic
  * Validacao automatica
  * Documentacao OpenAPI

---

## 4. Decisoes Tomadas

**Estrategia de Containerizacao:**
- Docker para desenvolvimento e producao
- Docker Compose para ambiente local
- Imagens otimizadas (multi-stage builds)

**Qualidade de Codigo:**
- Black como formatador oficial (linha de 88 caracteres)
- Flake8 para linting com regras customizadas
- Pre-commit hooks obrigatorios para todos

**Testes:**
- Pytest como framework principal
- Cobertura minima de 60% exigida
- Testes rodando automaticamente no CI

**Scripts de Automacao:**
- Scripts em Bash para tarefas comuns
- Documentacao clara de uso
- Versionados no repositorio

---

## 5. Metricas da Sprint

| Metrica | Valor |
|---------|-------|
| Story points planejados | 14 |
| Story points entregues | 14 |
| Velocity | 14 |
| Taxa de conclusao | 100% |
| Issues fechadas | 7 |
| Commits realizados | 35+ |
| Pull requests merged | 18 |
| Cobertura de testes | 62% |

---

## 6. Impacto das Melhorias

**Reducao de tempo:**
- Setup de ambiente: 60min → 5min (Docker)
- Deploy manual: 30min → automatico
- Validacao de codigo: 15min → automatica

**Melhoria de qualidade:**
- Bugs em producao: reducao de 70%
- Codigo inconsistente: eliminado (Black)
- Regressoes: prevenidas (testes)

---

## 7. Licoes Aprendidas

**O que funcionou bem:**
- Docker eliminou problemas de ambiente
- Pre-commit hooks preveniram codigo mal formatado
- Testes automatizados deram confianca para refatorar
- Scripts agilizaram tarefas repetitivas

**Desafios enfrentados:**
- Curva de aprendizado do Docker
- Configuracao inicial do pytest demorada
- Flake8 encontrou muitos problemas no codigo legado

**Acoes de melhoria:**
- Documentar padroes de teste
- Criar mais scripts utilitarios
- Aumentar cobertura de testes para 80%

---

## 8. Proximos Passos

- Aumentar cobertura de testes
- Adicionar testes E2E
- Melhorar documentacao da API
- Otimizar imagens Docker

---

## Resumo

* **Sprint:** 9
* **Periodo:** 23/10/25 a 28/10/25
* **Status:** Concluido
* **Foco:** Automacao completa da infraestrutura com Docker, implementacao de CI/CD com GitHub Actions, configuracao de ferramentas de qualidade (Black, Flake8) e criacao de suite de testes automatizados. Integracao da API de ranking finalizada.

---

## Participantes

- Pedro Araujo (pedroalucena04)
- Isabella (isalima2004)
- Giulia Paulucci (GiuliaPaulucci)
- Rodrigo (Fofodoido)
- Blaze Morales (Blazemorales)
- Ana Nunes (ananunesv)
- Paulo (Pirata2040)
- Pedro Ramos (PedroRSR)

---

## Anexos

### Configuracoes Implementadas

**Docker Compose:**
```yaml
version: '3.8'
services:
  backend:
    build: ./backend
    ports: ["8001:8001"]
    environment:
      GEMINI_API_KEY: ${GEMINI_API_KEY}
  frontend:
    build: ./frontend
    ports: ["3000:3000"]
    depends_on: [backend]
```

**GitHub Actions:**
```yaml
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run tests
        run: cd backend && pytest
```

**Pytest:**
```python
# pytest.ini
[pytest]
testpaths = tests
python_files = test_*.py
python_functions = test_*
```

