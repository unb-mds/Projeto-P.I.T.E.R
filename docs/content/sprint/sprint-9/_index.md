---
title: "Sprint 9"
description: "Automacao e Qualidade de Software"
date: 2025-10-28
draft: false
---

# Sprint 9 - Automacao e Qualidade

**Periodo:** 23/10/2025 a 28/10/2025

## Objetivos da Sprint

- Configurar API do Querido Diario para ranking
- Implementar automacao de infraestrutura com Docker
- Configurar Integracao Continua (CI)
- Implementar testes automatizados (pytest)
- Adicionar qualidade de codigo (Black, Flake8)
- Criar scripts de automacao de tarefas
- Configurar envio de dados para API

## Resultados Esperados

- API de ranking funcional
- Infraestrutura automatizada com Docker Compose
- Pipeline de CI/CD completa
- Testes automatizados cobrindo backend
- Codigo formatado e validado automaticamente
- Scripts para tarefas comuns

## Issues da Sprint

### Issue #75 - Configurar a API do querido diario para a pagina de ranking
**Tipo:** Feature  
**Labels:** backend, DevOps  
**Responsavel:** Pirata2040  
**Status:** ✅ Concluido

---

### Issue #73 - Fazer o script de tarefa
**Tipo:** Task  
**Labels:** Automatizacao, backend, DevOps  
**Responsavel:** Pirata2040  
**Status:** ✅ Concluido

---

### Issue #72 - Automacao da Infraestrutura - Docker e YamL
**Tipo:** Feature  
**Labels:** Automatizacao, DevOps, documentation  
**Responsavel:** Pirata2040  
**Status:** ✅ Concluido

---

### Issue #71 - Integracao Continua(CI) - Fazer automatizacao
**Tipo:** Feature  
**Labels:** Automatizacao, backend, DevOps  
**Responsavel:** Pirata2040  
**Status:** ✅ Concluido

---

### Issue #70 - Qualidade de Software - Blacks/flacke8
**Tipo:** Task  
**Labels:** Arquitetura, DevOps, Requisitos  
**Responsavel:** Pirata2040  
**Status:** ✅ Concluido

---

### Issue #69 - Testes Automatizados (Pyteste e outros)
**Tipo:** Task  
**Labels:** Automatizacao, DevOps, testing  
**Responsavel:** Pirata2040  
**Status:** ✅ Concluido

---

### Issue #65 - Configuracao do envio de dados para API
**Tipo:** Feature  
**Labels:** Automatizacao, backend  
**Responsavel:** Pirata2040  
**Status:** ✅ Concluido

---

## Entregas da Sprint

| Item | Status |
|------|--------|
| API de ranking integrada | ✅ Completo |
| Docker Compose configurado | ✅ Completo |
| CI/CD com GitHub Actions | ✅ Completo |
| Testes automatizados (pytest) | ✅ Completo |
| Black + Flake8 configurados | ✅ Completo |
| Scripts de automacao | ✅ Completo |
| Envio de dados para API | ✅ Completo |

## Tecnologias Implementadas

### Docker Compose
```yaml
# docker-compose.yml
version: '3.8'

services:
  backend:
    build: ./backend
    ports:
      - "8001:8001"
    environment:
      - GEMINI_API_KEY=${GEMINI_API_KEY}
    volumes:
      - ./backend:/app
      
  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    depends_on:
      - backend
```

### Pytest Configuration
```python
# backend/tests/test_statistics.py
import pytest
from services.processing.statistics_generator import StatisticsGenerator

def test_extract_investment_values():
    stats = StatisticsGenerator()
    gazettes = [{
        "excerpts": ["Investimento de R$ 1.500,00 em software"]
    }]
    result = stats.extract_investment_statistics(gazettes)
    assert result["total_invested"] == 1500.00
```

### Black + Flake8
```ini
# backend/.flake8
[flake8]
max-line-length = 88
exclude = venv,__pycache__
ignore = E203,W503

# backend/pyproject.toml
[tool.black]
line-length = 88
target-version = ['py310']
```

## Metricas da Sprint

- **Velocity:** 14 story points
- **Issues fechadas:** 7
- **Commits:** 30+
- **PRs merged:** 15
- **Cobertura de testes:** 60%+

## Documentacao

- [Reunioes](./reunioes)
- [Issues](./issues)

