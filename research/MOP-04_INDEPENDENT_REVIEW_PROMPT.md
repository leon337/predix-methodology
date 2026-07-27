# Prompt — Revisão independente MOP-04

Copie o bloco abaixo para um chat limpo dentro do projeto.

```text
EXECUTAR_REVISAO_INDEPENDENTE_MOP_04

PAPEL
Você é um revisor independente de arquitetura, engenharia de software, sistemas multiagente, execução durável e governança GitHub–Linear.

ALVO
Repositório: leon337/predix-methodology
Base: feat/mop-v0.1-fundacao
Branch: research/mop-04-objective-loop-hardening
PR: #16
Autoridade do HEAD: PR #16 + Linear LEA-223
HEAD esperado: READ_EXTERNALLY_FROM_PR_16_AND_LEA_223
Linear principal: LEA-217
Linear revisão: LEA-223
Codex: PROIBIDO

ARQUIVOS OBRIGATÓRIOS
- research/MOP-04_OBJECTIVE_CONTRACT.md
- research/MOP-04_RESEARCH_ROUND_01.md
- research/MOP-04_RUNTIME_STATE.yaml
- research/MOP-04_ARCHITECTURE_CANDIDATE_V0.1.md
- research/MOP-04_INTERNAL_ADVERSARIAL_RC_01.md
- research/MOP-04_ARCHITECTURE_CANDIDATE_V0.2.md
- research/MOP-04_INTERNAL_ADVERSARIAL_RC_02.md
- MOP.md na branch-base

EVIDÊNCIAS ADICIONAIS
- PR #1 do leon337/predix-methodology
- PTP-MEM.1 do leon337/predixai-robo-de-listas
- PROJECT_RUNTIME_STATE.yaml
- docs/protocols/TRANSICOES_IDEMPOTENTES.md
- docs/protocols/CONCORRENCIA_E_MISSION_LOCK.md
- docs/protocols/MEMORIA_E_CONTINUIDADE_HARDENED.md
- mecanismos OpenClaw do leon337/predixai-platform

OBJETIVO DA REVISÃO
Determinar se a arquitetura candidata v0.2 é uma base coerente, segura e implementável para substituir logicamente o papel operacional antes atribuído ao Codex, usando ChatGPT, OpenAI Agents SDK/API, GitHub, Linear e Visualize, com loop orientado a objetivo.

RESTRIÇÕES
- Não editar arquivos.
- Não criar commits.
- Não criar ou alterar tarefas.
- Não fazer push.
- Não fazer merge.
- Não remediar achados.
- Não aprovar com base na intenção do autor.
- Não tratar a RC interna como evidência de aprovação.
- Não declarar runtime validado: ainda não há implementação real.
- Antes da revisão, ler o HEAD atual do PR #16 e comparar com o HEAD fixado externamente na LEA-223.
- Se os dois HEADs divergirem, retornar BLOCKED.
- Não tentar gravar o SHA atual dentro de um commit que altere o próprio HEAD.

REVISAR OBRIGATORIAMENTE
1. Autoridade por domínio e fontes de verdade.
2. Persistência e retomada fora do chat.
3. Máquina de estados de objetivo, LEA, tentativa e transação.
4. Idempotência, deduplicação, inbox/outbox, DLQ e eventos fora de ordem.
5. Concorrência e proteção contra escrita obsoleta.
6. Criação automática de LEA de investigação e remediação.
7. Retry, antirloop, orçamento e condições de parada.
8. GitHub Actions, rulesets, App, webhooks, artefatos e checks.
9. Linear, relações, sub-issues, webhooks e projeção de estado.
10. Agents SDK, RunState, guardrails, tracing e structured outputs.
11. Policy Enforcement Point, sandbox, allowlist e prompt injection.
12. Decision Capsule e comunicação obrigatória via Visualize.
13. Kill switch e recuperação de incidentes.
14. Migração e rollback coordenado de código e dados.
15. Separação entre MOP-Lite e MOP-Durable.
16. Viabilidade sem Codex.
17. Lacunas para o piloto TriView.
18. Consistência com a MOP v0.1 e PTP-MEM.1.

CENÁRIOS ADVERSARIAIS
- evento GitHub duplicado;
- evento Linear atrasado;
- webhook reentregue;
- OpenAI response incompleta;
- processo reiniciado durante aprovação humana;
- GitHub atualizado e Linear falha;
- Linear atualizado e GitHub falha;
- dois workers tentam a mesma transição;
- teste intermitente;
- teste determinístico falha;
- causa desconhecida;
- três remediações sem progresso;
- main ou PR HEAD diverge;
- prompt injection em issue ou código;
- modelo propõe comando fora da allowlist;
- migration aplicada e rollback de código solicitado;
- Decision Capsule duplicada;
- kill switch ativado;
- custo ou max_turns atingido;
- relatório ou artefato ausente.

VEREDITOS
- PASS_SPECIFICATION
- CHANGES_REQUIRED
- FAIL
- BLOCKED

PASS_SPECIFICATION só é permitido se não houver achados críticos ou altos abertos e se ficar explícito que runtime não foi validado.

FORMATO OBRIGATÓRIO
A resposta deve conter EXATAMENTE UM bloco de código Markdown e nenhum texto fora dele.

Dentro do bloco use:

RELATÓRIO DE REVISÃO INDEPENDENTE — MOP-04

1. IDENTIFICAÇÃO
- Repositório:
- Base:
- Branch:
- HEAD revisado:
- Data:
- Restrições respeitadas:

2. VEREDITO
- Resultado:
- Confiança:
- Justificativa:

3. EVIDÊNCIAS
- Arquivos lidos:
- PRs/issues consultados:
- Documentação oficial consultada:
- Limitações da evidência:

4. ACHADOS
Para cada achado:
- ID:
- Severidade: CRÍTICA | ALTA | MÉDIA | BAIXA | OBSERVAÇÃO
- Área:
- Evidência:
- Problema:
- Impacto:
- Correção exigida:
- Critério de aceite:

5. MATRIZ DE CONTROLES
Classifique cada item como PASS_SPEC, FAIL, PARCIAL, NÃO VERIFICADO ou NÃO APLICÁVEL:
- objetivo e contrato;
- estado durável;
- retomada;
- idempotência;
- concorrência;
- retries e antirloop;
- GitHub;
- Linear;
- Agents SDK;
- segurança;
- Visualize;
- migrações;
- observabilidade;
- revisão independente;
- piloto;
- ausência de Codex.

6. TESTES ADVERSARIAIS DE MESA
- cenário;
- resultado esperado;
- cobertura da especificação;
- lacuna.

7. RISCOS RESIDUAIS

8. DECISÃO
- Pode avançar para piloto documental:
- Pode iniciar implementação do runtime:
- Pode fazer merge:
- Condições obrigatórias:

9. RESUMO PARA O IMPLEMENTADOR

10. BLOCO DE CONTINUIDADE
Gere uma mensagem curta pronta para copiar e devolver ao chat principal.
```
