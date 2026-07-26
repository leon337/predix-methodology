# Estado da integração normativa — MOP + Governança

## Estado

- **Data:** `2026-07-26`.
- **Última sincronização:** `2026-07-26T18:00:07-03:00`.
- **Branch:** `integration/mop-governance-v0.1`.
- **Base técnica original:** HEAD do PR #2 `e0da5c73ddbed2ded88f679396eba9d4729d3b51`.
- **Fonte incorporada do PR #1:** `MOP.md` no blob `4d1b7db945db9a37afa8ee8f283b7b8ebdbd6df1`.
- **Cultura sincronizada:** `CULTURA.md` v0.4-draft.
- **Guardrails:** v0.4-provisória, blob coincidente com a branch do PR #2.
- **Merge na `main`:** não autorizado e não realizado.
- **Merge entre PRs:** não realizado; conteúdos foram incorporados por cópia versionada e reconciliação documental.
- **Estado normativo:** candidato integrado, ainda não aprovado.

## Conteúdo reunido

A branch contém simultaneamente:

1. a fundação metodológica do PR #1 em `MOP.md`;
2. a Cultura v0.4-draft com as rodadas 1, 2 e 3;
3. a arquitetura Cultura–MOP–POPs;
4. guardrails, detecção, severidade e recuperação;
5. timeline, esquema, registro de decisões e testes;
6. pacote e resultado das decisões de Cultura;
7. validador executável TL-005 e sua automação de CI;
8. reconciliação semântica em `governance/NORMATIVE-RECONCILIATION-V04.md`.

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
- ciclo de 28 dias foi integrado ao fluxo operacional sem substituir branches, PRs, CI ou candidatos isolados;
- alocação dinâmica e continuidade definida por ciclo foram alinhadas à regra de não abandono;
- valores constitucionais foram vinculados aos grupos de guardrails;
- o gate da instrução global foi corrigido para exigir testes, RC e aprovação;
- o defeito de recomendação global da rodada 3 foi convertido em regra de recomendação por grupo para futura formalização e regressão;
- `CULTURA.md` e o resultado da rodada 3 foram sincronizados sem merge.

## Pendências de reconciliação textual e validação

- atualizar o texto principal da MOP com referências explícitas à Cultura, guardrails, recuperação, timeline e registro de decisões;
- atualizar `governance/ARCHITECTURE.md`, que ainda contém linguagem anterior à criação da Cultura;
- transformar as resoluções de UX em guardrail e teste de regressão explícitos;
- executar os testes restantes do plano de 64 cenários;
- criar linha de base e metas quantitativas;
- decidir desenvolvimento local e acessibilidade;
- executar RC independente em contexto separado;
- obter decisão explícita de Leo antes de qualquer promoção.

## Gate

Esta branch é somente um **candidato de integração**. Sua existência não encerra o PR #1, não encerra o PR #2, não autoriza merge, não aprova a Constituição e não libera a instrução global.
