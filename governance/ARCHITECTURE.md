# Arquitetura de Governança Documental da PREDIX

## Estado

- **Versão:** `0.2-integration-draft`.
- **Branch:** `integration/mop-governance-v0.1`.
- **Cultura:** `CULTURA.md` v0.4-draft existente e sincronizada.
- **Main:** não alterada.
- **Validação:** bateria de 64 testes, RC independente e aprovação explícita ainda exigidas.

## Objetivo

Separar regras constitucionais, metodologia, procedimentos, decisões e evidências temporais para evitar duplicidade, contradição, autoridade implícita e abandono silencioso.

## Hierarquia

```text
leis, políticas aplicáveis e segurança
                ↓
CULTURA.md — Cultura e Constituição candidata
                ↓
MOP.md — Metodologia Operacional
                ↓
POPs vigentes
                ↓
Registro de decisões e pendências
                ↓
Timeline, evidências, planos e execução
```

A Cultura ainda é minuta. A hierarquia serve para testar o candidato e não equivale à aprovação final.

## 1. Cultura e Constituição

### Fonte

[`../CULTURA.md`](../CULTURA.md), atualmente `0.4-draft`.

### Finalidade

Define propósito, missão, visão, frentes estratégicas, valores, limites éticos, autoridade de Leo, ciclo de 28 dias, continuidade e indicadores institucionais.

Não deve conter comandos específicos, procedimentos temporários ou evidências de uma execução isolada.

## 2. Metodologia Operacional PREDIX

### Fonte

[`../MOP.md`](../MOP.md), atualmente `0.2.0-integration-draft`.

### Finalidade

Define como a fábrica coordena pessoas, agentes e ferramentas; aplica N0–N4; conduz o Fluxo Assistido; opera ciclos; produz evidências; preserva decisões; testa e reconcilia resultados.

A MOP é subordinada à Cultura e não pode criar autorização implícita nem reduzir os dez grupos exclusivos de Leo.

## 3. Guardrails e recuperação

### Fontes

- [`GUARDRAILS.md`](GUARDRAILS.md);
- [`RECOVERY.md`](RECOVERY.md).

Os guardrails definem comportamentos proibidos, detecção, severidade e reação. A recuperação restaura o último estado válido. Nenhum dos dois cria autorização ou substitui decisão de Leo.

## 4. Procedimentos Operacionais Padrão

Um POP descreve atividade específica, repetível e estável.

Estrutura mínima:

1. objetivo;
2. gatilho;
3. pré-condições;
4. responsáveis;
5. ferramentas;
6. passos;
7. guardrails;
8. evidências;
9. conclusão;
10. rollback ou recuperação;
11. versão e histórico.

Criar somente quando houver repetição, necessidade de consistência, risco relevante ou ganho operacional superior ao custo de manutenção.

## 5. Registro de decisões

### Fonte

[`DECISION-REGISTER.md`](DECISION-REGISTER.md).

Preserva decisões aprovadas, provisórias, pendentes, bloqueadas, rejeitadas, substituídas e concluídas.

Campos mínimos: ID, data, origem, assunto, estado, responsável, evidência, condição de retomada e relações.

## 6. Timeline e evidências

### Fontes

- [`../timeline/SCHEMA.md`](../timeline/SCHEMA.md);
- arquivos em `timeline/`;
- validadores em `tools/`;
- testes em `tests/`.

A timeline registra quando conversa, decisão, ação, correção, teste ou bloqueio ocorreu. É append-only, distingue precisão temporal, usa IDs e chaves de idempotência e não pode persistir segredos.

A timeline não substitui documentos normativos nem o registro de decisões.

## 7. Estado operacional e evidência

Estados mínimos:

- `PROPOSTO`;
- `PLANEJADO`;
- `TENTADO`;
- `EXECUTADO`;
- `VERIFICADO`;
- `BLOQUEADO`.

Simulação, inspeção estática e observação manual devem ser identificadas. Ação externa exige evidência proporcional.

## 8. Testes

### Fonte

[`tests/TEST-PLAN-TIMELINE-GUARDRAILS.md`](tests/TEST-PLAN-TIMELINE-GUARDRAILS.md).

A bateria possui 64 cenários classificados como:

- automatizado;
- inspeção estática;
- manual/observado;
- simulado seguro;
- bloqueado;
- não executado.

Executar os 64 significa atribuir estado e evidência a cada cenário. Não significa aprovação global quando existir `FAIL`, `BLOCKED` ou `NOT_RUN`.

## 9. Precedência

Quando houver conflito:

1. leis, políticas aplicáveis e segurança;
2. Cultura aprovada ou candidata identificada para teste;
3. MOP vigente;
4. guardrails e recuperação;
5. POP vigente;
6. decisão específica válida;
7. plano ou tarefa;
8. timeline e conversa.

A camada inferior não substitui silenciosamente a superior.

## 10. Continuidade

Uma pendência deve ser concluída, rejeitada, substituída com vínculo, bloqueada com retomada ou mantida na fila. Mudança de assunto, ciclo, chat, branch ou ferramenta não encerra automaticamente a pendência.

## 11. Evolução documental

Toda mudança normativa relevante deve:

1. identificar a camada;
2. informar motivo e impacto;
3. verificar conflitos;
4. atualizar decisões e timeline;
5. executar testes afetados;
6. passar por revisão proporcional;
7. permanecer fora da `main` até autorização aplicável.

## 12. Gate

Esta arquitetura é candidata integrada. Permanecem bloqueados a aprovação constitucional, merge na `main`, produção, instrução global e promoção normativa sem testes e RC independente.
