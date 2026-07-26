# Pacote de Decisão — Cultura e Constituição PREDIX

## Estado

- **Versão:** `0.1-candidata`.
- **Autoridade final:** Leo.
- **Status:** recomendações para decisão; nada neste documento está aprovado como Cultura definitiva.
- **Documento final:** `CULTURA.md`, bloqueado até decisões explícitas e RC independente.

## Recomendação da IA

Adotar uma Cultura curta, observável e ligada ao funcionamento real da Fábrica de Softwares. Evitar valores genéricos que não possam ser verificados no comportamento dos agentes, documentos e produtos.

## Propósito candidato

> Democratizar o acesso a software e inteligência artificial úteis, transformando ideias e problemas reais em soluções compreensíveis, seguras e operacionalmente sustentáveis.

### Motivo

A PREDIX não existe apenas para produzir código. O valor está em permitir que pessoas e organizações, inclusive sem formação técnica profunda, consigam transformar necessidades em sistemas reais.

### Risco

O propósito pode ficar amplo demais. A futura versão deverá decidir público prioritário e alcance geográfico.

## Missão candidata

> Projetar, construir e evoluir sistemas, aplicativos e agentes de IA com autonomia controlada, evidências verificáveis, explicação acessível e responsabilidade sobre resultados.

### Comportamentos observáveis

- recomendar a melhor opção sem retirar a decisão de Leo;
- distinguir proposta, tentativa, execução e verificação;
- proteger dados e autorizações;
- manter decisões pendentes rastreadas;
- entregar software utilizável, não apenas documentação convincente.

## Visão candidata

> Tornar a PREDIX uma referência brasileira em fábricas de software assistidas por IA, capazes de atender pequenos negócios, operações locais e projetos complexos com qualidade, velocidade e rastreabilidade.

### Horizonte ainda aberto

A visão precisa de prazo e foco de mercado antes da aprovação definitiva.

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

## Público prioritário — recomendação provisória

Priorizar, nesta ordem:

1. pequenos negócios e empresas locais com problemas operacionais concretos;
2. equipes e profissionais que precisam de automação sem possuir equipe técnica própria;
3. projetos internos e produtos escaláveis da própria PREDIX;
4. clientes maiores quando houver capacidade operacional e governança compatíveis.

Esta ordem é candidata e precisa de decisão de Leo.

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

## Perguntas obrigatórias para Leo

1. O propósito candidato representa a transformação que você deseja produzir?
2. Pequenos negócios e operações locais devem ser o público inicial prioritário?
3. A visão deve ter horizonte de três, cinco ou dez anos?
4. Quais dos dez valores candidatos são inegociáveis?
5. Existe algum princípio que você rejeita ou deseja reescrever?
6. A PREDIX deve assumir compromisso explícito com desenvolvimento local e acessibilidade?
7. Que tipo de projeto a empresa não deve aceitar, mesmo sendo lucrativo?
8. Quais decisões você quer manter sempre sob sua autoridade pessoal?

## Próximo gate

1. Leo responde ou ajusta as perguntas obrigatórias;
2. os valores candidatos são classificados como aprovados, rejeitados ou em revisão;
3. conflitos com MOP e guardrails são mapeados;
4. cria-se uma primeira minuta de `CULTURA.md` em branch isolada;
5. RC independente revisa a minuta;
6. somente depois ocorre aprovação e derivação da instrução global.
