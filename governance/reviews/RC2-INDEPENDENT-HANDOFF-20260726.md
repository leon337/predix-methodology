# Handoff para RC independente — PR #2

## Objetivo

Permitir que outra sessão, agente ou revisor avalie o PR #2 sem compartilhar o contexto de implementação que produziu os documentos.

## Regra de independência

O revisor não deve reutilizar conclusões desta sessão como prova. Deve:

1. resolver o HEAD atual da branch no início da revisão;
2. registrar o SHA analisado;
3. ler os artefatos diretamente no GitHub;
4. reproduzir comparações e testes prioritários;
5. emitir conclusão própria.

## Alvo

```text
REPOSITÓRIO=leon337/predix-methodology
PR=2
BASE=main
HEAD_REF=mop/timeline-conversas-20260726
MERGE_AUTORIZADO=NAO
```

O SHA não é fixado neste arquivo porque a própria criação e remediações posteriores alteram o HEAD. O revisor deve capturar o SHA final no momento da RC e bloquear a revisão se ele mudar durante a análise.

## Arquivos prioritários

1. `MOP.md` no PR #1;
2. `README.md` no PR #2;
3. `governance/ARCHITECTURE.md`;
4. `governance/GUARDRAILS.md`;
5. `governance/RECOVERY.md`;
6. `governance/DECISION-REGISTER.md`;
7. `governance/PR1-PR2-RECONCILIATION.md`;
8. `timeline/SCHEMA.md`;
9. `TIMELINE.md` e timeline diária;
10. plano e resultados de testes;
11. investigação de mergeability;
12. descoberta e pacote candidato da Cultura.

## Evidências obrigatórias

- comparação `main...HEAD_REF`;
- comparação `feat/mop-v0.1-fundacao...HEAD_REF`;
- estado atual do PR #1 e PR #2;
- lista de arquivos alterados;
- resultados FA-005 e FA-010 com interação manual;
- TL-005 e TL-010;
- AU-001 a AU-008 em simulação segura;
- RC-001 a RC-006;
- fechamento diário real;
- verificação de ausência de segredos;
- causa ou tratamento formal do estado não mesclável.

## Perguntas adversariais

1. Algum documento afirma execução sem evidência suficiente?
2. Algum `PASS` deveria ser `BLOCKED` ou `NOT_RUN`?
3. Há regras incompatíveis entre MOP, guardrails e recuperação?
4. A timeline pode duplicar registros ou armazenar conteúdo sensível?
5. Uma ação N2/N3 pode escapar com comando genérico, referência alterada ou autorização reutilizada?
6. Uma decisão pendente pode desaparecer na troca de assunto?
7. A recomendação da IA pode selecionar ou impor uma escolha?
8. A cobertura da timeline é apresentada como global sem ingestão real?
9. O PR amplo deve ser dividido antes de integração?
10. A Cultura candidata foi confundida com Constituição aprovada?

## Saída exigida

O revisor deverá gerar:

```text
RESULTADO=PASS | FAIL | CHANGES_REQUIRED
HEAD_REVISADO=<sha>
INDEPENDENCIA=ATENDIDA | NAO_ATENDIDA
MERGE_RECOMENDADO=SIM | NAO
```

Além disso, deve listar:

- bloqueadores;
- achados importantes;
- evidências;
- remediações exigidas;
- testes repetidos;
- decisões que continuam pendentes.

## Comando de continuidade sugerido

```text
EXECUTAR_RC_INDEPENDENTE_PR_2
REPOSITORIO=leon337/predix-methodology
PR=2
HEAD_REF=mop/timeline-conversas-20260726
BASE=main
SEM_MERGE=SIM
```

## Proibições

- não realizar merge;
- não aprovar automaticamente;
- não usar a RC anterior como substituta da análise;
- não corrigir arquivos dentro da mesma revisão sem separar achado de remediação;
- não declarar cobertura global;
- não inventar resultado de teste indisponível.
