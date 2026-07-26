# Timeline Geral PREDIX

Índice cronológico das conversas, decisões, ações e evidências registradas pela metodologia PREDIX.

## Regras principais

- **Fuso oficial:** `America/Recife` (`UTC-03:00`).
- **Granularidade:** data e horário local, preferencialmente até segundos quando disponíveis.
- **Períodos:** madrugada, manhã, tarde e noite.
- **Origem:** cada entrada identifica chat normal ou projeto.
- **Projeto:** o nome é obrigatório quando a origem for projeto e estiver disponível.
- **Histórico:** append-only; correções não apagam registros anteriores.
- **Privacidade:** segredos não devem ser registrados.
- **Cobertura:** arquivos de backfill podem ser parciais e devem declarar seus limites.

## Índice por data

| Data | Dia | Cobertura | Arquivo |
|---|---|---|---|
| 2026-07-23 | quinta-feira | backfill parcial do contexto disponível | [`timeline/2026/07/2026-07-23.md`](timeline/2026/07/2026-07-23.md) |
| 2026-07-24 | sexta-feira | backfill parcial do contexto disponível | [`timeline/2026/07/2026-07-24.md`](timeline/2026/07/2026-07-24.md) |
| 2026-07-25 | sábado | backfill parcial do contexto disponível | [`timeline/2026/07/2026-07-25.md`](timeline/2026/07/2026-07-25.md) |
| 2026-07-26 | domingo | registro ativo do projeto Fábrica de softwares | [`timeline/2026/07/2026-07-26.md`](timeline/2026/07/2026-07-26.md) |

## Consulta temporal

Exemplos de perguntas que a estrutura deverá responder:

- O que foi decidido no domingo de manhã?
- Quais decisões foram tomadas no domingo à tarde?
- O que aconteceu no projeto Fábrica de softwares durante a semana?
- Quais ações foram aprovadas provisoriamente, mas ainda não validadas?
- O que foi executado de verdade e quais itens permaneceram apenas conceituais?

## Integração global

O plano para capturar conversas de projetos e chats normais está em:

- [`timeline/GLOBAL-INGESTION-PLAN.md`](timeline/GLOBAL-INGESTION-PLAN.md)

## Estado

- **Branch de trabalho:** `mop/timeline-conversas-20260726`.
- **Main:** ainda não alterada.
- **Validação definitiva:** pendente de testes e revisão.
