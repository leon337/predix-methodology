# Metodologia Operacional PREDIX — MOP

Fonte oficial candidata da metodologia de trabalho da PREDIX AI BR enquanto a versão integrada permanece em validação.

## Finalidade

A MOP transforma ideias em produtos digitais por meio de um fluxo padronizado, rastreável e progressivamente automatizado, preservando três recursos críticos:

- tempo e atenção do fundador;
- qualidade e rastreabilidade das entregas;
- conhecimento operacional reutilizável.

## Princípio central

> Cada resposta, decisão, documento e implementação deve aumentar a capacidade operacional da PREDIX, e não apenas resolver o momento atual.

## Papéis

### Leo

- define visão, problemas, prioridades e critérios de valor;
- valida decisões de produto e resultados no ambiente real;
- aprende durante a execução, sem depender de programação manual.

### IA e agentes

- refinam ideias e requisitos;
- propõem arquitetura e MVP;
- planejam, implementam, testam e documentam;
- preparam candidatos isolados para validação;
- explicam decisões com analogias ligadas a operações, redes, indústria e gestão.

## Fontes de verdade

- **CULTURA.md:** camada constitucional candidata;
- **MOP.md:** método operacional subordinado à Cultura;
- **governance/GUARDRAILS.md:** limites comportamentais e reações;
- **governance/RECOVERY.md:** restauração de estado;
- **GitHub:** histórico, versões, evidências e candidatos;
- **Linear:** planejamento, tarefas, dependências e estado operacional;
- **Chats:** discussão e execução corrente; não substituem a documentação oficial;
- **Timeline:** contexto temporal, decisões, execuções, evidências e retomadas;
- **Registro de decisões:** estado canônico das decisões e pendências.

## Arquitetura documental em validação

```text
Cultura e Constituição candidata da PREDIX
                ↓
Metodologia Operacional PREDIX — MOP
                ↓
Guardrails e Recuperação
                ↓
Procedimentos Operacionais Padrão — POPs
                ↓
Registro de decisões e pendências
                ↓
Timeline, evidências e execução dos projetos
```

## Estrutura principal da branch integrada

```text
predix-methodology/
├── CULTURA.md
├── MOP.md
├── README.md
├── TIMELINE.md
├── governance/
│   ├── ARCHITECTURE.md
│   ├── DECISION-REGISTER.md
│   ├── GUARDRAILS.md
│   ├── RECOVERY.md
│   ├── INTEGRATION-STATUS.md
│   ├── reviews/
│   └── tests/
├── tools/
├── tests/
└── timeline/
```

Novos documentos somente serão criados quando houver ganho operacional comprovado, responsabilidade definida e fonte canônica clara.

## Continuidade obrigatória

Nenhuma decisão pendente pode desaparecer por mudança de assunto. Toda decisão relevante deve ser concluída, rejeitada, substituída, bloqueada com condição de retomada ou preservada na fila de pendências.

## Estado atual

- Repositório iniciado em 25 de julho de 2026.
- Branch candidata integrada: `integration/mop-governance-v0.1`.
- `CULTURA.md` está em `0.4-draft`; não é Constituição final aprovada.
- `MOP.md`, arquitetura, guardrails e recuperação foram reunidos na branch integrada.
- Guardrails v0.4 continuam provisórios.
- Scanner TL-010 foi corrigido para cobrir segredos genéricos com `#` e recebeu regressões específicas.
- FA-008 e FA-009 foram reconciliados cronologicamente; FA-009 recebeu reteste manual multigrupo no cliente atual.
- O runner R6 invalida evidência manual antiga quando uma regressão posterior não foi retestada.
- A bateria integral deve ser reexecutada sobre um HEAD congelado exato após esta reconciliação.
- A análise feita no mesmo contexto é apenas pré-revisão interna/adversarial, não RC independente.
- A RC independente exige outra sessão, agente ou revisor e permanece pendente.
- Instrução global, promoção e merge continuam bloqueados.
- Nenhum merge desta branch na `main` foi realizado.
