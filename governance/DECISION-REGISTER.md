# Registro de Decisões e Pendências da PREDIX

## Estado

- **Data da auditoria:** `2026-07-26`.
- **Última reconciliação:** `2026-07-26T15:11:31-03:00`.
- **Origem:** projeto `Fábrica de softwares`.
- **Branch:** `mop/timeline-conversas-20260726`.
- **Objetivo:** impedir abandono silencioso e fornecer fila rastreável de retomada.

## Estados

`ATIVA` · `PENDENTE` · `BLOQUEADA` · `EM_TRATAMENTO` · `APROVADA_PROVISORIAMENTE` · `APROVADA` · `REJEITADA` · `SUBSTITUIDA` · `CONCLUIDA`

## Decisões ativas e pendentes

| ID | Assunto | Estado | Evidência/Origem | Condição de retomada |
|---|---|---|---|---|
| DEC-20260726-001 | Ampliar catálogo de guardrails | CONCLUIDA | `governance/GUARDRAILS.md` GR-044 a GR-049 | validar em testes e RC |
| DEC-20260726-002 | Definir detecção e severidade dos guardrails | CONCLUIDA | commit `46ae64602d4715b656617ed64c79073598ee3c3d` | executar testes restantes |
| DEC-20260726-003 | Revisar estrutura da timeline | CONCLUIDA | revisão e remediação TL-R01 a TL-R10 | executar TL-001 a TL-015 e fechamento diário |
| DEC-20260726-004 | Preparar testes da timeline global e guardrails | CONCLUIDA | plano e resultados FA-001 a FA-010 | executar grupos restantes |
| DEC-20260726-005 | Preparar revisão da branch sem merge | CONCLUIDA | PR #2 em rascunho | realizar RC com separação real de contexto após remediações |
| DEC-20260726-006 | Definir arquitetura Cultura/Constituição, MOP e POPs | CONCLUIDA | `governance/ARCHITECTURE.md` | revisar e aprovar após testes |
| DEC-20260726-007 | Adicionar GR-044 a GR-049 | CONCLUIDA | `governance/GUARDRAILS.md` | validar na bateria de testes |
| DEC-20260726-008 | Criar instrução geral para todos os chats | BLOQUEADA | decisão explícita de Leo | somente após ajustes, testes, RC e aprovação da arquitetura |
| DEC-20260726-009 | Captura automática global de todos os chats | BLOQUEADA | `timeline/GLOBAL-INGESTION-PLAN.md` | exige integração central ainda não implementada |
| DEC-20260726-010 | Atualizar timeline após cada mensagem | ATIVA | contrato da timeline | enquanto contexto e GitHub estiverem disponíveis |
| DEC-20260726-011 | Formalizar Cultura/Constituição em documento próprio | PENDENTE | descoberta e pacote de decisão candidato | Leo decidir propósito, missão, visão, valores e autoridade |
| DEC-20260726-012 | Criar POPs específicos | PENDENTE | arquitetura definida | criar somente conforme repetição, risco e ganho operacional |
| DEC-20260726-018 | Remediar revisão da timeline TL-R01 a TL-R10 | CONCLUIDA | `timeline/SCHEMA.md`, normalização e relatório de remediação | validar por testes e RC |
| DEC-20260726-019 | Executar plano de testes | EM_TRATAMENTO | simulações críticas executadas; FA-005 e FA-010 aguardam interação manual | receber evidência manual e executar grupos restantes |
| DEC-20260726-020 | Definir recuperação técnica dos guardrails | CONCLUIDA | `governance/RECOVERY.md` e guardrails v0.4 | implementar e automatizar RC-001 a RC-006 |
| DEC-20260726-021 | Realizar RC independente da branch de governança | PENDENTE | handoff independente preparado | executar em outra sessão/agente sobre HEAD estável |
| DEC-20260726-022 | Repetir manualmente FA-005 e FA-010 | BLOQUEADA | `governance/tests/results/FA-005-FA-010-MANUAL-RETEST-20260726.md` | Leo executar o painel de teste e devolver comando de evidência |
| DEC-20260726-023 | Executar TL-005, TL-010, AU-001 a AU-008 e RC-001 a RC-006 | EM_TRATAMENTO | relatório de simulação crítica | implementar validador de idempotência e repetir em mecanismo executável |
| DEC-20260726-024 | Investigar PR #2 não mesclável | CONCLUIDA_COM_BLOQUEIO | investigação documental | causa definitiva exige checkout Git ou nova branch reconciliada |
| DEC-20260726-025 | Reconciliar fontes normativas PR #1 e PR #2 | CONCLUIDA_COM_PENDENCIA_TECNICA | plano canônico criado | criar branch de integração e consolidar fisicamente os documentos |
| DEC-20260726-026 | Preparar RC independente em contexto separado | CONCLUIDA | `governance/reviews/RC2-INDEPENDENT-HANDOFF-20260726.md` | iniciar revisão em sessão/agente separado após estabilizar HEAD |

## Aprovações provisórias

| ID | Decisão | Estado | Próxima validação |
|---|---|---|---|
| DEC-20260726-013 | Aplicação proporcional de 5W1H e 5 Porquês | APROVADA_PROVISORIAMENTE | testes em casos simples, críticos e incidentes |
| DEC-20260726-014 | Catálogo GR-001 a GR-049 com detecção, severidade e recuperação | APROVADA_PROVISORIAMENTE | implementação executável, falsos positivos, falsos negativos e RC |
| DEC-20260726-015 | Sintaxe multilinha N2/N3 | APROVADA_PROVISORIAMENTE | validador formal e simulação independente |
| DEC-20260726-016 | Timeline diária com horário, período, origem e projeto | APROVADA_PROVISORIAMENTE | TL-005 executável, TL-010 automatizado e fechamento diário |
| DEC-20260726-017 | Painel com seleção única, múltipla e plano sequencial | APROVADA_PROVISORIAMENTE | concluir FA-005 e FA-010 manualmente e testar conflitos |

## Pendências recuperadas do PR #1 e da RC independente

| ID | Achado | Estado | Ação necessária |
|---|---|---|---|
| RC-01 | distinguir proposto, planejado, tentado, executado e verificado | EM_TRATAMENTO | taxonomia incorporada; falta execução ampla dos testes |
| RC-02 | dependência circular na aprovação da MOP | PENDENTE | separar gate de fundação e gate de versão estável |
| RC-03 | autonomia e ações irreversíveis insuficientes | EM_TRATAMENTO | níveis N0–N4 simulados; falta validador formal |
| RC-04 | ausência de separação de funções | PENDENTE | executar RC independente com contexto separado |
| RC-05 | segurança, segredos e ambientes | EM_TRATAMENTO | TL-010 e AU simulados; faltam scanner e integração executável |
| RC-06 | risco de Leo virar gargalo | PENDENTE | definir níveis de validação humana e automática |
| RC-07 | desalinhamento entre fontes oficiais | EM_TRATAMENTO | plano PR1–PR2 criado; integração física pendente |
| RC-08 | risco de respostas longas | PENDENTE | formalizar resposta mínima suficiente |
| RC-09 | ausência de verificação automatizada | PENDENTE | criar lint, verificador de IDs, links, estados e segredos |

## Planejamento relacionado

| Item | Estado | Observação |
|---|---|---|
| LEA-206 — revisar e aprovar fundação MOP v0.1 | PENDENTE | depende da integração normativa e nova RC |
| LEA-207 — derivar instrução geral mínima | BLOQUEADA | não iniciar antes do gate de fundação e dos testes acordados |
| LEA-208 — validar MOP na retomada real da LEA-197 | BLOQUEADA | iniciar somente após gate de fundação |

## Resultado da auditoria de órfãos

### Recuperados e agora rastreados

- Cultura/Constituição da empresa;
- relação entre MOP e POPs;
- guardrails de continuidade;
- instrução global para todos os chats;
- testes do fluxo assistido e da timeline;
- revisão da branch sem merge;
- bloqueadores RC-01 a RC-09;
- LEA-206, LEA-207 e LEA-208;
- remediações TL-R01 a TL-R10;
- recuperação técnica dos guardrails;
- retestes manuais FA-005 e FA-010;
- investigação de mergeability;
- reconciliação normativa PR #1–PR #2;
- handoff para RC independente.

### Não comprovados como artefatos implementados

- não existe `CULTURA.md` aprovado; há somente descoberta e candidatos;
- não existe POP formal aprovado;
- não existe instrução global implementada;
- não existe captura automática global de todos os chats;
- não existe validador executável de idempotência, autorização ou recuperação;
- não existe scanner automático de segredos;
- não existe RC independente aprovada com separação real de contexto;
- não existe branch de integração PR #1–PR #2.

## Regra de encerramento

Uma fase não pode ser declarada concluída enquanto existir decisão `ATIVA`, `PENDENTE`, `BLOQUEADA` ou `EM_TRATAMENTO` sem responsável e condição de retomada. Decisões substituídas devem apontar para sua sucessora.
