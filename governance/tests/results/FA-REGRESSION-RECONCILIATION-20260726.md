# Reconciliação de regressões do Fluxo Assistido — 2026-07-26

## Estado

- **Projeto:** Fábrica de softwares.
- **Cliente:** ChatGPT atual.
- **Escopo:** evidências FA-008 e FA-009 após os incidentes da rodada 3 e da RC pós-R5B.
- **Ações N2/N3 reais:** nenhuma.
- **Merge:** não autorizado.
- **Regra:** evidência antiga não pode mascarar regressão posterior.

## Linha do tempo da regressão

1. FA-001 a FA-010 receberam evidência manual inicial.
2. Na rodada 3, um painel exibiu uma recomendação global em vez de uma recomendação por grupo, não indicou claramente a decisão ausente e desviou para comando textual na opção personalizada.
3. Após a R5B, a resposta que classificou o gate da RC como bloqueado encerrou com lista estática e sem próximo painel.
4. O segundo desvio foi registrado como `INC-20260726-194538-001`.
5. A análise feita no mesmo contexto foi invalidada como RC independente e reclassificada como pré-revisão interna/adversarial.
6. Um painel de recuperação foi apresentado sem preseleção, com recomendação destacada e comando específico.
7. Leo retornou o comando `PLANO_ASSISTIDO_RECUPERACAO_RC_POS_INCIDENTE`, confirmando que a seleção e a geração do comando voltaram a funcionar.

## Estado por cenário afetado

### FA-008 — próximas opções após comando

- **Regressão:** confirmada após a resposta da RC bloqueada.
- **Recuperação observada:** um novo painel foi apresentado e o comando específico foi retornado por Leo.
- **Estado atual:** `PASS_MANUAL_RECUPERADO`.
- **Marcador executável:** `FA-008=PASS_MANUAL_RECUPERADO`.
- **Limite:** continua sendo evidência do cliente atual, não automação de interface.

### FA-009 — recomendação por grupo sem preseleção

- **Regressão:** confirmada no painel com vários grupos da rodada 3.
- **Recuperação parcial:** o painel posterior de grupo único apresentou recomendação sem preseleção.
- **Lacuna:** ainda falta repetir manualmente um painel com **dois ou mais grupos independentes**, cada grupo contendo sua própria recomendação, sem opção previamente marcada.
- **Estado atual:** `NOT_RUN_MULTIGROUP_RETEST`.
- **Marcador pendente:** `FA-009_MULTIGROUP=NOT_RUN`.

## Consequência para a bateria

Até existir evidência manual específica do cenário multigrupo:

- FA-008 pode permanecer `PASS_MANUAL` com referência a este documento;
- FA-009 deve ser `NOT_RUN`;
- a bateria integral não pode declarar `BLOCKED=0` e `NOT_RUN=0`;
- o HEAD final não deve ser entregue à RC independente como candidato favorável.

## Critério para liberar FA-009

1. apresentar no mínimo dois grupos independentes;
2. destacar uma recomendação dentro de cada grupo;
3. não preselecionar nenhuma alternativa;
4. permitir escolha diferente da recomendação em pelo menos um grupo;
5. gerar comando que preserve somente as escolhas confirmadas;
6. receber o comando de retorno de Leo;
7. registrar o marcador `FA-009_MULTIGROUP=PASS_MANUAL` neste documento ou em complemento append-only vinculado.
