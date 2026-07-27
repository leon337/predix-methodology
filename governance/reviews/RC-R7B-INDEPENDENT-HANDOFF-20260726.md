# Handoff — RC independente do candidato PREDIX R7B

## Objetivo

Executar revisão crítica independente do candidato R7B em contexto separado daquele que implementou e remediou as mudanças.

## Referência canônica

- repositório: `leon337/predix-methodology`;
- base: `main`;
- head ref: `test/governance-64-20260726-r7b`;
- head SHA esperado: `545c19a0379f6a9e5ac3342a4bb93e36f01fbf20`;
- PR Draft: `#15`;
- workflow governança: `30228853903`;
- workflow timeline: `30228853942`;
- artifact: `8639403389`;
- digest: `sha256:e682b1b774ff1147d2a88a53143915b3c15fe97a65baf4d6a6a237044f9f5ada`;
- relatório técnico externo ao HEAD: `governance/tests/results/R7B-VALIDATION-20260726.md` na branch de integração.

O revisor deve reconfirmar diretamente o SHA da branch. Mudança de referência bloqueia a revisão.

## Histórico obrigatório

- R6: tecnicamente verde, RC independente `CHANGES_REQUIRED`;
- R7 inicial: preservado após falha TL-005 no SHA `c38946abf8526a9ad47075efbb04f75ba4a0fe00`, PR #14 fechado sem merge;
- R7B: sucessor corrigido e testado no SHA exato acima.

## Achados R6 a verificar

1. `RC-R6-01`: fontes canônicas pós-R6 reconciliadas;
2. `RC-R6-02`: TL-005 exige campos em eventos novos, delimita legado e formaliza Markdown/YAML;
3. `RC-R6-03`: evidência manual usa cronologia estruturada e regressão posterior invalida PASS;
4. `RC-R6-04`: artifact contém cadeia bruta de evidências.

## Evidência técnica declarada

- 18 testes unitários PASS;
- TL-005 PASS sobre 19 arquivos, 11 eventos estruturados e zero erros;
- scanner com zero achados;
- 64 IDs únicos;
- 25 automatizados, 14 estáticos, 10 manuais e 15 simulados;
- zero `FAIL`, `BLOCKED` e `NOT_RUN`;
- artifact com logs, JSONs, manifesto, hashes e resultados.

A RC deve verificar essas declarações diretamente. Não deve presumir validade apenas por este handoff.

## Restrições

- não editar arquivos;
- não criar commits no PR #15;
- não remediar achados;
- não realizar merge;
- não criar instrução global;
- não aprovar automaticamente Cultura, MOP ou Constituição;
- não reutilizar a conclusão da sessão implementadora como resultado independente;
- distinguir automatizado, estático, manual e simulado.

## Escopo mínimo

1. referência e SHA exatos;
2. estado pós-R6 em README, integração, guardrails e decisões;
3. política de eventos novos, legado e YAML no TL-005;
4. testes adversariais de incompleto, YAML, parcial e duplicidade;
5. eventos cronológicos FA-008/FA-009;
6. teste de regressão posterior ao PASS;
7. scanner TL-010;
8. artifact bruto e manifesto do SHA;
9. distribuição e unicidade dos 64 cenários;
10. suficiência dos gates antes de promoção.

## Saída exigida

```text
RESULTADO=PASS | FAIL | BLOCKED | CHANGES_REQUIRED
HEAD_REVISADO=<sha>
HEAD_TESTADO=545c19a0379f6a9e5ac3342a4bb93e36f01fbf20
INDEPENDENCIA=ATENDIDA | NAO_ATENDIDA
MERGE_RECOMENDADO=SIM | NAO
MERGE_REALIZADO=NAO
EDICAO_EXECUTADA=NAO
REMEDIACAO_EXECUTADA=NAO
```

Listar achados por severidade, evidências, verificações repetidas, limitações e gates remanescentes.
