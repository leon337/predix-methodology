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
│   ├── evidence/
│   ├── reviews/
│   └── tests/
├── tools/
├── tests/
└── timeline/
```

Novos documentos somente serão criados quando houver ganho operacional comprovado, responsabilidade definida e fonte canônica clara.

## Continuidade obrigatória

Nenhuma decisão pendente pode desaparecer por mudança de assunto. Toda decisão relevante deve ser concluída, rejeitada, substituída, bloqueada com condição de retomada ou preservada na fila de pendências.

## Estado atual pós-R6

- Repositório iniciado em 25 de julho de 2026.
- Branch candidata integrada: `integration/mop-governance-v0.1`.
- `CULTURA.md` está em `0.4-draft`; não é Constituição final aprovada.
- `MOP.md`, arquitetura, guardrails e recuperação estão reunidos na branch integrada.
- Guardrails v0.4 continuam provisórios.
- O candidato histórico R6 foi congelado na branch `test/governance-64-20260726-r6`, SHA `9cb5414412a562e17ee41759c5965343b5192220`, PR Draft `#9`.
- Os workflows R6 `30224913937` e `30224914038` concluíram com sucesso sobre o SHA exato.
- O artifact R6 `8638274889` registrou 64 cenários: 25 automatizados, 14 estáticos, 10 manuais e 15 simulados, sem `FAIL`, `BLOCKED` ou `NOT_RUN` naquele snapshot.
- A RC independente R6 foi concluída com `CHANGES_REQUIRED`, independência atendida, sem edição, remediação ou merge durante a revisão.
- Achados ativos da RC: reconciliação de estado canônico, obrigatoriedade do TL-005, invalidação cronológica genérica e artifact bruto completo.
- A remediação R7 está em andamento na branch integrada; o R6 permanece imutável como evidência histórica.
- O TL-005 R7 delimita eventos novos em `timeline/**/events/*.md`, exige ID e chave e proíbe YAML persistido nesta versão.
- A evidência FA-008/FA-009 passa a ser resolvida por eventos estruturados e ordem temporal; regressão posterior força `NOT_RUN` até novo reteste.
- O próximo artifact deve incluir logs brutos, scanner, TL-005, manifesto, hashes e resultados consolidados.
- Instrução global, promoção e merge continuam bloqueados.
- Nenhum merge da branch integrada ou do PR #9 na `main` foi realizado.
