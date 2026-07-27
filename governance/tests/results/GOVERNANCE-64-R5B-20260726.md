# Resultado integral — 64 testes de governança — R5B

## Identificação

- **Data:** `2026-07-26`.
- **Branch fonte congelada:** `test/governance-64-20260726-r5b`.
- **HEAD fonte:** `05f9df090c94f5ca3a9dcd3a308a332416c22c10`.
- **Commit sintético efetivamente testado pelo evento de PR:** `e2d2fb16cb2a4d93821f49ebb9bdf6ee285d2da5`.
- **PR de teste:** `#8`.
- **Workflow:** `Governance 64 scenarios`.
- **Run:** `30222472929`.
- **Job:** `89847127241`.
- **Artifact:** `8637600465`.
- **Digest do artifact:** `sha256:8212454fdf019e4121ed184427ac0445d020142815e105a23e94b88208d8bc5b`.
- **Conclusão do workflow:** `success`.
- **Efeitos externos N2/N3:** nenhum.
- **Merge:** não realizado.

## Resumo

| Estado | Quantidade |
|---|---:|
| `PASS_AUTOMATED` | 25 |
| `PASS_STATIC` | 14 |
| `PASS_MANUAL` | 10 |
| `PASS_SIMULATED` | 15 |
| `BLOCKED` | 0 |
| `NOT_RUN` | 0 |
| `FAIL` | 0 |
| **Total** | **64** |

## Remediações verificadas

### TL-010 — scanner automático de segredos

- scanner: `tools/scan_secrets.py`;
- regressão: `tests/test_scan_secrets.py` com seis casos;
- etapa isolada do CI: `success`;
- cenário TL-010: `PASS_AUTOMATED`;
- resultado observado: scanner executado no repositório sem segredos potenciais;
- valores detectados, quando houver em testes controlados, são mascarados e representados por impressão digital curta.

### TL-012 — fechamento diário

- artefato: `timeline/2026/07/2026-07-26-CLOSURE.md`;
- cenário TL-012: `PASS_STATIC`;
- blocos verificados: executados, pendências, bloqueios, divergências, primeira ação e cobertura/lacunas;
- o fechamento declara cobertura somente até seu timestamp e não converte pendências em conclusões.

## Histórico R5

### R5-A — PR #7

- workflow run `30222354733`: `failure`;
- falha em fixtures da regressão do scanner antes da execução da bateria;
- scanner e gates não foram declarados aprovados;
- PR fechado sem merge;
- fixtures corrigidas no candidato integrado.

### R5B — PR #8

- testes unitários e regressões: `success`;
- scanner TL-010: `success`;
- 64 cenários: `success`;
- artifact publicado;
- nenhum `FAIL`, `BLOCKED` ou `NOT_RUN`.

## Limites da evidência

1. FA-001 a FA-010 permanecem `PASS_MANUAL`; o CI verifica a existência das evidências versionadas, não reproduz a interface do ChatGPT.
2. AU-001 a AU-008 e RC-001 a RC-006 permanecem `PASS_SIMULATED`; nenhum deploy, merge, produção ou efeito destrutivo real foi executado.
3. TL-015 permanece simulação segura porque o conjunto acessível de eventos estruturados não comprova dois projetos reais completos na mesma bateria.
4. O sucesso desta bateria não aprova automaticamente Cultura, MOP, Constituição, instrução global ou merge.
5. A RC independente continua obrigatória antes de promoção normativa.

## Gate R5B

Os gates específicos TL-010 e TL-012 foram removidos nesta referência congelada. A bateria integral não possui `FAIL`, `BLOCKED` ou `NOT_RUN`.

O próximo gate é preparar um HEAD integrado estável, reconfirmar decisões e executar a RC independente da issue #3 sem remediação no mesmo contexto.
