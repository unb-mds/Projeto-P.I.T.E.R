---
title: "Reunioes da Sprint 13"
description: "Registro das reunioes realizadas durante a Sprint 13"
date: 2025-11-19
draft: false
---

# Reunioes da Sprint 13

## Relatorio da Reuniao
19 de Novembro de 2025

**Data:** 19/11/25  
**Formato:** Reuniao online  
**Tema:** Implementacao de dashboards e integracao com IA

---

## 1. Sumario

* Criacao de dashboards visuais para ranking e comparacao
* Integracao completa com Google Gemini para analise qualitativa
* Implementacao de botao "Gerar Analise por IA" em todas as paginas
* Geracao automatica de PDF com analise da IA
* Refinamentos finais no frontend da comparacao
* Harmonizacao de cores e UI/UX em todo o sistema

---

## 2. Topicos Abordados

**Dashboards Visuais (Issues #103, #102):**

A equipe focou em criar dashboards visuais atraentes e funcionais para as paginas de ranking e comparacao. Os principais componentes desenvolvidos foram:

1. **Dashboard de Ranking:** Implementacao de podio visual estilo olimpico para o top 3 subcategorias mais investidas, grafico de barras horizontais com Recharts mostrando valores por subcategoria, cards informativos com total investido e numero de diarios, botao "Fontes" que direciona aos diarios oficiais originais, e paleta de cores indigo/purple para consistencia

2. **Dashboard de Comparacao:** Cards lado a lado mostrando totais de cada municipio, grafico de barras duplas (dois Bar por periodo) para comparacao visual direta, card central destacando a diferenca percentual com cores (verde/vermelho), agrupamento dinamico (mes <= 1 ano, ano > 1 ano), e tooltips customizados mostrando valores originais formatados

3. **Responsividade:** Ambos dashboards testados em desktop, tablet e mobile, com grid adaptativo que empilha cards em telas pequenas, e graficos com altura minima e proporcoes ajustadas

**Integracao com Google Gemini (Issue #100):**

A integracao com IA foi uma das entregas mais importantes da sprint:

* **Backend:** Cliente Gemini implementado (`gemini_client.py`) que configura API com GEMINI_API_KEY do .env, seleciona automaticamente melhor modelo disponivel (gemini-1.5-flash ou gemini-1.5-flash-8b como fallback), e endpoint `/analyze` que busca diarios, extrai contexto relevante, e envia para o Gemini com prompt estruturado

* **Analise Qualitativa:** Gemini retorna analise com objeto do investimento (o que foi contratado), justificativa (por que foi contratado), fornecedor/empresa contratada, marca/modelo (quando aplicavel), e observacoes relevantes sobre contexto

* **Frontend:** Botao "Gerar Analise por IA" adicionado em Dashboard, Comparacao e Ranking, com estado de loading durante processamento (spinner + mensagem), tratamento de erros com toast notifications, e geracao de PDF com HTML estilizado contendo a analise

**Geracao de PDF:**

Sistema de geracao de PDF implementado:
```typescript
generatePDFReport(data) {
  const htmlContent = `
    <!DOCTYPE html>
    <html>
    <head>
      <title>Analise por IA - P.I.T.E.R</title>
      <style>
        body { font-family: Arial; padding: 40px; }
        h1 { color: #4F46E5; }
        .section { margin: 20px 0; }
      </style>
    </head>
    <body>
      <h1>Analise de Investimentos em Tecnologia</h1>
      <div class="section">
        <strong>Municipio:</strong> ${data.municipio}
        <strong>Periodo:</strong> ${data.periodo}
        <strong>Total Investido:</strong> R$ ${data.total_invested}
      </div>
      <h2>Analise Qualitativa (IA)</h2>
      <p>${data.ai_analysis}</p>
    </body>
    </html>
  `;
  
  const printWindow = window.open('', '_blank');
  printWindow.document.write(htmlContent);
  printWindow.print();
}
```

**Refinamentos de UI/UX (Issue #99):**

* Correcao de "Comparacao" para "Comparação" em todos os lugares
* Harmonizacao de cores: indigo/purple como paleta principal
* Graficos com minPointSize={5} para valores pequenos serem visiveis
* Tooltips mostrando valores originais (nao os ajustados para visualizacao)
* Textos revisados para clareza
* Layout centralizado e consistente

---

## 3. Issues da Sprint 13

* **#103 - Dashboard pagina de ranking** - DevOps / enhancement / Epico / frontend
  * Podio top 3 subcategorias
  * Grafico de barras horizontais
  * Cards informativos
  * Botao "Fontes"

* **#102 - Dasboard pagina de comparacao** - DevOps / enhancement / Epico / frontend
  * Cards lado a lado
  * Grafico de barras duplas
  * Card de diferenca percentual
  * Agrupamento dinamico

* **#100 - Botao do resumo por IA** - Automatizacao / DevOps / enhancement / Epico / frontend
  * Integracao com Gemini
  * Analise qualitativa
  * Geracao de PDF
  * Loading states

* **#99 - FRONTEND- ajustes da pagina de comparacao** - Automatizacao / DevOps / enhancement / Epico / frontend
  * Correcoes de texto
  * Harmonizacao de cores
  * Tooltips melhorados
  * Responsividade

---

## 4. Decisoes Tomadas

**Escolha do Modelo de IA:**
- Google Gemini escolhido por API gratuita e generosa
- Modelo gemini-1.5-flash para balanco custo/qualidade
- Fallback para gemini-1.5-flash-8b se necessario

**Formato de Analise:**
- Prompt estruturado em topicos claros
- Foco em objeto, justificativa, fornecedor, marca
- Linguagem acessivel e objetiva

**Geracao de PDF:**
- HTML puro com CSS inline
- window.open + print() para compatibilidade
- Sem dependencias externas (jsPDF, etc.)

**UI/UX:**
- Paleta indigo/purple como padrao
- Cards com glass effect
- Animacoes sutis e discretas
- Responsividade mobile-first

---

## 5. Metricas da Sprint

| Metrica | Valor |
|---------|-------|
| Story points planejados | 10 |
| Story points entregues | 10 |
| Velocity | 10 |
| Taxa de conclusao | 100% |
| Issues fechadas | 4 |
| Commits realizados | 35+ |
| Pull requests merged | 18 |
| Integracao com IA | 100% |

---

## 6. Impacto das Entregas

**Valor para o Usuario:**
- Analise qualitativa por IA adiciona insights valiosos
- Dashboards visuais facilitam compreensao dos dados
- PDF exportavel permite compartilhamento facil
- Interface polida melhora experiencia geral

**Inovacao:**
- Primeira integracao com IA generativa no projeto
- Analise automatica de diarios oficiais
- Reducao de tempo de analise manual de horas para segundos

**Diferencial Competitivo:**
- Nenhuma outra ferramenta oferece analise por IA de diarios
- Visualizacoes claras e intuitivas
- Processo end-to-end completo (busca → analise → relatorio)

---

## 7. Licoes Aprendidas

**O que funcionou bem:**
- Gemini respondeu rapido (2-5 segundos por analise)
- Prompt estruturado gerou analises consistentes
- PDF com HTML simples funcionou em todos os browsers
- Dashboards visuais muito bem recebidos

**Desafios enfrentados:**
- Configuracao inicial do Gemini API key
- Balanceamento de informacao no prompt (muito texto = timeout)
- Estilizacao de PDF sem bibliotecas externas

**Acoes de melhoria:**
- Adicionar cache de analises IA (evitar reprocessamento)
- Melhorar tratamento de erros da API Gemini
- Adicionar opcao de download direto do PDF

---

## 8. Proximos Passos

- Melhorar UI/UX com feedback de usuarios
- Deploy em producao (Vercel + Railway)
- Testes de integracao end-to-end
- Documentacao final do projeto

---

## Resumo

* **Sprint:** 13
* **Periodo:** 19/11/25 a 24/11/25
* **Status:** Concluido
* **Foco:** Sprint marcada pela implementacao de dashboards visuais para ranking e comparacao, e pela integracao revolucionaria com Google Gemini para analise qualitativa automatica de investimentos. Botao "Gerar Analise por IA" agora permite aos usuarios obterem insights textuais e contextuais em segundos, exportados em PDF profissional. UI/UX harmonizado em todo o sistema.

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

### Exemplo de Analise por IA (Gemini)

**Input (Prompt):**
```
Analise os seguintes investimentos em tecnologia educacional:

CONTRATO N 123/2024
Contratacao de sistema de gestao escolar ERP no valor de R$ 150.000,00
com a empresa SOFTWARE AG BRASIL para otimizacao de processos 
administrativos e financeiros das escolas municipais.
...
```

**Output (Gemini):**
```
ANALISE QUALITATIVA DOS INVESTIMENTOS

1. OBJETO DO INVESTIMENTO
   Sistema de gestao escolar (ERP) para administracao de escolas municipais

2. JUSTIFICATIVA
   Otimizacao de processos administrativos e financeiros, buscando maior
   eficiencia na gestao dos recursos e melhor acompanhamento dos dados
   escolares

3. FORNECEDOR/EMPRESA
   SOFTWARE AG BRASIL

4. MARCA/MODELO
   Nao especificado no texto

5. OBSERVACOES
   Investimento significativo em infraestrutura de gestao. O valor sugere
   sistema robusto com multiplos modulos. Recomenda-se acompanhar metricas
   de eficiencia pos-implantacao para validar ROI.
```

### Dashboard de Ranking - Screenshot Conceitual

```
┌─────────────────────────────────────────┐
│         TOP 3 SUBCATEGORIAS             │
│                                         │
│    🥇          🥈          🥉            │
│  Software    Rede    Servidor           │
│  R$ 2.5M    R$ 1.8M   R$ 1.2M          │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│   Software  ████████████████ 2.5M       │
│   Rede      ███████████ 1.8M            │
│   Servidor  ████████ 1.2M               │
└─────────────────────────────────────────┘

[ Gerar Analise por IA ]  [ Fontes ]
```

### Dashboard de Comparacao - Screenshot Conceitual

```
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│  Brasilia    │  │  Diferenca   │  │  Goiania     │
│  R$ 265M     │  │  +220M       │  │  R$ 45M      │
│             │  │  (+490%)     │  │             │
└──────────────┘  └──────────────┘  └──────────────┘

┌─────────────────────────────────────────┐
│  Jan  ██ Brasilia  █ Goiania            │
│  Fev  ████         ██                   │
│  Mar  ███          █                    │
└─────────────────────────────────────────┘

[ Gerar Analise por IA ]  [ Nova Busca ]
```

