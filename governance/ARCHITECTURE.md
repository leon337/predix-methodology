# Arquitetura de Governança Documental da PREDIX

## Estado

- **Status:** proposta operacional autorizada no Fluxo Assistido.
- **Branch:** `mop/timeline-conversas-20260726`.
- **Main:** não alterada.
- **Validação:** pendente de testes, RC independente e aprovação explícita de Leo.

## Objetivo

Separar princípios permanentes, metodologia geral, procedimentos repetíveis, decisões e evidências temporais, evitando duplicidade, contradição e abandono silencioso de assuntos.

## Hierarquia

```text
Cultura e Constituição da PREDIX
                ↓
Metodologia Operacional PREDIX — MOP
                ↓
Procedimentos Operacionais Padrão — POPs
                ↓
Registro de decisões e pendências
                ↓
Timeline, evidências e execução dos projetos
```

## 1. Cultura e Constituição da PREDIX

### Finalidade

Define a identidade organizacional e as regras superiores que não devem mudar a cada projeto.

### Conteúdo permitido

- missão, visão e princípios;
- valores e comportamento esperado;
- autoridade de Leo e limites de autonomia da IA;
- hierarquia de fontes de verdade;
- regras inegociáveis de segurança, honestidade, evidência e responsabilidade;
- critérios para alterar a própria governança.

### Conteúdo proibido

- passos detalhados de deploy;
- comandos específicos de ferramentas;
- procedimentos temporários de um projeto;
- decisões pontuais que pertencem ao registro de decisões.

### Fonte canônica futura

Um documento separado, provisoriamente chamado `CULTURA.md`, somente deverá ser criado após definição e aprovação explícita de seu conteúdo.

## 2. Metodologia Operacional PREDIX — MOP

### Finalidade

Define como a fábrica transforma ideias em produtos, coordena agentes, trata riscos, valida resultados e preserva conhecimento.

### Conteúdo permitido

- ciclo de produto e engenharia;
- papéis e responsabilidades;
- modos autônomo, assistido e assistido recomendado;
- níveis de risco e autorização;
- critérios de entrada, saída, aceite e evidência;
- relação entre GitHub, Linear, Vercel, Supabase, chats e demais ferramentas;
- regras de continuidade, reconciliação e revisão independente.

### Regra de autoridade

A MOP deve respeitar a Cultura/Constituição. Nenhum POP pode contrariar a MOP.

## 3. Procedimentos Operacionais Padrão — POPs

### Finalidade

Descrever como executar uma atividade específica, repetível e suficientemente estável.

### Exemplos

- atualizar a timeline;
- revisar um pull request;
- realizar deploy em staging;
- preparar release;
- tratar incidente;
- executar migration;
- reconciliar GitHub, Linear, Vercel e Supabase.

### Estrutura mínima de um POP

1. objetivo;
2. gatilho de início;
3. pré-condições;
4. responsáveis;
5. ferramentas;
6. passos;
7. guardrails;
8. evidências obrigatórias;
9. critérios de conclusão;
10. rollback ou recuperação;
11. versão e histórico de alterações.

### Critério de criação

Um POP somente deve ser criado quando o procedimento:

- ocorrer mais de uma vez ou tiver alta probabilidade de repetição;
- exigir consistência entre agentes ou projetos;
- possuir risco, dependências ou evidências relevantes;
- produzir ganho operacional maior que seu custo de manutenção.

## 4. Registro de decisões e pendências

### Finalidade

Preservar o estado de cada decisão, inclusive quando o assunto mudar.

### Estados válidos

- `ATIVA`;
- `PENDENTE`;
- `BLOQUEADA`;
- `APROVADA_PROVISORIAMENTE`;
- `APROVADA`;
- `REJEITADA`;
- `SUBSTITUIDA`;
- `CONCLUIDA`.

### Campos mínimos

- identificador;
- data e horário;
- origem e projeto;
- decisão ou pergunta;
- estado;
- responsável;
- evidência;
- condição de retomada;
- relação com outras decisões.

## 5. Timeline e evidências

### Finalidade

Registrar quando uma conversa, decisão, execução, correção ou bloqueio ocorreu.

A timeline não substitui documentos normativos nem o registro de decisões. Ela preserva contexto temporal e aponta para as fontes canônicas.

## Regras de precedência

Quando houver conflito:

1. segurança, leis e políticas aplicáveis;
2. Cultura/Constituição aprovada;
3. MOP aprovada;
4. POP vigente;
5. decisão específica válida;
6. plano ou tarefa atual;
7. conversa corrente.

O conflito deve ser exposto; nenhuma camada inferior pode substituir silenciosamente uma superior.

## Regra de continuidade

Nenhuma decisão pendente pode desaparecer por mudança de assunto. Ela deve ser:

- concluída;
- explicitamente rejeitada;
- substituída por outra decisão vinculada;
- bloqueada com condição de retomada;
- ou mantida na fila de pendências.

## Evolução documental

Toda mudança normativa relevante deve:

1. identificar a camada afetada;
2. apresentar motivo e impacto;
3. verificar conflitos;
4. atualizar decisões e timeline;
5. passar por revisão proporcional ao risco;
6. permanecer fora da `main` até aprovação explícita quando classificada como crítica.
