# Registro de Decisões e Pendências da PREDIX

## Estado

- **Data da auditoria:** `2026-07-26`.
- **Última reconciliação:** `2026-07-26T20:12:10-03:00`.
- **Origem:** projeto `Fábrica de softwares`.
- **Branch canônica do candidato integrado:** `integration/mop-governance-v0.1`.
- **Objetivo:** impedir abandono silencioso e fornecer fila rastreável de retomada.

## Estados

`ATIVA` · `PENDENTE` · `BLOQUEADA` · `EM_TRATAMENTO` · `APROVADA_PROVISORIAMENTE` · `APROVADA` · `REJEITADA` · `SUBSTITUIDA` · `CONCLUIDA`

## Decisões ativas e pendentes

| ID | Assunto | Estado | Evidência/Origem | Condição de retomada |
|---|---|---|---|---|
| DEC-20260726-001 | Ampliar catálogo de guardrails | CONCLUIDA | `governance/GUARDRAILS.md` GR-044 a GR-049 | validar em RC independente |
| DEC-20260726-002 | Definir detecção e severidade | CONCLUIDA | guardrails e baterias históricas | validar em RC e operação real |
| DEC-20260726-003 | Revisar estrutura da timeline | CONCLUIDA | TL-R01 a TL-R10; validadores TL-005/TL-010 | repetir no HEAD R6 |
| DEC-20260726-004 | Preparar plano de testes | CONCLUIDA | matriz de 64 cenários | manter regressão integral |
| DEC-20260726-005 | Preparar revisão sem merge | CONCLUIDA | PR #2 Draft e issue #3 | executar RC no HEAD R6 congelado |
| DEC-20260726-006 | Definir arquitetura Cultura–MOP–POPs | CONCLUIDA | `governance/ARCHITECTURE.md` | revisar na RC |
| DEC-20260726-007 | Consolidar GR-001 a GR-049 | CONCLUIDA | `governance/GUARDRAILS.md` | validar na RC |
| DEC-20260726-008 | Criar instrução geral para todos os chats | BLOQUEADA | decisão explícita de Leo | somente após testes, RC e aprovação normativa |
| DEC-20260726-009 | Captura automática global de chats | BLOQUEADA | `timeline/GLOBAL-INGESTION-PLAN.md` | integração central real e privacidade validada |
| DEC-20260726-010 | Atualizar timeline por evento relevante | ATIVA | contrato da timeline | enquanto contexto e GitHub estiverem acessíveis |
| DEC-20260726-011 | Formalizar Cultura/Constituição | EM_TRATAMENTO | `CULTURA.md` v0.4-draft | pendências finais, RC e aprovação explícita |
| DEC-20260726-012 | Criar POPs específicos | PENDENTE | arquitetura definida | criar por repetição, risco e ganho operacional |
| DEC-20260726-018 | Remediar TL-R01 a TL-R10 | CONCLUIDA | esquema e normalização | validar no R6 e na RC |
| DEC-20260726-019 | Executar plano de 64 testes | EM_TRATAMENTO | R5B histórica concluída; runner R6 preparado | executar R6 no mesmo HEAD congelado e publicar evidência |
| DEC-20260726-020 | Definir recuperação técnica | CONCLUIDA | `governance/RECOVERY.md` | implementar recuperação executável completa |
| DEC-20260726-021 | Realizar RC independente | EM_TRATAMENTO | issue #3 e handoff R6 | executar em outra sessão/agente após PASS do R6 |
| DEC-20260726-022 | Repetir FA-005 e FA-010 | CONCLUIDA | evidência manual versionada | repetir em outro cliente quando possível |
| DEC-20260726-023 | Executar TL-005, TL-010, AU e RC | EM_TRATAMENTO | TL executáveis; AU/RC simulados | executar R6 e implementar validadores formais futuramente |
| DEC-20260726-024 | Investigar mergeability do PR #2 | CONCLUIDA | API reportou mesclável | repetir somente se estado mudar |
| DEC-20260726-025 | Reconciliar PR #1 e PR #2 | CONCLUIDA | branch integrada, README e documentos reconciliados | validar no R6 e RC |
| DEC-20260726-026 | Preparar RC em contexto separado | CONCLUIDA | issue #3 e handoff atualizado | revisor independente reconfirma HEAD R6 |
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
| DEC-20260726-042 | Processar os 64 cenários na R4 | CONCLUIDA | run `30221124112` | preservada como linha de base histórica |
| DEC-20260726-043 | Implementar scanner TL-010 | EM_TRATAMENTO | scanner corrigido para `#`; regressões ampliadas | obter PASS no CI R6 |
| DEC-20260726-044 | Publicar fechamento TL-012 | CONCLUIDA | fechamento real e complemento append-only | validar no R6 |
| DEC-20260726-045 | Executar remediação R5 integral | CONCLUIDA | run `30222472929` | resultado histórico; não substitui R6 |
| DEC-20260726-046 | Preservar falha R5-A | CONCLUIDA | PR #7 e run `30222354733` | manter como histórico |
| DEC-20260726-047 | Invalidar análise do mesmo contexto como RC independente | CONCLUIDA | issue #3 e incidente `INC-20260726-194538-001` | somente outra sessão/agente pode concluir RC |
| DEC-20260726-048 | Corrigir falso negativo do scanner com `#` | EM_TRATAMENTO | commits do scanner e regressões | executar testes e scanner no HEAD R6 |
| DEC-20260726-049 | Reconciliar regressões FA-008 e FA-009 | CONCLUIDA | reteste manual multigrupo e comando de Leo | invalidar novamente se houver regressão posterior |
| DEC-20260726-050 | Atualizar fontes contraditórias | CONCLUIDA | README, integração, reconciliação e guardrails atualizados | verificar no R6 e RC |
| DEC-20260726-051 | Congelar e testar candidato R6 | EM_TRATAMENTO | workflow e runner R6 preparados | criar branch congelada e executar CI |
| DEC-20260726-052 | Executar RC independente pós-R6 | BLOQUEADA | handoff atualizado | desbloqueia após PASS do R6 e abertura do alvo Draft |

## Aprovações provisórias

| ID | Decisão | Estado | Próxima validação |
|---|---|---|---|
| DEC-20260726-013 | Aplicação proporcional de 5W1H e 5 Porquês | APROVADA_PROVISORIAMENTE | RC e casos reais |
| DEC-20260726-014 | Guardrails, detecção, severidade e recuperação | APROVADA_PROVISORIAMENTE | implementação executável adicional e RC |
| DEC-20260726-015 | Sintaxe N2/N3 | APROVADA_PROVISORIAMENTE | parser formal e integração segura |
| DEC-20260726-016 | Timeline diária estruturada | APROVADA_PROVISORIAMENTE | R6 e RC independente |
| DEC-20260726-017 | Painel assistido com recomendação | APROVADA_PROVISORIAMENTE | repetir em outro cliente quando possível |

## Estado reconciliado de PRs e revisão

| Artefato | Estado | Merge |
|---|---|---|
| PR #1 — fundação MOP | ABERTO | não realizado |
| PR #2 — governança e timeline | ABERTO_DRAFT_HISTORICO | não realizado |
| PR #4 — teste R2 | FECHADO | não realizado |
| PR #5 — teste R3 | FECHADO | não realizado |
| PR #6 — teste R4 | FECHADO | não realizado |
| PR #7 — teste R5-A | FECHADO_APÓS_FALHA | não realizado |
| PR #8 — teste R5B | FECHADO_APÓS_PASS | não realizado |
| Issue #3 — RC independente | ABERTA | não aplicável |
| Branch `integration/mop-governance-v0.1` | ATIVA | não promovida |
| Branch `test/governance-64-20260726-r6` | A_CRIAR | não aplicável |

## Achados RC ainda abertos

| ID | Estado | Ação necessária |
|---|---|---|
| RC-01 | EM_TRATAMENTO | validar taxonomia em operação real |
| RC-02 | PENDENTE | separar gate de fundação e gate estável |
| RC-03 | EM_TRATAMENTO | implementar validadores formais N2/N3 |
| RC-04 | EM_TRATAMENTO | executar revisão realmente independente |
| RC-05 | EM_TRATAMENTO | validar scanner corrigido e demais controles no R6 |
| RC-06 | EM_TRATAMENTO | validar que a autoridade não cria gargalo |
| RC-07 | EM_TRATAMENTO | submeter candidato reconciliado à RC |
| RC-08 | PENDENTE | formalizar resposta mínima suficiente |
| RC-09 | EM_TRATAMENTO | ampliar lint para links, estados e validadores formais |

## Planejamento relacionado

| Item | Estado | Observação |
|---|---|---|
| LEA-206 | PENDENTE | próximo gate é R6, RC e decisão de fundação |
| LEA-207 | BLOQUEADA | não iniciar antes do gate de fundação |
| LEA-208 | BLOQUEADA | iniciar após gate de fundação |

## Não comprovados como concluídos

- Constituição final aprovada;
- POP formal dos ciclos;
- linha de base e metas numéricas;
- instrução global implementada;
- captura automática global;
- validadores completos N2/N3 e recuperação executável;
- bateria R6 concluída sobre HEAD congelado;
- RC independente aprovada;
- repetição integral do Fluxo Assistido em outro cliente/dispositivo.

## Regra de encerramento

Uma fase não pode ser declarada concluída enquanto existir decisão `ATIVA`, `PENDENTE`, `BLOQUEADA` ou `EM_TRATAMENTO` sem responsável e condição de retomada. Decisões substituídas devem apontar para sua sucessora.
