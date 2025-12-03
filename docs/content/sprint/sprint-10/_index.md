---
title: "Sprint 10"
description: "Processamento NLP e Pre-filtragens"
date: 2025-10-30
draft: false
---

# Sprint 10 - Processamento NLP

**Periodo:** 30/10/2025 a 04/11/2025

## Objetivos da Sprint

- Configurar spaCy para processamento de linguagem natural
- Implementar pre-filtragens de pesquisa
- Melhorar extracao de entidades nos diarios
- Otimizar performance do processamento de texto
- Integrar modelo de NLP com pipeline existente

## Resultados Esperados

- spaCy configurado e funcionando
- Pre-filtragens inteligentes implementadas
- Melhoria na precisao de extracao de dados
- Performance otimizada para textos grandes
- Pipeline de NLP integrada ao backend

## Issues da Sprint

### Issue #80 - Configurar o spacy (pesquisa)
**Tipo:** Task  
**Labels:** Automatizacao, backend, DevOps  
**Responsavel:** Pirata2040  
**Status:** ✅ Concluido

---

### Issue #79 - Fazer pre-filtragens (pesquisa)
**Tipo:** Feature  
**Labels:** backend, DevOps, Epico  
**Responsavel:** Pirata2040  
**Status:** ✅ Concluido

---

## Entregas da Sprint

| Item | Status |
|------|--------|
| spaCy configurado | ✅ Completo |
| Modelo pt_core_news_lg instalado | ✅ Completo |
| Pre-filtragens implementadas | ✅ Completo |
| Extracao de entidades funcionando | ✅ Completo |
| Limpeza de texto otimizada | ✅ Completo |

## Tecnologias Implementadas

### spaCy Configuration
```python
# services/api/clients/spacy_api_client.py
import spacy

# Carregar modelo em portugues
nlp = spacy.load("pt_core_news_lg")

async def extract_entities(text: str):
    doc = nlp(text)
    entities = {
        "MISC": [],
        "ORG": [],
        "LOC": [],
        "PER": []
    }
    for ent in doc.ents:
        entities[ent.label_].append(ent.text)
    return entities
```

### Pre-filtragens
```python
# services/processing/data_cleaner.py
def pre_filter_spacy_input(text: str) -> str:
    # Remove caracteres especiais
    text = re.sub(r'[^\w\s\.,\-]', '', text)
    
    # Remove multiplos espacos
    text = re.sub(r'\s+', ' ', text)
    
    # Remove linhas duplicadas
    lines = text.split('\n')
    text = '\n'.join(list(dict.fromkeys(lines)))
    
    return text.strip()
```

## Metricas da Sprint

- **Velocity:** 8 story points
- **Issues fechadas:** 2
- **Commits:** 15+
- **PRs merged:** 8
- **Melhoria na extracao:** +15% precisao

## Documentacao

- [Reunioes](./reunioes)
- [Issues](./issues)

