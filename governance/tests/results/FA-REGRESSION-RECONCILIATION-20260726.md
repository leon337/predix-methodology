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
8. Foi apresentado um painel de reteste com dois grupos independentes, uma indicação técnica dentro de cada grupo e nenhuma alternativa previamente selecionada.
9. Leo escolheu alternativas diferentes das indicações técnicas nos dois grupos e retornou o comando `RETESTE_MANUAL_FA009_MULTIGRUPO`.

## Estado por cenário afetado

### FA-008 — próximas opções após comando

- **Regressão:** confirmada após a resposta da RC bloqueada.
- **Recuperação observada:** um novo painel foi apresentado e o comando específico foi retornado por Leo.
- **Estado atual:** `PASS_MANUAL_RECUPERADO`.
- **Marcador executável:** `FA-008=PASS_MANUAL_RECUPERADO`.
- **Limite:** continua sendo evidência do cliente atual, não automação de interface.

### FA-009 — recomendação por grupo sem preseleção

- **Regressão:** confirmada no painel com vários grupos da rodada 3.
- **Reteste multigrupo:** executado no cliente atual.
- **Grupos apresentados:** densidade do relatório e ordem das informações.
- **Recomendação em cada grupo:** sim.
- **Preseleção:** não.
- **Escolha contrária:** sim, nos dois grupos.
- **Comando retornado por Leo:**

```text
RETESTE_MANUAL_FA009_MULTIGRUPO
FORMATO=RELATORIO_DETALHADO_COM_EVIDENCIAS
ORDEM=ORDEM_CRONOLOGICA
CRITERIO=RECOMENDACAO_EM_CADA_GRUPO_SEM_PRESELECAO
ESCOLHA_CONTRARIA_EM_PELO_MENOS_UM_GRUPO=SIM
EFEITO_OPERACIONAL=NAO
MERGE=NAO
```

- **Estado atual:** `PASS_MANUAL_RECUPERADO`.
- **Marcador executável:** `FA-009_MULTIGROUP=PASS_MANUAL`.
- **Limite:** evidência manual do cliente atual; não equivale a teste automatizado de interface nem prova comportamento em todos os clientes.

## Consequência para a bateria

- FA-008 e FA-009 podem ser classificados como `PASS_MANUAL` pelo executor R6;
- os PASS anteriores continuam históricos e não substituem esta evidência cronológica;
- a bateria integral deve ser executada no HEAD exato após a reconciliação documental;
- qualquer regressão posterior invalida novamente o marcador até novo reteste.

## Critério de liberação atendido

1. foram apresentados dois grupos independentes;
2. uma indicação técnica foi destacada dentro de cada grupo;
3. nenhuma alternativa foi previamente selecionada;
4. Leo escolheu alternativas diferentes das indicações técnicas;
5. o comando preservou somente as escolhas confirmadas;
6. o comando foi recebido de volta na conversa;
7. o marcador `FA-009_MULTIGROUP=PASS_MANUAL` foi registrado.
