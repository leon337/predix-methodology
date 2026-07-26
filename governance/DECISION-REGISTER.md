# Registro de Decisões e Pendências da PREDIX

## Estado

- **Data da auditoria:** `2026-07-26`.
- **Última reconciliação:** `2026-07-26T18:30:31-03:00`.
- **Origem:** projeto `Fábrica de softwares`.
- **Branch:** `mop/timeline-conversas-20260726`.
- **Objetivo:** impedir abandono silencioso e fornecer fila rastreável de retomada.

## Estados

`ATIVA` · `PENDENTE` · `BLOQUEADA` · `EM_TRATAMENTO` · `APROVADA_PROVISORIAMENTE` · `APROVADA` · `REJEITADA` · `SUBSTITUIDA` · `CONCLUIDA`

## Decisões ativas e pendentes

| ID | Assunto | Estado | Evidência/Origem | Condição de retomada |
|---|---|---|---|---|
| DEC-20260726-001 | Ampliar catálogo de guardrails | CONCLUIDA | `governance/GUARDRAILS.md` GR-044 a GR-049 | validar em RC |
| DEC-20260726-002 | Definir detecção e severidade dos guardrails | CONCLUIDA | commit `46ae64602d4715b656617ed64c79073598ee3c3d` | validar em RC e implementação real |
| DEC-20260726-003 | Revisar estrutura da timeline | CONCLUIDA | revisão, remediação TL-R01 a TL-R10 e bateria R4 | concluir TL-010 e TL-012 |
| DEC-20260726-004 | Preparar testes da timeline global e guardrails | CONCLUIDA | plano de 64 cenários e execução R4 | remediar bloqueios identificados |
| DEC-20260726-005 | Preparar revisão da branch sem merge | CONCLUIDA | PR #2 em rascunho | realizar RC com separação real de contexto após remediações |
| DEC-20260726-006 | Definir arquitetura Cultura/Constituição, MOP e POPs | CONCLUIDA | `governance/ARCHITECTURE.md` v0.2-integration-draft | revisar e aprovar após testes |
| DEC-20260726-007 | Adicionar GR-044 a GR-049 | CONCLUIDA | `governance/GUARDRAILS.md` | validar na RC |
| DEC-20260726-008 | Criar instrução geral para todos os chats | BLOQUEADA | decisão explícita de Leo | somente após TL-010, TL-012, RC e aprovação normativa |
| DEC-20260726-009 | Captura automática global de todos os chats | BLOQUEADA | `timeline/GLOBAL-INGESTION-PLAN.md` | exige integração central ainda não implementada |
| DEC-20260726-010 | Atualizar timeline após cada mensagem | ATIVA | contrato da timeline | enquanto contexto e GitHub estiverem disponíveis |
| DEC-20260726-011 | Formalizar Cultura/Constituição em documento próprio | EM_TRATAMENTO | `CULTURA.md` v0.4-draft com rodadas 1–3 registradas | decidir pendências finais e executar RC |
| DEC-20260726-012 | Criar POPs específicos | PENDENTE | arquitetura definida | criar somente conforme repetição, risco e ganho operacional |
| DEC-20260726-018 | Remediar revisão da timeline TL-R01 a TL-R10 | CONCLUIDA | `timeline/SCHEMA.md`, normalização e bateria R4 | validar TL-010 e TL-012 |
| DEC-20260726-019 | Executar plano de 64 testes | EM_TRATAMENTO | R4: 24 automatizados, 13 estáticos, 10 manuais, 15 simulados, 1 bloqueado, 1 não executado e 0 falhas | implementar TL-010, publicar TL-012 e repetir bateria |
| DEC-20260726-020 | Definir recuperação técnica dos guardrails | CONCLUIDA | `governance/RECOVERY.md` e guardrails v0.4 | implementar armazenamento e recuperação executável |
| DEC-20260726-021 | Realizar RC independente da branch de governança | EM_TRATAMENTO | issue #3 e handoff independente preparados | executar sobre HEAD estável após TL-010 e TL-012 |
| DEC-20260726-022 | Repetir manualmente FA-005 e FA-010 | CONCLUIDA | `governance/tests/results/FA-005-FA-010-MANUAL-RETEST-20260726.md` | repetir em outro cliente ou dispositivo quando possível |
| DEC-20260726-023 | Executar TL-005, TL-010, AU-001 a AU-008 e RC-001 a RC-006 | EM_TRATAMENTO | TL-005 executável; TL-010 bloqueado; AU e RC simulados com segurança | scanner, validadores formais e recuperação executável |
| DEC-20260726-024 | Investigar PR #2 não mesclável | CONCLUIDA | API revalidada e PR reportado como mesclável | repetir apenas se estado mudar |
| DEC-20260726-025 | Reconciliar fontes normativas PR #1 e PR #2 | CONCLUIDA | MOP 0.2, arquitetura 0.2 e Cultura v0.4 sincronizadas em `integration/mop-governance-v0.1` | submeter candidato integrado à RC após testes |
| DEC-20260726-026 | Preparar RC independente em contexto separado | CONCLUIDA | handoff, issue #3 e comentário no PR #2 | revisor separado deve reconfirmar o HEAD e emitir resultado |
| DEC-20260726-027 | Rodada 1 de decisões da Cultura | CONCLUIDA | comando explícito de Leo e pacote v0.2 | decisões preservadas na minuta |
| DEC-20260726-028 | Aprovar propósito candidato da PREDIX | APROVADA | `PROPOSITO=APROVAR_PROPOSITO_CANDIDATO` | preservar na minuta e validar coerência na RC |
| DEC-20260726-029 | Adotar duas frentes equivalentes | APROVADA | `PUBLICO_INICIAL=ADOTAR_DUAS_FRENTES_EQUIVALENTES` | aplicar por meio da política dinâmica de ciclos |
| DEC-20260726-030 | Adotar horizonte de visão de 10 anos | APROVADA | `HORIZONTE_VISAO=10_ANOS` | definir linha de base e metas quantitativas |
| DEC-20260726-031 | Adotar alocação dinâmica por ciclo | APROVADA | `ALOCACAO_DUAS_FRENTES=ALOCACAO_DINAMICA_POR_CICLO` | aplicar nos ciclos de 28 dias |
| DEC-20260726-032 | Aprovar missão da PREDIX | APROVADA | `MISSAO=APROVAR_MISSAO_CANDIDATA` | preservar na minuta e validar coerência na RC |
| DEC-20260726-033 | Aprovar visão institucional de 10 anos | APROVADA | `VISAO_10_ANOS=APROVAR_VISAO_CANDIDATA_10_ANOS` | definir linha de base e metas quantitativas |
| DEC-20260726-034 | Concluir rodada 2 da Cultura | CONCLUIDA | comando explícito de Leo e pacote v0.3 | decisões incorporadas na minuta |
| DEC-20260726-035 | Abrir rodada 3 da Cultura | CONCLUIDA | plano assistido e comando completo de Leo | decisões incorporadas em `CULTURA.md` v0.4-draft |
| DEC-20260726-036 | Classificar valores da PREDIX | APROVADA | `VALORES=NUCLEO_7_E_3_REVISAVEIS` | revisar coerência na RC constitucional |
| DEC-20260726-037 | Definir limites éticos e projetos proibidos | APROVADA | `LIMITES_ETICOS=BASE_CONSTITUCIONAL_ESTRITA` | mapear controles executáveis e setores restritos |
| DEC-20260726-038 | Definir decisões sob autoridade exclusiva de Leo | APROVADA | autoridade personalizada com dez grupos exclusivos | validar operação real e conflitos na RC |
| DEC-20260726-039 | Definir duração, planejamento, continuidade e fechamento dos ciclos | APROVADA | `CICLO=28_DIAS`; `CONTINUIDADE=DEFINICAO_POR_CICLO` | criar POP operacional quando o modelo for aplicado |
| DEC-20260726-040 | Definir marcos e indicadores de 3, 5 e 10 anos | APROVADA | `INDICADORES=PAINEL_EQUILIBRADO` | criar linha de base e metas numéricas verificáveis |
| DEC-20260726-041 | Concluir rodada 3 da Cultura | CONCLUIDA | comando `DECISAO_CULTURA_PREDIX_RODADA_3_COMPLETA` | avançar para pendências finais e RC independente |
| DEC-20260726-042 | Processar integralmente os 64 cenários em HEAD congelado | CONCLUIDA | workflow R4 `30221124112`; artifact `8637232519`; relatório consolidado | usar resultados para remediação, sem declarar gate aprovado |
| DEC-20260726-043 | Implementar scanner automático de segredos para TL-010 | PENDENTE | TL-010=`BLOCKED` na bateria R4 | criar scanner, testes de regressão e executar novamente |
| DEC-20260726-044 | Publicar fechamento diário para TL-012 | PENDENTE | TL-012=`NOT_RUN` na bateria R4 | criar `DAILY-CLOSE`, reconciliar o dia e executar novamente |

## Aprovações provisórias

| ID | Decisão | Estado | Próxima validação |
|---|---|---|---|
| DEC-20260726-013 | Aplicação proporcional de 5W1H e 5 Porquês | APROVADA_PROVISORIAMENTE | validação em RC e casos reais |
| DEC-20260726-014 | Catálogo GR-001 a GR-049 com detecção, severidade e recuperação | APROVADA_PROVISORIAMENTE | implementação executável e RC |
| DEC-20260726-015 | Sintaxe multilinha N2/N3 | APROVADA_PROVISORIAMENTE | parser formal e integração segura |
| DEC-20260726-016 | Timeline diária com horário, período, origem e projeto | APROVADA_PROVISORIAMENTE | TL-010, TL-012 e RC |
| DEC-20260726-017 | Painel com seleção única, múltipla e plano sequencial | APROVADA_PROVISORIAMENTE | regressão de recomendações por grupo e outro cliente/dispositivo |

## Pendências recuperadas do PR #1 e da RC independente

| ID | Achado | Estado | Ação necessária |
|---|---|---|---|
| RC-01 | distinguir proposto, planejado, tentado, executado e verificado | EM_TRATAMENTO | taxonomia incorporada e bateria executada; validar em operação real |
| RC-02 | dependência circular na aprovação da MOP | PENDENTE | separar gate de fundação e gate de versão estável |
| RC-03 | autonomia e ações irreversíveis insuficientes | EM_TRATAMENTO | implementar validadores formais N2/N3 |
| RC-04 | ausência de separação de funções | EM_TRATAMENTO | issue #3 criada; revisão separada ainda não executada |
| RC-05 | segurança, segredos e ambientes | EM_TRATAMENTO | TL-010 bloqueado; implementar scanner e integração executável |
| RC-06 | risco de Leo virar gargalo | EM_TRATAMENTO | autoridade limitada a dez grupos; validar operação real |
| RC-07 | desalinhamento entre fontes oficiais | EM_TRATAMENTO | candidato integrado reconciliado; falta RC e aprovação |
| RC-08 | risco de respostas longas | PENDENTE | formalizar resposta mínima suficiente |
| RC-09 | ausência de verificação automatizada | EM_TRATAMENTO | runner de 64 cenários criado; ainda faltam scanner e validadores formais |

## Planejamento relacionado

| Item | Estado | Observação |
|---|---|---|
| LEA-206 — revisar e aprovar fundação MOP v0.1 | PENDENTE | depende de TL-010, TL-012 e nova RC |
| LEA-207 — derivar instrução geral mínima | BLOQUEADA | não iniciar antes do gate de fundação e dos testes acordados |
| LEA-208 — validar MOP na retomada real da LEA-197 | BLOQUEADA | iniciar somente após gate de fundação |

## Resultado da auditoria de órfãos

### Recuperados e agora rastreados

- Cultura/Constituição da empresa;
- relação entre MOP e POPs;
- guardrails de continuidade;
- instrução global para todos os chats;
- bateria integral de 64 testes;
- revisão da branch sem merge;
- bloqueadores RC-01 a RC-09;
- LEA-206, LEA-207 e LEA-208;
- remediações TL-R01 a TL-R10;
- recuperação técnica dos guardrails;
- retestes manuais FA-005 e FA-010;
- investigação de mergeability;
- reconciliação normativa PR #1–PR #2;
- handoff e issue para RC independente;
- rodadas 1, 2 e 3 da Cultura;
- valores, ética, autoridade, ciclos e indicadores;
- TL-010 e TL-012 como pendências explícitas.

### Não comprovados como artefatos implementados

- `CULTURA.md` continua minuta; não existe Constituição aprovada;
- não existe POP formal aprovado para operação dos ciclos;
- não existe linha de base numérica dos indicadores;
- não existe instrução global implementada;
- não existe captura automática global de todos os chats;
- não existem validadores executáveis completos de autorização e recuperação;
- não existe scanner automático de segredos;
- não existe fechamento diário validado por TL-012;
- não existe RC independente aprovada com separação real de contexto;
- resultados manuais e simulados não comprovam integração executável completa.

## Regra de encerramento

Uma fase não pode ser declarada concluída enquanto existir decisão `ATIVA`, `PENDENTE`, `BLOQUEADA` ou `EM_TRATAMENTO` sem responsável e condição de retomada. Decisões substituídas devem apontar para sua sucessora.
