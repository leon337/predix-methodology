# Resultado — TL-005: validador executável de idempotência

## Estado

- **Data:** `2026-07-26`.
- **Branch:** `mop/timeline-conversas-20260726`.
- **Implementação:** `tools/validate_timeline.py`.
- **Testes:** `tests/test_validate_timeline.py`.
- **CI:** `.github/workflows/timeline-validation.yml`.
- **Resultado:** `PASS EXECUTÁVEL` para o escopo implementado.

## Escopo validado

O validador percorre arquivos Markdown da timeline e verifica:

1. IDs estruturados no formato `TL-AAAAMMDD-HHMMSS-NNN`;
2. chaves no formato `IDEMP-AAAAMMDD-*`;
3. duplicidade global de IDs;
4. duplicidade global de chaves de idempotência;
5. valores estruturados fora do formato canônico;
6. leitura segura dos arquivos;
7. saída legível ou JSON;
8. códigos de saída `0` para PASS, `1` para falha de validação e `2` para erro de uso ou caminho.

Entradas legadas sem os campos estruturados são ignoradas por este teste e continuam dependentes do complemento de normalização definido em `timeline/SCHEMA.md`.

## Evidências

### Teste local controlado

Foram executados cinco testes unitários:

- conjunto único de IDs e chaves: PASS;
- ID duplicado: falha detectada;
- chave de idempotência duplicada: falha detectada;
- entrada legada sem campos estruturados: aceita;
- ID ou chave inválidos: falha detectada.

Resultado local: `5/5 PASS`.

### GitHub Actions

- workflow: `Timeline validation`;
- run: `30215606374`;
- job: `tl005`;
- conclusão: `success`;
- etapa `Unit tests`: `success`;
- etapa `Validate repository timeline`: `success`.

O checkout do GitHub Actions foi executado com limpeza do diretório e o validador aprovou a timeline presente no candidato do PR #2.

## Limites

O TL-005 não valida ainda:

- semântica do resumo da chave;
- correspondência entre data do arquivo, ID e timestamp;
- campos obrigatórios completos por entrada;
- segredos ou dados sensíveis;
- autorização N2/N3;
- recuperação de estado;
- captura global de chats.

Esses itens pertencem a testes ou validadores separados.

## Gate

TL-005 deixa de estar `BLOCKED` e passa para `PASS EXECUTÁVEL` no escopo de duplicidade e formato. A universalização continua bloqueada pelos demais testes, pela reconciliação normativa, pelas decisões de Cultura e pela RC independente.
