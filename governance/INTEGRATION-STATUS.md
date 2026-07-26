# Estado da integração normativa — MOP + Governança

## Estado

- **Data:** `2026-07-26`.
- **Branch:** `integration/mop-governance-v0.1`.
- **Base técnica:** HEAD do PR #2 `e0da5c73ddbed2ded88f679396eba9d4729d3b51`.
- **Fonte incorporada do PR #1:** `MOP.md` no blob `4d1b7db945db9a37afa8ee8f283b7b8ebdbd6df1`.
- **Merge na `main`:** não autorizado e não realizado.
- **Merge entre PRs:** não realizado; o conteúdo exclusivo do PR #1 foi incorporado por cópia versionada.
- **Estado normativo:** candidato integrado, ainda não aprovado.

## Conteúdo reunido

A branch contém simultaneamente:

1. a fundação metodológica do PR #1 em `MOP.md`;
2. a arquitetura Cultura–MOP–POPs;
3. guardrails, detecção, severidade e recuperação;
4. timeline, esquema, registro de decisões e testes;
5. descoberta e pacote de decisão da Cultura;
6. validador executável TL-005 e sua automação de CI.

## Regra de precedência provisória

1. `MOP.md` define o corpo metodológico geral;
2. `governance/ARCHITECTURE.md` define as camadas documentais;
3. `governance/GUARDRAILS.md` define comportamentos proibidos e reação;
4. `governance/RECOVERY.md` define restauração de estado;
5. `governance/DECISION-REGISTER.md` define o estado das decisões;
6. `timeline/*` registra sequência temporal e evidências;
7. em conflito, segurança, verdade operacional, autorização válida e preservação do último estado confirmado prevalecem.

## Pendências de reconciliação de conteúdo

- incluir na MOP referências explícitas aos guardrails, recuperação, timeline e registro de decisões;
- resolver possíveis duplicidades entre as regras gerais da MOP e documentos de governança;
- atualizar versões e estados de forma coerente;
- executar o TL-005 sobre o conjunto integrado em CI;
- concluir decisões de Cultura sem transformar candidatos em valores aprovados;
- realizar RC independente em contexto separado;
- obter decisão explícita de Leo antes de qualquer promoção.

## Gate

Esta branch é somente um **candidato de integração**. Sua existência não encerra o PR #1, não encerra o PR #2, não autoriza merge e não libera a instrução global.
