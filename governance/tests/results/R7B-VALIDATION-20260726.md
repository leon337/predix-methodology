# Validação integral do candidato R7B — 2026-07-26

## Referência congelada

- branch: `test/governance-64-20260726-r7b`;
- SHA: `545c19a0379f6a9e5ac3342a4bb93e36f01fbf20`;
- PR Draft: `#15`;
- base: `main`;
- merge: não autorizado e não realizado.

## Workflows

- `Governance 64 scenarios`: run `30228853903`, conclusão `success`;
- `Timeline validation`: run `30228853942`, conclusão `success`.

Os workflows fizeram checkout explícito do SHA congelado.

## Testes unitários

- total: 18;
- resultado: PASS;
- cobertura nova: TL-005 incompleto/YAML/parcial/legado; cronologia FA; regressão posterior invalida PASS; scanner com `#`.

## TL-005

- resultado: PASS;
- arquivos Markdown examinados: 19;
- eventos estruturados: 11;
- arquivos legado/suporte: 8;
- erros: 0;
- avisos: 0.

## Scanner TL-010

- resultado: PASS;
- ocorrências: 0.

## Matriz de 64 cenários

- IDs: 64;
- IDs únicos: 64;
- `PASS_AUTOMATED=25`;
- `PASS_STATIC=14`;
- `PASS_MANUAL=10`;
- `PASS_SIMULATED=15`;
- `FAIL=0`;
- `BLOCKED=0`;
- `NOT_RUN=0`.

## Artifact bruto

- artifact: `8639403389`;
- digest: `sha256:e682b1b774ff1147d2a88a53143915b3c15fe97a65baf4d6a6a237044f9f5ada`;
- SHA registrado no manifesto: `545c19a0379f6a9e5ac3342a4bb93e36f01fbf20`;
- arquivos avaliados com hash: 71.

Arquivos presentes:

1. `evaluated-files.sha256`;
2. `evidence-manifest.json`;
3. `governance-runner.log`;
4. `results.json`;
5. `results.md`;
6. `secret-scan.json`;
7. `tested-sha.txt`;
8. `timeline-validation.json`;
9. `unit-tests.log`;
10. `workflow-summary.json`.

## Limites

- PASS manual continua manual;
- PASS simulado continua simulado;
- autorização N2/N3 e recuperação crítica não foram convertidas automaticamente em efeitos reais;
- nenhuma produção, instrução global ou merge foi autorizado;
- o resultado técnico não substitui a nova RC independente.

## Gate

O candidato R7B está tecnicamente pronto para ser entregue a outra sessão, agente ou revisor. A promoção permanece bloqueada até nova RC independente favorável e autorização explícita aplicável.
