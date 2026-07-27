# RC independente — Candidato PREDIX R6

## Resultado formal

```text
RESULTADO=CHANGES_REQUIRED
HEAD_REVISADO=9cb5414412a562e17ee41759c5965343b5192220
HEAD_TESTADO=9cb5414412a562e17ee41759c5965343b5192220
INDEPENDENCIA=ATENDIDA
MERGE_RECOMENDADO=NAO
MERGE_REALIZADO=NAO
EDICAO_EXECUTADA=NAO
REMEDIACAO_EXECUTADA=NAO
```

## Alvo validado

- PR `#9` aberto como Draft;
- base `main`;
- head `test/governance-64-20260726-r6`;
- SHA exato `9cb5414412a562e17ee41759c5965343b5192220`;
- PR não mesclado;
- workflow `Governance 64 scenarios` run `30224913937` em sucesso;
- workflow `Timeline validation` run `30224914038` em sucesso;
- artifact oficial analisado separadamente;
- 64 cenários, 64 IDs únicos e todos os grupos presentes;
- distribuição: 25 automatizados, 14 estáticos, 10 manuais e 15 simulados;
- zero `FAIL`, `BLOCKED` e `NOT_RUN` no snapshot R6.

## Achados

### RC-R6-01 — S3 — Fontes canônicas mantêm estado anterior ao R6

Documentos apresentados como estado atual ainda registram como pendentes atividades já executadas no GitHub, incluindo execução R6, publicação das evidências, atualização do handoff, abertura do PR Draft e criação da branch congelada.

**Impacto:** GitHub, registro de decisões e documentos de integração apresentam estados incompatíveis, contrariando verdade operacional, reconciliação D4 e continuidade.

**Remediação exigida:** registrar um estado pós-R6 com SHA, PR, runs e artifact; marcar estados pré-R6 como históricos ou superados.

### RC-R6-02 — S3 — TL-005 permite que entradas novas escapem da validação

O esquema exige ID e chave de idempotência, mas o validador reconhece somente os campos Markdown canônicos. Arquivos sem esses campos podem produzir zero ocorrências sem erro. O formato YAML mostrado no esquema também não é reconhecido.

**Reprodução adversarial:** Markdown canônico detectado; YAML com zero IDs/chaves; entrada nova incompleta com zero IDs/chaves e validação favorável.

**Impacto:** entradas novas podem omitir campos obrigatórios ou usar formato incompatível e ainda passar no workflow.

**Remediação exigida:** exigir campos em entradas novas; definir identificação de legado; validar ausência de obrigatórios; aceitar ou proibir YAML formalmente; criar regressões para incompletos, YAML e formatos parciais.

### RC-R6-03 — S3 — Runner R6 não implementa invalidação cronológica geral

O runner promove FA-008 e FA-009 por marcadores fixos em um único arquivo. Não compara timestamps, não lê incidentes posteriores e não relaciona regressão e PASS de forma estruturada.

O reteste FA-009 atual permanece aceitável para o snapshot revisado, pois não foi localizada regressão posterior. O achado invalida somente a alegação de proteção genérica contra regressões futuras.

**Impacto:** uma regressão futura registrada em outro artefato pode não invalidar o PASS anterior.

**Remediação exigida:** usar evidências estruturadas e ordenadas temporalmente; relacionar PASS/regressão ao mesmo cenário; adicionar teste em que regressão posterior força `NOT_RUN` ou `BLOCKED`.

### RC-R6-04 — S2 — Artifact não contém toda a cadeia bruta de evidências

O artifact contém apenas `results.json` e `results.md`. Não inclui saída integral da suíte, JSON do scanner, JSON do TL-005, manifesto do workflow, hashes dos arquivos avaliados ou logs das verificações anteriores ao runner.

**Impacto:** o artifact isolado não reproduz offline toda a conclusão, embora os status dos workflows no GitHub sustentem o snapshot.

**Remediação exigida:** incluir no próximo artifact resultados brutos, scanner, timeline, manifesto do SHA, hashes e resumo dos workflows.

## Evidências favoráveis

- scanner TL-010 corrigido para `#` e com regressões específicas;
- FA-008 e FA-009 com evidência manual aceitável para o snapshot atual;
- classes automatizada, estática, manual e simulada preservadas sem reclassificação indevida;
- Cultura, MOP, arquitetura, guardrails e recuperação mantêm hierarquia e autoridade final de Leo;
- nenhum merge, edição ou remediação ocorreu durante a RC.

## Verificações repetidas

| Verificação | Resultado |
|---|---|
| HEAD da branch | PASS |
| HEAD igual ao esperado | PASS |
| PR apontando para `main` | PASS |
| PR sem merge | PASS |
| Workflows no mesmo SHA | PASS |
| Artifact com 64 IDs únicos | PASS |
| Distribuição 25/14/10/15 | PASS |
| Ausência de FAIL/BLOCKED/NOT_RUN | PASS |
| Regressões scanner com `#` | PASS |
| Bypass TL-005 sem campos | CONFIRMADO |
| Bypass TL-005 com YAML | CONFIRMADO |
| Coerência do estado canônico | FAIL |
| Cronologia genérica no runner | FAIL |

## Limite da reprodução

A suíte completa do repositório não foi reexecutada localmente porque o ambiente independente não conseguiu realizar checkout externo. A validação integral foi baseada nos workflows do SHA exato e no artifact oficial. As verificações adversariais do TL-005 e da lógica do runner foram reproduzidas separadamente.

## Gates para novo candidato

1. corrigir obrigatoriedade e cobertura de formatos do TL-005;
2. implementar invalidação cronológica estruturada;
3. reconciliar o estado pós-R6 nas fontes canônicas;
4. gerar artifact com evidências brutas;
5. congelar novo HEAD;
6. executar novamente testes, scanner, TL-005 e 64 cenários no mesmo SHA;
7. submeter o novo candidato a outra RC independente;
8. manter merge bloqueado até resultado favorável e autorização explícita.

## Conclusão

O R6 representa avanço técnico real e possui workflows verdes, mas não satisfaz o gate de promoção. O resultado independente é `CHANGES_REQUIRED`.
