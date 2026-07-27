# Estado da integração normativa — MOP + Governança

## Estado

- **Data:** `2026-07-26`.
- **Última reconciliação:** pós-falha do R7 inicial, durante preparação do R7B.
- **Branch canônica de trabalho:** `integration/mop-governance-v0.1`.
- **Candidato histórico R6:** `test/governance-64-20260726-r6`, SHA `9cb5414412a562e17ee41759c5965343b5192220`, PR #9.
- **Candidato histórico R7 inicial:** `test/governance-64-20260726-r7`, SHA `c38946abf8526a9ad47075efbb04f75ba4a0fe00`, PR #14 fechado após falha.
- **Sucessor:** R7B a congelar a partir da branch integrada corrigida.
- **Cultura sincronizada:** `CULTURA.md` v0.4-draft.
- **Guardrails:** v0.4-provisória.
- **Merge na `main`:** não autorizado e não realizado.
- **Estado normativo:** candidato integrado em remediação; ainda não aprovado.

## Resultado histórico R6

- workflow governança: `30224913937`, sucesso;
- workflow timeline: `30224914038`, sucesso;
- artifact: `8638274889`;
- distribuição: 25 automatizados, 14 estáticos, 10 manuais e 15 simulados;
- `FAIL=0`, `BLOCKED=0`, `NOT_RUN=0` no snapshot;
- RC independente: `CHANGES_REQUIRED`;
- independência: atendida;
- merge recomendado: não;
- edição/remediação durante a RC: não.

O R6 permanece como evidência histórica imutável. Seus PASS não autorizam promoção porque a RC identificou quatro achados obrigatórios.

## Resultado histórico R7 inicial

- workflow governança: `30228522319`, failure;
- workflow timeline: `30228522369`, failure;
- artifact parcial: `8639293479`;
- testes unitários: 18 PASS;
- TL-005: FAIL por notação conceitual do esquema que imitava campos persistidos com placeholders;
- PR #14: fechado sem merge;
- branch e SHA: preservados sem alteração.

A correção foi aplicada somente na branch integrada. O R7 inicial não foi reescrito e não será apresentado como candidato válido.

## Achados RC-R6 ativos

1. `RC-R6-01` — fontes canônicas mantinham estados anteriores ao R6;
2. `RC-R6-02` — TL-005 não exigia campos em entradas novas e não formalizava YAML;
3. `RC-R6-03` — runner não realizava invalidação cronológica genérica;
4. `RC-R6-04` — artifact não continha toda a cadeia bruta de evidências.

## Conteúdo reunido

A branch contém simultaneamente:

1. a fundação metodológica em `MOP.md`;
2. a Cultura v0.4-draft com as rodadas 1, 2 e 3;
3. a arquitetura Cultura–MOP–POPs;
4. guardrails, detecção, severidade e recuperação;
5. timeline, esquema, registro de decisões e testes;
6. pacote e resultado das decisões de Cultura;
7. validadores TL-005 e TL-010;
8. executores históricos e o executor cronológico R7;
9. reconciliação semântica em `governance/NORMATIVE-RECONCILIATION-V04.md`;
10. registro de incidentes e evidência estruturada das regressões FA.

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

## Remediação R7/R7B executada na branch de trabalho

- estado pós-R6 registrado nas fontes canônicas;
- política TL-005 alterada para exigir exatamente um ID e uma chave em `timeline/**/events/*.md`;
- fronteira de legado definida por caminho;
- YAML persistido formalmente proibido na versão 0.3 do esquema;
- testes adicionados para entrada incompleta, YAML, formato parcial e arquivo legado;
- eventos FA-008/FA-009 estruturados em JSONL com timestamp e resultado;
- runner criado para fazer a evidência mais recente do mesmo cenário prevalecer;
- teste criado para provar que regressão posterior força `NOT_RUN`;
- workflow ampliado para produzir logs de testes, scanner, TL-005, manifesto, hashes e resumo bruto;
- falha do R7 inicial preservada;
- notação conceitual do esquema corrigida para não ser confundida com evento persistido.

## Pendências atuais

- congelar o HEAD R7B sem alterar R6 ou R7 inicial;
- abrir PR Draft específico do R7B;
- executar testes unitários, scanner, TL-005 e 64 cenários no mesmo SHA;
- verificar o artifact bruto completo;
- registrar resultado R7B fora do HEAD congelado;
- submeter o novo candidato a outra RC independente;
- criar linha de base e metas quantitativas;
- decidir desenvolvimento local e acessibilidade;
- obter decisão explícita de Leo antes de qualquer promoção;
- exigir autorização N3 específica antes de qualquer merge.

## Gate

Esta branch é somente um **candidato de integração em remediação**. Sua existência não encerra automaticamente os PRs históricos, não autoriza merge, não aprova a Constituição e não libera a instrução global.
