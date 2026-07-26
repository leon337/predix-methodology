# Registro de Decisões e Pendências da PREDIX

## Estado

- **Data da auditoria:** `2026-07-26`.
- **Última reconciliação:** `2026-07-26T19:08:35-03:00`.
- **Origem:** projeto `Fábrica de softwares`.
- **Branch canônica do candidato integrado:** `integration/mop-governance-v0.1`.
- **Objetivo:** impedir abandono silencioso e fornecer fila rastreável de retomada.

## Estados

`ATIVA` · `PENDENTE` · `BLOQUEADA` · `EM_TRATAMENTO` · `APROVADA_PROVISORIAMENTE` · `APROVADA` · `REJEITADA` · `SUBSTITUIDA` · `CONCLUIDA`

## Decisões ativas e pendentes

| ID | Assunto | Estado | Evidência/Origem | Condição de retomada |
|---|---|---|---|---|
| DEC-20260726-001 | Ampliar catálogo de guardrails | CONCLUIDA | `governance/GUARDRAILS.md` GR-044 a GR-049 | validar em RC |
| DEC-20260726-002 | Definir detecção e severidade | CONCLUIDA | guardrails e baterias R4/R5B | validar em RC e operação real |
| DEC-20260726-003 | Revisar estrutura da timeline | CONCLUIDA | TL-R01 a TL-R10; TL-010/TL-012 PASS na R5B | validar em RC |
| DEC-20260726-004 | Preparar plano de testes | CONCLUIDA | matriz de 64 cenários e regressão R5B | manter regressão integral |
| DEC-20260726-005 | Preparar revisão sem merge | CONCLUIDA | PR #2 Draft e issue #3 | executar RC no HEAD integrado estável |
| DEC-20260726-006 | Definir arquitetura Cultura–MOP–POPs | CONCLUIDA | `governance/ARCHITECTURE.md` | revisar na RC |
| DEC-20260726-007 | Consolidar GR-001 a GR-049 | CONCLUIDA | `governance/GUARDRAILS.md` | validar na RC |
| DEC-20260726-008 | Criar instrução geral para todos os chats | BLOQUEADA | decisão explícita de Leo | somente após RC e aprovação normativa |
| DEC-20260726-009 | Captura automática global de chats | BLOQUEADA | `timeline/GLOBAL-INGESTION-PLAN.md` | integração central real e privacidade validada |
| DEC-20260726-010 | Atualizar timeline por evento relevante | ATIVA | contrato da timeline | enquanto contexto e GitHub estiverem acessíveis |
| DEC-20260726-011 | Formalizar Cultura/Constituição | EM_TRATAMENTO | `CULTURA.md` v0.4-draft | pendências finais, RC e aprovação explícita |
| DEC-20260726-012 | Criar POPs específicos | PENDENTE | arquitetura definida | criar por repetição, risco e ganho operacional |
| DEC-20260726-018 | Remediar TL-R01 a TL-R10 | CONCLUIDA | esquema, normalização e R5B | validar em RC |
| DEC-20260726-019 | Executar plano de 64 testes | CONCLUIDA | R5B: 25 automatizados, 14 estáticos, 10 manuais, 15 simulados, 0 bloqueados, 0 não executados e 0 falhas | manter regressão; não confundir manual/simulado com integração executável |
| DEC-20260726-020 | Definir recuperação técnica | CONCLUIDA | `governance/RECOVERY.md` | implementar recuperação executável completa |
| DEC-20260726-021 | Realizar RC independente | EM_TRATAMENTO | issue #3 e handoff | reconfirmar HEAD integrado e executar em outro contexto |
| DEC-20260726-022 | Repetir FA-005 e FA-010 | CONCLUIDA | evidência manual versionada | repetir em outro cliente quando possível |
| DEC-20260726-023 | Executar TL-005, TL-010, AU e RC | EM_TRATAMENTO | TL-005/TL-010 executáveis; AU/RC simulados | implementar validadores formais N2/N3 e recuperação executável |
| DEC-20260726-024 | Investigar mergeability do PR #2 | CONCLUIDA | API reportou mesclável | repetir somente se estado mudar |
| DEC-20260726-025 | Reconciliar PR #1 e PR #2 | CONCLUIDA | candidato integrado com MOP 0.2, Cultura v0.4 e arquitetura 0.2 | submeter à RC |
| DEC-20260726-026 | Preparar RC em contexto separado | CONCLUIDA | issue #3 | revisor independente reconfirma HEAD |
| DEC-20260726-027 | Rodada 1 da Cultura | CONCLUIDA | comando explícito | preservar na minuta |
| DEC-20260726-028 | Aprovar propósito | APROVADA | Cultura v0.4 | validar na RC |
| DEC-20260726-029 | Adotar duas frentes estratégicas | APROVADA | Cultura v0.4 | aplicar por ciclos |
| DEC-20260726-030 | Visão com horizonte de 10 anos | APROVADA | Cultura v0.4 | definir linha de base e metas |
| DEC-20260726-031 | Alocação dinâmica por ciclo | APROVADA | Cultura v0.4 | aplicar nos ciclos de 28 dias |
| DEC-20260726-032 | Aprovar missão | APROVADA | Cultura v0.4 | validar na RC |
| DEC-20260726-033 | Aprovar visão institucional | APROVADA | Cultura v0.4 | definir indicadores quantitativos |
| DEC-20260726-034 | Concluir rodada 2 | CONCLUIDA | pacote v0.3 | decisões preservadas |
| DEC-20260726-035 | Abrir e concluir rodada 3 | CONCLUIDA | comando completo | decisões incorporadas |
| DEC-20260726-036 | Sete valores inegociáveis e três revisáveis | APROVADA | Cultura v0.4 | revisar coerência na RC |
| DEC-20260726-037 | Base ética constitucional estrita | APROVADA | Cultura v0.4 | mapear controles executáveis |
| DEC-20260726-038 | Autoridade personalizada de Leo | APROVADA | dez grupos exclusivos | validar operação real e N0–N4 |
| DEC-20260726-039 | Ciclos de 28 dias e continuidade por ciclo | APROVADA | Cultura v0.4 | criar POP quando aplicado |
| DEC-20260726-040 | Painel equilibrado de indicadores | APROVADA | Cultura v0.4 | criar linha de base e metas |
| DEC-20260726-041 | Concluir rodada 3 | CONCLUIDA | `CULTURE-ROUND-3-RESULT.md` | avançar para gates finais |
| DEC-20260726-042 | Processar os 64 cenários na R4 | CONCLUIDA | run `30221124112`, artifact `8637232519` | preservada como linha de base |
| DEC-20260726-043 | Implementar scanner TL-010 | CONCLUIDA | scanner, seis regressões e etapa CI em PASS na R5B | ampliar padrões somente com testes contra falsos positivos |
| DEC-20260726-044 | Publicar fechamento TL-012 | CONCLUIDA | DAILY-CLOSE e TL-012 PASS_STATIC na R5B | complementar fatos posteriores por append-only |
| DEC-20260726-045 | Executar remediação R5 integral | CONCLUIDA | run `30222472929`, job `89847127241`, artifact `8637600465` | preparar RC independente |
| DEC-20260726-046 | Preservar falha R5-A | CONCLUIDA | PR #7 e run `30222354733` | usar como evidência de correção de fixtures |

## Aprovações provisórias

| ID | Decisão | Estado | Próxima validação |
|---|---|---|---|
| DEC-20260726-013 | Aplicação proporcional de 5W1H e 5 Porquês | APROVADA_PROVISORIAMENTE | RC e casos reais |
| DEC-20260726-014 | Guardrails, detecção, severidade e recuperação | APROVADA_PROVISORIAMENTE | implementação executável adicional e RC |
| DEC-20260726-015 | Sintaxe N2/N3 | APROVADA_PROVISORIAMENTE | parser formal e integração segura |
| DEC-20260726-016 | Timeline diária estruturada | APROVADA_PROVISORIAMENTE | RC independente |
| DEC-20260726-017 | Painel assistido com recomendação | APROVADA_PROVISORIAMENTE | regressão de UX em outro cliente |

## Estado reconciliado de PRs e revisão

| Artefato | Estado | Merge |
|---|---|---|
| PR #1 — fundação MOP | ABERTO | não realizado |
| PR #2 — governança e timeline | ABERTO_DRAFT | não realizado |
| PR #4 — teste R2 | FECHADO | não realizado |
| PR #5 — teste R3 | FECHADO | não realizado |
| PR #6 — teste R4 | FECHADO | não realizado |
| PR #7 — teste R5-A | FECHADO_APÓS_FALHA | não realizado |
| PR #8 — teste R5B | ABERTO_DRAFT_APÓS_PASS | não realizado |
| Issue #3 — RC independente | ABERTA | não aplicável |
| Branch `integration/mop-governance-v0.1` | ATIVA | não promovida |

## Achados RC ainda abertos

| ID | Estado | Ação necessária |
|---|---|---|
| RC-01 | EM_TRATAMENTO | validar taxonomia em operação real |
| RC-02 | PENDENTE | separar gate de fundação e gate estável |
| RC-03 | EM_TRATAMENTO | implementar validadores formais N2/N3 |
| RC-04 | EM_TRATAMENTO | executar revisão realmente independente |
| RC-05 | EM_TRATAMENTO | scanner passou; validar demais controles de ambiente |
| RC-06 | EM_TRATAMENTO | validar que a autoridade não cria gargalo |
| RC-07 | EM_TRATAMENTO | submeter candidato reconciliado à RC |
| RC-08 | PENDENTE | formalizar resposta mínima suficiente |
| RC-09 | EM_TRATAMENTO | ampliar lint para links, estados e validadores formais |

## Planejamento relacionado

| Item | Estado | Observação |
|---|---|---|
| LEA-206 | PENDENTE | próximo gate é RC e decisão de fundação |
| LEA-207 | BLOQUEADA | não iniciar antes do gate de fundação |
| LEA-208 | BLOQUEADA | iniciar após gate de fundação |

## Não comprovados como concluídos

- Constituição final aprovada;
- POP formal dos ciclos;
- linha de base e metas numéricas;
- instrução global implementada;
- captura automática global;
- validadores completos N2/N3 e recuperação executável;
- RC independente aprovada;
- repetição integral do Fluxo Assistido em outro cliente/dispositivo.

## Regra de encerramento

Uma fase não pode ser declarada concluída enquanto existir decisão `ATIVA`, `PENDENTE`, `BLOQUEADA` ou `EM_TRATAMENTO` sem responsável e condição de retomada. Decisões substituídas devem apontar para sua sucessora.
