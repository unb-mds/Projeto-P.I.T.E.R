---
title: "Reunioes da Sprint 8"
description: "Registro das reunioes realizadas durante a Sprint 8"
date: 2025-10-22
draft: false
---

# Reunioes da Sprint 8

## Relatorio da Reuniao
17 de Outubro de 2025

**Data:** 17/10/25  
**Formato:** Reuniao online  
**Tema:** Finalizacao do MVP e preparacao para entrega

---

## 1. Sumario

* Configuracao de pipeline de CI/CD
* Implementacao de deploy automatico
* Finalizacao da documentacao completa
* Preparacao da apresentacao final
* Testes de integracao end-to-end
* Revisao final do MVP

---

## 2. Topicos Abordados

**Automacao e DevOps:**

A equipe focou em automatizar o processo de build e deploy para garantir entregas continuas e qualidade do codigo. As principais acoes foram:

1. **Pipeline de CI/CD:** Configuracao do GitHub Actions com validacao de lint para frontend (ESLint) e backend (Ruff), build automatico do Next.js e execucao de testes
2. **Deploy automatico:** Integracao com Vercel para o frontend e Railway para o backend, com deploy acionado automaticamente a cada push na branch main
3. **Testes automatizados:** Implementacao de testes unitarios no backend usando pytest e validacao de build no frontend

**Finalizacao do MVP:**

* Dashboard funcional com dados mockados para testes de interface
* Prototipo definitivo aprovado com todas as paginas (Home, Dashboard, Comparacao, Ranking)
* Documentacao completa no GitPages com secoes de Visao Geral, XP, Interface, MVP e Integrantes
* Integracao final entre frontend e backend validada

**Preparacao para entrega:**

* Apresentacao do MVP estruturada com demonstracao ao vivo
* Video de demonstracao gravado mostrando fluxo completo
* README atualizado com instrucoes de instalacao e uso
* Release v1.0 criada no GitHub

---

## 3. Issues da Sprint 8

* **#68 - Fazer a pipeline da build** - Automatizacao / documentation
  * Configurar GitHub Actions para lint e build
  * Implementar deploy automatico
  * Criar documentacao do processo

* **#67 - Fazer a simulacao de dashboard** - desing / frontend
  * Implementar dashboard com dados mockados
  * Testar interacoes de usuario
  * Validar responsividade

* **#66 - Prototipo definitivo** - frontend / prototipo
  * Finalizar prototipo no Figma
  * Definir design system completo
  * Obter aprovacao da equipe

---

## 4. Decisoes Tomadas

**Estrategia de Deploy:**
- Frontend no Vercel (Next.js otimizado)
- Backend no Railway (Python/FastAPI)
- Deploy automatico via GitHub Actions

**Documentacao:**
- GitPages usando Hugo para documentacao tecnica
- README detalhado no repositorio
- Comentarios no codigo para facilitar manutencao

**Testes:**
- Testes unitarios no backend (pytest)
- Testes de integracao manuais documentados
- Validacao de lint automatica no CI

---

## 5. Metricas da Sprint

| Metrica | Valor |
|---------|-------|
| Story points planejados | 10 |
| Story points entregues | 10 |
| Velocity | 10 |
| Taxa de conclusao | 100% |
| Issues fechadas | 3 |
| Commits realizados | 20+ |
| Pull requests merged | 10 |

---

## 6. Licoes Aprendidas

**O que funcionou bem:**
- Pipeline de CI/CD reduziu erros em producao
- Deploy automatico acelerou entregas
- Prototipo facilitou alinhamento da equipe
- Pair programming nas configuracoes complexas

**Desafios enfrentados:**
- Configuracao inicial do Vercel com monorepo
- Integracao do Railway com variaveis de ambiente
- Sincronizacao de branches durante merge final

**Melhorias para projetos futuros:**
- Iniciar automacao desde a Sprint 1
- Documentar decisoes tecnicas em tempo real
- Fazer testes de deploy desde o inicio

---

## 7. Proximos Passos

- Apresentacao final do MVP para a disciplina
- Manutencao e correcoes pos-entrega (se necessario)
- Planejamento de evolucao futura (backlog)
- Retrospectiva final do projeto

---

## Resumo

* **Sprint:** 8
* **Periodo:** 17/10/25 a 22/10/25
* **Status:** Concluido
* **Foco:** Finalizacao do MVP com automacao de CI/CD, deploy automatico e documentacao completa. Preparacao para apresentacao final com validacao de todos os componentes do sistema.

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

