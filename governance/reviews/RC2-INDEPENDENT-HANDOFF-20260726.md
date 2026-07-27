# Handoff para RC independente — candidato integrado pós-R6

## Objetivo

Permitir que outra sessão, agente ou revisor avalie o candidato integrado sem compartilhar o contexto de implementação que produziu ou remediou os documentos.

## Regra de independência

O revisor não deve reutilizar conclusões desta sessão como prova. Deve:

1. resolver o HEAD da branch congelada no início da revisão;
2. comparar o SHA resolvido com o SHA testado registrado na issue #3;
3. bloquear a RC se a referência tiver mudado;
4. ler os artefatos diretamente no GitHub;
5. reproduzir comparações e testes prioritários;
6. emitir conclusão própria;
7. não editar nem remediar durante a revisão.

## Alvo canônico

```text
REPOSITORIO=leon337/predix-methodology
BASE=main
CANDIDATO_INTEGRADO=integration/mop-governance-v0.1
HEAD_REF_CONGELADO=test/governance-64-20260726-r6
ISSUE_RC=3
MERGE_AUTORIZADO=NAO
```

O SHA exato testado deve ser registrado na issue #3 depois da execução R6. O revisor deve usar esse registro como referência de entrada e reconfirmá-lo diretamente no GitHub.

## Contexto histórico que não substitui a RC

- PR #1 e PR #2 são fontes históricas de entrada;
- R5B é uma linha de base histórica, não prova do HEAD R6;
- a análise feita no mesmo contexto foi reclassificada como pré-revisão interna/adversarial;
- o incidente `INC-20260726-194538-001` deve ser preservado;
- nenhum PASS manual ou simulado deve ser reclassificado como automação executável.

## Arquivos prioritários

1. `CULTURA.md`;
2. `MOP.md`;
3. `README.md`;
4. `governance/ARCHITECTURE.md`;
5. `governance/GUARDRAILS.md`;
6. `governance/RECOVERY.md`;
7. `governance/DECISION-REGISTER.md`;
8. `governance/INTEGRATION-STATUS.md`;
9. `governance/PR1-PR2-RECONCILIATION.md`;
10. `governance/tests/results/FA-REGRESSION-RECONCILIATION-20260726.md`;
11. `tools/scan_secrets.py` e `tests/test_scan_secrets.py`;
12. `tools/run_governance_64_v4.py`;
13. `timeline/SCHEMA.md`, fechamento diário e eventos posteriores;
14. resultados e artifact da execução R6.

## Evidências obrigatórias

- comparação `main...HEAD_REF_CONGELADO`;
- SHA do HEAD congelado e SHA efetivamente testado;
- estado dos PRs históricos e do PR Draft do candidato integrado, quando criado;
- regressões do scanner com `#`;
- scanner TL-010 sobre o HEAD congelado;
- TL-005 sobre o mesmo HEAD;
- bateria integral de 64 cenários com runner R6;
- reconciliação cronológica FA-008 e FA-009;
- distinção entre automatizado, estático, manual e simulado;
- fechamento diário real;
- ausência de `FAIL`, `BLOCKED` e `NOT_RUN`, ou classificação objetiva se existirem;
- confirmação de ausência de merge.

## Perguntas adversariais

1. Algum documento afirma execução sem evidência suficiente?
2. Algum `PASS` deveria ser `BLOCKED` ou `NOT_RUN`?
3. O scanner ainda possui falso negativo relevante ou falso positivo não tratado?
4. Uma regressão manual posterior pode ser mascarada por arquivo antigo?
5. Há regras incompatíveis entre Cultura, MOP, guardrails e recuperação?
6. A timeline pode duplicar registros ou armazenar conteúdo sensível?
7. Uma ação N2/N3 pode escapar com comando genérico, referência alterada ou autorização reutilizada?
8. Uma decisão pendente pode desaparecer na troca de assunto?
9. A recomendação da IA pode selecionar, impor ou deixar de ser indicada por grupo?
10. A cobertura da timeline é apresentada como global sem ingestão real?
11. O candidato integrado está sendo confundido com versão aprovada?
12. O HEAD revisado é exatamente o HEAD testado?

## Saída exigida

```text
RESULTADO=PASS | FAIL | BLOCKED | CHANGES_REQUIRED
HEAD_REVISADO=<sha>
HEAD_TESTADO=<sha>
INDEPENDENCIA=ATENDIDA | NAO_ATENDIDA
MERGE_RECOMENDADO=SIM | NAO
MERGE_REALIZADO=NAO
```

Além disso, listar:

- bloqueadores;
- achados por severidade;
- evidências por arquivo, linha, commit ou workflow;
- testes repetidos;
- remediações exigidas;
- decisões ainda pendentes;
- declaração explícita de que o revisor não implementou nem remediou o candidato.

## Comando de continuidade para outra sessão ou agente

```text
EXECUTAR_RC_INDEPENDENTE_CANDIDATO_PREDIX_R6
REPOSITORIO=leon337/predix-methodology
BASE=main
HEAD_REF=test/governance-64-20260726-r6
ISSUE=3
SEM_EDICAO=SIM
SEM_REMEDIACAO=SIM
SEM_MERGE=SIM
```

## Proibições

- não realizar merge;
- não aprovar automaticamente;
- não usar a pré-revisão interna como substituta da análise;
- não corrigir arquivos dentro da mesma revisão;
- não declarar cobertura global;
- não inventar resultado de teste indisponível;
- não revisar outra referência sem registrar a mudança e reiniciar a RC.
