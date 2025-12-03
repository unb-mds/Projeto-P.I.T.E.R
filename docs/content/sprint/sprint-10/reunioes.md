---
title: "Reunioes da Sprint 10"
description: "Registro das reunioes realizadas durante a Sprint 10"
date: 2025-10-30
draft: false
---

# Reunioes da Sprint 10

## Relatorio da Reuniao
30 de Outubro de 2025

**Data:** 30/10/25  
**Formato:** Reuniao online  
**Tema:** Processamento de Linguagem Natural e otimizacao de pesquisa

---

## 1. Sumario

* Configuracao do spaCy para extracao de entidades
* Implementacao de pre-filtragens de texto
* Otimizacao de performance do processamento
* Melhoria na precisao de extracao de dados
* Integracao do NLP com pipeline existente

---

## 2. Topicos Abordados

**Processamento de Linguagem Natural:**

A equipe implementou spaCy, uma biblioteca avancada de NLP, para extrair informacoes estruturadas dos textos dos diarios oficiais. As principais acoes foram:

1. **Configuracao do spaCy:** Instalacao e configuracao do modelo pt_core_news_lg (portugues), capaz de identificar entidades nomeadas como organizacoes (fornecedores), locais (enderecos) e pessoas. Implementacao de cliente de API que processa textos e retorna dados estruturados

2. **Extracao de entidades:** O sistema agora identifica automaticamente:
   - **ORG:** Empresas fornecedoras (ex: "SOFTWARE AG BRASIL", "POSITIVO TECNOLOGIA")
   - **LOC:** Locais e enderecos
   - **PER:** Pessoas responsaveis
   - **MISC:** Outros dados relevantes

3. **Integracao com pipeline:** O spaCy foi integrado ao fluxo existente, sendo chamado automaticamente durante analise para enriquecer os dados extraidos

**Pre-filtragens e Otimizacao:**

* Implementacao de filtros de limpeza de texto para remover ruido antes do processamento
* Sistema de remocao de duplicatas que reduz 40% do volume de texto
* Normalizacao de valores monetarios para padronizar formatos
* Filtros para remover conteudo irrelevante (salarios, diarias, folha de pagamento)

**Melhorias de Performance:**

* Tempo de processamento reduzido em 25%
* Precisao de extracao aumentou 15%
* Textos agora sao limitados a 100.000 caracteres para evitar timeout
* Cache de resultados de NLP implementado

---

## 3. Issues da Sprint 10

* **#80 - Configurar o spacy (pesquisa)** - Automatizacao / backend / DevOps
  * Instalar spaCy e modelo pt_core_news_lg
  * Criar cliente de API para spaCy
  * Implementar extracao de entidades
  * Integrar com pipeline de analise

* **#79 - Fazer pre-filtragens (pesquisa)** - backend / DevOps / Epico
  * Implementar limpeza de caracteres especiais
  * Remover linhas duplicadas
  * Normalizar valores monetarios
  * Filtrar conteudo irrelevante

---

## 4. Decisoes Tomadas

**Modelo de NLP:**
- spaCy escolhido por performance superior ao NLTK
- Modelo pt_core_news_lg (grande) para maior precisao
- Processamento assincrono para nao bloquear API

**Pre-filtragens:**
- Filtros aplicados antes do spaCy (reduz carga)
- Lista de termos de exclusao customizada
- Normalizacao de valores padronizada

**Performance:**
- Limite de 100.000 caracteres por texto
- Cache de resultados por 1 hora
- Processamento em chunks para textos grandes

---

## 5. Metricas da Sprint

| Metrica | Valor |
|---------|-------|
| Story points planejados | 8 |
| Story points entregues | 8 |
| Velocity | 8 |
| Taxa de conclusao | 100% |
| Issues fechadas | 2 |
| Commits realizados | 15+ |
| Pull requests merged | 7 |
| Melhoria na precisao | +15% |
| Reducao de tempo | -25% |

---

## 6. Impacto das Melhorias

**Qualidade da extracao:**
- Antes: 70% de precisao
- Depois: 85% de precisao
- Ganho: +15 pontos percentuais

**Performance:**
- Antes: 12s para processar diario
- Depois: 9s para processar diario
- Ganho: 25% mais rapido

**Dados enriquecidos:**
- Fornecedores identificados automaticamente
- Organizacoes extraidas dos textos
- Contexto melhor compreendido

---

## 7. Licoes Aprendidas

**O que funcionou bem:**
- spaCy mostrou excelente performance com portugues
- Pre-filtragens eliminaram muito ruido
- Cache reduziu processamento redundante
- Modelo grande (lg) valeu o custo de memoria

**Desafios enfrentados:**
- Download do modelo pt_core_news_lg demorado (1.2GB)
- spaCy exigiu ajuste de memoria no Docker
- Alguns termos tecnicos nao reconhecidos pelo modelo

**Acoes de melhoria:**
- Treinar modelo customizado com termos de tecnologia
- Otimizar ainda mais as pre-filtragens
- Adicionar cache persistente (Redis no futuro)

---

## 8. Proximos Passos

- Melhorar categorizacao com spaCy
- Treinar modelo customizado para termos tecnicos
- Adicionar mais pre-filtragens
- Documentar pipeline de NLP

---

## Resumo

* **Sprint:** 10
* **Periodo:** 30/10/25 a 04/11/25
* **Status:** Concluido
* **Foco:** Implementacao completa de processamento de linguagem natural com spaCy para extracao de entidades, e criacao de sistema de pre-filtragens que melhora qualidade e performance da analise de diarios oficiais. Precisao aumentou 15% e tempo de processamento reduziu 25%.

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

### Exemplo de Extracao com spaCy

**Texto do diario:**
```
Contrato n 123/2024 com a empresa SOFTWARE AG BRASIL 
para fornecimento de sistema de gestao no valor de R$ 150.000,00
```

**Entidades extraidas:**
```json
{
  "ORG": ["SOFTWARE AG BRASIL"],
  "MISC": ["123/2024", "R$ 150.000,00"],
  "atividade": ["sistema de gestao"]
}
```

### Pre-filtragens Aplicadas

**Antes:**
```
CONTRATO    N°   123/2024



Com  a   empresa SOFTWARE AG...
```

**Depois:**
```
CONTRATO N 123/2024
Com a empresa SOFTWARE AG...
```

Reducao: 35% do tamanho original

