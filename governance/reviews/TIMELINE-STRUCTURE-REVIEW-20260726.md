# Revisão da Estrutura da Timeline — 2026-07-26

## Escopo

Revisão da estrutura composta por:

- `TIMELINE.md`;
- `timeline/AAAA/MM/AAAA-MM-DD.md`;
- backfills disponíveis;
- `timeline/GLOBAL-INGESTION-PLAN.md`;
- vínculo com `governance/DECISION-REGISTER.md`.

## Resultado original

**CHANGES REQUIRED — estrutura funcional, porém ainda não pronta para validação global.**

## Pontos fortes

- índice cronológico por data;
- fuso oficial `America/Recife`;
- divisão por madrugada, manhã, tarde e noite;
- identificação de projeto ou chat normal;
- histórico append-only;
- distinção entre cobertura ativa e backfill parcial;
- vínculo conceitual com decisões, evidências e próximos passos.

## Achados originais

### TL-R01 — Entradas antigas não seguem o esquema completo

As entradas anteriores à formalização do contrato não possuem, em todos os casos:

- timestamp ISO 8601 completo;
- segundos;
- período do dia;
- conversa identificada;
- ação, evidência e próxima etapa separadas.

**Remediação:** manter o registro original e acrescentar uma entrada de normalização ou metadados complementares, sem reescrever silenciosamente o histórico.

### TL-R02 — Falta identificador estável por entrada

Somente data e horário podem gerar colisões ou dificultar referências.

**Remediação proposta:** usar `TL-AAAAMMDD-HHMMSS-NNN`.

### TL-R03 — Falta chave de idempotência

Uma mesma mensagem pode ser registrada duas vezes em caso de repetição, falha de rede ou retomada.

**Remediação proposta:** registrar uma chave derivada de data, conversa, ordem local e resumo normalizado, sem armazenar conteúdo sensível.

### TL-R04 — Falta vínculo direto com decisões e artefatos

Entradas devem apontar para IDs como `DEC-*`, commits, PRs, issues, deployments ou testes.

**Remediação proposta:** adicionar campos `decisoes_relacionadas` e `evidencias`.

### TL-R05 — Falta classificação do estado operacional

A timeline descreve o estado em texto livre, mas não usa sempre uma taxonomia consistente.

**Remediação proposta:** adotar `PROPOSTO`, `PLANEJADO`, `TENTADO`, `EXECUTADO`, `VERIFICADO`, `BLOQUEADO` ou `CORRIGIDO`.

### TL-R06 — Captura global ainda não existe

A estrutura registra somente chats cujo contexto e GitHub estejam acessíveis. Não existe ingestão automática de toda a conta.

**Remediação:** manter aviso explícito e implementar integração central antes de declarar cobertura global.

### TL-R07 — Frequência de commit precisa de regra operacional

O requisito é atualizar após cada mensagem. Commits individuais garantem rastreabilidade, mas podem gerar ruído e conflitos.

**Regra provisória:** uma atualização lógica por mensagem; quando o conector exigir, um commit por atualização. Uma futura integração poderá agrupar tecnicamente sem perder a granularidade lógica.

### TL-R08 — Falta estratégia de correção de horário

Horários inferidos ou indisponíveis não devem ser apresentados como exatos.

**Remediação:** adicionar `precisao_temporal: exata | aproximada | inferida`.

### TL-R09 — Privacidade precisa de filtro verificável

A regra proíbe segredos, mas falta uma lista mínima de exclusão.

**Remediação:** não registrar senhas, tokens, chaves, dados bancários, conteúdo sensível desnecessário, mensagens privadas integrais ou identificadores pessoais sem finalidade operacional.

### TL-R10 — Falta reconciliação de fim de dia

Não há um fechamento diário que compare timeline, decisões e ações reais.

**Remediação:** gerar resumo de encerramento com concluídos, pendentes, bloqueados, divergências e primeira retomada do próximo dia.

## Estado após remediação estrutural

| Achado | Estado | Evidência |
|---|---|---|
| TL-R01 | REMEDIADO | `timeline/2026/07/2026-07-26-NORMALIZATION.md` |
| TL-R02 | REMEDIADO | `timeline/SCHEMA.md` |
| TL-R03 | REMEDIADO E NÃO TESTADO | `timeline/SCHEMA.md` |
| TL-R04 | REMEDIADO | esquema e normalização |
| TL-R05 | REMEDIADO | taxonomia do esquema |
| TL-R06 | LIMITAÇÃO EXPLÍCITA | índice e esquema |
| TL-R07 | REMEDIADO | regra de atualização lógica |
| TL-R08 | REMEDIADO | precisão temporal |
| TL-R09 | REMEDIADO E NÃO TESTADO | filtro mínimo de privacidade |
| TL-R10 | REMEDIADO E NÃO EXECUTADO | procedimento de fechamento diário |

Relatório detalhado: `governance/reviews/TIMELINE-REMEDIATION-20260726.md`.

## Gate atualizado

A estrutura pode seguir para testes TL-001 a TL-015, mas ainda não está validada globalmente. Permanecem obrigatórios:

1. testes de duplicidade, privacidade, horário, origem e fechamento;
2. execução real do fechamento diário;
3. RC independente com separação de contexto;
4. limitação global explícita até integração real.
