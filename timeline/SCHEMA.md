# Esquema Operacional da Timeline PREDIX

## Estado

- **Versão:** `0.2-provisória`.
- **Fuso oficial:** `America/Recife` (`UTC-03:00`).
- **Cobertura global:** não implementada; somente fontes acessíveis e explicitamente registradas.
- **Histórico:** append-only; correções geram nova entrada ou complemento vinculado.

## Objetivo

Padronizar registros temporais, evitar duplicidade lógica, preservar vínculos com decisões e evidências e permitir consultas por data, período, projeto, conversa e estado operacional.

## Identificador estável

Cada entrada utiliza:

```text
TL-AAAAMMDD-HHMMSS-NNN
```

- `AAAAMMDD`: data local;
- `HHMMSS`: horário local disponível ou valor aproximado declarado;
- `NNN`: sequência local para evitar colisões.

O ID nunca é reutilizado. Correções apontam para o ID original.

## Chave de idempotência

Formato recomendado:

```text
IDEMP-AAAAMMDD-ORIGEM-CONVERSA-ORDEM-RESUMO
```

A chave é formada por:

1. data local;
2. origem (`projeto` ou `chat-normal`);
3. identificador normalizado da conversa;
4. ordem local da mensagem ou evento;
5. resumo normalizado sem conteúdo sensível.

Antes de gravar, o agente deve verificar se a chave já existe no arquivo do dia. Uma repetição técnica não cria nova entrada; uma correção real cria nova entrada com `corrige:` apontando para a anterior.

## Campos mínimos

```yaml
id: TL-20260726-145032-001
idempotency_key: IDEMP-20260726-PROJETO-FABRICA-SOFTWARES-001-PLANO-VALIDACAO
timestamp: 2026-07-26T14:50:32-03:00
precisao_temporal: exata
periodo: tarde
origem: projeto
projeto: Fábrica de softwares
conversa: Governança e Fluxo Assistido
intencao: executar plano confirmado
estado_operacional: EXECUTADO
decisoes_relacionadas:
  - DEC-20260726-002
evidencias:
  - commit: abc123
pendencias:
  - validar em RC
proxima_etapa: executar revisão independente
```

## Precisão temporal

Valores permitidos:

- `exata`: horário obtido de fonte confiável no momento do registro;
- `aproximada`: minuto conhecido, segundos ausentes ou arredondados;
- `inferida`: horário deduzido de metadados ou ordem relativa.

Horário inferido ou aproximado nunca deve ser apresentado como exato.

## Período do dia

- madrugada: `00:00:00–05:59:59`;
- manhã: `06:00:00–11:59:59`;
- tarde: `12:00:00–17:59:59`;
- noite: `18:00:00–23:59:59`.

## Estado operacional

Valores permitidos:

- `PROPOSTO`;
- `PLANEJADO`;
- `TENTADO`;
- `EXECUTADO`;
- `VERIFICADO`;
- `BLOQUEADO`;
- `CORRIGIDO`.

A timeline registra o estado observável do evento; o estado normativo da decisão permanece em `governance/DECISION-REGISTER.md`.

## Vínculos obrigatórios

Quando disponíveis, a entrada deve apontar para:

- IDs `DEC-*`;
- commits;
- PRs;
- issues ou tarefas;
- testes;
- deployments;
- documentos canônicos.

## Filtro mínimo de privacidade

Nunca registrar:

- senhas, tokens, chaves ou segredos;
- dados bancários ou financeiros sensíveis;
- mensagens privadas integrais sem necessidade operacional;
- documentos pessoais ou identificadores pessoais sem finalidade legítima;
- dados de saúde, localização precisa ou informações familiares sem necessidade explícita;
- conteúdo sensível que possa ser substituído por resumo operacional.

Ao detectar conteúdo sensível, resumir, mascarar ou bloquear o registro. A timeline deve registrar que houve filtragem, sem reproduzir o dado removido.

## Frequência de atualização

- uma atualização lógica por mensagem ou evento relevante;
- quando o conector exigir, um commit por atualização;
- integrações futuras podem agrupar commits tecnicamente, desde que preservem IDs, ordem e granularidade lógica.

## Normalização de entradas legadas

Entradas antigas não são reescritas silenciosamente. A remediação ocorre por bloco complementar contendo:

- novo ID estável;
- precisão temporal;
- origem e conversa;
- estado operacional;
- decisões e evidências conhecidas;
- referência textual à entrada original.

## Fechamento diário

No fim do dia, criar uma entrada `DAILY-CLOSE` com:

1. itens `VERIFICADO` ou `EXECUTADO`;
2. pendências ativas;
3. bloqueios e condições de retomada;
4. divergências entre timeline, decisões, PRs e tarefas;
5. primeira ação recomendada para o próximo dia;
6. cobertura e lacunas do dia.

O fechamento não transforma automaticamente pendências em concluídas.

## Falha de atualização

Quando a gravação falhar:

1. não declarar registro concluído;
2. informar a falha;
3. manter pendência de sincronização;
4. tentar novamente somente com estado e SHA atualizados;
5. registrar a recuperação em nova entrada após sucesso.

## Gate de validação

A timeline somente poderá ser universalizada quando:

- o esquema estiver aplicado;
- entradas legadas tiverem complemento de normalização;
- testes de idempotência, privacidade, horário, origem e fechamento passarem;
- decisões e evidências estiverem vinculadas;
- a cobertura global real estiver implementada ou sua limitação continuar explícita;
- uma RC independente aprovar a estrutura.
