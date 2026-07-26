# Complemento de Normalização — Timeline 2026-07-26

## Estado

Este complemento remedia entradas legadas sem apagar ou reescrever silenciosamente o arquivo original.

## Mapeamento

| Entrada original | ID estável | Precisão | Período | Conversa | Estado operacional | Decisões relacionadas |
|---|---|---|---|---|---|---|
| 13:03 — Correção do uso do @Visualize | `TL-20260726-130300-001` | aproximada | tarde | Governança e Fluxo Assistido | CORRIGIDO | `DEC-20260726-017` |
| 13:08 — Ações críticas | `TL-20260726-130800-002` | aproximada | tarde | Governança e Fluxo Assistido | PROPOSTO | `DEC-20260726-014`, `DEC-20260726-015` |
| 13:13 — Política completa | `TL-20260726-131300-003` | aproximada | tarde | Governança e Fluxo Assistido | PROPOSTO | `DEC-20260726-015` |
| 13:35 — 5W1H, 5 Porquês e guardrails | `TL-20260726-133500-004` | aproximada | tarde | Governança e Fluxo Assistido | EXECUTADO | `DEC-20260726-013`, `DEC-20260726-014` |
| 13:47 — Seleção múltipla | `TL-20260726-134700-005` | aproximada | tarde | Governança e Fluxo Assistido | EXECUTADO | `DEC-20260726-017` |
| 13:52 — Timeline persistente | `TL-20260726-135200-006` | aproximada | tarde | Governança e Fluxo Assistido | EXECUTADO | `DEC-20260726-010`, `DEC-20260726-016` |
| 14:04:40 — Plano da timeline | `TL-20260726-140440-007` | exata | tarde | Governança e Fluxo Assistido | EXECUTADO | `DEC-20260726-009`, `DEC-20260726-010`, `DEC-20260726-016` |
| 14:07:55 — Execução da timeline | `TL-20260726-140755-008` | exata | tarde | Governança e Fluxo Assistido | VERIFICADO | `DEC-20260726-010`, `DEC-20260726-016` |
| 14:27:49 — Cultura, MOP e POPs | `TL-20260726-142749-009` | exata | tarde | Governança e Fluxo Assistido | VERIFICADO | `DEC-20260726-006`, `DEC-20260726-007`, `DEC-20260726-011`, `DEC-20260726-012` |
| 14:43:11 — Governança, testes e Cultura | `TL-20260726-144311-010` | exata | tarde | Governança, timeline, guardrails e Fluxo Assistido | VERIFICADO | `DEC-20260726-002`, `DEC-20260726-003`, `DEC-20260726-004`, `DEC-20260726-005`, `DEC-20260726-011` |

## Idempotência

As chaves seguem `timeline/SCHEMA.md` e usam a ordem local das entradas. O complemento não cria eventos novos; apenas adiciona metadados canônicos aos registros históricos.

## Limites

- segundos ausentes foram marcados como `aproximada`;
- conteúdo não comprovado não foi inventado;
- o complemento não transforma propostas em execuções;
- a cobertura continua limitada ao contexto acessível.
