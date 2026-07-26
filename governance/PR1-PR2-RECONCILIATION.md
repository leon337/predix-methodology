# Reconciliação normativa — PR #1 e PR #2

## Estado

- **Data:** `2026-07-26`.
- **PR #1:** `feat/mop-v0.1-fundacao` → `main`.
- **PR #2:** `mop/timeline-conversas-20260726` → `main`.
- **Merge autorizado:** não.
- **Objetivo:** impedir que duas branches paralelas criem fontes normativas contraditórias.

## Divergência confirmada

A comparação entre as branches retornou:

- `status: diverged`;
- PR #2/branch de governança à frente por dezenas de commits;
- branch da MOP com dois commits que não estão na branch de governança;
- merge base comum: `ef296e2b2404c6acf47676c01d224ae478e6e569`.

## Conteúdo exclusivo relevante

### PR #1 — Fundação da MOP

Fonte provisória de:

- `MOP.md` completo;
- fluxo de produto e desenvolvimento;
- papéis e ensino aplicado;
- fontes de verdade;
- trem, reconciliação e organização de chats;
- regras iniciais da metodologia.

### PR #2 — Governança operacional

Fonte provisória de:

- arquitetura Cultura–MOP–POPs;
- guardrails GR-001 a GR-049;
- detecção, severidade e recuperação;
- timeline e registro de decisões;
- testes e revisões;
- descoberta da Cultura;
- continuidade e não abandono de decisões.

## Regra canônica provisória

Enquanto a reconciliação não for implementada:

1. `MOP.md` do PR #1 é a fonte provisória para o corpo metodológico;
2. documentos `governance/*` do PR #2 são fontes provisórias para guardrails, recuperação, decisões e arquitetura documental;
3. nenhum dos PRs pode ser tratado isoladamente como versão normativa final;
4. em conflito, segurança, transparência, evidência e bloqueio de ações críticas prevalecem;
5. qualquer conflito deve ser registrado, não resolvido silenciosamente por ordem de commit.

## Arquitetura de integração recomendada

Criar posteriormente uma branch limpa, por exemplo:

```text
integration/mop-governance-v0.1
```

A branch deve nascer do HEAD validado do PR #1 e receber, de forma controlada:

1. documentos de governança do PR #2;
2. atualização manual de `README.md`;
3. integração das regras N0–N4, guardrails, timeline e continuidade no `MOP.md`;
4. remoção de duplicidades e contradições;
5. atualização do registro de decisões;
6. testes e RC independente sobre o conjunto final.

## Mapa de consolidação

| Assunto | Fonte de entrada | Destino canônico futuro |
|---|---|---|
| propósito, valores e autoridade superior | descoberta do PR #2 | `CULTURA.md`, após decisão de Leo |
| metodologia geral | `MOP.md` do PR #1 | `MOP.md` reconciliado |
| guardrails e níveis de risco | PR #2 e decisões da conversa | `MOP.md` + `governance/GUARDRAILS.md` |
| recuperação de estado | PR #2 | `governance/RECOVERY.md` e referência na MOP |
| procedimentos repetíveis | ainda não aprovados | `pops/*.md` quando houver procedimento estável |
| decisões e pendências | PR #2 | `governance/DECISION-REGISTER.md` |
| histórico temporal | PR #2 | `TIMELINE.md` e `timeline/*` |

## Gates

A reconciliação somente pode ser considerada concluída quando:

- existe uma branch de integração identificada;
- `MOP.md` contém ou referencia as regras aprovadas sem contradição;
- README, MOP, guardrails e registro de decisões usam estados e versões coerentes;
- testes críticos possuem evidência suficiente;
- o PR é tecnicamente mesclável;
- uma RC independente em contexto separado emite resultado favorável;
- Leo autoriza explicitamente a versão.

## Decisão atual

**Reconciliação planejada e fonte provisória definida; integração física ainda não executada.**

PR #1 e PR #2 devem permanecer sem merge até a criação e validação da branch reconciliada.
