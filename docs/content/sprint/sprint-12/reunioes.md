---
title: "Reunioes da Sprint 12"
description: "Registro das reunioes realizadas durante a Sprint 12"
date: 2025-11-13
draft: false
---

# Reunioes da Sprint 12

## Relatorio da Reuniao
13 de Novembro de 2025

**Data:** 13/11/25  
**Formato:** Reuniao online  
**Tema:** Ajustes, refinamentos e correcao de bugs

---

## 1. Sumario

* Correcao de bug critico no ranking que bloqueava funcionalidade
* Ajustes nas estatisticas da pagina de comparacao
* Refinamento do spaCy para melhor performance
* Finalizacao da pagina de pesquisa
* Correcoes na integracao com Querido Diario
* Atualizacao completa da documentacao
* Implementacao de logica de negocio da comparacao

---

## 2. Topicos Abordados

**Correcao de Bug Critico (Issue #95):**

A equipe identificou e corrigiu um bug critico que impedia a geracao do ranking. O problema estava em duas frentes:

1. **Backend:** O endpoint `/api/v1/save_search` retornava apenas o filename do JSON salvo, mas o frontend esperava receber os dados completos (investments_by_category, total_invested, etc.) diretamente na resposta. Solucao: modificar o endpoint para retornar todos os dados necessarios na resposta

2. **Frontend:** A categoria "Outros" nao estava sendo filtrada do ranking, causando distorcao nos resultados. Solucao: adicionar filtro que remove "Outros" antes de ordenar e exibir o top 3

**Refinamento de Estatisticas (Issues #98, #89):**

* Sincronizacao de periodos entre municipios na comparacao para garantir que ambos tenham os mesmos buckets de tempo
* Protecao contra divisao por zero no calculo de diferenca percentual
* Normalizacao de valores nulos/zerados
* Validacao de contexto com 500 caracteres obrigatoria
* Implementacao de word boundaries (\b) para evitar matches parciais

**Otimizacao de spaCy (Issues #97, #88):**

* Processamento paralelo de textos de dois municipios
* Cache de resultados (LRU cache com maxsize=100)
* Ajuste de timeout para textos grandes
* Limite de 100.000 caracteres por processamento

**Finalizacao da Pagina de Pesquisa (Issue #90):**

* Graficos com minPointSize={5} para valores pequenos serem visiveis
* Todos os periodos exibidos, mesmo com valor zero
* Botoes "Nova busca" e "Fontes" implementados
* Estados de loading e erro tratados adequadamente
* Responsividade ajustada para mobile

**Correcoes no Querido Diario (Issue #91):**

* Parametros de data corrigidos: `since/until` → `published_since/published_until`
* Validacao de intervalo de datas implementada
* Download prioritario de txt_url para texto completo
* Filtros de data sendo respeitados corretamente

**Atualizacao de Documentacao (Issue #92):**

* README reorganizado sem emojis e repeticoes
* Secoes "Como executar" e "Docker" melhoradas
* Configuracao do Gemini documentada
* Lista de tecnologias atualizada

---

## 3. Issues da Sprint 12

* **#98 - Ajuste estatisticas da pagina de comparacao** - backend / DevOps / enhancement
* **#97 - Ajuste da spacy para a pagina de comparacao** - backend / DevOps / enhancement
* **#95 - Arrumar bug ranking** - Arquitetura / backend / bug / DevOps
* **#92 - Arrumar documentacao** - documentation
* **#91 - Arrumar querido diario/pre-filtragem** - Automatizacao / backend
* **#90 - Terminar pagina de Pesquisa** - DevOps / Epico / frontend
* **#89 - Ajustar a parte de Estatistica (Pesquisa)** - Automatizacao / backend / DevOps
* **#88 - Arrumar SPACY (Pesquisa)** - backend / DevOps
* **#87 - Logica de negocio da pagina de comparacao** - DevOps / documentation

---

## 4. Decisoes Tomadas

**Arquitetura de Resposta:**
- Endpoints devem retornar dados completos, nao apenas referencias
- Frontend consome dados diretamente da resposta
- Evitar multiplas requisicoes para mesmos dados

**Tratamento de Dados:**
- Categoria "Outros" filtrada de rankings
- Protecao contra divisao por zero em calculos
- Normalizacao de periodos para comparacao justa

**Performance:**
- Cache de spaCy implementado (LRU cache)
- Processamento paralelo onde possivel
- Limite de caracteres para evitar timeout

**Documentacao:**
- Manter documentacao atualizada a cada sprint
- Remover informacoes obsoletas
- Adicionar exemplos praticos

---

## 5. Metricas da Sprint

| Metrica | Valor |
|---------|-------|
| Story points planejados | 12 |
| Story points entregues | 12 |
| Velocity | 12 |
| Taxa de conclusao | 100% |
| Issues fechadas | 9 |
| Commits realizados | 40+ |
| Pull requests merged | 22 |
| Bugs corrigidos | 1 critico |

---

## 6. Impacto das Entregas

**Estabilidade:**
- Bug critico do ranking corrigido
- Sistema mais robusto e confiavel
- Menos erros em producao

**Qualidade dos Dados:**
- Estatisticas mais precisas
- Comparacao justa entre municipios
- Categorizacao refinada

**Experiencia do Usuario:**
- Pagina de pesquisa completa e funcional
- Loading states claros
- Botoes "Fontes" para transparencia
- Graficos sempre visiveis (minPointSize)

**Manutencao:**
- Documentacao atualizada facilita onboarding
- Codigo mais limpo e organizado
- Logica de negocio documentada

---

## 7. Licoes Aprendidas

**O que funcionou bem:**
- Identificacao rapida da causa raiz do bug
- Comunicacao eficiente entre frontend e backend
- Testes manuais revelaram problemas importantes
- Refatoracao incremental evitou grandes mudancas

**Desafios enfrentados:**
- Bug do ranking so aparecia em producao
- Sincronizacao de periodos entre municipios complexa
- Parametros da API do Querido Diario mudaram

**Acoes de melhoria:**
- Implementar testes end-to-end
- Adicionar logs mais detalhados
- Documentar APIs externas melhor

---

## 8. Proximos Passos (Sprint 13)

- Implementar dashboard de ranking
- Criar dashboard de comparacao
- Adicionar botao de resumo por IA
- Ajustes finais no frontend da comparacao

---

## Resumo

* **Sprint:** 12
* **Periodo:** 13/11/25 a 18/11/25
* **Status:** Concluido
* **Foco:** Sprint focada em ajustes e refinamentos, com destaque para correcao de bug critico no ranking que estava bloqueando funcionalidade essencial. Finalizacao da pagina de pesquisa, otimizacao de spaCy e atualizacao completa da documentacao. Todas as 9 issues foram entregues com sucesso.

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

### Bug do Ranking - Antes e Depois

**Antes (Bug):**
```javascript
// Frontend esperava dados, mas backend retornava apenas filename
const response = await fetch('/api/v1/save_search');
const data = await response.json();
console.log(data); // { status: "saved", filename: "search_123.json" }
// ❌ investments_by_category nao disponivel
```

**Depois (Corrigido):**
```javascript
const response = await fetch('/api/v1/save_search');
const data = await response.json();
console.log(data); 
// ✅ { 
//   status: "saved", 
//   filename: "search_123.json",
//   total_invested: 123000,
//   investments_by_category: {...}
// }
```

### Exemplo de Sincronizacao de Periodos

**Problema:**
- Municipio 1: tem dados em Jan, Fev, Mar
- Municipio 2: tem dados em Fev, Mar, Abr
- Grafico ficava descoordenado

**Solucao:**
```python
all_periods = set(stats1.keys()) | set(stats2.keys())
# all_periods = {Jan, Fev, Mar, Abr}

normalized1 = {p: stats1.get(p, 0) for p in all_periods}
normalized2 = {p: stats2.get(p, 0) for p in all_periods}

# Agora ambos tem os 4 periodos (com 0 onde nao havia dados)
```

