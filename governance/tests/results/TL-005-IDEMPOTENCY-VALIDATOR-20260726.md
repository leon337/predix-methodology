# Resultado — TL-005: validador executável de idempotência

## Estado

- **Data:** `2026-07-26`.
- **Origem:** branch `mop/timeline-conversas-20260726`.
- **Sincronização:** branch `integration/mop-governance-v0.1`.
- **Implementação:** `tools/validate_timeline.py`.
- **Testes:** `tests/test_validate_timeline.py`.
- **CI:** `.github/workflows/timeline-validation.yml`.
- **Resultado:** `PASS EXECUTÁVEL` para duplicidade e formato.

## Escopo validado

O validador verifica IDs `TL-AAAAMMDD-HHMMSS-NNN`, chaves `IDEMP-AAAAMMDD-*`, duplicidades globais, formatos inválidos, leitura segura e códigos de saída.

## Evidências

- cinco testes unitários: `5/5 PASS`;
- workflow `Timeline validation`;
- run `30215606374`;
- job `tl005`;
- conclusão `success`;
- validação da timeline do candidato: `success`.

## Limites

O TL-005 não valida segredos, autorização N2/N3, recuperação, semântica da chave ou captura global de chats.

## Gate

TL-005 está em `PASS EXECUTÁVEL` no escopo declarado. A universalização permanece bloqueada pelos demais testes e pela RC independente.
