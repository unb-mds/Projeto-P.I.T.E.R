---
title: "Reunioes da Sprint 11"
description: "Registro das reunioes realizadas durante a Sprint 11"
date: 2025-11-06
draft: false
---

# Reunioes da Sprint 11

## Relatorio da Reuniao
6 de Novembro de 2025

**Data:** 06/11/25  
**Formato:** Reuniao online  
**Tema:** Implementacao de estatisticas e pagina de comparacao

---

## 1. Sumario

* Desenvolvimento de sistema de estatisticas comparativas
* Configuracao de spaCy para analise de dois municipios
* Aplicacao de pre-filtragens na comparacao
* Implementacao completa de estatisticas para pesquisa
* Integracao da API do Querido Diario para comparacao
* Criacao de calculos de diferenca percentual

---

## 2. Topicos Abordados

**Sistema de Estatisticas:**

A equipe focou em criar um sistema robusto de calculo de estatisticas que pudesse ser reutilizado em multiplas paginas (pesquisa, comparacao, ranking). As principais implementacoes foram:

1. **Estatisticas de Pesquisa (Issue #81):** Funcao principal `extract_investment_statistics()` que processa diarios oficiais, extrai valores monetarios, valida contexto (software/robotica presente), categoriza em subcategorias, e agrupa por periodo. Esta funcao se tornou o core do sistema, sendo reutilizada em todas as paginas

2. **Estatisticas de Comparacao (Issue #84):** Funcao `compare_investments()` que executa processamento paralelo de dois municipios, calcula diferencas absolutas e percentuais, e agrupa dados por periodo para visualizacao comparativa em graficos de barras duplas

3. **Agrupamento Dinamico:** Sistema inteligente que decide automaticamente entre agrupamento mensal (periodos <= 1 ano) ou anual (periodos > 1 ano), garantindo visualizacao otimizada independente do range de datas selecionado

**Processamento de Linguagem Natural:**

* Configuracao de spaCy para processar textos de ambos os municipios na comparacao
* Extracao de entidades nomeadas (organizacoes, locais) de forma paralela
* Identificacao automatica de fornecedores em ambos municipios para comparacao

**Pre-filtragens e Consistencia:**

* Aplicacao das mesmas pre-filtragens em pesquisa e comparacao para garantir criterios identicos
* Limpeza de caracteres especiais, remocao de duplicatas, normalizacao de espacos
* Validacao de contexto com janela de 500 caracteres ao redor de cada valor encontrado

**Integracao com Querido Diario:**

* Endpoint de comparacao que busca diarios de dois municipios em paralelo usando asyncio.gather()
* Aplicacao dos mesmos filtros (categoria, periodo) em ambas as buscas
* Parametros corrigidos (published_since/published_until) para respeitar filtros de data

---

## 3. Issues da Sprint 11

* **#84 - Fazer as estatisticas (comparacao)** - backend / DevOps
  * Implementar calculo comparativo
  * Calcular diferenca absoluta e percentual
  * Agrupar por periodo
  * Estruturar retorno para frontend

* **#83 - Configurar o spacy (comparacao)** - Automatizacao / backend / DevOps
  * Processar textos de ambos municipios
  * Extrair entidades de cada um
  * Comparar fornecedores identificados
  * Otimizar performance

* **#82 - Fazer pre-filtragens (comparacao)** - Automatizacao / backend / DevOps
  * Aplicar limpeza de texto
  * Remover duplicatas
  * Normalizar valores
  * Garantir consistencia com pesquisa

* **#81 - Fazer as estatisticas (pesquisa)** - backend / DevOps
  * Implementar extracao de valores
  * Validar contexto (software/robotica)
  * Categorizar em subcategorias
  * Agrupar por periodo (mes/ano)
  * Baixar texto completo via txt_url

* **#74 - Configurar API do querido diario para pagina de comparacao** - backend / DevOps
  * Criar endpoint de comparacao
  * Implementar busca paralela
  * Aplicar mesmos filtros em ambos
  * Retornar dados comparativos

---

## 4. Decisoes Tomadas

**Arquitetura de Estatisticas:**
- Funcao unica reutilizada em todas as paginas
- Processamento consistente para comparacao justa
- Agrupamento dinamico baseado no periodo

**Performance:**
- Busca paralela reduz tempo em 50%
- Cache de resultados por municipio
- Limite de 100.000 caracteres por texto

**Categorizacao:**
- 10 subcategorias definidas
- Mapa de 50+ palavras-chave
- Contexto de 500 caracteres obrigatorio
- "Outros" apenas como fallback

**Validacao de Dados:**
- Valores entre R$ 100 e R$ 1 bilhao
- Requer "software" ou "robotica" no contexto
- Exclui termos irrelevantes (salario, diaria, etc.)

---

## 5. Metricas da Sprint

| Metrica | Valor |
|---------|-------|
| Story points planejados | 10 |
| Story points entregues | 10 |
| Velocity | 10 |
| Taxa de conclusao | 100% |
| Issues fechadas | 5 |
| Commits realizados | 28+ |
| Pull requests merged | 15 |
| Linhas de codigo | 800+ |

---

## 6. Impacto das Entregas

**Funcionalidade nova:**
- Pagina de comparacao 100% funcional
- Usuarios podem comparar 2 municipios lado a lado
- Grafico de barras duplas mostrando evolucao temporal
- Diferenca percentual calculada automaticamente

**Precisao melhorada:**
- Download de texto completo aumentou extracao
- Contexto de 500 chars reduziu falsos positivos
- Validacao de intervalo eliminou valores absurdos

**Reutilizacao de codigo:**
- Funcao de estatisticas usada em 3 paginas
- Pre-filtragens consistentes em todo sistema
- Menos bugs e manutencao facilitada

---

## 7. Licoes Aprendidas

**O que funcionou bem:**
- Busca paralela de municipios muito eficiente
- Reutilizacao de codigo evitou duplicacao
- spaCy funcionou bem com textos de ambos municipios
- Agrupamento dinamico atendeu todos os casos

**Desafios enfrentados:**
- Sincronizar filtros entre dois municipios no frontend
- Garantir que mesmas pre-filtragens fossem aplicadas
- Download de texto completo as vezes lento

**Acoes de melhoria:**
- Adicionar cache para downloads de txt_url
- Implementar retry automatico em falhas
- Otimizar ainda mais a categorizacao

---

## 8. Proximos Passos

- Adicionar mais municipios para comparacao
- Implementar comparacao de 3+ municipios
- Melhorar visualizacao de diferencas
- Adicionar export de dados comparativos

---

## Resumo

* **Sprint:** 11
* **Periodo:** 06/11/25 a 11/11/25
* **Status:** Concluido
* **Foco:** Implementacao completa do sistema de estatisticas reutilizavel em pesquisa e comparacao, configuracao de spaCy para analise de multiplos municipios, e criacao da pagina de comparacao com graficos de barras duplas e calculo de diferencas. Busca paralela otimizou performance em 50%.

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

### Exemplo de Comparacao

**Entrada:**
- Municipio 1: Brasilia
- Municipio 2: Goiania
- Periodo: Jan-Jun 2024
- Categoria: Software

**Resultado:**
```json
{
  "municipio1": {
    "name": "Brasilia",
    "total_invested": 265925289.63,
    "by_period": {
      "2024-01": 39322540.62,
      "2024-02": 170620519.22,
      ...
    }
  },
  "municipio2": {
    "name": "Goiania",
    "total_invested": 45000000.00,
    "by_period": {...}
  },
  "difference": 220925289.63,
  "difference_percent": 490.94
}
```

**Interpretacao:**
Brasilia investiu 490% a mais que Goiania em software educacional no periodo.

