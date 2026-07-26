# Plano de Integração Global da Timeline PREDIX

## Objetivo

Registrar conversas provenientes de qualquer contexto autorizado, distinguindo:

- chat normal fora de projetos;
- conversa dentro de um projeto;
- nome do projeto;
- título ou identificador da conversa;
- data, horário, fuso e período do dia;
- decisões, ações, evidências, estado e próximos passos.

## Regra desejada

Toda conversa deverá produzir eventos estruturados para a timeline. A regra é global como requisito da MOP, mas sua aplicação automática depende das capacidades disponíveis em cada chat e de uma integração central ainda não implementada.

## Envelope mínimo de evento

```yaml
event_id: TL-AAAAMMDD-HHMMSS-SEQ
timestamp: AAAA-MM-DDTHH:MM:SS-03:00
timezone: America/Recife
period: madrugada|manha|tarde|noite
source_type: project|normal_chat
project_name: nome-ou-null
conversation_title: titulo-ou-identificacao
user_intent: resumo
status: proposed|provisional|approved|rejected|blocked|executed
execution: none|proposed|performed
result: resumo
 evidence: []
next_steps: []
privacy: public|internal|sensitive|secret-redacted
```

## Arquitetura em fases

### Fase 0 — Registro assistido por conversa

- Atualizar o GitHub após cada mensagem quando o contexto e o conector estiverem disponíveis.
- Não alegar salvamento quando a gravação falhar.
- Usar branch isolada até revisão e aprovação.

### Fase 1 — Padronização e índice

- Um arquivo diário por data.
- Um índice geral `TIMELINE.md`.
- Identificadores únicos e timestamps completos.
- Classificação de origem e projeto.
- Backfill somente a partir de contexto comprovadamente disponível.

### Fase 2 — Coletor central autorizado

Construir um serviço PREDIX responsável por receber eventos de múltiplos chats e gravá-los de forma idempotente. O mecanismo de ingestão deverá ser escolhido somente após confirmar quais interfaces de exportação, integração ou compartilhamento estão oficialmente disponíveis.

Componentes previstos:

1. endpoint autenticado de ingestão;
2. validação de esquema;
3. remoção de segredos;
4. deduplicação por `event_id` e hash;
5. fila de processamento;
6. gravador GitHub ou banco durável;
7. reconciliação e auditoria;
8. painel de consulta por data, período, projeto e conversa.

### Fase 3 — Cobertura global e análise

- Capturar conversas autorizadas de todos os projetos e chats normais.
- Consultar por manhã, tarde, noite, projeto, decisão ou assunto.
- Gerar retrospectiva diária e semanal.
- Detectar contradições entre decisões antigas e novas.
- Sugerir prioridades com base no histórico real.

## Guardrails

- Não registrar chaves, senhas, tokens ou segredos.
- Não inventar conversas ausentes.
- Não tratar resumo parcial como cobertura completa.
- Não misturar projetos sem registrar a origem.
- Não apagar decisões anteriores; correções são novos eventos.
- Não alterar a `main` sem autorização adequada.
- Toda falha de gravação deve ser explicitamente informada.

## Critérios de aceite da integração global

1. captura eventos de chats normais e projetos;
2. registra data, horário, fuso e período;
3. identifica projeto e conversa;
4. grava sem duplicar eventos;
5. remove ou mascara segredos;
6. informa falhas de ingestão;
7. permite consultar decisões por intervalo e origem;
8. preserva histórico append-only;
9. possui testes de concorrência, idempotência e recuperação;
10. só promove registros à fonte oficial após validação.

## Estado

- **Planejamento:** iniciado em 26 de julho de 2026.
- **Implementação central:** pendente.
- **Dependência principal:** confirmar e escolher um canal autorizado para captura global das conversas.
