---
title: "Visao Geral"
description: "Contextualizacao, motivacao e objetivos do projeto P.I.T.E.R"
date: 2025-09-09
draft: false
weight: 1
---

# Visao Geral do Projeto P.I.T.E.R

## 1. O Problema

Os Diarios Oficiais municipais brasileiros publicam diariamente informacoes sobre licitacoes, contratos e gastos publicos. No entanto, **acompanhar investimentos especificos em tecnologia educacional** (software, robotica, infraestrutura) e extremamente dificil:

- **Dados dispersos**: Milhares de publicacoes diarias em formato PDF
- **Linguagem tecnica**: Termos nao padronizados (ex: "licenca de software", "sistema informatizado", "plataforma educacional")
- **Valores escondidos**: Montantes aparecem em meio a textos longos
- **Sem visualizacao**: Impossivel comparar investimentos entre municipios ou ao longo do tempo

**Exemplo real**: Brasilia investiu R$ 265 milhoes em tecnologia entre janeiro e maio de 2024, mas essa informacao estava espalhada em 50 diarios diferentes.

## 2. Nossa Solucao

P.I.T.E.R (Procurador de Investimentos em Tecnologia na Educacao Regional) e uma plataforma web que:

1. **Busca automaticamente** nos Diarios Oficiais via API do Querido Diario
2. **Extrai valores monetarios** usando expressoes regulares e contexto
3. **Categoriza inteligentemente** em subcategorias (Educacao, Infraestrutura, Gestao, etc.)
4. **Visualiza em graficos** interativos (barras, pizza, comparativos)
5. **Analisa com IA** usando Google Gemini para insights qualitativos
6. **Gera relatorios PDF** completos com dados e analises

## 3. Objetivos Alcancados

### Objetivo Principal
✅ **Plataforma funcional** que automatiza busca, analise e visualizacao de investimentos em tecnologia educacional

### Objetivos Especificos Entregues

| Objetivo | Status | Implementacao |
|----------|--------|---------------|
| Integracao com Querido Diario | ✅ Completo | Endpoint `/search` consome API externa com filtros de municipio, periodo e categoria |
| Extracao de valores monetarios | ✅ Completo | Regex avancado + contexto de 500 caracteres + validacao de intervalo (R$ 100 - R$ 1bi) |
| Categorizacao inteligente | ✅ Completo | Mapa de 50+ palavras-chave divididas em 10 subcategorias |
| Dashboard interativo | ✅ Completo | Recharts com graficos de barras (tempo) e pizza (categoria) |
| Comparacao de municipios | ✅ Completo | Pagina `/compare` com grafico comparativo e diferenca percentual |
| Ranking de subcategorias | ✅ Completo | Pagina `/ranking` com top 3 mais investidas |
| Analise por IA | ✅ Completo | Google Gemini extrai objeto, justificativa, fornecedor e marca |
| Geracao de PDF | ✅ Completo | Relatorios com dados + analise IA exportaveis |

## 4. Escopo Implementado

### Funcionalidades Entregues

#### Pagina de Busca
- Filtros: Municipio (Goiania, Brasilia, Anapolis, Aparecida de Goiania)
- Categorias: Software e Robotica
- Periodo: Datas customizadas
- Resultado: Redirecionamento para dashboard

#### Dashboard de Pesquisa
- **Grafico de barras**: Investimentos por mes (periodo < 1 ano) ou por ano (periodo > 1 ano)
- **Grafico de pizza**: Distribuicao por subcategorias com percentuais
- **Resumo**: Total investido, quantidade de diarios analisados
- **Acoes**: Nova busca, Gerar Analise por IA, Ver fontes oficiais

#### Comparacao de Municipios
- Selecao de 2 municipios diferentes
- Grafico de barras lado a lado
- Diferenca absoluta e percentual
- Analise por IA de ambos os municipios

#### Ranking de Investimentos
- Top 3 subcategorias mais investidas
- Grafico horizontal de barras
- Total por subcategoria
- Links para diarios oficiais

### Tecnologias Utilizadas

**Frontend:**
- Next.js 14 (App Router)
- React 18 + TypeScript
- TailwindCSS (design system)
- Recharts (graficos)
- Lucide React (icones)

**Backend:**
- FastAPI (Python 3.10+)
- Google Gemini API (analise IA)
- Querido Diario API (dados oficiais)
- Pydantic (validacao)

**DevOps:**
- Docker + Docker Compose
- GitHub Actions (CI/CD)
- Hugo (documentacao)

## 5. Stakeholders e Valor Gerado

| Stakeholder | Valor Entregue |
|-------------|----------------|
| **Cidadaos** | Transparencia sobre gastos publicos em educacao tecnologica |
| **Pesquisadores** | Dados estruturados para analise de padroes de investimento |
| **Jornalistas** | Ferramenta para investigacao de uso de recursos |
| **Gestores Publicos** | Benchmark com outros municipios e analise de gaps |
| **Educadores** | Visibilidade sobre investimentos em tecnologia nas escolas |

## 6. Resultados Quantitativos

### Metricas do MVP
- **8 Sprints** concluidas
- **50+ commits** no repositorio
- **4 paginas** funcionais (Home, Dashboard, Compare, Ranking)
- **10 subcategorias** de investimento identificadas
- **85%+ precisao** na extracao de valores monetarios
- **< 5s tempo** de busca media

### Exemplo de Analise Real

**Municipio:** Brasilia  
**Periodo:** Janeiro a Maio 2024  
**Categoria:** Software

**Resultado:**
- Total investido: **R$ 265.925.289,63**
- Subcategoria mais investida: **Gestao (R$ 123.746.394,35)**
- Diarios analisados: **50**
- Fornecedores identificados: **5** (via IA)

## Links de Evidencias

- [Repositorio do Projeto](https://github.com/unb-mds/Projeto-P.I.T.E.R)
- [API Querido Diario](https://queridodiario.ok.org.br/api/docs)
- [Board de Tarefas](https://github.com/orgs/unb-mds/projects)
- [Issues e PRs](https://github.com/unb-mds/Projeto-P.I.T.E.R/issues)
