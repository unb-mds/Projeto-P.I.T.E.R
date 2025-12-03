---
title: "Issues da Sprint 12"
description: "Issues trabalhadas durante a Sprint 12"
date: 2025-11-13
draft: false
---

# Issues da Sprint 12

## Issue #98 - Ajuste estatisticas da pagina de comparacao

**Tipo:** Task  
**Labels:** Automatizacao, backend, DevOps, enhancement, Epico, Requisitos, testing  
**Responsavel:** ananunesv  
**Status:** ✅ Closed

### O que fazer
Refinar calculo de estatisticas na comparacao para garantir precisao e consistencia

### Por que fazer
Estatisticas estavam apresentando inconsistencias entre os dois municipios comparados

### Pronto quando
- [x] Calculo de diferenca percentual corrigido
- [x] Agregacao por periodo sincronizada
- [x] Valores totais validados
- [x] Testes implementados

### Tamanho
[ ] Pequena [X] Media [ ] Grande

### Descricao Tecnica

Ajustes realizados:
- Sincronizacao de periodos entre municipios
- Correcao no calculo de diferenca percentual
- Validacao de valores nulos/zerados
- Normalizacao de datas antes da comparacao

```python
def compare_investments_adjusted(stats1, stats2):
    # Garantir que ambos tenham os mesmos periodos
    all_periods = set(stats1["by_period"].keys()) | set(stats2["by_period"].keys())
    
    normalized1 = {p: stats1["by_period"].get(p, 0) for p in all_periods}
    normalized2 = {p: stats2["by_period"].get(p, 0) for p in all_periods}
    
    # Calcular diferenca com protecao contra divisao por zero
    total1 = stats1["total_invested"]
    total2 = stats2["total_invested"]
    
    if total2 == 0:
        diff_percent = float('inf') if total1 > 0 else 0
    else:
        diff_percent = ((total1 - total2) / total2) * 100
    
    return {
        "total1": total1,
        "total2": total2,
        "difference": total1 - total2,
        "difference_percent": diff_percent,
        "by_period1": normalized1,
        "by_period2": normalized2
    }
```

---

## Issue #97 - Ajuste da spacy para a pagina de comparacao

**Tipo:** Task  
**Labels:** Automatizacao, backend, DevOps, enhancement, Epico, Requisitos, testing  
**Responsavel:** ananunesv  
**Status:** ✅ Closed

### O que fazer
Otimizar processamento de spaCy para lidar com textos de dois municipios simultaneamente

### Por que fazer
Performance estava lenta e algumas entidades nao eram extraidas corretamente

### Pronto quando
- [x] Processamento paralelo implementado
- [x] Cache de resultados adicionado
- [x] Extracao de entidades melhorada
- [x] Timeout ajustado

### Tamanho
[ ] Pequena [X] Media [ ] Grande

### Descricao Tecnica

Melhorias implementadas:
```python
async def extract_entities_comparison(text1, text2):
    # Processar em paralelo
    entities1, entities2 = await asyncio.gather(
        extract_entities_cached(text1),
        extract_entities_cached(text2)
    )
    
    return {
        "municipio1": entities1,
        "municipio2": entities2,
        "common_orgs": set(entities1["ORG"]) & set(entities2["ORG"])
    }

@lru_cache(maxsize=100)
def extract_entities_cached(text_hash):
    # Cache para evitar reprocessamento
    doc = nlp(text[:100000])
    return extract_from_doc(doc)
```

---

## Issue #95 - Arrumar bug ranking

**Tipo:** Bug  
**Labels:** Arquitetura, backend, bug, DevOps  
**Responsavel:** ananunesv  
**Status:** ✅ Closed

### O que fazer
Corrigir bug critico que impedia geracao de ranking

### Por que fazer
Pagina de ranking nao estava carregando dados, bloqueando funcionalidade essencial

### Pronto quando
- [x] Causa raiz identificada
- [x] Bug corrigido
- [x] Testes de regressao adicionados
- [x] Ranking gerando corretamente

### Tamanho
[X] Pequena [ ] Media [ ] Grande

### Descricao Tecnica

**Problema identificado:**
- Endpoint `/api/v1/save_search` retornava apenas filename
- Frontend esperava dados completos (investments_by_category)
- Categoria "Outros" nao estava sendo filtrada

**Solucao:**
```python
@app.post("/api/v1/save_search")
async def save_search_results(request: Dict):
    # ... processamento ...
    
    # Retornar dados diretamente (nao apenas filename)
    return {
        "status": "saved",
        "filename": filename,
        "total_invested": data["data"]["total_invested"],
        "investments_by_category": data["data"]["investments_by_category"],
        "investments_by_period": data["data"]["investments_by_period"]
    }
```

Frontend:
```typescript
const topCategories = Object.entries(investments_by_category)
    .filter(([cat, val]) => cat !== "Outros" && val > 0)
    .sort(([, a], [, b]) => b - a)
    .slice(0, 3);
```

---

## Issue #92 - Arrumar documentacao

**Tipo:** Task  
**Labels:** documentation  
**Responsavel:** ananunesv  
**Status:** ✅ Closed

### O que fazer
Atualizar documentacao do projeto com informacoes recentes

### Por que fazer
Documentacao desatualizada dificultava onboarding e manutencao

### Pronto quando
- [x] README atualizado
- [x] API endpoints documentados
- [x] Guia de instalacao revisado
- [x] Exemplos adicionados

### Tamanho
[X] Pequena [ ] Media [ ] Grande

### Descricao Tecnica

Atualizacoes realizadas:
- README com estrutura reorganizada
- Remocao de emojis e repeticoes
- Secoes "Como executar" e "Docker" melhoradas
- Configuracao do Gemini adicionada
- Lista de tecnologias atualizada

---

## Issue #91 - Arrumar querido diario/pre-filtragem

**Tipo:** Task  
**Labels:** Automatizacao, backend  
**Responsavel:** Pirata2040  
**Status:** ✅ Closed

### O que fazer
Corrigir integracao com API do Querido Diario e refinar pre-filtragens

### Por que fazer
Parametros de data incorretos e pre-filtragens insuficientes

### Pronto quando
- [x] Parametros de data corrigidos
- [x] Pre-filtragens melhoradas
- [x] Download de txt_url implementado
- [x] Filtros de data validados

### Tamanho
[ ] Pequena [X] Media [ ] Grande

### Descricao Tecnica

**Correcoes:**
- Parametros `since/until` → `published_since/published_until`
- Validacao de intervalo de datas no frontend
- Download prioritario de txt_url para texto completo

```python
def fetch_gazettes(territory_id, since, until, keywords):
    params = {
        "territory_ids": [territory_id],
        "published_since": since,  # Corrigido
        "published_until": until,  # Corrigido
        "querystring": keywords,
        "size": 500
    }
    
    response = requests.get(API_URL, params=params)
    gazettes = response.json()["gazettes"]
    
    # Priorizar txt_url
    for gazette in gazettes:
        if gazette.get("txt_url"):
            gazette["full_text"] = download_full_text(gazette["txt_url"])
    
    return gazettes
```

---

## Issue #90 - Terminar pagina de Pesquisa

**Tipo:** Task  
**Labels:** DevOps, Epico, frontend  
**Responsavel:** Pirata2040  
**Status:** ✅ Closed

### O que fazer
Finalizar implementacao completa da pagina de pesquisa/dashboard

### Por que fazer
Pagina ainda tinha componentes incompletos e bugs visuais

### Pronto quando
- [x] Graficos renderizando corretamente
- [x] Botao "Nova busca" implementado
- [x] Botao "Fontes" adicionado
- [x] Responsividade ajustada
- [x] Loading states implementados

### Tamanho
[ ] Pequena [ ] Media [X] Grande

### Descricao Tecnica

Implementacoes finais:
- Graficos com altura minima visivel (minPointSize={5})
- Todos os periodos exibidos (mesmo com valor 0)
- Botao "Nova busca" ao lado de "Gerar relatorio"
- Botao "Fontes" que abre diarios oficiais
- Estados de loading e erro tratados

---

## Issue #89 - Ajustar a parte de Estatistica (Pesquisa)

**Tipo:** Task  
**Labels:** Automatizacao, backend, DevOps  
**Responsavel:** Pirata2040  
**Status:** ✅ Closed

### O que fazer
Refinar algoritmo de extracao de estatisticas para pesquisa

### Por que fazer
Valores inconsistentes e categorizacao imprecisa

### Pronto quando
- [x] Contexto de 500 chars validado
- [x] Word boundaries implementados
- [x] Subcategorizacao refinada
- [x] "Outros" como fallback

### Tamanho
[ ] Pequena [X] Media [ ] Grande

### Descricao Tecnica

Refinamentos:
```python
# Validacao de contexto obrigatoria
context = text[match.start()-500:match.end()+500].lower()

# Primeiro: validar se e tech-related
if not (re.search(r'\bsoftware\b', context) or re.search(r'\brobótica\b', context)):
    continue

# Segundo: tentar subcategorizar
found_category = "Outros"  # Fallback
for category, keywords in CATEGORY_MAP.items():
    for keyword in keywords:
        pattern = r'\b' + re.escape(keyword) + r'\b'
        if re.search(pattern, context):
            found_category = category
            break
```

---

## Issue #88 - Arrumar SPACY (Pesquisa)

**Tipo:** Task  
**Labels:** backend, DevOps  
**Responsavel:** Pirata2040  
**Status:** ✅ Closed

### O que fazer
Corrigir problemas no processamento de spaCy para pesquisa

### Por que fazer
Entidades nao estavam sendo extraidas corretamente

### Pronto quando
- [x] Modelo carregando corretamente
- [x] Limite de caracteres ajustado
- [x] Entidades sendo extraidas
- [x] Performance otimizada

### Tamanho
[X] Pequena [ ] Media [ ] Grande

---

## Issue #87 - Logica de negocio da pagina de comparacao

**Tipo:** Task  
**Labels:** DevOps, documentation  
**Responsavel:** Pirata2040  
**Status:** ✅ Closed

### O que fazer
Documentar e implementar logica de negocio da comparacao

### Por que fazer
Regras de negocio nao estavam claras e documentadas

### Pronto quando
- [x] Fluxo de comparacao documentado
- [x] Regras de agregacao definidas
- [x] Calculo de diferencas especificado
- [x] Casos de borda tratados

### Tamanho
[X] Pequena [ ] Media [ ] Grande

---

## Resumo da Sprint 12

| Metrica | Valor |
|---------|-------|
| Issues abertas | 9 |
| Issues fechadas | 9 |
| Story points | 12 |
| Taxa de conclusao | 100% |
| Bugs corrigidos | 1 critico |
| Paginas finalizadas | 2 (Pesquisa e Comparacao) |

