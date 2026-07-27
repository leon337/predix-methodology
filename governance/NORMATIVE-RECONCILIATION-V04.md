# Reconciliação normativa — Cultura v0.4, MOP e Guardrails

## Estado

- **Data:** `2026-07-26`.
- **Branch:** `integration/mop-governance-v0.1`.
- **Cultura:** `CULTURA.md` v0.4-draft.
- **MOP:** `MOP.md` v0.1.0-draft.
- **Guardrails:** `governance/GUARDRAILS.md` v0.4-provisória.
- **Merge na `main`:** não autorizado e não realizado.
- **Resultado:** reconciliação semântica concluída para o candidato integrado; aprovação normativa final continua pendente.

## 1. Hierarquia aplicada

A precedência utilizada nesta branch é:

1. leis, políticas aplicáveis e segurança;
2. `CULTURA.md` v0.4-draft, como camada constitucional candidata;
3. `MOP.md`, como método operacional subordinado;
4. `governance/GUARDRAILS.md`, como catálogo de limites comportamentais e reações;
5. POPs vigentes;
6. decisões específicas válidas;
7. planos, tarefas, timeline e conversa corrente.

A Cultura ainda é uma minuta. A precedência acima serve para verificar coerência do candidato e não transforma o documento em Constituição final.

## 2. Relação entre Cultura e MOP

### Decisões exclusivas de Leo

A MOP afirma que Leo aprova decisões de produto, continuidade e correção. A Cultura v0.4 detalha dez grupos que jamais podem ser delegados integralmente.

**Resolução:**

- os dez grupos de `CULTURA.md` permanecem sob decisão final explícita de Leo;
- as demais operações podem ser delegadas conforme escopo, reversibilidade, N0–N4, guardrails e autorização válida;
- a MOP não pode ser interpretada de modo a criar autorização implícita ou retirar a autoridade exclusiva definida na Cultura.

### Ciclos operacionais

A MOP descreve o fluxo de produto e desenvolvimento, mas não fixa duração de ciclo.

**Resolução:**

- o ciclo padrão passa a ser interpretado como 28 dias;
- abertura, continuidade, replanejamento e fechamento seguem `CULTURA.md`;
- fluxos técnicos menores podem existir dentro do ciclo, desde que não apaguem o estado do ciclo principal.

### Duas frentes e alocação

A MOP é aplicável às duas frentes estratégicas:

1. produtos próprios da PREDIX;
2. soluções para clientes e operações reais.

**Resolução:** cada abertura de ciclo registra concentração de recursos, justificativa e continuidade de ambas as frentes. Não existe divisão fixa de 50%.

### Gate da instrução global

A MOP previa a derivação de uma instrução geral mínima como parte de sua aprovação. O registro de decisões e a Cultura exigem testes, reconciliação e RC antes dessa universalização.

**Resolução:** prevalece o gate mais seguro. A instrução global permanece bloqueada até:

- testes críticos suficientes;
- proteção de segredos e recuperação verificadas;
- RC independente;
- aprovação explícita de Leo;
- versão normativa identificada.

## 3. Relação entre Cultura e Guardrails

### Valores e grupos de guardrails

| Valor constitucional | Guardrails relacionados |
|---|---|
| verdade operacional | GR-005, GR-028 a GR-033 |
| clareza | GR-007, GR-008, GR-011, GR-019 |
| autonomia responsável | GR-006, GR-010, GR-020 a GR-027 |
| continuidade | GR-001 a GR-004, GR-044 a GR-049 |
| segurança por padrão | GR-020 a GR-027, GR-040 a GR-043 |
| utilidade | GR-001, GR-018, GR-039 |
| evolução rastreável | GR-003 a GR-005, GR-030, GR-046 a GR-049 |

Os valores revisáveis continuam operacionais nos contextos em que forem exigidos pela MOP ou pelos guardrails. Ser revisável não significa opcional em uma ação específica.

### Autoridade exclusiva

Os guardrails de autorização crítica devem bloquear qualquer tentativa de substituir Leo nos dez grupos exclusivos.

**Resolução:** silêncio, recomendação, comando genérico ou aprovação automática não constituem autorização.

### Recomendação no Fluxo Assistido

O defeito observado na rodada 3 mostrou que uma recomendação global não é suficiente quando existem vários grupos independentes.

**Resolução interpretativa:**

- quando cada grupo possuir uma recomendação técnica própria, a recomendação deve aparecer dentro do respectivo grupo;
- nenhuma recomendação pode vir previamente selecionada;
- dependências ou campos faltantes devem ser apresentados explicitamente;
- uma opção personalizada deve abrir a subdecisão necessária antes de gerar o comando final.

Essa interpretação reforça GR-007 a GR-019 e deve ser convertida em guardrail explícito ou teste de regressão antes da aprovação final.

## 4. Pontos sem conflito direto

Não foi identificado conflito semântico direto entre:

- a base ética constitucional estrita e os guardrails de segurança;
- o painel equilibrado de indicadores e os objetivos de utilidade, evidência e rastreabilidade da MOP;
- a alocação dinâmica e a obrigação de preservar pendências;
- os 28 dias de ciclo e o uso de branches, PRs, CI e candidatos isolados.

## 5. Lacunas ainda abertas

1. atualizar o texto principal da MOP para referenciar formalmente Cultura, guardrails, recuperação, registro de decisões e timeline;
2. corrigir em `governance/ARCHITECTURE.md` a descrição antiga que tratava `CULTURA.md` apenas como fonte futura;
3. transformar a regra de recomendação por grupo em teste de regressão;
4. criar linha de base e metas quantitativas;
5. decidir desenvolvimento local e acessibilidade;
6. executar os testes restantes do plano de 64 cenários;
7. executar RC independente sobre um HEAD estável.

## 6. Resultado da sincronização

A branch de integração recebeu:

- `CULTURA.md` v0.4-draft;
- `governance/CULTURE-ROUND-3-RESULT.md`;
- este relatório de reconciliação;
- estado de integração atualizado.

`governance/GUARDRAILS.md` já estava sincronizado com o mesmo blob da branch do PR #2. `MOP.md` foi preservado sem reescrita destrutiva; as resoluções deste documento funcionam como mapa de integração até a atualização textual controlada da MOP.

## 7. Gate

A reconciliação semântica não equivale a aprovação final. Permanecem bloqueados:

- merge na `main`;
- publicação da Constituição final;
- instrução global;
- ações externas ou críticas não autorizadas.
