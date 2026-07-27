# Candidato R7 inicial — falha TL-005 preservada

## Referência

- branch: `test/governance-64-20260726-r7`;
- SHA: `c38946abf8526a9ad47075efbb04f75ba4a0fe00`;
- PR: `#14`, fechado sem merge;
- workflow governança: `30228522319`, failure;
- workflow timeline: `30228522369`, failure;
- artifact: `8639293479`.

## Resultado observado

Os 18 testes unitários passaram. O TL-005 do repositório falhou porque a notação conceitual do esquema usava exatamente os rótulos Markdown com placeholders:

- `TL-AAAAMMDD-HHMMSS-NNN`;
- `IDEMP-AAAAMMDD-ORIGEM-CONVERSA-ORDEM-RESUMO`.

O validador interpretou esses exemplos como campos persistidos e reportou `TL005-INVALID-ID` e `TL005-INVALID-KEY`.

## Correção

A notação conceitual foi alterada para não simular um campo Markdown persistido. O exemplo real continua canônico. A correção foi feita somente na branch de integração; o HEAD R7 inicial permanece imutável.

## Próximo candidato

Criar `test/governance-64-20260726-r7b` a partir do HEAD corrigido, abrir novo PR Draft e repetir toda a validação. Merge continua não autorizado.
