---
title: "Interface"
description: "Design e UX do P.I.T.E.R"
date: 2025-09-09
draft: false
weight: 4
---

# Interface e Design do P.I.T.E.R

Design moderno, intuitivo e acessivel focado em visualizacao de dados.

## Design System

### Paleta de Cores

Escolhemos cores que transmitem **confianca** (indigo/azul) e **energia** (gradientes):

| Cor | Uso | Codigo Hex |
|-----|-----|------------|
| **Indigo** | Cor primaria, botoes principais, destaques | `#6366F1` |
| **Purple** | Cor secundaria, graficos, gradientes | `#8B5CF6` |
| **Emerald** | Valores positivos, sucesso | `#10B981` |
| **Amber** | Alertas, valores em destaque | `#F59E0B` |
| **Neutral** | Textos, backgrounds | `#1F2937` |
| **Gray** | Bordas, dividers | `#E5E7EB` |

**Exemplo de uso:**
```css
/* Botao primario */
.btn-primary {
  background: #6366F1;
  hover: #4F46E5;
}

/* Grafico de pizza */
const COLORS = ['#6366F1', '#8B5CF6', '#10B981', '#F59E0B'];
```

### Tipografia

- **Fonte:** Inter (Google Fonts) - escolhida por legibilidade em graficos
- **Escala:** 14px (small) → 16px (base) → 48px (titulos)
- **Pesos:** 400 (regular), 600 (semibold), 700 (bold)

### Componentes (Atomic Design)

```
components/
├── atoms/
│   ├── Navbar_sec.tsx        # Navbar secundaria
│   └── Button, Input, Badge
├── molecules/
│   ├── GazetteCard.tsx        # Card de diario oficial
│   ├── search/SearchForm.tsx  # Formulario de busca
│   └── ranking/SearchForm.tsx
└── organisms/
    ├── DashboardCharts.tsx    # Dashboard completo
    ├── Navbar.tsx             # Header principal
    ├── Footer.tsx             # Rodape
    └── ranking/SearchRanking.tsx
```

## Paginas Implementadas

### 1. Home (`/`)

**Layout:**
- Hero section com gradiente indigo → purple
- Formulario de busca centralizado
- 3 feature cards (Pesquisa, Dados Oficiais, Analise Visual)
- Dica de uso

**Decisoes de UX:**
- ✅ Botao "Buscar" redireciona direto para `/dashboard_pesquisa`
- ✅ Filtros visíveis (nao em modal)
- ✅ Placeholder com datas exemplo

### 2. Dashboard de Pesquisa (`/dashboard_pesquisa`)

**Visualizacoes:**

#### Grafico de Barras
```typescript
// Logica dinamica: mes vs ano
if (delta_days <= 366) {
  // Grafico por mes
  data = [{name: "Jan/2024", value: 50000}, ...]
} else {
  // Grafico por ano
  data = [{name: "2023", value: 1200000}, ...]
}
```

**Problema resolvido:** Barras muito pequenas ficavam invisiveis
**Solucao:** Altura minima de 5% do valor maximo

```typescript
const minVisibleValue = maxValue * 0.05;
valueDisplay = value < minVisibleValue ? minVisibleValue : value;
```

#### Grafico de Pizza
- **Subcategorias:** Educacao, Capacitacao, Servidor, Cloud, Gestao, etc.
- **Interativo:** Hover mostra valor e percentual
- **Destaque:** "Outros" aparece apenas se > 0

**Cards de Resumo:**
- Total investido (formato monetario brasileiro)
- Quantidade de diarios analisados
- Periodo da busca

**Acoes:**
- 🔄 Nova Busca
- ✨ Gerar Analise por IA (PDF com Gemini)
- 🔗 Fontes (links para diarios oficiais)

### 3. Comparacao (`/compare`)

**Layout lado a lado:**

```
┌──────────────────────┬──────────────────────┐
│   Municipio 1        │   Municipio 2        │
│   Total: R$ X        │   Total: R$ Y        │
└──────────────────────┴──────────────────────┘
        ┌──────────────────────────┐
        │  Grafico Comparativo     │
        │  (barras duplas)         │
        └──────────────────────────┘
        ┌──────────────────────────┐
        │  Diferenca: ±X%          │
        └──────────────────────────┘
```

**Decisao de UX:**
- Mesmos filtros (categoria, periodo) para ambos
- Cores distintas: Azul vs Roxo
- Tooltip mostra valores originais (nao ajustados)

### 4. Ranking (`/ranking`)

**Podio de Subcategorias:**

```
    ┌─────┐
    │  🥇  │  Top 1: Gestao (R$ 123M)
    │ 60% │
    └─────┘
  ┌─────┐
  │ 🥈  │    Top 2: Capacitacao (R$ 80M)
  │ 32% │
  └─────┘
┌─────┐
│ 🥉  │      Top 3: Servidor (R$ 28M)
│ 11% │
└─────┘
```

**Grafico Horizontal:**
- Barras coloridas com largura dinamica
- Ignoramos "Outros" automaticamente
- Mostra proxima subcategoria se Outros estiver no top 3

## Responsividade

| Dispositivo | Breakpoint | Adaptacoes |
|-------------|------------|------------|
| Mobile | < 640px | Cards empilhados, graficos menores, menu hamburger |
| Tablet | 640px - 1024px | Grid 2 colunas, graficos medios |
| Desktop | > 1024px | Layout completo, graficos grandes |

**Exemplo:**
```typescript
// TailwindCSS
<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
  {/* Responsive automaticamente */}
</div>
```

## Acessibilidade (WCAG AA)

✅ **Contraste:** Minimo 4.5:1 para textos  
✅ **Navegacao:** Tab index correto  
✅ **Labels:** Todos os inputs tem `<label>`  
✅ **Alt text:** Imagens (se houver)  
✅ **Semantica:** Tags HTML corretas (`<nav>`, `<main>`, `<footer>`)

## Animacoes e Feedback

**Loading states:**
```typescript
{loading && (
  <div className="animate-spin">
    <Loader2 />
  </div>
)}
```

**Hover effects:**
```css
.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(0,0,0,0.1);
}
```

**Transicoes suaves:**
- Fade in nas paginas
- Stagger nos cards (delay de 50ms entre cada)

## Tecnologias de UI

| Biblioteca | Versao | Uso |
|------------|--------|-----|
| **Next.js** | 14.2 | Framework React com SSR |
| **TailwindCSS** | 3.3 | Utility-first CSS |
| **Recharts** | 3.5 | Graficos responsivos |
| **Lucide React** | 0.546 | Icones SVG leves |
| **React Hook Form** | - | Validacao de forms |

## Fluxo de Usuario

```
1. Usuario acessa "/"
2. Preenche filtros (Municipio, Categoria, Periodo)
3. Clica "Buscar"
   ↓
4. Redireciona para "/dashboard_pesquisa"
5. Ve graficos carregando (skeleton)
6. Graficos aparecem com dados
   ↓
7. Opcoes:
   → "Nova Busca" (volta pra home)
   → "Gerar Analise por IA" (abre PDF)
   → "Fontes" (abre diarios oficiais)
```

## Decisoes de Design

### Por que Recharts?
- ✅ Responsivo por padrao
- ✅ Customizavel
- ✅ Performatico (ate 1000 pontos)
- ✅ TypeScript nativo

### Por que Graficos de Barras e Pizza?
- **Barras:** Melhor para comparacao temporal
- **Pizza:** Intuitivo para distribuicao percentual

### Por que nao usamos tabelas?
- Graficos sao mais rapidos de interpretar
- Tabelas ficaram para versao futura (export CSV)

## Prototipo vs Implementado

**Figma:** [Ver prototipo](https://www.figma.com/design/SrD9XAdENSImL4DVWmEZD5/Organizacao-MDS)

**Mudancas do prototipo:**
- ✅ Adicionamos grafico de comparacao
- ✅ Ranking como pagina separada (nao modal)
- ✅ Botao "Analise por IA" (nao estava no prototipo)

## Evidencias

- [Codigo dos Componentes](https://github.com/unb-mds/Projeto-P.I.T.E.R/tree/main/frontend/components)
- [Estilos TailwindCSS](https://github.com/unb-mds/Projeto-P.I.T.E.R/blob/main/frontend/app/globals.css)
- [Prototipo Figma](https://www.figma.com/design/SrD9XAdENSImL4DVWmEZD5/Organizacao-MDS)
