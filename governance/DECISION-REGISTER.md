# Registro de Decisões e Pendências da PREDIX

## Estado

- **Data da auditoria:** `2026-07-26`.
- **Última reconciliação:** `2026-07-26T14:34:30-03:00`.
- **Origem:** projeto `Fábrica de softwares`.
- **Branch:** `mop/timeline-conversas-20260726`.
- **Objetivo:** impedir abandono silencioso e fornecer fila rastreável de retomada.

## Estados

`ATIVA` · `PENDENTE` · `BLOQUEADA` · `EM_TRATAMENTO` · `APROVADA_PROVISORIAMENTE` · `APROVADA` · `REJEITADA` · `SUBSTITUIDA` · `CONCLUIDA`

## Decisões ativas e pendentes

| ID | Assunto | Estado | Evidência/Origem | Condição de retomada |
|---|---|---|---|---|
| DEC-20260726-001 | Ampliar catálogo de guardrails | CONCLUIDA | `governance/GUARDRAILS.md` GR-044 a GR-049 | validar em testes e RC |
| DEC-20260726-002 | Definir detecção e severidade dos guardrails | CONCLUIDA | commit `46ae64602d4715b656617ed64c79073598ee3c3d` | executar testes e definir recuperação técnica |
| DEC-20260726-003 | Revisar estrutura da timeline | CONCLUIDA | `governance/reviews/TIMELINE-STRUCTURE-REVIEW-20260726.md` | remediar TL-R01 a TL-R10 |
| DEC-20260726-004 | Preparar testes da timeline global e guardrails | CONCLUIDA | `governance/tests/TEST-PLAN-TIMELINE-GUARDRAILS.md` | executar testes na ordem recomendada |
| DEC-20260726-005 | Preparar revisão da branch sem merge | CONCLUIDA | `governance/reviews/BRANCH-REVIEW-PREP-20260726.md` | abrir PR em rascunho e realizar RC independente |
| DEC-20260726-006 | Definir arquitetura Cultura/Constituição, MOP e POPs | CONCLUIDA | `governance/ARCHITECTURE.md` | revisar e aprovar após testes |
| DEC-20260726-007 | Adicionar GR-044 a GR-049 | CONCLUIDA | `governance/GUARDRAILS.md` | validar na bateria de testes |
| DEC-20260726-008 | Criar instrução geral para todos os chats | BLOQUEADA | decisão explícita de Leo | somente após ajustes, testes, RC e aprovação da arquitetura |
| DEC-20260726-009 | Captura automática global de todos os chats | BLOQUEADA | `timeline/GLOBAL-INGESTION-PLAN.md` | exige integração central ainda não implementada |
| DEC-20260726-010 | Atualizar timeline após cada mensagem | ATIVA | contrato da timeline | enquanto contexto e GitHub estiverem disponíveis |
| DEC-20260726-011 | Formalizar Cultura/Constituição em documento próprio | PENDENTE | `governance/CULTURE-DISCOVERY.md` criado; conteúdo não aprovado | decidir propósito, missão, visão, valores, princípios e autoridade |
| DEC-20260726-012 | Criar POPs específicos | PENDENTE | arquitetura definida | criar somente conforme repetição, risco e ganho operacional |
| DEC-20260726-018 | Remediar revisão da timeline TL-R01 a TL-R10 | PENDENTE | revisão estrutural | após priorização assistida dos achados |
| DEC-20260726-019 | Executar plano de testes | PENDENTE | plano de testes preparado | iniciar por FA-001 a FA-010 |
| DEC-20260726-020 | Definir recuperação técnica dos guardrails | PENDENTE | detecção e severidade concluídas | após testes iniciais de continuidade e estado |
| DEC-20260726-021 | Realizar RC independente da branch de governança | PENDENTE | relatório de preparação criado | após remediações e execução de testes mínimos |

## Aprovações provisórias

| ID | Decisão | Estado | Próxima validação |
|---|---|---|---|
| DEC-20260726-013 | Aplicação proporcional de 5W1H e 5 Porquês | APROVADA_PROVISORIAMENTE | testes em casos simples, críticos e incidentes |
| DEC-20260726-014 | Catálogo GR-001 a GR-049 com detecção e severidade | APROVADA_PROVISORIAMENTE | recuperação, falsos positivos, falsos negativos e RC |
| DEC-20260726-015 | Sintaxe multilinha N2/N3 | APROVADA_PROVISORIAMENTE | simulação e validação operacional |
| DEC-20260726-016 | Timeline diária com horário, período, origem e projeto | APROVADA_PROVISORIAMENTE | remediar TL-R01 a TL-R10 e testar cobertura |
| DEC-20260726-017 | Painel com seleção única, múltipla e plano sequencial | APROVADA_PROVISORIAMENTE | bateria de testes do @Visualize |

## Pendências recuperadas do PR #1 e da RC independente

| ID | Achado | Estado | Ação necessária |
|---|---|---|---|
| RC-01 | distinguir proposto, planejado, tentado, executado e verificado | EM_TRATAMENTO | timeline review propõe taxonomia; falta incorporar e testar |
| RC-02 | dependência circular na aprovação da MOP | PENDENTE | separar gate de fundação e gate de versão estável |
| RC-03 | autonomia e ações irreversíveis insuficientes | EM_TRATAMENTO | níveis N0–N4 e comandos N2/N3 definidos provisoriamente |
| RC-04 | ausência de separação de funções | PENDENTE | exigir RC independente para alto risco e MOP |
| RC-05 | segurança, segredos e ambientes | PENDENTE | definir isolamento, menor privilégio, backup e dados sensíveis |
| RC-06 | risco de Leo virar gargalo | PENDENTE | definir níveis de validação humana e automática |
| RC-07 | desalinhamento entre fontes oficiais | EM_TRATAMENTO | reconciliar README, PR, branches e planejamento |
| RC-08 | risco de respostas longas | PENDENTE | formalizar resposta mínima suficiente |
| RC-09 | ausência de verificação automatizada | PENDENTE | planejar lint, links e consistência de versão |

## Planejamento relacionado

| Item | Estado | Observação |
|---|---|---|
| LEA-206 — revisar e aprovar fundação MOP v0.1 | PENDENTE | depende da remediação e nova RC |
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
- recuperação técnica dos guardrails.

### Não comprovados como artefatos implementados

- não existe `CULTURA.md` aprovado; há somente descoberta;
- não existe POP formal aprovado;
- não existe instrução global implementada;
- não existe captura automática global de todos os chats;
- não existem resultados executados do plano de testes;
- não existe RC independente aprovada para esta branch.

## Regra de encerramento

Uma fase não pode ser declarada concluída enquanto existir decisão `ATIVA`, `PENDENTE`, `BLOQUEADA` ou `EM_TRATAMENTO` sem responsável e condição de retomada. Decisões substituídas devem apontar para sua sucessora.