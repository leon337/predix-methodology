# Timeline Geral PREDIX

Índice cronológico das conversas, decisões, ações e evidências registradas pela metodologia PREDIX.

## Regras principais

- **Fuso oficial:** `America/Recife` (`UTC-03:00`).
- **Granularidade:** data e horário local, preferencialmente até segundos quando disponíveis.
- **Precisão temporal:** `exata`, `aproximada` ou `inferida`.
- **Períodos:** madrugada, manhã, tarde e noite.
- **Origem:** cada entrada identifica chat normal ou projeto.
- **Projeto:** o nome é obrigatório quando a origem for projeto e estiver disponível.
- **Identificador:** cada entrada usa `TL-AAAAMMDD-HHMMSS-NNN`.
- **Idempotência:** cada evento lógico possui chave estável para impedir duplicidade.
- **Estado operacional:** `PROPOSTO`, `PLANEJADO`, `TENTADO`, `EXECUTADO`, `VERIFICADO`, `BLOQUEADO` ou `CORRIGIDO`.
- **Histórico:** append-only; correções não apagam registros anteriores.
- **Privacidade:** segredos e conteúdo sensível desnecessário não devem ser registrados.
- **Cobertura:** arquivos de backfill podem ser parciais e devem declarar seus limites.
- **Fechamento diário:** deve reconciliar executados, pendentes, bloqueios, divergências e próxima retomada.

O esquema canônico provisório está em [`timeline/SCHEMA.md`](timeline/SCHEMA.md).

## Índice por data

| Data | Dia | Cobertura | Arquivo |
|---|---|---|---|
| 2026-07-23 | quinta-feira | backfill parcial do contexto disponível | [`timeline/2026/07/2026-07-23.md`](timeline/2026/07/2026-07-23.md) |
| 2026-07-24 | sexta-feira | backfill parcial do contexto disponível | [`timeline/2026/07/2026-07-24.md`](timeline/2026/07/2026-07-24.md) |
| 2026-07-25 | sábado | backfill parcial do contexto disponível | [`timeline/2026/07/2026-07-25.md`](timeline/2026/07/2026-07-25.md) |
| 2026-07-26 | domingo | registro ativo do projeto Fábrica de softwares | [`timeline/2026/07/2026-07-26.md`](timeline/2026/07/2026-07-26.md) |

## Eventos estruturados recentes

- [`TL-20260726-155608-016`](timeline/2026/07/events/TL-20260726-155608-016.md) — TL-005, integração normativa, mergeability, RC e Cultura.
- [`TL-20260726-161353-017`](timeline/2026/07/events/TL-20260726-161353-017.md) — decisões da rodada 1 da Cultura PREDIX.

## Consulta temporal

Exemplos de perguntas que a estrutura deverá responder:

- O que foi decidido no domingo de manhã?
- Quais decisões foram tomadas no domingo à tarde?
- O que aconteceu no projeto Fábrica de softwares durante a semana?
- Quais ações foram aprovadas provisoriamente, mas ainda não validadas?
- O que foi executado de verdade e quais itens permaneceram apenas conceituais?
- Quais decisões ficaram bloqueadas e qual é o gatilho de retomada?

## Integração global

O plano para capturar conversas de projetos e chats normais está em:

- [`timeline/GLOBAL-INGESTION-PLAN.md`](timeline/GLOBAL-INGESTION-PLAN.md)

## Estado

- **Branch de trabalho:** `mop/timeline-conversas-20260726`.
- **Main:** ainda não alterada.
- **Esquema:** `0.2-provisório`.
- **Validação definitiva:** pendente de execução dos testes e RC independente.
- **Cobertura global real:** ainda não implementada.
