---
title: "Sprint 13"
description: "Dashboards e Integracao com IA"
date: 2025-11-19
draft: false
---

# Sprint 13 - Dashboards e IA

**Periodo:** 19/11/2025 a 24/11/2025

## Objetivos da Sprint

- Implementar dashboard completo da pagina de ranking
- Criar dashboard da pagina de comparacao
- Integrar Google Gemini para analise qualitativa por IA
- Implementar botao de geracao de PDF com analise IA
- Finalizar ajustes do frontend da comparacao

## Resultados Esperados

- Dashboard de ranking funcional e visual
- Dashboard de comparacao com graficos interativos
- Botao "Gerar Analise por IA" funcionando
- PDF gerado com analise qualitativa do Gemini
- Frontend da comparacao polido e completo

## Issues da Sprint

### Issue #103 - Dashboard pagina de ranking
**Tipo:** Feature  
**Labels:** DevOps, enhancement, Epico, frontend, help wanted, prototipo  
**Responsavel:** ananunesv  
**Status:** ✅ Concluido

---

### Issue #102 - Dasboard pagina de comparacao
**Tipo:** Feature  
**Labels:** DevOps, enhancement, Epico, frontend, help wanted, prototipo  
**Responsavel:** ananunesv  
**Status:** ✅ Concluido

---

### Issue #100 - Botao do resumo por IA (faz analise qualitativa e gera um pdf)
**Tipo:** Task  
**Labels:** Automatizacao, DevOps, enhancement, Epico, frontend, Requisitos, testing  
**Responsavel:** ananunesv  
**Status:** ✅ Concluido

---

### Issue #99 - FRONTEND- ajustes da pagina de comparacao
**Tipo:** Task  
**Labels:** Automatizacao, DevOps, enhancement, Epico, frontend, Requisitos, testing  
**Responsavel:** ananunesv  
**Status:** ✅ Concluido

---

## Entregas da Sprint

| Item | Status |
|------|--------|
| Dashboard de ranking | ✅ Completo |
| Dashboard de comparacao | ✅ Completo |
| Integracao com Gemini | ✅ Completo |
| Botao "Gerar Analise por IA" | ✅ Completo |
| Geracao de PDF com IA | ✅ Completo |
| Ajustes frontend comparacao | ✅ Completo |

## Tecnologias Implementadas

### Integracao com Google Gemini
```python
# backend/services/api/clients/gemini_client.py
import google.generativeai as genai

class GeminiClient:
    def __init__(self):
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel('gemini-1.5-flash')
    
    async def analyze_investments(self, text: str):
        prompt = f"""
        Analise os seguintes investimentos em tecnologia educacional:
        
        {text}
        
        Forneça:
        1. Objeto do investimento
        2. Justificativa
        3. Fornecedor/empresa
        4. Marca/modelo (se houver)
        """
        
        response = self.model.generate_content(prompt)
        return response.text
```

### Geracao de PDF com Analise IA
```typescript
// frontend/services/ai-report.ts
export async function generateAIAnalysis(
  territoryId: string,
  since: string,
  until: string,
  keywords?: string
) {
  const params = new URLSearchParams({
    territory_id: territoryId,
    since,
    until,
  });
  
  if (keywords) params.append('keywords', keywords);
  
  const response = await fetch(`${API_URL}/analyze?${params}`);
  return await response.json();
}

export function generatePDFReport(data: AnalysisData) {
  const htmlContent = `
    <!DOCTYPE html>
    <html>
      <head><title>Analise por IA</title></head>
      <body>
        <h1>Analise de Investimentos</h1>
        <p>${data.ai_analysis}</p>
      </body>
    </html>
  `;
  
  const printWindow = window.open('', '_blank');
  printWindow.document.write(htmlContent);
  printWindow.print();
}
```

## Metricas da Sprint

- **Velocity:** 10 story points
- **Issues fechadas:** 4
- **Commits:** 30+
- **PRs merged:** 16
- **Integracao com IA:** 100% funcional

## Documentacao

- [Reunioes](./reunioes)
- [Issues](./issues)

