# Remediação dos achados RC-R6 — Candidato R7

## Estado

- **Origem:** RC independente R6 com resultado `CHANGES_REQUIRED`.
- **R6 preservado:** branch `test/governance-64-20260726-r6`, SHA `9cb5414412a562e17ee41759c5965343b5192220`, PR #9.
- **Branch de trabalho:** `integration/mop-governance-v0.1`.
- **Estado desta remediação:** `IMPLEMENTADA_AGUARDANDO_CI_R7`.
- **Merge:** não autorizado e não realizado.

## RC-R6-01 — Estado canônico pós-R6

### Alterações

- `README.md` passou a registrar branch, SHA, PR, workflows, artifact e resultado da RC R6;
- `governance/INTEGRATION-STATUS.md` diferencia R6 histórico de R7 em remediação;
- `governance/GUARDRAILS.md` substitui pendências pré-R6 pelos gates R7;
- `governance/DECISION-REGISTER.md` marca R6 e sua RC como concluídos, preserva `CHANGES_REQUIRED` e abre sucessores R7.

### Critério de aceitação

Nenhuma fonte apresentada como estado atual pode declarar branch R6, testes R6, artifact R6 ou RC R6 como ainda não executados. Referências pré-R6 devem estar marcadas como históricas, substituídas ou superadas.

## RC-R6-02 — Obrigatoriedade e formatos TL-005

### Alterações

- eventos estruturados novos são definidos por `timeline/**/events/*.md`;
- cada arquivo novo deve conter exatamente um ID e exatamente uma chave de idempotência no formato Markdown canônico;
- arquivos fora de `events` são legado/suporte e podem omitir os campos;
- YAML persistido é proibido na versão 0.3 do esquema;
- ausência de ID ou chave produz erro;
- dois IDs ou duas chaves no mesmo evento produzem erro.

### Regressões

- entrada nova completa: PASS;
- entrada nova sem campos: FAIL;
- YAML em evento novo: FAIL;
- formato parcialmente válido: FAIL;
- legado fora de `events` sem campos: PASS;
- ID e chave inválidos: FAIL;
- duplicidades: FAIL.

## RC-R6-03 — Invalidação cronológica estruturada

### Alterações

- eventos FA-008 e FA-009 foram estruturados em `governance/evidence/assisted-flow-events.jsonl`;
- cada evento possui cenário, timestamp com fuso, outcome, evidência e nota;
- o runner R7 resolve o último evento do mesmo cenário;
- `PASS_MANUAL` mais recente libera o cenário;
- `REGRESSION` mais recente força `NOT_RUN` até novo reteste;
- o runner deixou de depender de duas strings fixas em um documento Markdown.

### Regressão obrigatória

Um teste automatizado cria PASS seguido de regressão posterior e exige resultado `NOT_RUN`.

## RC-R6-04 — Artifact bruto completo

### Alterações do workflow R7

O próximo artifact inclui:

1. `unit-tests.log`;
2. `timeline-validation.json`;
3. `secret-scan.json`;
4. `governance-runner.log`;
5. `results.json`;
6. `results.md`;
7. `tested-sha.txt`;
8. `evaluated-files.sha256`;
9. `evidence-manifest.json`;
10. `workflow-summary.json`.

O manifesto registra SHA testado, evento, ref, workflow, run, versão Python, runner e resumos das verificações.

## Gate R7

A remediação somente pode ser classificada como verificada quando:

1. um novo HEAD for congelado sem alterar o R6;
2. o PR R7 estiver aberto como Draft;
3. testes unitários passarem;
4. TL-005 passar sobre o repositório real;
5. scanner passar;
6. os 64 cenários terminarem sem `FAIL`, `BLOCKED` ou `NOT_RUN`;
7. o SHA do artifact for igual ao SHA da branch congelada;
8. o artifact contiver a cadeia bruta declarada;
9. o resultado for registrado fora do HEAD congelado;
10. uma nova RC ocorrer em contexto separado, sem remediação e sem merge.
