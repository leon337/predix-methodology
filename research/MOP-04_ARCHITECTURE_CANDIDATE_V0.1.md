# MOP-04 — Arquitetura candidata do Loop Autônomo por Objetivo

**Versão:** 0.1.0-candidate  
**Estado:** modelagem para RC  
**Linear:** LEA-217 / LEA-222  
**Branch:** `research/mop-04-objective-loop-hardening`  
**Codex:** proibido  
**Merge:** não autorizado

## 1. Decisão arquitetural central

A nova metodologia não será apenas uma sequência de prompts. Ela será um sistema operacional de desenvolvimento composto por:

```text
Leo + ChatGPT + Visualize
            ↓
Objective Loop Orchestrator — OLO
            ↓
OpenAI Agents SDK
            ↓
GitHub + Linear + executor isolado
            ↓
Testes, revisão, candidato e evidências
```

O chat é a sala de comando e comunicação. Ele não é a única memória e não pode ser o único processo responsável por um loop que precise sobreviver ao encerramento da conversa.

## 2. Princípios inegociáveis

1. O objetivo aprovado é o contrato principal.
2. Nenhum avanço ocorre sem estado e evidência persistidos.
3. Falha não significa repetir cegamente; significa classificar, diagnosticar e escolher a próxima transição.
4. Toda mutação é idempotente ou possui compensação.
5. GitHub, Linear e runtime possuem autoridades por domínio explícitas.
6. Nenhum agente escreve na `main`.
7. Nenhum merge ocorre sem política e autorização aplicáveis.
8. O implementador não emite sozinho o gate final.
9. Decisões humanas reais usam Visualize obrigatoriamente.
10. Leo não é interrompido para confirmar continuidade técnica já autorizada.
11. Recursos beta ou preview são encapsulados por adaptadores.
12. O Codex não participa da arquitetura.

## 3. Planos da arquitetura

### 3.1 Plano humano e de produto

Responsáveis:

- Leo;
- ChatGPT;
- Visualize.

Funções:

- refinar ideia e objetivo;
- explicar decisões sem exigir conhecimento técnico profundo;
- escolher entre alternativas de produto ou risco material;
- validar candidato no ambiente real;
- autorizar merge, migração irreversível ou mudança de escopo quando necessário.

### 3.2 Plano de controle

Componente:

```text
Objective Loop Orchestrator — OLO
```

Funções:

- manter máquina de estados;
- selecionar a próxima LEA pronta;
- criar tentativas;
- despachar agentes e jobs;
- consumir eventos;
- deduplicar webhooks;
- aplicar retries e limites;
- criar LEAs de investigação ou remediação;
- pausar somente em decisão humana ou bloqueio formal;
- sincronizar GitHub e Linear;
- produzir checkpoints e relatório final.

O OLO não implementa funcionalidades do produto. Ele coordena o processo.

### 3.3 Plano de raciocínio

Runtime recomendado:

```text
OpenAI Agents SDK
```

Agentes iniciais:

1. **Goal Planner** — transforma contrato em plano e grafo de LEAs.
2. **Implementation Agent** — produz mudança mínima e testes relacionados.
3. **Failure Analyst** — classifica falhas e comprova causa ou abre investigação.
4. **Test Analyst** — interpreta CI, cobertura e regressões.
5. **Independent Reviewer** — revisa escopo, arquitetura, segurança e evidências sem remediar silenciosamente.
6. **Release Agent** — prepara manifesto, candidato e relatório de promoção.
7. **Recovery Agent** — reconstrói estado após interrupção, drift ou sincronização parcial.
8. **Policy Agent** — aplica guardrails, autorização e limites.

Cada agente possui schema de entrada e saída. Nenhuma decisão de máquina depende de texto livre.

### 3.4 Plano de execução

Executor principal:

```text
GitHub Actions + workspace isolado
```

Responsabilidades:

- aplicar patch autorizado;
- lint e análise estática;
- testes unitários e integração;
- build;
- validação de contratos;
- geração de artefatos;
- teste de instalação;
- checks de PR;
- publicação de logs e evidências.

O executor não decide produto, não cria escopo e não contorna gates.

### 3.5 Plano de memória e evidência

#### Estado transacional

Fonte canônica para a máquina:

```text
DurableStateAdapter
```

Implementações previstas:

- piloto: arquivo de estado versionado com compare-and-swap por SHA;
- produção: banco transacional ou workflow engine durável.

#### GitHub

Fonte canônica de:

- código;
- metodologia;
- contratos;
- branches e commits;
- PRs e checks;
- artefatos e manifests;
- checkpoints auditáveis;
- histórico imutável.

#### Linear

Fonte canônica humana de:

- objetivo;
- LEAs e sub-LEAs;
- dependências;
- prioridade;
- bloqueios;
- estado operacional visível;
- critérios de aceite;
- resumo das evidências.

Linear é uma projeção operacional sincronizada. A transação não pode ser considerada concluída se GitHub, Linear e estado durável divergirem.

#### OpenAI tracing

Fonte técnica de:

- turnos dos agentes;
- tool calls;
- handoffs;
- guardrails;
- uso e duração;
- erros do runtime de raciocínio.

## 4. Contratos persistentes

### 4.1 Objective Contract

```yaml
objective_id: OBJ-001
project: TriView
statement: "Resultado verificável pretendido"
acceptance_criteria: []
non_goals: []
authorized_actions: []
prohibited_actions: []
risk_level: R2
execution_mode: SEQUENTIAL_TRAIN
merge_policy: EXPLICIT_HUMAN_APPROVAL
human_decision_policy: VISUALIZE_REQUIRED
budget:
  max_leas: 20
  max_remediations_per_root: 3
  max_agent_turns_per_attempt: 20
  max_cost: null
```

### 4.2 Objective Runtime State

```yaml
schema_version: "1.0"
objective_id: OBJ-001
state_revision: 12
transition_id: OBJ-001-T12
objective_state: RUNNING
active_lea: LEA-301
active_attempt: ATT-301-02
baseline_sha: abc123
working_head: def456
linear_issue: LEA-300
github_pr: 41
lock:
  owner: olo-worker-02
  expires_at: "..."
last_event_id: evt-xyz
next_action: WAIT_FOR_CI
blockers: []
```

### 4.3 Event Envelope

```json
{
  "event_id": "uuid",
  "delivery_id": "source-delivery-id",
  "idempotency_key": "objective:transition:effect",
  "objective_id": "OBJ-001",
  "lea_id": "LEA-301",
  "attempt_id": "ATT-301-02",
  "transition_id": "OBJ-001-T12",
  "expected_state_revision": 12,
  "source": "github|linear|openai|olo|human",
  "type": "CI_COMPLETED",
  "payload_hash": "sha256",
  "occurred_at": "ISO-8601",
  "received_at": "ISO-8601"
}
```

### 4.4 Agent Decision

```json
{
  "decision": "PASS|REMEDIATE|INVESTIGATE|RETRY|BLOCKED|HUMAN_DECISION",
  "confidence": 0.95,
  "evidence_ids": [],
  "failure_class": null,
  "next_lea": null,
  "policy_checks": [],
  "human_message": null
}
```

## 5. Máquina de estados

### 5.1 Objetivo

```text
DRAFT
→ REFINING
→ READY
→ PLANNING
→ RUNNING
→ INTEGRATING
→ REVIEWING
→ CANDIDATE
→ REAL_VALIDATION
→ PASS
```

Estados excepcionais:

```text
BLOCKED_HUMAN_DECISION
BLOCKED_EXTERNAL
BLOCKED_STATE_DRIFT
BLOCKED_SECURITY
STOPPED_BUDGET
STOPPED_NO_PROGRESS
FAILED_CONTROLLED
CANCELLED
```

### 5.2 LEA

```text
PROPOSED
→ READY
→ CLAIMED
→ IMPLEMENTING
→ TESTING
→ REVIEWING
→ PASS
→ INTEGRATED
```

Estados alternativos:

```text
INVESTIGATING
REMEDIATING
CHANGES_REQUIRED
BLOCKED
SUPERSEDED
CANCELLED
```

### 5.3 Tentativa

```text
PREPARED
→ EXECUTING
→ WAITING_CI
→ ANALYZING_RESULT
→ COMMITTED
```

Saídas alternativas:

```text
RETRY_SCHEDULED
ROLLED_BACK
ABORTED
FAILED
```

## 6. Algoritmo do loop por objetivo

```text
1. Reconstruir estado somente leitura.
2. Validar SHA, state_revision, transition_id e lock.
3. Confirmar que o objetivo permanece dentro do contrato.
4. Selecionar a próxima LEA sem bloqueadores.
5. Criar tentativa e chave de idempotência.
6. Gerar plano de mudança estruturado.
7. Executar em branch e workspace isolados.
8. Rodar CI e coletar evidências.
9. Classificar o resultado.
10. Aplicar uma das transições:
    PASS → revisão independente;
    FAIL conhecido → LEA de remediação;
    causa desconhecida → LEA de investigação;
    falha transitória → retry da mesma tentativa;
    drift/concorrência → reconstrução;
    decisão humana → Visualize;
    risco ou limite → bloqueio formal.
11. Sincronizar estado, GitHub e Linear.
12. Repetir sem solicitar “posso continuar?”.
13. Quando todas as LEAs passarem, integrar e gerar candidato.
14. Validar candidato e emitir decisão final.
```

## 7. Classificação de falhas

### TRANSIENT_INFRA

Exemplos:

- timeout;
- runner indisponível;
- rate limit;
- falha temporária de rede.

Ação:

- retry da mesma tentativa;
- backoff exponencial com jitter;
- sem criar nova LEA inicialmente.

### DETERMINISTIC_IMPLEMENTATION_FAILURE

Exemplos:

- teste reproduzível falha;
- compilação falha;
- contrato violado.

Ação:

- comprovar causa;
- criar LEA de remediação vinculada;
- adicionar teste de regressão.

### UNKNOWN_CAUSE

Ação:

- criar LEA de investigação;
- proibir correção especulativa;
- produzir hipóteses e experimento mínimo.

### STATE_DRIFT

Ação:

- bloquear escrita;
- reconstruir GitHub, Linear e estado;
- preservar `transition_id` quando a transação estiver incompleta.

### CONCURRENT_WRITE

Ação:

- abortar mutação;
- reconsultar fontes vivas;
- replanejar a partir da nova revisão.

### POLICY_OR_SECURITY_VIOLATION

Ação:

- tripwire;
- nenhuma execução;
- relatório seguro;
- BLOCKED.

### HUMAN_PRODUCT_DECISION

Ação:

- pausar em `BLOCKED_HUMAN_DECISION`;
- apresentar Visualize;
- persistir `RunState` e contexto da decisão;
- retomar após escolha.

## 8. Política de retries e antirloop

1. Retry técnico máximo padrão: 3.
2. Retry não cria nova LEA quando a causa é transitória.
3. Falha determinística nunca recebe retry cego.
4. Máximo de 3 remediações por LEA raiz.
5. Terceira remediação sem atingir critério abre `RA — Reavaliação Arquitetural`.
6. Repetição da mesma assinatura de falha sem progresso incrementa contador de estagnação.
7. Duas tentativas sem mudança mensurável acionam análise de causa.
8. Três ciclos sem progresso acionam `STOPPED_NO_PROGRESS`.
9. `max_turns`, tempo e orçamento são obrigatórios.
10. Nenhum limite pode ser desativado silenciosamente pelo agente.

## 9. Idempotência e side effects

Cada mutação externa possui chave única:

```text
objective_id + transition_id + operation + target
```

Antes de executar:

1. consultar ledger;
2. consultar estado atual do alvo;
3. comparar revisão esperada;
4. executar somente se ainda necessário;
5. registrar resultado e identificador externo.

Exemplos:

- issue já criada: reutilizar;
- comentário já publicado: não duplicar;
- branch já existente no SHA correto: reutilizar;
- PR já aberto: reutilizar;
- check já concluído para o mesmo HEAD: reutilizar;
- merge já ocorrido: iniciar confirmação pós-merge, não repetir.

## 10. Concorrência

Camadas combinadas:

1. lock com expiração e heartbeat;
2. GitHub Actions `concurrency` por objetivo;
3. compare-and-swap por `state_revision`;
4. comparação de base SHA e PR HEAD;
5. ledger de eventos e side effects;
6. escrita sequencial por objetivo;
7. células paralelas somente em escopos não conflitantes.

Um lock expirado não é autorização para assumir trabalho. Primeiro ocorre reconstrução.

## 11. Modalidades de desenvolvimento

### UNITÁRIA

Uma LEA completa o loop até PASS antes da próxima.

Uso:

- alto risco;
- requisitos incertos;
- arquitetura nova;
- segurança, dados e migrações.

### TREM SEQUENCIAL

LEAs são executadas em ordem e preservam commits separados.

Regra:

- falha para o trem;
- remediação ocorre antes do próximo vagão.

### TREM COM ESTAÇÕES

Grupos de LEAs terminam em checkpoint, integração e revisão.

Uso:

- trem longo;
- risco moderado;
- necessidade de detectar regressões cedo.

### CÉLULAS PARALELAS

Permitidas somente quando:

- contratos estão congelados;
- arquivos e módulos não colidem;
- WIP está limitado;
- integração possui ordem definida.

### SPIKE

Investiga dúvida e não produz release diretamente.

### CORREÇÃO

Reproduzir → provar causa → teste de regressão → corrigir → validar.

### HOTFIX

Alteração mínima derivada da versão estável, rollback pronto e reconciliação posterior com a linha principal.

### MIGRAÇÃO

Executada primeiro em cópia, com backup validado, versão de origem/destino e reversão definida.

### ESTABILIZAÇÃO

Feature freeze, regressão, RC independente e candidato imutável.

## 12. Gates

### G0 — Contrato

- objetivo verificável;
- critérios de aceite;
- escopo e não escopo;
- riscos;
- autorização por objetivo.

### G1 — Prontidão da LEA

- dependências atendidas;
- arquivos permitidos;
- testes exigidos;
- risco classificado.

### G2 — Implementação

- diff coerente;
- nenhuma alteração proibida;
- commit rastreável.

### G3 — CI

- lint;
- análise estática;
- testes;
- build;
- segurança aplicável.

### G4 — Revisão independente

- escopo;
- arquitetura;
- evidências;
- regressões;
- segurança;
- decisão PASS ou CHANGES_REQUIRED.

### G5 — Integração

- trem consistente;
- suíte cumulativa;
- estado sincronizado.

### G6 — Candidato

- artefato imutável;
- hash;
- manifesto;
- provenance/attestation quando aplicável;
- instalador, atualizador, diagnóstico e rollback.

### G7 — Validação real

- teste no ambiente de Leo;
- relatório;
- critérios observáveis.

### G8 — Promoção

- autorização aplicável;
- checks obrigatórios;
- confirmação pós-merge separada.

## 13. Protocolo obrigatório do Visualize

O loop só chama Leo quando não existe resposta legítima por contrato, teste, política ou evidência.

O Visualize deve apresentar:

```text
SITUAÇÃO
O que aconteceu em linguagem simples.

POR QUE O LOOP PAROU
Qual decisão não pode ser tomada tecnicamente.

OPÇÕES
De 2 a 4 alternativas reais.

RECOMENDAÇÃO
Uma opção recomendada e o motivo.

IMPACTO
Prazo, risco, custo, dados, manutenção e experiência.

REVERSIBILIDADE
Fácil, moderada, difícil ou irreversível.

DECISÃO
Controle claro para Leo selecionar.
```

É proibido apresentar:

- “pode continuar?”;
- opções sem recomendação;
- jargão sem tradução;
- decisão técnica rotineira que o protocolo já resolve.

Após a escolha:

1. registrar decisão no estado;
2. comentar no Linear;
3. registrar ADR quando durável;
4. retomar o `RunState`;
5. continuar automaticamente.

## 14. Segurança

- GitHub App com permissões mínimas;
- secrets fora de prompts, logs e relatórios;
- webhooks validados por HMAC e timestamp;
- delivery IDs deduplicados;
- rulesets impedindo escrita e merge indevidos;
- tools com schemas estritos;
- allowlist para comandos locais;
- workspace isolado por tentativa;
- rede e filesystem limitados conforme necessidade;
- relatório seguro para suporte e relatório local restrito;
- entrada de repositório, issues e comentários tratada como dado, não instrução.

## 15. Três níveis de implantação

### Nível 1 — Chat orquestrado

Disponível imediatamente:

- ChatGPT usa conectores GitHub e Linear;
- estado é checkpointado;
- execução acontece dentro da duração da interação;
- sem Codex.

Limite:

- não sobrevive sozinho ao encerramento da interação.

### Nível 2 — Executor orientado a eventos

- GitHub Actions;
- workflows reutilizáveis;
- estado versionado;
- repository dispatch;
- Linear sincronizado;
- ChatGPT inicia e interpreta resultados.

Limite:

- raciocínio prolongado e retomada ainda dependem de novas execuções.

### Nível 3 — OLO durável

- serviço/event worker;
- Agents SDK;
- RunState persistente;
- webhook GitHub, Linear e OpenAI;
- workflow engine ou state store durável;
- retomada após falhas e longas esperas;
- Visualize para decisão humana;
- GitHub e Linear continuam como interfaces oficiais.

Este é o alvo definitivo para substituir logicamente o papel operacional anteriormente atribuído ao Codex.

## 16. Piloto recomendado

Projeto piloto:

```text
TriView Workspace
```

Escopo inicial seguro:

```text
criar e validar o núcleo universal de manutenção:
abrir + atualizar + diagnosticar + relatório
```

Por que esse piloto:

- problema já conhecido;
- requisitos concretos;
- necessidade de instalação limpa;
- falhas anteriores documentadas;
- resultado observável por Leo;
- risco controlável sem produção crítica.

### Fases do piloto

1. Criar contratos e schemas sem mudar o TriView.
2. Criar templates Linear e workflows reutilizáveis.
3. Implementar runtime de estado e ledger.
4. Executar uma LEA unitária em loop.
5. Simular falha de teste e criação automática de remediação.
6. Simular webhook duplicado.
7. Simular interrupção e retomada.
8. Simular decisão humana via Visualize.
9. Executar trem curto de três LEAs.
10. Gerar candidato isolado e relatório.

## 17. Critérios de aprovação da arquitetura

- [ ] objetivo reconstruível em chat novo;
- [ ] nenhuma fonte possui autoridade ambígua;
- [ ] evento duplicado não duplica efeito;
- [ ] escrita concorrente é bloqueada;
- [ ] falha parcial mantém a mesma transição;
- [ ] retry transitório não cria LEA desnecessária;
- [ ] falha determinística cria remediação rastreável;
- [ ] causa desconhecida cria investigação;
- [ ] loop possui limites;
- [ ] decisão humana usa Visualize;
- [ ] execução continua sem confirmação genérica;
- [ ] candidato possui hash e evidências;
- [ ] revisão independente não é feita pelo implementador;
- [ ] merge permanece controlado;
- [ ] Codex não é necessário.

## 18. Estado da candidata

```text
ARCHITECTURE_MODEL=CREATED
INTERNAL_RESEARCH=PASS_INITIAL
OFFICIAL_RESEARCH=PASS_INITIAL
ADVERSARIAL_RC=PENDING
RUNTIME_TESTS=NOT_EXECUTED
MERGE_AUTHORIZED=NO
```
