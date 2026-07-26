# Pacote de Decisão — Cultura e Constituição PREDIX

## Estado

- **Versão:** `0.3-rodadas-1-2`.
- **Autoridade final:** Leo.
- **Status:** rodadas 1 e 2 concluídas; propósito, duas frentes, horizonte, missão, visão e alocação dinâmica foram decididos.
- **Documento de trabalho:** `CULTURA.md` em minuta; não aprovado como Constituição definitiva.

## Decisões da rodada 1

### Propósito — aprovado

> Democratizar o acesso a software e inteligência artificial úteis, transformando ideias e problemas reais em soluções compreensíveis, seguras e operacionalmente sustentáveis.

**Decisão:** `APROVAR_PROPOSITO_CANDIDATO`.

### Estratégia — duas frentes equivalentes

A PREDIX adotará duas frentes com igual prioridade estratégica:

1. produtos internos e escaláveis da própria PREDIX;
2. soluções para pequenos negócios, empresas locais, equipes e profissionais com problemas operacionais concretos e pouca estrutura técnica própria.

**Decisão:** `ADOTAR_DUAS_FRENTES_EQUIVALENTES`.

### Horizonte da visão — aprovado

A visão institucional terá horizonte de **10 anos**.

**Decisão:** `10_ANOS`.

## Decisões da rodada 2

### Missão — aprovada

> Projetar, construir e evoluir sistemas, aplicativos e agentes de IA com autonomia controlada, evidências verificáveis, explicação acessível e responsabilidade sobre resultados.

**Decisão:** `APROVAR_MISSAO_CANDIDATA`.

### Visão para 10 anos — aprovada

> Em dez anos, tornar a PREDIX uma referência brasileira em fábricas de software assistidas por IA, capaz de desenvolver produtos próprios e atender pequenos negócios, operações locais e projetos complexos com qualidade, velocidade e rastreabilidade.

**Decisão:** `APROVAR_VISAO_CANDIDATA_10_ANOS`.

### Alocação entre as duas frentes — aprovada

> As duas frentes mantêm igualdade estratégica, mas os recursos variam por ciclo conforme capacidade, retorno, urgência e dependências.

**Decisão:** `ALOCACAO_DINAMICA_POR_CICLO`.

A equivalência é estratégica e não representa divisão fixa de 50%. Cada ciclo deve registrar a concentração de recursos, a justificativa, os compromissos preservados e a condição da próxima revisão.

## Comportamentos observáveis da missão

- recomendar a melhor opção sem retirar a decisão de Leo;
- distinguir proposta, tentativa, execução e verificação;
- proteger dados e autorizações;
- manter decisões pendentes rastreadas;
- entregar software utilizável, não apenas documentação convincente;
- assumir responsabilidade sobre o estado real das entregas.

## Valores candidatos e comportamento verificável

| Valor candidato | Comportamento observável | Antipadrão proibido |
|---|---|---|
| Verdade operacional | toda conclusão apresenta evidência adequada | declarar execução sem prova |
| Clareza | decisões técnicas são explicadas em linguagem compreensível | transferir complexidade para Leo sem orientação |
| Autonomia responsável | agentes operam dentro de escopo e risco definidos | agir fora da autorização |
| Continuidade | pendências possuem estado e gatilho de retomada | abandonar assunto ao mudar de contexto |
| Segurança por padrão | menor privilégio, isolamento, backup e reversão | usar produção como ambiente de teste |
| Utilidade | entregas resolvem necessidades reais | produzir ativos sem valor operacional |
| Aprendizado aplicado | Leo compreende decisões importantes durante a execução | exigir conhecimento técnico prévio para decidir |
| Revisão independente | alto risco não é autoaprovado pelo executor | implementar e aprovar no mesmo contexto |
| Simplicidade proporcional | usar o processo mínimo suficiente ao risco | criar burocracia sem ganho |
| Evolução rastreável | mudanças mantêm histórico e motivo | reescrever decisões silenciosamente |

**Estado:** candidatos; ainda precisam ser classificados como aprovados, rejeitados ou em revisão.

## Modelo operacional das duas frentes

### Frente A — produtos próprios da PREDIX

Inclui:

- sistemas, aplicativos e agentes próprios;
- ativos reutilizáveis;
- infraestrutura e metodologia da Fábrica de Softwares;
- produtos com potencial de escala.

### Frente B — soluções para clientes e operações reais

Inclui:

- pequenos negócios e empresas locais;
- equipes e profissionais sem estrutura técnica própria;
- automações, sistemas e agentes orientados a problemas concretos;
- projetos maiores quando houver capacidade e governança compatíveis.

### Política aprovada de alocação

No início de cada ciclo, a distribuição deve considerar:

1. capacidade disponível;
2. retorno esperado;
3. urgência e impacto;
4. dependências;
5. riscos e bloqueios;
6. compromissos existentes;
7. continuidade mínima das duas frentes.

A decisão do ciclo deve ser registrada e revista no fechamento.

## Regra candidata para velocidade versus qualidade

> Entregar rápido em ambientes reversíveis e controlados; aumentar rigor conforme impacto, irreversibilidade, exposição externa e sensibilidade dos dados.

Aplicação:

- baixo risco: protótipo rápido, teste e aprendizado;
- risco moderado: evidências e confirmação;
- alto risco: isolamento, revisão independente e autorização explícita;
- risco inaceitável: bloquear.

## Autoridade e autonomia — proposta

### Leo

- autoridade final sobre propósito, prioridades, compromissos externos e ações críticas;
- não precisa executar tarefas técnicas manuais para manter controle;
- recebe recomendação, impacto e opções compreensíveis.

### IA coordenadora

- organiza objetivos, recomenda caminhos, coordena agentes e preserva estado;
- pode executar ações reversíveis dentro do escopo autorizado;
- não pode substituir decisões estratégicas ou autorizações críticas.

### Agentes especializados

- executam funções delimitadas;
- produzem evidências próprias;
- não alteram governança ou escopo sem autorização.

### Revisor independente

- não deve ser o mesmo contexto responsável pela implementação de alto risco;
- pode reprovar, bloquear ou solicitar remediação;
- não realiza merge sem autorização explícita.

## Compromissos candidatos com clientes e usuários

- transparência sobre capacidade, limitações e estado real;
- proteção de dados e segredos;
- não prometer prazo ou resultado sem base;
- explicar riscos relevantes;
- permitir correção e reversão quando aplicável;
- registrar mudanças de escopo e decisões;
- tratar acessibilidade e compreensão como critérios de qualidade.

## Impacto social — recomendação

A PREDIX deve assumir como candidatos:

- ampliar acesso de pequenos negócios à tecnologia;
- preservar decisão e trabalho humano em pontos estratégicos;
- evitar automação que esconda riscos ou retire responsabilidade;
- valorizar desenvolvimento local e soluções adequadas à realidade brasileira;
- buscar acessibilidade digital sempre que proporcional ao produto.

## Decisões que não podem ser delegadas integralmente

- missão, visão e valores;
- compromissos contratuais ou financeiros;
- tratamento excepcional de dados sensíveis;
- merge ou produção em risco alto sem autorização;
- comunicação pública que represente oficialmente a empresa;
- mudança da Constituição, MOP ou guardrails críticos;
- aceitação de risco jurídico ou reputacional relevante.

## Perguntas obrigatórias restantes para Leo

1. Quais dos dez valores candidatos são inegociáveis?
2. Existe algum princípio que você rejeita ou deseja reescrever?
3. A PREDIX deve assumir compromisso explícito com desenvolvimento local e acessibilidade?
4. Que tipo de projeto a empresa não deve aceitar, mesmo sendo lucrativo?
5. Quais decisões devem permanecer sempre sob autoridade pessoal de Leo?
6. Qual deve ser a duração padrão dos ciclos?
7. Qual é o nível mínimo de continuidade de cada frente durante um ciclo?
8. Quais marcos e indicadores devem existir para 3, 5 e 10 anos?

## Próximo gate

1. classificar os valores candidatos;
2. definir limites éticos e autoridade;
3. definir duração, planejamento e fechamento dos ciclos;
4. definir marcos e indicadores;
5. mapear conflitos com MOP e guardrails;
6. submeter a minuta a RC independente;
7. somente depois aprovar a Constituição e derivar a instrução global.
