# MOP-04 — Rodada 01 de pesquisa

**Estado:** pesquisa inicial concluída  
**Linear:** LEA-217, LEA-218, LEA-219, LEA-220 e LEA-221  
**Branch:** `research/mop-04-objective-loop-hardening`  
**Codex:** não utilizado e proibido neste objetivo

## 1. Pergunta investigada

Quais mecanismos já existentes na PREDIX e quais capacidades oficiais da OpenAI, GitHub e Linear permitem construir um loop autônomo por objetivo que:

- transforma objetivo em LEAs;
- executa, testa e revisa cada LEA;
- cria investigação ou remediação quando houver falha;
- persiste o estado fora do chat;
- retoma após interrupção;
- evita duplicidade, concorrência e avanço indevido;
- solicita Leo somente quando existir decisão humana real;
- apresenta essa decisão obrigatoriamente por Visualize;
- não depende do Codex.

## 2. Evidências internas recuperadas

### 2.1 MOP v0.1

O PR #1 do `leon337/predix-methodology` já separa responsabilidades:

- GitHub: metodologia, código, documentação, branches, commits, PRs e versões;
- Linear: planejamento, tarefas, dependências, estado e critérios;
- chat: descoberta, debate, ensino e execução corrente;
- memória da plataforma: preferências duráveis, não estado técnico temporário.

Também já define tarefa → branch → commits → PR → CI → correção até PASS → candidato → teste de aceite.

### 2.2 PTP-MEM.1

O `leon337/predixai-robo-de-listas` contém a base mais madura de continuidade GitHub–Linear–Multichat:

- `PROJECT_RUNTIME_STATE.yaml` como estado operacional estruturado;
- `state_revision` inteira e monotônica;
- `transition_id` persistente;
- snapshots efêmeros de pré-escrita;
- comparação de SHA, PR HEAD, revisão e transição antes de cada mutação;
- transições idempotentes;
- recuperação de sincronização parcial sem abrir nova missão;
- lock consultivo e concorrência otimista;
- bootstrap somente leitura;
- separação entre especificação de teste e execução real;
- confirmação pós-merge em transição separada.

Esses mecanismos devem ser preservados e generalizados para qualquer produto.

### 2.3 Projeto histórico com OpenClaw

O projeto identificado por evidências como fonte técnica histórica do OpenClaw é `leon337/predixai-platform`. Ele contém:

- `PROJECT_STATE.md`;
- `predixai_context.json`;
- `data/project_memory/project_memory_spine.json`;
- `docs/protocols/PREDIXAI_EXECUTION_POLICY.md`;
- `scripts/predixai_task_protocol.py`;
- `scripts/predixai_handoff_runner.py`;
- `scripts/predixai_agent_runner.py`;
- `tools/openclaw/openclaw_runner.py`;
- allowlist e wrappers operacionais.

A pesquisa histórica de Akita foi recuperada conceitualmente nas conversas de 28 e 29 de junho de 2026. Foram estudados `ai-memory`, `ai-jail`, `FrankSherlock` e variantes, com a decisão `PredixAI-MEM-001`: iniciar memória persistente com Markdown, JSON e Git e evoluir para busca, scripts, multiagentes, hooks e MCP. O nome exato da pasta antiga do ChatGPT ainda não foi confirmado pelas fontes acessíveis. Não foi usada a pasta posterior chamada “Repositórios do Akita”.

### 2.4 Princípios recuperados do estudo Akita

- memória só é útil quando estruturada, indexável, auditável e reconstruível;
- arquivos históricos devem virar inteligência pesquisável, não depósitos passivos;
- soluções simples e locais devem preceder infraestrutura complexa;
- cada automação precisa de limites claros, observabilidade e recuperação;
- o sistema deve registrar decisões e estado em formatos legíveis por humanos e máquinas;
- abstrações só devem nascer quando reduzem repetição ou risco real.

## 3. O que já funciona bem

1. Separação entre GitHub, Linear e chat.
2. Estado estruturado com revisão monotônica.
3. Identificador de transição.
4. Escrita condicionada a snapshots atuais.
5. Recuperação de sincronização parcial.
6. Histórico imutável e relatórios.
7. Execução local limitada por allowlist.
8. Classificação inicial entre seguro, aprovação e bloqueio.
9. Guardrails explícitos de produto.
10. Revisão independente separada do implementador.

## 4. Lacunas internas encontradas

### 4.1 Não existe runtime durável do loop

Os scripts executam processos pontuais. Não existe um orquestrador persistente que retome automaticamente depois de reinício, espera longa, webhook ou falha de processo.

### 4.2 A política atual interrompe Leo em cada etapa

A política antiga exige relatório colado, análise no chat e confirmação da próxima etapa. Isso protege o projeto, mas contradiz o novo objetivo de continuidade automática. Deve ser substituída por uma autorização por objetivo e por gates automáticos, mantendo Leo apenas nos pontos de decisão humana.

### 4.3 O task protocol ainda não delega

O classificador atual retorna `can_call_agent=false` em todas as classificações. Ele funciona como pré-classificador, não como orquestrador.

### 4.4 Saídas frágeis

O agent runner identifica sucesso por texto marcador e remove ruído por heurística. O handoff runner usa busca textual para bloquear conteúdo. O novo padrão deve usar saídas estruturadas validadas por schema.

### 4.5 Falta de fail-fast transacional

O runner de comandos registra resultados, mas não possui contrato universal de:

- parar na primeira falha bloqueante;
- classificar falha transitória ou determinística;
- executar compensação;
- registrar side effects;
- retomar do último checkpoint seguro.

### 4.6 Eventual duplicação de eventos

Não existe ledger geral de `delivery_id`, `event_id` ou chave de idempotência para webhooks, retries e retomadas.

### 4.7 Lock apenas consultivo

O modelo otimista é válido, porém precisa ser combinado com:

- grupo de concorrência no executor;
- compare-and-swap no estado;
- chave de idempotência por side effect;
- bloqueio de escrita por revisão divergente.

### 4.8 Estado frequente dentro do Git pode gerar ruído

O Git é excelente para decisões, contratos e checkpoints. Ele é menos adequado para cada heartbeat e evento efêmero. O piloto pode usar arquivo versionado; a arquitetura durável deve separar event store operacional de checkpoints auditáveis no GitHub.

## 5. Pesquisa oficial OpenAI

### 5.1 Agents SDK

A documentação oficial oferece:

- loop nativo de agente;
- function tools;
- agentes como ferramentas e handoffs;
- guardrails;
- sessions;
- human-in-the-loop;
- tracing;
- execução em sandbox, atualmente beta;
- integração com mecanismos de execução durável.

O `Runner` repete turnos, tools e handoffs até saída final, limite de turnos ou tripwire. Portanto, `max_turns` deve ser obrigatório para impedir loop infinito.

### 5.2 Estado e retomada

`RunState` pode ser serializado e retomado. Isso atende pausas de aprovação e retomadas após espera, desde que o estado seja armazenado fora do processo.

### 5.3 Execução durável

A documentação aponta integrações com Dapr, Temporal, Restate e DBOS para trabalhos longos, retries, reinícios e human-in-the-loop. A MOP não deve acoplar o contrato a um fornecedor; deve definir uma interface `DurableWorkflowAdapter`.

### 5.4 Tracing e avaliações

Tracing registra turnos, tools, handoffs, guardrails e eventos personalizados. O identificador do trace deve ser ligado ao objetivo, LEA e tentativa.

### 5.5 Structured Outputs

As decisões de agentes devem sair em JSON schema estrito. Texto narrativo continua útil para humanos, mas não pode controlar a máquina de estados.

### 5.6 Background responses e webhooks

Respostas em background podem emitir eventos de conclusão, falha, cancelamento ou incompletude. Esses eventos devem entrar no mesmo ledger idempotente dos eventos de GitHub e Linear.

### 5.7 Decisão preliminar

- usar Agents SDK para orquestração gerenciada, tools, handoffs, guardrails, sessions e tracing;
- usar Responses API diretamente apenas em caminhos curtos ou de baixo nível;
- não tornar Sandbox Agents beta uma dependência central;
- exigir runtime durável externo quando o loop precisar sobreviver a encerramento do chat ou do processo.

## 6. Pesquisa oficial GitHub

### 6.1 GitHub Actions

GitHub Actions deve ser o executor determinístico de:

- lint;
- testes;
- build;
- validações de contrato;
- criação de artefatos;
- validação de instalação;
- checks do PR.

Não deve ser tratado sozinho como cérebro conversacional.

### 6.2 Workflows reutilizáveis

`workflow_call` permite criar uma biblioteca universal da fábrica. Os workflows reutilizáveis devem ser referenciados por SHA imutável quando usados entre repositórios.

### 6.3 Eventos

- `workflow_dispatch`: início manual ou controlado;
- `repository_dispatch`: evento vindo do orquestrador;
- `workflow_run`: encadeamento após conclusão de outro workflow;
- webhooks: eventos de PR, push, check e workflow.

### 6.4 Concorrência

Cada objetivo deve usar um grupo de concorrência, por exemplo:

```text
objective-${objective_id}
```

Isso reduz execuções concorrentes dentro do Actions, mas não elimina a necessidade de `state_revision` e verificação de SHA para escritas externas.

### 6.5 Hard gates

Rulesets devem impedir:

- escrita direta na `main`;
- merge sem PR;
- merge sem checks obrigatórios;
- force push;
- promoção sem ambiente ou validação exigida.

Status checks críticos devem aceitar somente o GitHub App ou workflow autorizado como fonte.

### 6.6 GitHub App

Uma GitHub App deve ser preferida a token pessoal para o runtime durável porque permite:

- permissões mínimas;
- instalação por repositório;
- webhooks;
- identidade própria;
- revogação controlada.

### 6.7 Artefatos e procedência

Builds candidatos devem gerar hash, manifesto e artifact attestation. A attestação precisa ser verificada; apenas gerá-la não produz benefício operacional.

### 6.8 Limitação de merge queue

Merge queue não deve ser requisito universal, pois disponibilidade depende do tipo de proprietário e plano. O trem PREDIX precisa funcionar com branch de integração mesmo sem merge queue.

## 7. Pesquisa oficial Linear

### 7.1 Grafo de trabalho

Linear oferece:

- issue pai e sub-issues;
- relações `blocked by`, `blocks`, `related` e `duplicate`;
- projetos, milestones e dependências;
- templates de issues e projetos.

O objetivo principal deve ser uma issue pai ou projeto, e cada LEA deve ser issue vinculada, com sub-LEAs para investigação e remediação.

### 7.2 Webhooks

Webhooks permitem reação a mudanças sem polling. O consumidor precisa:

- ser HTTPS público;
- responder rapidamente;
- validar HMAC sobre corpo bruto;
- validar timestamp;
- deduplicar por `Linear-Delivery`;
- processar o trabalho pesado de forma assíncrona;
- lidar com retries e possível desativação do webhook.

### 7.3 API GraphQL

O runtime deve:

- inspecionar `errors` mesmo quando houver resposta parcial;
- usar paginação e filtros;
- evitar polling;
- respeitar rate limits;
- aplicar retry com backoff somente em falhas apropriadas.

### 7.4 Linear Agents

Agent Sessions permitem menção ou delegação de issues e estado visível ao usuário. Como a funcionalidade é recente e sujeita a evolução, o núcleo da MOP deve usar um adaptador. A máquina de estados não pode depender exclusivamente de Agent Sessions.

## 8. Conclusão da rodada

A arquitetura não deve ser “ChatGPT escrevendo diretamente até terminar”. Deve possuir cinco camadas:

```text
COMUNICAÇÃO HUMANA
→ Visualize e chat

PLANO DE CONTROLE
→ máquina de estados, políticas, ledger e orquestrador

RACIOCÍNIO
→ OpenAI Agents SDK e agentes especializados

EXECUÇÃO
→ workspace isolado e GitHub Actions

MEMÓRIA E EVIDÊNCIA
→ estado durável, GitHub, Linear, traces e artefatos
```

O chat continua sendo a sala de comando de Leo, mas não pode ser a única memória nem o único processo de execução.

## 9. Fontes oficiais consultadas

### OpenAI

- https://openai.github.io/openai-agents-python/
- https://openai.github.io/openai-agents-python/running_agents/
- https://openai.github.io/openai-agents-python/human_in_the_loop/
- https://openai.github.io/openai-agents-python/sessions/
- https://openai.github.io/openai-agents-python/tracing/
- https://platform.openai.com/docs/api-reference/webhook-events

### GitHub

- https://docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows
- https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-workflow-concurrency
- https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows
- https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets
- https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/choosing-permissions-for-a-github-app
- https://docs.github.com/en/webhooks/using-webhooks/validating-webhook-deliveries
- https://docs.github.com/en/actions/how-tos/secure-your-work/use-artifact-attestations/use-artifact-attestations

### Linear

- https://linear.app/developers/agents
- https://linear.app/developers/webhooks
- https://linear.app/developers/graphql
- https://linear.app/developers/rate-limiting
- https://linear.app/docs/parent-and-sub-issues
- https://linear.app/docs/issue-relations
- https://linear.app/docs/issue-templates

## 10. Próxima transição

```text
FROM=RESEARCHING
TO=MODELING
NEXT=LEA-222
CONDITION=RESEARCH_CHECKPOINT_PUBLISHED
MERGE_AUTHORIZED=NO
```
