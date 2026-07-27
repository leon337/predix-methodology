# MOP-04 — RC adversarial interna 01

**Alvo:** `MOP-04_ARCHITECTURE_CANDIDATE_V0.1.md`  
**HEAD revisado:** `219b85701d2356a349b6e8b8d804d434b8fccbe4`  
**Natureza:** autorrevisão adversarial, não substitui revisão independente  
**Resultado:** `CHANGES_REQUIRED`

## 1. Resumo

A arquitetura candidata define corretamente os planos humano, controle, raciocínio, execução e memória. Entretanto, ainda não está pronta para piloto porque existem lacunas entre o desenho conceitual e a operação recuperável.

## 2. Achados

### MOP04-RC01-F01 — Canal de decisão humana incompleto

**Severidade:** ALTA

**Problema:** o documento exige Visualize, porém não define como um runtime externo entrega uma decisão ao chat. GitHub, Linear e webhooks não abrem automaticamente uma interface Visualize na conversa.

**Impacto:** o loop pode ficar bloqueado sem Leo saber onde recuperar a decisão ou pode regressar para perguntas técnicas comuns.

**Correção exigida:** criar `Decision Capsule`, inbox de decisões, regra de notificação e protocolo `iniciar/retomar` que lê a cápsula e renderiza Visualize.

### MOP04-RC01-F02 — Event store e fila de falhas insuficientemente definidos

**Severidade:** ALTA

**Problema:** existe Event Envelope, mas faltam ordenação, estado de consumo, dead-letter queue, redelivery, retenção e recuperação de eventos fora de ordem.

**Impacto:** eventos duplicados ou atrasados podem promover estado incorreto.

**Correção exigida:** definir inbox/outbox, sequência por objetivo, ledger de consumo, DLQ, replay controlado e política de retenção.

### MOP04-RC01-F03 — O executor ainda pode receber intenção de modelo sem barreira suficiente

**Severidade:** ALTA

**Problema:** a arquitetura não especifica que o modelo apenas propõe um plano/patch e que um validador determinístico deve verificar arquivos, comandos e permissões antes da execução.

**Impacto:** prompt injection, mudança fora de escopo ou comando perigoso pode alcançar o executor.

**Correção exigida:** adicionar Policy Enforcement Point, allowlist por LEA, patch validator, command broker e sandbox sem credenciais desnecessárias.

### MOP04-RC01-F04 — Não existe política de modelos e avaliações

**Severidade:** MÉDIA

**Problema:** faltam versão de prompt, versão de modelo, conjunto de evals e critério para promover mudanças no comportamento dos agentes.

**Impacto:** atualização de modelo ou prompt pode alterar silenciosamente decisões e taxa de falhas.

**Correção exigida:** criar Agent Manifest versionado, eval suite, golden cases, shadow run e gate de promoção.

### MOP04-RC01-F05 — Falta kill switch operacional

**Severidade:** ALTA

**Problema:** não existe mecanismo global para pausar novos jobs e impedir novas mutações em incidente.

**Impacto:** uma falha de política ou integração pode continuar gerando efeitos.

**Correção exigida:** adicionar `FACTORY_PAUSED`, `OBJECTIVE_PAUSED`, cancelamento de jobs, revogação de credenciais e modo read-only.

### MOP04-RC01-F06 — Recuperação de dados e migrações ainda genérica

**Severidade:** ALTA

**Problema:** rollback de código está descrito, mas a arquitetura universal não define coordenação entre versão de código, schema, backup e compatibilidade reversa.

**Impacto:** código anterior pode não funcionar depois de migração.

**Correção exigida:** adicionar Migration Contract, snapshot verificado, expand/contract, compatibility window e rollback testado.

### MOP04-RC01-F07 — Estado em Git para piloto pode gerar loops recursivos

**Severidade:** MÉDIA

**Problema:** commits de estado podem disparar o próprio workflow e gerar ruído ou recorrência.

**Impacto:** consumo desnecessário, concorrência e histórico poluído.

**Correção exigida:** separar paths, filtros de workflow, branch de controle ou backend de estado; commits apenas em checkpoints significativos.

### MOP04-RC01-F08 — Falta modelo de observabilidade operacional

**Severidade:** MÉDIA

**Problema:** tracing é citado, mas faltam métricas, SLOs, alertas e correlação entre OpenAI, GitHub, Linear e runtime.

**Impacto:** falhas silenciosas e diagnóstico lento.

**Correção exigida:** definir correlation ID, métricas de loop, alertas, health checks e relatório de incidente.

### MOP04-RC01-F09 — Separação do revisor independente precisa ser reforçada

**Severidade:** MÉDIA

**Problema:** existe agente revisor, mas não está definido como evitar que ele herde conclusões do implementador como instruções.

**Impacto:** viés de confirmação e aprovação por narrativa.

**Correção exigida:** contexto mínimo independente, evidência bruta, prompt próprio, proibição de remediação e gate externo.

### MOP04-RC01-F10 — Arquitetura durável exige API/runtime além do chat

**Severidade:** ALTA

**Problema:** o Nível 3 pressupõe OpenAI API, hospedagem do OLO e armazenamento durável, mas esses custos e responsabilidades ainda não foram transformados em decisão de produto.

**Impacto:** expectativa de autonomia incompatível com o Nível 1.

**Correção exigida:** separar piloto sem runtime contínuo do alvo durável e preparar decisão futura via Visualize sobre hospedagem, estado e orçamento.

## 3. Decisão

```text
ARCHITECTURE_V0_1=CHANGES_REQUIRED
CRITICAL_FINDINGS=0
HIGH_FINDINGS=6
MEDIUM_FINDINGS=4
INDEPENDENT_REVIEW=NOT_EXECUTED
MERGE_AUTHORIZED=NO
NEXT_ACTION=CREATE_AND_EXECUTE_REMEDIATION_LEA
```
