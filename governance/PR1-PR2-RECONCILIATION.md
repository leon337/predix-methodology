# Reconciliação normativa — PR #1 e PR #2

## Estado atual

- **Data da descoberta original:** `2026-07-26`.
- **Documento histórico:** sim; a conclusão original foi substituída pela branch integrada.
- **PR #1:** `feat/mop-v0.1-fundacao` → `main`.
- **PR #2:** `mop/timeline-conversas-20260726` → `main`.
- **Branch sucessora:** `integration/mop-governance-v0.1`.
- **Merge autorizado:** não.
- **Estado:** integração física executada por cópia versionada e reconciliação documental; validação e RC independente ainda pendentes.

## Divergência histórica confirmada

Na descoberta inicial:

- PR #1 e PR #2 possuíam conteúdo exclusivo;
- a branch de governança estava à frente por dezenas de commits;
- a branch da MOP possuía commits ausentes na branch de governança;
- o merge base comum era `ef296e2b2404c6acf47676c01d224ae478e6e569`.

Essa divergência motivou a criação da branch integrada. Ela não deve mais ser interpretada como integração ainda inexistente.

## Conteúdo consolidado

### Fundação metodológica

A branch integrada incorporou de forma versionada:

- `MOP.md`;
- fluxo de produto e desenvolvimento;
- papéis e ensino aplicado;
- fontes de verdade;
- trem, reconciliação e organização de chats;
- regras iniciais da metodologia.

### Governança operacional

Também incorporou:

- `CULTURA.md` v0.4-draft;
- arquitetura Cultura–MOP–POPs;
- guardrails GR-001 a GR-049;
- detecção, severidade e recuperação;
- timeline e registro de decisões;
- testes, resultados, incidentes e revisões;
- continuidade e não abandono de decisões.

## Fonte canônica candidata

Enquanto não houver aprovação e merge:

1. `integration/mop-governance-v0.1` é o candidato integrado para testes e RC;
2. PR #1 e PR #2 permanecem fontes históricas de entrada;
3. nenhum PR histórico isolado deve ser tratado como versão normativa final;
4. conflitos devem ser resolvidos na branch integrada com evidência e registro;
5. segurança, transparência, autorização e verdade operacional prevalecem.

## Mapa de consolidação

| Assunto | Fonte histórica | Destino candidato integrado |
|---|---|---|
| propósito, valores e autoridade superior | descoberta e decisões do PR #2 | `CULTURA.md` |
| metodologia geral | `MOP.md` do PR #1 | `MOP.md` reconciliado |
| guardrails e níveis de risco | PR #2 e decisões | `MOP.md` + `governance/GUARDRAILS.md` |
| recuperação de estado | PR #2 | `governance/RECOVERY.md` |
| procedimentos repetíveis | ainda não aprovados | `pops/*.md` quando houver procedimento estável |
| decisões e pendências | PR #2 | `governance/DECISION-REGISTER.md` |
| histórico temporal | PR #2 | `TIMELINE.md` e `timeline/*` |
| estado da integração | branch sucessora | `governance/INTEGRATION-STATUS.md` |

## Gates atuais

A reconciliação somente poderá ser promovida quando:

- README, MOP, arquitetura, guardrails, recuperação e registro de decisões estiverem coerentes;
- scanner, TL-005 e bateria de 64 cenários forem executados no mesmo HEAD congelado;
- regressões manuais posteriores forem consideradas pelo executor;
- existir um alvo único e explícito para a RC;
- uma RC independente em contexto separado emitir resultado favorável;
- Leo autorizar explicitamente a promoção;
- qualquer merge receber autorização N3 específica.

## Decisão atual

**Integração física e reconciliação documental executadas na branch `integration/mop-governance-v0.1`; promoção, RC independente e merge permanecem bloqueados.**
