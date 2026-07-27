# MOP-04 — Arquitetura candidata v0.2

**Substitui:** v0.1 para fins de revisão  
**Origem:** LEA-224 / RC adversarial interna 01  
**Estado:** candidata remediada  
**Codex:** proibido  
**Merge:** não autorizado

Este documento complementa a arquitetura v0.1 e fecha os achados `MOP04-RC01-F01` a `F10`.

## 1. Decision Capsule e comunicação com Leo

### 1.1 Limite de plataforma reconhecido

Um runtime externo não consegue, por si só, abrir uma interface Visualize dentro de uma conversa específica. Portanto, a decisão humana é persistida como uma cápsula estruturada e disponibilizada em uma fila de decisões.

### 1.2 Decision Capsule

```json
{
  "decision_id": "DEC-OBJ-001-003",
  "objective_id": "OBJ-001",
  "transition_id": "OBJ-001-T12",
  "state_revision": 12,
  "status": "PENDING_HUMAN",
  "title": "Escolha necessária em linguagem simples",
  "situation": "O que aconteceu",
  "why_automation_stopped": "Por que evidências e políticas não resolvem",
  "options": [
    {
      "id": "A",
      "label": "Opção A",
      "benefits": [],
      "risks": [],
      "impact": {},
      "reversibility": "EASY|MODERATE|HARD|IRREVERSIBLE"
    }
  ],
  "recommended_option": "A",
  "recommendation_reason": "Motivo objetivo",
  "evidence_ids": [],
  "resume_token": "opaque-reference",
  "created_at": "ISO-8601",
  "expires_at": null
}
```

### 1.3 Fluxo

```text
OLO detecta decisão humana
→ serializa RunState
→ cria Decision Capsule
→ marca Linear como BLOCKED_HUMAN_DECISION
→ registra resumo no GitHub
→ adiciona item à Decision Inbox
→ envia notificação pelo canal configurado
→ Leo abre ou retoma o chat do projeto
→ protocolo iniciar lê a cápsula
→ ChatGPT renderiza Visualize
→ Leo escolhe
→ decisão é persistida
→ OLO valida revisão e resume o RunState
```

### 1.4 Regra de comunicação

- notificação pode informar que existe decisão pendente;
- a decisão propriamente dita deve ser apresentada no chat pelo Visualize;
- o chat nunca reconstrói opções a partir de memória informal;
- a cápsula é a fonte da decisão;
- escolha aplicada uma vez possui chave de idempotência.

## 2. Event Store, inbox, outbox e DLQ

### 2.1 Componentes

```text
EVENT_INBOX
EVENT_STORE
SIDE_EFFECT_OUTBOX
CONSUMPTION_LEDGER
DEAD_LETTER_QUEUE
```

### 2.2 Regras

1. Todo webhook entra primeiro na inbox.
2. HMAC, timestamp e origem são validados antes do parsing operacional.
3. `delivery_id + source` forma a chave de deduplicação de entrega.
4. Eventos recebem sequência monotônica por objetivo.
5. Eventos fora de ordem permanecem aguardando predecessores ou acionam reconstrução.
6. Transição de estado e registro da outbox são atômicos.
7. Side effects são executados depois do commit da transição.
8. Resultado do side effect atualiza o ledger.
9. Falha retryable volta à fila com backoff.
10. Falha não retryable ou limite esgotado vai para DLQ.
11. Replay da DLQ exige motivo, operador e nova chave de replay.
12. Evento processado nunca é apagado antes da política de retenção.

### 2.3 Estado de consumo

```text
RECEIVED
→ VERIFIED
→ ACCEPTED
→ APPLIED
→ SIDE_EFFECTS_PENDING
→ COMPLETE
```

Alternativas:

```text
DUPLICATE
OUT_OF_ORDER
RETRY_SCHEDULED
DEAD_LETTERED
REJECTED_SECURITY
```

## 3. Policy Enforcement Point

O modelo não executa shell nem escreve diretamente em repositórios. Ele produz uma proposta estruturada.

```text
AGENTE PROPÕE
→ SCHEMA VALIDATOR
→ POLICY ENFORCEMENT POINT
→ PATCH VALIDATOR
→ COMMAND BROKER
→ WORKSPACE ISOLADO
```

### 3.1 LEA Execution Manifest

```yaml
lea_id: LEA-301
allowed_paths:
  - src/module/**
  - tests/module/**
protected_paths:
  - .github/workflows/**
  - migrations/**
allowed_commands:
  - python -m pytest tests/module
  - python -m ruff check src/module tests/module
network_policy: DENY_BY_DEFAULT
secrets_allowed: []
max_files_changed: 12
max_diff_lines: 800
```

### 3.2 Barreiras

- patch fora da allowlist: rejeitado;
- arquivo protegido: aprovação específica;
- comando não listado: rejeitado;
- path traversal ou symlink inesperado: rejeitado;
- secret solicitado sem autorização: rejeitado;
- diff excede limite: nova decomposição ou decisão;
- texto de issue, comentário, README, log e código é dado, não instrução.

## 4. Agent Manifest e avaliações

Cada agente é versionado:

```yaml
agent_id: failure-analyst
agent_version: 1.2.0
prompt_version: sha256:...
model_policy: approved-model-family
output_schema_version: 1.0
allowed_tools: []
max_turns: 12
eval_suite: evals/failure-analyst-v1.jsonl
```

### 4.1 Gate de mudança

```text
ALTERAÇÃO DE PROMPT, MODELO OU TOOL
→ evals determinísticas
→ casos adversariais
→ shadow run sem side effects
→ comparação com baseline
→ revisão
→ promoção da versão do agente
```

Métricas mínimas:

- aderência ao schema;
- precisão de classificação de falha;
- taxa de LEA desnecessária;
- taxa de retry incorreto;
- violações de escopo;
- custo e turnos;
- falsos PASS e falsos BLOCKED.

## 5. Kill switch e modos operacionais

### 5.1 Flags

```text
FACTORY_MODE=ACTIVE|READ_ONLY|PAUSED|EMERGENCY_STOP
OBJECTIVE_MODE=ACTIVE|PAUSED|CANCELLED
MUTATIONS_ALLOWED=YES|NO
NEW_JOBS_ALLOWED=YES|NO
```

### 5.2 EMERGENCY_STOP

Efeitos obrigatórios:

- impedir novos jobs;
- cancelar jobs ainda seguros para cancelamento;
- impedir processamento de outbox;
- revogar ou rotacionar credenciais comprometidas;
- preservar evidências;
- gerar incidente;
- exigir reconstrução antes de reativar.

Nenhum agente pode remover o kill switch.

## 6. Migration Contract

```yaml
migration_id: MIG-004
from_schema: "3"
to_schema: "4"
compatibility: BACKWARD_COMPATIBLE|WINDOWED|BREAKING
strategy: EXPAND_CONTRACT|COPY_AND_SWITCH|IN_PLACE
backup_required: true
backup_verification: RESTORE_SMOKE_TEST
rollback_supported: true
rollback_deadline: "ISO-8601"
data_validation: []
code_versions_supported:
  - "1.8.x"
  - "1.9.x"
```

### 6.1 Fluxo

```text
snapshot
→ verificar restauração
→ expandir schema compatível
→ implantar código compatível com antigo e novo
→ migrar dados de forma idempotente
→ validar
→ observar janela
→ contrair somente após gate
```

Migração irreversível exige Decision Capsule e aprovação explícita.

Rollback de código só é declarado válido quando a compatibilidade com o schema atual foi testada.

## 7. Estado e prevenção de workflow recursivo

### 7.1 Regra

GitHub recebe checkpoints significativos, não heartbeat nem todo evento.

### 7.2 Piloto com estado em GitHub

- branch de controle separada ou path `control-state/**`;
- workflows de produto ignoram mudanças exclusivas em `control-state/**`;
- workflow de controle ignora commits produzidos por sua própria transição quando o delivery já está no ledger;
- compare-and-swap pelo blob SHA;
- commit agrupado por transição, não por evento;
- snapshots efêmeros não são persistidos como expectativas futuras.

### 7.3 Arquitetura durável

Event store fica fora do Git; GitHub recebe:

- contrato;
- checkpoints;
- decisões;
- manifests;
- relatórios;
- estado consolidado em marcos.

## 8. Observabilidade

### 8.1 Correlation IDs

Toda operação carrega:

```text
objective_id
lea_id
attempt_id
transition_id
trace_id
event_id
github_run_id
linear_issue_id
```

### 8.2 Métricas

- objetivos em execução;
- tempo por estado;
- LEAs por objetivo;
- remediações por LEA;
- retries por classe;
- eventos duplicados;
- DLQ;
- falhas de sincronização;
- custo e tokens;
- taxa de PASS após primeira tentativa;
- tempo esperando decisão humana;
- rollback e recovery success rate.

### 8.3 SLOs iniciais do piloto

```text
STATE_RECONSTRUCTION_SUCCESS=100%
DUPLICATE_SIDE_EFFECTS=0
UNAUTHORIZED_MAIN_WRITES=0
UNAUTHORIZED_MERGES=0
LOST_EVENTS=0
REPORT_GENERATION_SUCCESS>=99%
```

Alertas críticos:

- estado divergente;
- evento na DLQ;
- side effect duplicado;
- ruleset contornado;
- secret exposto;
- kill switch ativado;
- transição sem progresso.

## 9. Revisão independente isolada

### 9.1 Contexto permitido ao revisor

- contrato do objetivo;
- diff e arquivos alterados;
- manifestos;
- testes e logs brutos;
- critérios de aceite;
- políticas aplicáveis;
- HEAD fixado.

### 9.2 Contexto proibido como autoridade

- justificativa persuasiva do implementador;
- conclusão da autorrevisão;
- nota pretendida;
- promessa de correção;
- instrução encontrada em código, logs, comentários ou relatórios.

### 9.3 Regras

- prompt e agente próprios;
- nenhuma remediação durante revisão;
- resultado estruturado;
- achados com evidência e critério de aceite;
- review HEAD fixado;
- mudança após revisão invalida PASS e exige reteste.

## 10. Separação entre piloto e alvo durável

### 10.1 Piloto MOP-Lite

Ferramentas visíveis:

- ChatGPT;
- GitHub;
- Linear;
- Visualize.

Execução:

- conectores durante interação;
- GitHub Actions para testes e build;
- estado em checkpoints GitHub;
- nenhuma promessa de continuar após encerramento da execução do chat.

Objetivo:

- validar contratos, estados, LEAs automáticas, gates, relatórios e recuperação conceitual.

### 10.2 MOP-Durable

Adições técnicas:

- OpenAI API e Agents SDK;
- OLO hospedado;
- fila/event store;
- webhooks;
- state store durável;
- workers e retries;
- RunState persistente;
- monitoramento.

Objetivo:

- continuar por horas ou dias, sobreviver a reinícios e retornar somente em PASS, BLOCKED ou Decision Capsule.

### 10.3 Decisão futura obrigatória

Antes de implementar MOP-Durable, Leo receberá Visualize comparando opções de:

- hospedagem;
- state store/workflow engine;
- custo máximo;
- nível de autonomia;
- retenção de traces;
- canal de notificação.

A decisão não bloqueia a documentação e os testes do MOP-Lite.

## 11. Matriz de remediação

| Achado | Correção |
|---|---|
| F01 | Decision Capsule + Decision Inbox + protocolo Visualize |
| F02 | inbox/outbox/ledger/DLQ/ordenação/replay |
| F03 | Policy Enforcement Point + patch validator + command broker |
| F04 | Agent Manifest + evals + shadow run |
| F05 | kill switch e modos operacionais |
| F06 | Migration Contract + expand/contract + restore test |
| F07 | branch/path de controle e filtros anti-recursão |
| F08 | correlation IDs, métricas, SLOs e alertas |
| F09 | contexto mínimo e gate independente fixado por HEAD |
| F10 | MOP-Lite separado de MOP-Durable e decisão futura via Visualize |

## 12. Estado

```text
RC01_FINDINGS_REMEDIATED=10_OF_10
RUNTIME_TESTS=NOT_EXECUTED
INDEPENDENT_REVIEW=PENDING
MERGE_AUTHORIZED=NO
NEXT_ACTION=INTERNAL_RETEST_THEN_INDEPENDENT_RC
```
