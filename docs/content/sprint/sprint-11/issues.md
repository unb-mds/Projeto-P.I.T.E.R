---
title: "Issues da Sprint 11"
description: "Issues trabalhadas durante a Sprint 11"
date: 2025-11-06
draft: false
---

# Issues da Sprint 11

## Issue #84 - Fazer as estatisticas (comparacao)

**Tipo:** Task  
**Labels:** backend, DevOps  
**Responsavel:** Pirata2040  
**Status:** ✅ Closed

### O que fazer
Implementar calculo de estatisticas para comparacao entre dois municipios

### Por que fazer
Permitir analise comparativa de investimentos entre municipios diferentes

### Pronto quando
- [x] Funcao de comparacao implementada
- [x] Calculo de diferenca absoluta e percentual
- [x] Agregacao por periodo (mes/ano)
- [x] Retorno estruturado para frontend

### Tamanho
[ ] Pequena [X] Media [ ] Grande

### Descricao Tecnica

Implementar funcao que:
- Calcula estatisticas individuais de cada municipio
- Compara valores totais investidos
- Calcula diferenca percentual
- Agrupa por periodo (mes ou ano)
- Identifica qual municipio investiu mais

```python
def compare_investments(gazettes1, gazettes2):
    stats1 = extract_investment_statistics(gazettes1)
    stats2 = extract_investment_statistics(gazettes2)
    
    return {
        "total1": stats1["total_invested"],
        "total2": stats2["total_invested"],
        "difference": stats1["total_invested"] - stats2["total_invested"],
        "difference_percent": ((stats1["total_invested"] - stats2["total_invested"]) / stats2["total_invested"]) * 100,
        "by_period1": stats1["investments_by_period"],
        "by_period2": stats2["investments_by_period"]
    }
```

---

## Issue #83 - Configurar o spacy (comparacao)

**Tipo:** Task  
**Labels:** Automatizacao, backend, DevOps  
**Responsavel:** Pirata2040  
**Status:** ✅ Closed

### O que fazer
Aplicar processamento de NLP com spaCy nos textos dos dois municipios para comparacao

### Por que fazer
Extrair entidades de ambos os municipios para analise comparativa de fornecedores e contexto

### Pronto quando
- [x] spaCy processando diarios do municipio 1
- [x] spaCy processando diarios do municipio 2
- [x] Entidades extraidas de ambos
- [x] Comparacao de entidades implementada

### Tamanho
[X] Pequena [ ] Media [ ] Grande

### Descricao Tecnica

Processar textos de ambos municipios:
```python
entities1 = await spacy_client.extract_entities(text_municipio1)
entities2 = await spacy_client.extract_entities(text_municipio2)

comparison = {
    "municipio1": {
        "fornecedores": entities1["ORG"],
        "locais": entities1["LOC"]
    },
    "municipio2": {
        "fornecedores": entities2["ORG"],
        "locais": entities2["LOC"]
    }
}
```

---

## Issue #82 - Fazer pre-filtragens (comparacao)

**Tipo:** Feature  
**Labels:** Automatizacao, backend, DevOps  
**Responsavel:** Pirata2040  
**Status:** ✅ Closed

### O que fazer
Aplicar mesmas pre-filtragens usadas na pesquisa para pagina de comparacao

### Por que fazer
Garantir consistencia na limpeza de dados e melhorar qualidade da comparacao

### Pronto quando
- [x] Pre-filtragens aplicadas em ambos municipios
- [x] Limpeza consistente
- [x] Performance otimizada
- [x] Testes validados

### Tamanho
[X] Pequena [ ] Media [ ] Grande

### Descricao Tecnica

Reutilizar funcoes de limpeza:
```python
# Aplicar mesmas pre-filtragens
text1_cleaned = data_cleaner.pre_filter_spacy_input(text1)
text2_cleaned = data_cleaner.pre_filter_spacy_input(text2)

# Garantir mesmo padrao de extracao
values1 = extract_money_values(text1_cleaned)
values2 = extract_money_values(text2_cleaned)
```

Beneficios:
- Comparacao justa (mesmo criterio)
- Codigo reutilizado (DRY)
- Menos bugs

---

## Issue #81 - Fazer as estatisticas (pesquisa)

**Tipo:** Feature  
**Labels:** backend, DevOps  
**Responsavel:** Pirata2040  
**Status:** ✅ Closed

### O que fazer
Implementar calculo completo de estatisticas para pagina de pesquisa/dashboard

### Por que fazer
Fornecer dados estruturados para graficos e visualizacoes do dashboard

### Pronto quando
- [x] Total investido calculado
- [x] Investimentos por categoria
- [x] Investimentos por periodo (mes/ano)
- [x] Publicacoes por periodo
- [x] Agrupamento dinamico (mes vs ano)

### Tamanho
[ ] Pequena [ ] Media [X] Grande

### Descricao Tecnica

Funcao principal do sistema:
```python
def extract_investment_statistics(gazettes, selected_category=None):
    total_invested = 0.0
    category_totals = {}
    
    # Determinar agrupamento (mes ou ano)
    delta_days = (end_date - start_date).days
    group_by = 'month' if delta_days <= 366 else 'year'
    
    # Processar cada diario
    for gazette in gazettes:
        # Baixar texto completo
        text = download_full_text(gazette["txt_url"])
        
        # Extrair valores monetarios
        matches = money_regex.finditer(text)
        
        for match in matches:
            value = parse_value(match.group(1))
            context = text[match.start()-500:match.end()+500]
            
            # Validar contexto (software/robotica)
            if 'software' in context or 'robotica' in context:
                # Categorizar
                category = categorize(context)
                
                total_invested += value
                category_totals[category] += value
    
    return {
        "total_invested": total_invested,
        "investments_by_category": category_totals,
        "investments_by_period": {...},
        "period_grouping": group_by
    }
```

Complexidade:
- Regex avancado para valores monetarios
- Validacao de contexto (500 chars)
- Categorizacao com 50+ keywords
- Agrupamento dinamico (mes/ano)
- Download de texto completo via txt_url

---

## Issue #74 - Configurar API do querido diario para pagina de comparacao

**Tipo:** Feature  
**Labels:** backend, DevOps  
**Responsavel:** Pirata2040  
**Status:** ✅ Closed

### O que fazer
Integrar API do Querido Diario especificamente para comparacao de municipios

### Por que fazer
Permitir busca paralela de diarios de dois municipios diferentes com mesmos filtros

### Pronto quando
- [x] Endpoint de comparacao criado
- [x] Busca paralela implementada
- [x] Mesmos filtros aplicados em ambos
- [x] Resultado comparativo retornado

### Tamanho
[ ] Pequena [X] Media [ ] Grande

### Descricao Tecnica

Endpoint de comparacao:
```python
@app.post("/api/v1/compare")
async def compare_municipalities(
    municipio1: str,
    municipio2: str,
    categoria: str,
    dataInicio: str,
    dataFim: str
):
    # Buscar em paralelo (mais rapido)
    gazettes1, gazettes2 = await asyncio.gather(
        querido_diario_client.fetch_gazettes(municipio1, dataInicio, dataFim, categoria),
        querido_diario_client.fetch_gazettes(municipio2, dataInicio, dataFim, categoria)
    )
    
    # Processar estatisticas
    stats1 = extract_investment_statistics(gazettes1)
    stats2 = extract_investment_statistics(gazettes2)
    
    # Calcular diferenca
    diff = stats1["total_invested"] - stats2["total_invested"]
    diff_percent = (diff / stats2["total_invested"]) * 100
    
    return {
        "municipio1": {"name": get_name(municipio1), "stats": stats1},
        "municipio2": {"name": get_name(municipio2), "stats": stats2},
        "difference": diff,
        "difference_percent": diff_percent
    }
```

Vantagens:
- Busca paralela (2x mais rapido)
- Mesmos filtros garantem comparacao justa
- Diferenca calculada no backend

---

## Resumo da Sprint 11

| Metrica | Valor |
|---------|-------|
| Issues abertas | 5 |
| Issues fechadas | 5 |
| Story points | 10 |
| Taxa de conclusao | 100% |
| Paginas entregues | 1 (Comparacao) |
