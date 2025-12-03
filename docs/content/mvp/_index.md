---
title: "MVP"
description: "Minimo Produto Viavel do P.I.T.E.R"
date: 2025-09-09
draft: false
weight: 5
---

# MVP - Minimo Produto Viavel

O que entregamos em 8 sprints para validar a proposta do P.I.T.E.R.

## Criterios de Sucesso do MVP

✅ **Usuario busca diarios** por municipio e periodo  
✅ **Sistema extrai valores** monetarios com 85%+ precisao  
✅ **Dashboard mostra graficos** de investimentos  
✅ **Usuario compara municipios** lado a lado  
✅ **IA analisa contexto** e gera relatorios

## User Stories Implementadas

### US01 - Busca de Diarios
**Como** cidadao interessado em educacao  
**Quero** buscar diarios oficiais por municipio, categoria e periodo  
**Para** encontrar informacoes sobre investimentos em tecnologia

**Implementacao:**
```typescript
// frontend/hooks/useGazetteSearch.ts
const search = async () => {
  const response = await fetch(`/api/search`, {
    method: 'POST',
    body: JSON.stringify({
      municipio: '5300108',  // Brasilia
      categoria: 'software',
      dataInicio: '2024-01-01',
      dataFim: '2024-06-01'
    })
  });
};
```

**Criterios de Aceitacao:**
- ✅ Dropdown com 4 municipios (Goiania, Brasilia, Anapolis, Aparecida)
- ✅ Input de datas com validacao
- ✅ Loading state durante busca
- ✅ Mensagem de erro se falhar

---

### US02 - Visualizacao de Investimentos
**Como** pesquisador  
**Quero** ver graficos de investimentos ao longo do tempo  
**Para** identificar tendencias e padroes

**Implementacao:**
- **Grafico de Barras:** Recharts `<BarChart>` com dados mensais/anuais
- **Grafico de Pizza:** `<PieChart>` com subcategorias

**Logica de agrupamento:**
```python
# backend/services/processing/statistics_generator.py
if (end_date - start_date).days <= 366:
    group_by = 'month'  # Jan/2024, Fev/2024, ...
else:
    group_by = 'year'   # 2023, 2024, ...
```

**Criterios de Aceitacao:**
- ✅ Barras coloridas (indigo)
- ✅ Pizza com labels de percentual
- ✅ Tooltip interativo
- ✅ Minimo visivel para valores pequenos (5% do maximo)

---

### US03 - Comparacao de Municipios
**Como** gestor publico  
**Quero** comparar investimentos entre dois municipios  
**Para** fazer benchmark e identificar gaps

**Implementacao:**
```typescript
// frontend/components/pages/CompareClient.tsx
const chartData = sortedDates.map(date => ({
  name: MONTH_NAMES[parseInt(date.split('-')[1]) - 1],
  municipio1: investments1[date] || 0,
  municipio2: investments2[date] || 0
}));
```

**Criterios de Aceitacao:**
- ✅ Barras duplas (azul vs roxo)
- ✅ Diferenca absoluta e percentual
- ✅ Mesmos filtros aplicados em ambos

---

### US04 - Analise por IA
**Como** jornalista  
**Quero** um relatorio detalhado gerado por IA  
**Para** entender o contexto dos investimentos

**Implementacao:**
```python
# backend/services/api/clients/gemini_client.py
async def analyze_investment_context(text: str):
    model = genai.GenerativeModel('gemini-2.5-flash')
    prompt = f"""
    Analise o seguinte diario oficial e extraia:
    - Objeto da contratacao
    - Justificativa
    - Fornecedor
    - Marca/Modelo
    
    Texto: {text[:30000]}
    """
    response = model.generate_content(prompt)
    return json.loads(response.text)
```

**Criterios de Aceitacao:**
- ✅ Extrai objeto, justificativa, fornecedor, marca
- ✅ Gera PDF com dados + analise
- ✅ Fallback se IA nao disponivel

---

## Funcionalidades por Sprint

| Sprint | Entrega | Status |
|--------|---------|--------|
| **1** | Setup do projeto + repositorio | ✅ |
| **2** | Integracao com Querido Diario API | ✅ |
| **3** | Extracao de valores monetarios (regex) | ✅ |
| **4** | Categorizacao em subcategorias | ✅ |
| **5** | Dashboard com graficos (Recharts) | ✅ |
| **6** | Paginas de Comparacao e Ranking | ✅ |
| **7** | Integracao Google Gemini + PDF | ✅ |
| **8** | Refinamentos de UI/UX + Deploy | ✅ |

## Arquitetura do MVP

```
┌──────────────────────────────────────┐
│         Frontend (Next.js)           │
│  ┌────────┐  ┌────────┐  ┌────────┐ │
│  │  Home  │  │Dashbrd │  │Compare │ │
│  └────────┘  └────────┘  └────────┘ │
└──────────────┬───────────────────────┘
               │ HTTP
┌──────────────▼───────────────────────┐
│         Backend (FastAPI)            │
│  /search  /analyze  /save_search     │
└──────────┬────────────┬──────────────┘
           │            │
           ▼            ▼
    ┌──────────┐   ┌──────────┐
    │ Querido  │   │  Gemini  │
    │ Diario   │   │   API    │
    └──────────┘   └──────────┘
```

## Algoritmo de Extracao (Core do MVP)

```python
# Passo 1: Baixar texto completo
txt_url = gazette.get("txt_url")
text = download_full_text(txt_url)

# Passo 2: Encontrar valores monetarios
regex = r"R\$\s?(\d{1,3}(?:\.\d{3})*,\d{2})"
matches = regex.finditer(text)

# Passo 3: Validar contexto (500 chars ao redor)
for match in matches:
    context = text[match.start() - 500 : match.end() + 500]
    
    # Requer "software" ou "robotica" no contexto
    if 'software' in context or 'robotica' in context:
        value = parse_value(match.group(1))
        
        # Passo 4: Categorizar
        if 'educacao' in context or 'curso' in context:
            category = "Educacao"
        elif 'servidor' in context or 'cloud' in context:
            category = "Servidor"
        # ... outras categorias
        
        total_invested += value
        category_totals[category] += value
```

## Decisoes Tecnicas do MVP

### Por que FastAPI (nao Flask)?
- ✅ Async nativo (importante para APIs externas)
- ✅ Validacao automatica com Pydantic
- ✅ Documentacao auto-gerada (Swagger)

### Por que Next.js (nao Create React App)?
- ✅ SSR para SEO futuro
- ✅ Roteamento built-in
- ✅ Otimizacoes automaticas

### Por que JSON local (nao banco de dados)?
- ✅ MVP mais rapido de desenvolver
- ✅ Sem custos de hospedagem
- ✅ Dados nao sao grandes (< 10MB)
- ⚠️ Limitacao: Nao escala para producao

## Validacao do MVP

### Testes Manuais Realizados

| Caso de Teste | Resultado |
|---------------|-----------|
| Buscar Brasilia, Jan-Jun 2024, Software | ✅ Retornou 50 diarios, R$ 265M |
| Comparar Goiania vs Brasilia | ✅ Grafico comparativo correto |
| Gerar PDF com analise IA | ✅ PDF com dados + insights |
| Busca sem resultados | ✅ Mensagem "Nenhum resultado" |
| Periodo > 1 ano | ✅ Agrupou por ano (nao mes) |

### Metricas Alcancadas

- ⏱️ **Tempo de busca:** 3-5 segundos
- 🎯 **Precisao de extracao:** ~85%
- 📊 **Cobertura:** 4 municipios, 2 categorias
- 💾 **Tamanho do build:** Frontend 15MB, Backend 50MB

## Exemplo Real de Uso

**Caso: Jornalista investigando gastos em Brasilia**

1. Acessa P.I.T.E.R
2. Seleciona: Brasilia, Software, Jan-Mai/2024
3. Ve dashboard: R$ 265M investidos
4. Identifica: 47% em "Gestao" (R$ 123M)
5. Clica "Gerar Analise por IA"
6. Recebe PDF com:
   - Objeto: "Sistema de gestao documental (SEL)"
   - Fornecedor: "SOFTWARE AG BRASIL"
   - Justificativa: "Modernizacao de TI"

**Resultado:** Materia publicada com dados oficiais em 15 minutos.

## Limitacoes do MVP (Backlog Futuro)

| Limitacao | Impacto | Priorizacao |
|-----------|---------|-------------|
| Apenas 4 municipios | Baixa cobertura | Alta |
| Precisao de 85% | Alguns valores perdidos | Media |
| Sem historico de buscas | Usuario precisa rebuscar | Baixa |
| Sem export CSV | Dificil analise externa | Media |
| Deploy manual | Atualizacoes lentas | Alta |

## Evolucao Pos-MVP

**Proximas features sugeridas:**
1. Expandir para todos municipios de Goias (40+)
2. Adicionar mais categorias (Saude, Transporte)
3. Sistema de alertas (email quando novo diario)
4. Export de dados (CSV, Excel)
5. API publica para terceiros

## Evidencias do MVP

- [Release v1.0](https://github.com/unb-mds/Projeto-P.I.T.E.R/releases)
- [Issues do MVP](https://github.com/unb-mds/Projeto-P.I.T.E.R/milestone/1)
- [Demo Video](#) (se disponivel)
- [Commits da Sprint 8](https://github.com/unb-mds/Projeto-P.I.T.E.R/commits/main)
