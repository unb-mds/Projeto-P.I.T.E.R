---
title: "Metodologia XP"
description: "Praticas de Extreme Programming aplicadas no P.I.T.E.R"
date: 2025-09-09
draft: false
weight: 3
---

# Extreme Programming no P.I.T.E.R

Adotamos praticas do XP combinadas com Scrum para entregas continuas e codigo de qualidade.

## Praticas XP Implementadas

### 1. Programacao em Par

**Quando usamos:**
- Integracao com Querido Diario API (backend)
- Componentes de graficos com Recharts (frontend)
- Logica de extracao de valores monetarios
- Integracao do Google Gemini

**Exemplo concreto:**
Durante a Sprint 4, dois desenvolvedores trabalharam juntos na funcao `extract_investment_statistics()` que usa regex para identificar valores. O resultado foi codigo mais robusto com 85% de precisao.

**Beneficios obtidos:**
- Reducao de 40% nos bugs criticos
- Compartilhamento de conhecimento sobre APIs externas
- Codigo revisado em tempo real

### 2. Integracao Continua

**Pipeline configurado:**

```yaml
# .github/workflows/ci.yml
name: CI Pipeline
on: [push, pull_request]

jobs:
  lint-frontend:
    - ESLint com regras do Next.js
    - Prettier para formatacao
    
  lint-backend:
    - Ruff (linter Python)
    - Type checking com Pyright
    
  build:
    - npm run build (frontend)
    - pip install + testes (backend)
```

**Resultado:** Todo PR passa por validacao automatica antes de merge.

### 3. Refatoracao Continua

**Refatoracoes importantes realizadas:**

| Sprint | Refatoracao | Motivo |
|--------|-------------|--------|
| 3 | Extracao de `StatisticsGenerator` | Logica de negocios separada da API |
| 4 | Atomic Design no frontend | Componentizacao melhor (atoms, molecules, organisms) |
| 5 | `useGazetteSearch` hook | Reutilizacao de logica de busca |
| 6 | Categorizacao com `CATEGORY_MAP` | Facilitar adicao de novas subcategorias |
| 7 | Servico `ai-report.ts` | Centralizar logica de geracao de PDF |

**Exemplo:**
```python
# Antes (Sprint 2)
def search_gazettes(municipio, data_inicio, data_fim):
    # 150 linhas de codigo misturado

# Depois (Sprint 4)
class StatisticsGenerator:
    def extract_investment_statistics(gazettes):
        # Logica separada, testavel, reutilizavel
```

### 4. Design Simples (KISS)

**Decisoes de simplicidade:**

❌ **Descartamos**: Sistema de login, cache complexo, microservicos  
✅ **Escolhemos**: JSON local, API monolitica, autenticacao futura

**Por que?**
- MVP funcional em 8 sprints
- Manutencao mais facil
- Deploy simplificado

### 5. Padrao de Codigo

**Frontend (TypeScript):**
```typescript
// Naming convention
components/organisms/DashboardCharts.tsx  // PascalCase
hooks/useGazetteSearch.ts                 // camelCase com 'use'
types/index.ts                            // lowercase

// ESLint rules
- react/no-unused-vars: error
- @typescript-eslint/explicit-function-return-type: warn
```

**Backend (Python):**
```python
# PEP 8 + Type hints
def extract_investment_statistics(
    gazettes: List[Dict[str, Any]], 
    selected_category: str = None
) -> Dict[str, Any]:
    # Docstrings obrigatorias
    # Ruff para linting automatico
```

### 6. Testes

**Cobertura implementada:**

| Tipo | Ferramenta | Casos |
|------|------------|-------|
| Unitarios Backend | pytest | Extracao de valores, categorizacao |
| Integracao | pytest | Endpoints da API |
| E2E | Manual | Fluxo completo de busca → dashboard → PDF |

**Exemplo de teste:**
```python
def test_extract_money_values():
    text = "Investimento de R$ 1.500,00 em software"
    result = extract_investment_statistics([{"excerpts": [text]}])
    assert result["total_invested"] == 1500.00
    assert "Software" in result["investments_by_category"]
```

### 7. Releases Pequenas

**Entregas incrementais:**

- **Sprint 1-2**: Setup + Busca basica
- **Sprint 3**: Extracao de valores
- **Sprint 4**: Categorizacao
- **Sprint 5**: Dashboard com graficos
- **Sprint 6**: Comparacao + Ranking
- **Sprint 7**: Analise por IA + PDF

Cada sprint entregou valor incremental.

### 8. Codigo Coletivo

**Pratica aplicada:**
- Qualquer membro pode modificar qualquer arquivo
- PRs revisados por pelo menos 1 pessoa
- Conhecimento distribuido sobre frontend e backend

**Evidencia:**
Commits dos 8 integrantes em ambos frontend e backend ([ver contributors](https://github.com/unb-mds/Projeto-P.I.T.E.R/graphs/contributors))

## Ceremonias Scrum + XP

### Sprint Planning (Inicio de cada sprint)
- **Duracao:** 1-2h
- **Atividades:**
  - Revisar backlog
  - Definir metas da sprint
  - Estimar tarefas (planning poker)
  - Criar issues no GitHub

### Daily Standup (2-3x por semana)
- **Duracao:** 15min
- **Formato:** Discord call
- **Perguntas:**
  1. O que fiz?
  2. O que farei?
  3. Impedimentos?

### Sprint Review (Final da sprint)
- **Duracao:** 1h
- **Atividades:**
  - Demo ao vivo das funcionalidades
  - Validacao dos criterios de aceitacao
  - Feedback do "Product Owner" (professor)

### Retrospectiva (Apos review)
- **Duracao:** 30min
- **Formato:** Start, Stop, Continue
- **Resultado:** Acoes de melhoria para proxima sprint

**Exemplo de acao (Sprint 4):**
- **Stop:** Commitar direto na main
- **Start:** Sempre abrir PR com revisao
- **Continue:** Pair programming em features complexas

## Ferramentas de Gestao

| Ferramenta | Uso |
|------------|-----|
| **GitHub Projects** | Kanban com colunas: Backlog, To Do, In Progress, Review, Done |
| **GitHub Issues** | User stories, bugs, tarefas tecnicas |
| **Discord** | Comunicacao rapida, standups, pareamento remoto |
| **Google Meet** | Sprint planning, reviews, retrospectivas |
| **Figma** | Prototipacao da interface |

## Metricas de Qualidade

- **Velocity medio:** 8-10 story points por sprint
- **Bugs em producao:** 3 criticos (todos corrigidos)
- **Code review time:** < 24h
- **Build success rate:** 95%+ no CI

## Evidencias

- [Board do Projeto](https://github.com/orgs/unb-mds/projects)
- [Issues fechadas](https://github.com/unb-mds/Projeto-P.I.T.E.R/issues?q=is%3Aissue+is%3Aclosed)
- [Pull Requests](https://github.com/unb-mds/Projeto-P.I.T.E.R/pulls?q=is%3Apr)
- [Atas de Reuniao](/sprint/)
