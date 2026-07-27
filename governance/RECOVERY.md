# Recuperação Técnica dos Guardrails PREDIX

## Estado

- **Versão:** `0.1-provisória`.
- **Escopo:** restauração de objetivo, decisão, comando, autorização, timeline e execução parcial.
- **Execução automática:** ainda não implementada em software.
- **Validação:** pendente de testes RC-001 a RC-006 e RC independente.

## Objetivo

Definir como o sistema deve reagir quando perder estado, detectar comando divergente, falhar em uma gravação ou encontrar conflito entre decisões, documentos e ferramentas.

## Princípios

1. recuperação nunca cria nova autorização;
2. recuperação nunca amplia o escopo;
3. o último estado válido deve possuir evidência;
4. restauração de estado não apaga o incidente;
5. correções são append-only na timeline e no registro de decisões;
6. ações externas parcialmente executadas exigem reconciliação antes de qualquer nova tentativa;
7. quando não houver estado confiável, o fluxo deve bloquear e pedir decisão assistida.

## Pacote mínimo de estado recuperável

```yaml
recovery_state:
  objective_id: OBJ-...
  objective_text: ...
  mode: ASSISTIDO_RECOMENDADO
  project: ...
  conversation: ...
  selected_options: []
  ordered_plan: []
  generated_command: ...
  authorization_level: N0|N1|N2|N3|N4
  authorization_reference: ...
  repository: ...
  branch: ...
  environment: ...
  commit_or_state_hash: ...
  related_decisions: []
  last_verified_evidence: []
  pending_timeline_entry: ...
```

Campos ausentes devem ser declarados como desconhecidos; não podem ser inventados.

## Checkpoint válido

Um checkpoint só pode ser usado quando:

- foi registrado antes da violação;
- identifica objetivo, projeto e modo;
- possui decisão ou comando correspondente;
- quando houver ferramenta, contém referência verificável;
- não foi invalidado por mudança posterior de ambiente, commit, branch ou escopo.

## Fluxo geral de recuperação

```text
detectar violação
→ classificar severidade
→ congelar novas ações
→ preservar evidência
→ localizar último checkpoint válido
→ comparar estado atual com checkpoint
→ escolher restauração, reconciliação ou bloqueio
→ registrar incidente
→ apresentar opções assistidas
→ somente depois retomar
```

## Estratégias por severidade

### S1 — Correção local

- corrigir texto, rótulo ou apresentação;
- não alterar decisão;
- registrar apenas se recorrente.

### S2 — Revalidação da etapa

- invalidar o comando visual anterior;
- retornar à última seleção confirmada;
- gerar novamente o comando específico;
- revalidar objetivo e ordem do plano.

### S3 — Restauração de estado

- bloquear continuidade;
- restaurar objetivo, modo, projeto e decisão do último checkpoint;
- marcar o evento como incidente;
- verificar timeline e registro de decisões;
- oferecer opções de retomar, revisar ou cancelar.

### S4 — Bloqueio absoluto

- não executar ou repetir a ação;
- preservar evidências e referências;
- revogar autorização inválida;
- exigir nova autorização ou procedimento manual especial;
- quando houver efeito externo, reconciliar o estado real antes de qualquer correção.

## Cenários obrigatórios

### RC-001 — Perda de objetivo

1. comparar comando recebido com objetivo anterior;
2. restaurar o último objetivo válido;
3. reabrir o painel com opções compatíveis;
4. registrar GR-001/GR-044 e severidade S3.

### RC-002 — Comando divergente

1. descartar o comando;
2. voltar à seleção confirmada;
3. mostrar a divergência;
4. gerar novo comando somente após confirmação.

### RC-003 — Autorização expirada ou estado alterado

1. invalidar a autorização;
2. comparar commit, branch, ambiente e hash;
3. exigir nova apresentação do pacote N2/N3;
4. nunca reutilizar autorização anterior.

### RC-004 — Falha de commit da timeline

1. registrar a atualização como `PENDENTE_DE_SINCRONIZACAO` fora da alegação de sucesso;
2. informar a falha ao usuário;
3. buscar o SHA atual antes de nova tentativa;
4. após sucesso, criar entrada de recuperação vinculada à tentativa.

### RC-005 — Atualização parcial de vários arquivos

1. listar quais commits foram realizados;
2. listar arquivos ainda pendentes;
3. não declarar o plano completo;
4. retomar apenas itens faltantes com SHAs atuais;
5. reconciliar o registro de decisões e a timeline.

### RC-006 — Conflito entre decisão e documento

1. identificar fontes conflitantes;
2. aplicar a hierarquia de precedência;
3. bloquear aprovação ou merge;
4. apresentar alternativas de reconciliação;
5. registrar a decisão que resolver o conflito.

## Recuperação do painel assistido

Quando o painel falhar:

- nenhuma opção deve ser presumida;
- seleções anteriores permanecem apenas se houver confirmação registrada;
- comando ocultado ou inválido não pode ser reutilizado;
- opções incompatíveis devem ser desmarcadas e explicadas;
- a recomendação da IA deve ser recalculada após mudança relevante de estado.

## Recuperação de autorização N2/N3

Uma autorização deve ser revogada quando mudar:

- ação;
- projeto;
- repositório;
- branch ou destino;
- ambiente;
- commit, migration ou hash de estado;
- impacto esperado;
- backup ou plano de reversão.

## Registro de incidente

Campos mínimos:

```yaml
incident_id: INC-AAAAMMDD-HHMMSS-NNN
guardrails: []
severity: S0|S1|S2|S3|S4
detected_at: D1|D2|D3|D4
last_valid_checkpoint: ...
current_state: ...
action_taken: ...
recovered: true|false
remaining_risk: ...
evidence: []
```

## Critérios de sucesso

A recuperação somente é considerada concluída quando:

- o estado restaurado foi verificado;
- nenhuma autorização inválida permanece ativa;
- o incidente foi registrado;
- decisões e timeline foram reconciliadas;
- o próximo painel apresenta opções compatíveis;
- não existem efeitos externos desconhecidos.

## Bloqueios

O fluxo permanece bloqueado quando:

- não existe checkpoint confiável;
- o efeito externo real é desconhecido;
- a autorização foi perdida;
- existem conflitos entre fontes oficiais;
- o risco residual é S4;
- a recuperação exigiria apagar evidências ou inventar estado.

## Gate

Este documento não autoriza recuperação automática em produção. Primeiro devem passar RC-001 a RC-006, testes de falha parcial e RC independente.
