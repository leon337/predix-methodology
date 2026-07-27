# MOP-04 — Contrato de Pesquisa e Endurecimento do Loop por Objetivo

**Data de abertura:** 2026-07-27  
**Linear:** LEA-217  
**Branch:** `research/mop-04-objective-loop-hardening`  
**Base:** `feat/mop-v0.1-fundacao`  
**Codex:** proibido  
**Merge:** não autorizado  

## 1. Objetivo

Pesquisar, comparar, testar conceitualmente e consolidar mecanismos para que a Metodologia Operacional PREDIX execute objetivos em ciclos rastreáveis de planejamento, LEA, implementação, teste, revisão, diagnóstico e remediação, sem depender do Codex.

## 2. Arquitetura pretendida

- ChatGPT: raciocínio, pesquisa, coordenação e comunicação.
- Linear: objetivo, LEAs, dependências, estados, bloqueios e decisões operacionais.
- GitHub: código, documentação, branches, commits, PRs, CI e evidências.
- Visualize: interface obrigatória para decisões humanas legítimas.

## 3. Fontes obrigatórias

1. Documentação oficial OpenAI Developers.
2. Documentação oficial GitHub.
3. Documentação oficial Linear.
4. `leon337/predix-methodology` e PR #1.
5. PTP-MEM.1 no `leon337/predixai-robo-de-listas`.
6. Projeto histórico `leon337/predixai-platform`, identificado por evidências como a fonte que contém OpenClaw, protocolos, runners, estado e memória operacional.
7. Materiais históricos do projeto ChatGPT relacionados a Akita, `ai-memory`, `FrankSherlock` e Academia PredixAI.

## 4. Restrições

- nenhuma escrita direta na `main`;
- nenhum merge;
- nenhuma conclusão sem evidência;
- não confundir a pasta "Repositórios do Akita" com o projeto histórico correto;
- não solicitar continuidade genérica durante o loop;
- só interromper por PASS, BLOCKED formal ou decisão humana obrigatória;
- toda decisão humana deve ser apresentada pelo Visualize com explicação, opções, recomendação, riscos e reversibilidade.

## 5. Máquina de estados provisória

```text
DISCOVERY
→ RESEARCHING
→ MODELING
→ REVIEWING
→ CHANGES_REQUIRED
→ VALIDATING
→ PASS
```

Estados excepcionais:

```text
BLOCKED_HUMAN_DECISION
BLOCKED_EXTERNAL
STOPPED_SAFETY_LIMIT
```

## 6. Checkpoint 0 — evidências já localizadas

- O repositório `predix-methodology` define GitHub como fonte oficial da metodologia e Linear como fonte do planejamento e estado.
- O PR #1 contém a fundação MOP v0.1 em revisão.
- A Linear já possui o projeto `Metodologia Operacional PREDIX — MOP` e as tarefas MOP-01, MOP-02 e MOP-03.
- A PTP-MEM.1 já especifica `PROJECT_RUNTIME_STATE.yaml`, `state_revision`, `transition_id`, transições idempotentes, reconstrução multichat e modelo otimista de concorrência.
- O repositório `predixai-platform` contém `PROJECT_STATE.md`, `predixai_context.json`, `PREDIXAI_EXECUTION_POLICY.md`, runners de agentes, handoff, protocolo de tarefas, memória operacional e ferramentas OpenClaw.

## 7. Próximas rodadas

1. Auditoria do material histórico interno.
2. Pesquisa OpenAI Developers.
3. Pesquisa GitHub.
4. Pesquisa Linear.
5. Síntese arquitetural.
6. RC adversarial independente.
7. Plano piloto e critérios de aceitação.
