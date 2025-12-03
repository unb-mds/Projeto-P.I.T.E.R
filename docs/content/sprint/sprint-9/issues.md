---
title: "Issues da Sprint 9"
description: "Issues trabalhadas durante a Sprint 9"
date: 2025-10-28
draft: false
---

# Issues da Sprint 9

## Issue #75 - Configurar a API do querido diario para a pagina de ranking

**Tipo:** Feature  
**Labels:** backend, DevOps  
**Responsavel:** Pirata2040  
**Status:** ✅ Closed

### O que fazer
Integrar API do Querido Diario especificamente para a funcionalidade de ranking de investimentos

### Por que fazer
Permitir que usuarios visualizem ranking de municipios e subcategorias de investimento

### Pronto quando
- [x] Endpoint de ranking integrado com Querido Diario
- [x] Dados processados e categorizados
- [x] Retorno estruturado para o frontend

### Tamanho
[ ] Pequena [X] Media [ ] Grande

### Descricao Tecnica

Criar endpoint `/ranking` que:
- Busca diarios oficiais por municipio e periodo
- Extrai valores de investimento
- Agrupa por subcategorias
- Retorna top 3 subcategorias mais investidas

---

## Issue #73 - Fazer o script de tarefa

**Tipo:** Task  
**Labels:** Automatizacao, backend, DevOps  
**Responsavel:** Pirata2040  
**Status:** ✅ Closed

### O que fazer
Criar scripts utilitarios para tarefas comuns de desenvolvimento e deploy

### Por que fazer
Automatizar tarefas repetitivas e padronizar processos da equipe

### Pronto quando
- [x] Script de setup do ambiente
- [x] Script de limpeza de cache
- [x] Script de backup de dados
- [x] Documentacao dos scripts

### Tamanho
[X] Pequena [ ] Media [ ] Grande

### Descricao Tecnica

Scripts criados:
```bash
# scripts/setup.sh
# scripts/clean.sh
# scripts/backup.sh
# scripts/deploy.sh
```

---

## Issue #72 - Automacao da Infraestrutura - Docker e YamL

**Tipo:** Feature  
**Labels:** Automatizacao, DevOps, documentation  
**Responsavel:** Pirata2040  
**Status:** ✅ Closed

### O que fazer
Containerizar aplicacao completa com Docker Compose

### Por que fazer
Facilitar setup do ambiente e garantir consistencia entre desenvolvimento e producao

### Pronto quando
- [x] Dockerfile para frontend
- [x] Dockerfile para backend
- [x] Docker Compose configurado
- [x] Documentacao de uso

### Tamanho
[ ] Pequena [ ] Media [X] Grande

### Descricao Tecnica

Infraestrutura completa:
- Frontend: Next.js em container Node 18
- Backend: FastAPI em container Python 3.10
- Volumes para persistencia de dados
- Network bridge entre servicos
- Health checks configurados

---

## Issue #71 - Integracao Continua(CI) - Fazer automatizacao

**Tipo:** Feature  
**Labels:** Automatizacao, backend, DevOps  
**Responsavel:** Pirata2040  
**Status:** ✅ Closed

### O que fazer
Implementar pipeline completa de CI com GitHub Actions

### Por que fazer
Automatizar validacao de codigo e garantir qualidade antes de merge

### Pronto quando
- [x] Workflow de lint configurado
- [x] Workflow de testes configurado
- [x] Workflow de build configurado
- [x] Integracao com PRs

### Tamanho
[ ] Pequena [X] Media [ ] Grande

### Descricao Tecnica

GitHub Actions workflows:
- `.github/workflows/lint.yml` - ESLint + Ruff
- `.github/workflows/test.yml` - Pytest
- `.github/workflows/build.yml` - Build Next.js
- `.github/workflows/deploy.yml` - Deploy automatico

---

## Issue #70 - Qualidade de Software - Blacks/flacke8

**Tipo:** Task  
**Labels:** Arquitetura, DevOps, Requisitos  
**Responsavel:** Pirata2040  
**Status:** ✅ Closed

### O que fazer
Configurar Black (formatador) e Flake8 (linter) para o backend Python

### Por que fazer
Manter codigo consistente e seguindo boas praticas PEP 8

### Pronto quando
- [x] Black configurado e integrado
- [x] Flake8 configurado e integrado
- [x] Pre-commit hooks instalados
- [x] Codigo existente formatado

### Tamanho
[X] Pequena [ ] Media [ ] Grande

### Descricao Tecnica

Configuracoes:
```ini
# .flake8
[flake8]
max-line-length = 88
extend-ignore = E203, W503

# pyproject.toml
[tool.black]
line-length = 88
```

Pre-commit hook:
```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/psf/black
    hooks:
      - id: black
  - repo: https://github.com/pycqa/flake8
    hooks:
      - id: flake8
```

---

## Issue #69 - Testes Automatizados (Pyteste e outros)

**Tipo:** Task  
**Labels:** Automatizacao, DevOps, testing  
**Responsavel:** Pirata2040  
**Status:** ✅ Closed

### O que fazer
Implementar suite de testes automatizados para o backend

### Por que fazer
Garantir qualidade e prevenir regressoes no codigo

### Pronto quando
- [x] Pytest configurado
- [x] Testes unitarios criados
- [x] Testes de integracao criados
- [x] Cobertura minima de 60%

### Tamanho
[ ] Pequena [X] Media [ ] Grande

### Descricao Tecnica

Testes implementados:
```python
# tests/test_statistics_generator.py
# tests/test_querido_diario_client.py
# tests/test_gemini_client.py
# tests/test_main_api.py
```

Cobertura:
- Extracao de valores: 85%
- Categorizacao: 80%
- APIs externas: 70%
- Endpoints: 75%

---

## Issue #65 - Configuracao do envio de dados para API

**Tipo:** Feature  
**Labels:** Automatizacao, backend  
**Responsavel:** Pirata2040  
**Status:** ✅ Closed

### O que fazer
Configurar envio estruturado de dados entre frontend e backend

### Por que fazer
Padronizar comunicacao e garantir integridade dos dados

### Pronto quando
- [x] Schemas Pydantic definidos
- [x] Validacao automatica implementada
- [x] Documentacao OpenAPI gerada
- [x] Frontend integrado

### Tamanho
[X] Pequena [ ] Media [ ] Grande

### Descricao Tecnica

Schemas criados:
```python
# models/schemas.py
class SearchFilters(BaseModel):
    municipio: str
    categoria: str
    dataInicio: str
    dataFim: str

class SearchResponse(BaseModel):
    total_gazettes: int
    total_invested: float
    investments_by_category: dict
```

---

## Resumo da Sprint 9

| Metrica | Valor |
|---------|-------|
| Issues abertas | 7 |
| Issues fechadas | 7 |
| Story points | 14 |
| Taxa de conclusao | 100% |

