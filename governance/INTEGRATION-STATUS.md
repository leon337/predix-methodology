# Estado da integração normativa — MOP + Governança

## Estado

- **Data:** `2026-07-26`.
- **Última reconciliação:** pós-reteste manual FA-009 multigrupo.
- **Branch:** `integration/mop-governance-v0.1`.
- **Base técnica original:** HEAD histórico do PR #2 `e0da5c73ddbed2ded88f679396eba9d4729d3b51`.
- **Fonte incorporada do PR #1:** `MOP.md` copiado e posteriormente reconciliado na branch integrada.
- **Cultura sincronizada:** `CULTURA.md` v0.4-draft.
- **Guardrails:** v0.4-provisória.
- **Merge na `main`:** não autorizado e não realizado.
- **Merge entre PRs:** não realizado; conteúdos foram incorporados por cópia versionada e reconciliação documental.
- **Estado normativo:** candidato integrado, ainda não aprovado.

## Conteúdo reunido

A branch contém simultaneamente:

1. a fundação metodológica em `MOP.md`;
2. a Cultura v0.4-draft com as rodadas 1, 2 e 3;
3. a arquitetura Cultura–MOP–POPs;
4. guardrails, detecção, severidade e recuperação;
5. timeline, esquema, registro de decisões e testes;
6. pacote e resultado das decisões de Cultura;
7. validadores TL-005 e TL-010;
8. executor da bateria de 64 cenários;
9. reconciliação semântica em `governance/NORMATIVE-RECONCILIATION-V04.md`;
10. registro de incidentes e reconciliação cronológica das regressões FA.

## Regra de precedência provisória

1. leis, políticas aplicáveis e segurança;
2. `CULTURA.md` v0.4-draft como camada constitucional candidata;
3. `MOP.md` como método operacional subordinado;
4. `governance/GUARDRAILS.md` como limites comportamentais e reações;
5. `governance/RECOVERY.md` como restauração de estado;
6. POPs vigentes;
7. `governance/DECISION-REGISTER.md` como estado das decisões;
8. `timeline/*` como sequência temporal e evidências;
9. em conflito, segurança, verdade operacional, autorização válida e preservação do último estado confirmado prevalecem.

A precedência nesta branch serve para testar o candidato. Ela não converte a minuta em Constituição final.

## Reconciliação realizada

- autoridade exclusiva de Leo foi mapeada contra papéis e delegação da MOP;
- ciclo de 28 dias foi integrado ao fluxo operacional;
- alocação dinâmica e continuidade definida por ciclo foram alinhadas à regra de não abandono;
- valores constitucionais foram vinculados aos grupos de guardrails;
- o gate da instrução global exige testes, RC independente e aprovação explícita;
- `CULTURA.md` e o resultado da rodada 3 foram sincronizados;
- `MOP.md` e `governance/ARCHITECTURE.md` foram atualizados com referências à Cultura, guardrails, recuperação, timeline e registro de decisões;
- a bateria R5B foi executada, mas sua referência histórica não é usada como substituta do novo HEAD;
- o falso negativo do scanner com `#` foi corrigido e recebeu regressões específicas;
- FA-008 e FA-009 foram reconciliados por evidência cronológica;
- o runner R6 invalida regressão manual não retestada;
- o incidente de abandono do Fluxo Assistido foi preservado;
- a análise no mesmo contexto foi reclassificada como pré-revisão interna/adversarial.

## Pendências atuais

- reexecutar regressões, scanner, TL-005 e os 64 cenários no mesmo HEAD congelado;
- publicar as evidências do novo ciclo R6;
- atualizar o handoff canônico com a referência exata testada;
- abrir ou atualizar um PR Draft específico do candidato integrado para permitir revisão sobre uma referência única;
- executar RC independente em outra sessão, agente ou revisor;
- criar linha de base e metas quantitativas;
- decidir desenvolvimento local e acessibilidade;
- obter decisão explícita de Leo antes de qualquer promoção;
- exigir autorização N3 específica antes de qualquer merge.

## Gate

Esta branch é somente um **candidato de integração**. Sua existência não encerra automaticamente os PRs históricos, não autoriza merge, não aprova a Constituição e não libera a instrução global.
