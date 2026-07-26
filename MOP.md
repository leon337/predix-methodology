# Metodologia Operacional PREDIX — MOP

**Versão:** 0.1.0-draft  
**Estado:** fundação em revisão  
**Autoridade:** PREDIX AI BR  
**Fonte oficial:** `leon337/predix-methodology`

## 1. Objetivo

A MOP define como Leo, IAs, agentes e ferramentas transformam ideias em produtos digitais com:

- mínima intervenção manual desnecessária;
- máxima rastreabilidade;
- aprendizagem durante a execução;
- conhecimento operacional reutilizável;
- proteção das versões estáveis;
- evolução por testes e evidências.

A metodologia deve reduzir sobrecarga mental, retrabalho, repetição de contexto e consumo sem retorno de tempo, atenção e tokens.

## 2. Princípio de valor operacional

Cada resposta, decisão ou entrega deve ser avaliada por cinco perguntas:

1. Resolve o problema atual?
2. Produz conhecimento reutilizável?
3. Reduz trabalho futuro?
4. Preserva rastreabilidade e segurança?
5. Justifica o tempo, a atenção e os tokens consumidos?

Texto sem efeito operacional deve ser removido.

## 3. Papéis

### 3.1 Leo — fundador e validador

Responsável por:

- apresentar problemas, oportunidades e ideias;
- definir público, prioridade e resultado desejado;
- aprovar decisões de produto;
- testar candidatos no ambiente real;
- relatar resultados observáveis;
- decidir continuidade, correção ou encerramento.

Leo não precisa programar manualmente para operar a fábrica.

### 3.2 IA e agentes — equipe técnica de execução

Responsáveis por:

- interpretar o objetivo real;
- identificar requisitos, riscos e dúvidas críticas;
- separar MVP, futuras versões e itens fora do escopo;
- propor arquitetura e fluxo;
- planejar tarefas;
- implementar, testar, revisar e documentar;
- preparar candidatos isolados;
- explicar decisões durante a execução.

## 4. Método de ensino aplicado

Não presumir conhecimento profundo de programação, Git, GitHub, arquitetura ou engenharia de software.

Ao surgir um conceito relevante, explicar nesta sequência:

```text
O que aconteceu
→ O que significa
→ Analogia com redes, provedor, indústria, produção ou gestão
→ Risco evitado
→ Próxima ação
→ Regra reutilizável
```

A explicação deve aumentar a autonomia de decisão de Leo sem transferir para ele trabalho técnico desnecessário.

## 5. Contrato mínimo de contexto

Quando iniciar ou retomar uma frente, usar o menor endereço capaz de localizar o raciocínio correto:

```text
Projeto:
Fase ou momento:
Objetivo atual:
Referência opcional:
```

Exemplo:

```text
Projeto: TriView
Fase: V1 — testes sequenciais
Objetivo atual: testar a LEA-197
Referência: depois da reconciliação do trem LEA-197–205
```

Não exigir esse formato quando o contexto da conversa já for suficiente.

## 6. Tratamento de ambiguidades

Pontuação, acentuação ou digitação imperfeita não devem interromper o fluxo.

Antes de executar uma ação irreversível, distinguir:

- pergunta;
- proposta;
- hipótese;
- ordem de execução;
- aprovação explícita.

Quando a intenção estiver clara pelo contexto, prosseguir. Quando houver risco material, confirmar com uma pergunta objetiva.

## 7. Arquitetura das fontes de verdade

Cada ferramenta possui uma responsabilidade. Nenhuma delas deve ser tratada como fonte universal de tudo.

### GitHub

Fonte oficial de:

- metodologia aprovada;
- código e documentação técnica;
- histórico de mudanças;
- branches, commits, PRs e versões;
- esquemas, migrations e configurações que precisam ser reproduzíveis.

### Linear

Fonte oficial de:

- planejamento operacional;
- tarefas e dependências;
- prioridade e estado;
- critérios de aceitação;
- evidências e próximos passos.

### Vercel — quando adotada pelo projeto

Fonte operacional de:

- previews isolados de branches e PRs;
- publicação de aplicações web;
- estado dos deployments;
- domínio e ambiente de produção;
- logs e falhas relacionadas à implantação.

A Vercel não substitui o GitHub como fonte do código. Ela mostra **o que foi implantado e como está funcionando no ambiente publicado**.

Usar Vercel quando o produto precisar de frontend web, site, painel, API compatível ou preview acessível por link. Não exigir Vercel para aplicativos exclusivamente locais ou desktop, salvo decisão arquitetural específica.

### Supabase — quando adotado pelo projeto

Fonte operacional de:

- banco de dados gerenciado;
- autenticação e usuários;
- armazenamento de arquivos;
- políticas de acesso;
- funções de backend e recursos em tempo real, quando utilizados;
- estado operacional dos serviços de dados.

O Supabase não substitui o GitHub: migrations, esquemas, políticas e funções reproduzíveis devem permanecer versionados no repositório.

Usar Supabase quando o produto precisar de dados em nuvem, autenticação, armazenamento compartilhado, sincronização entre usuários ou backend gerenciado. Não adotar apenas por padrão quando armazenamento local ou uma arquitetura mais simples resolverem o problema.

### Chats

Espaço para:

- descoberta;
- debate;
- execução corrente;
- ensino aplicado;
- decisões ainda não formalizadas.

Chats não substituem as fontes oficiais. Conhecimento durável deve ser consolidado no local correto.

### Memória da plataforma

Reservada para preferências e princípios pessoais duráveis que mudem a forma de trabalhar em qualquer projeto.

Não usar memória para commits, branches, bugs, versões ou estados temporários.

## 8. Regra de documentação mínima

Começar com o menor número de documentos capaz de sustentar o trabalho.

Regra:

> Um novo documento somente nasce quando separar o conteúdo reduz claramente busca, conflito, manutenção ou risco.

Estrutura inicial da MOP:

```text
README.md
MOP.md
```

## 9. Fluxo padrão de produto

```text
IDEIA
→ PROBLEMA
→ PÚBLICO
→ RESULTADO ESPERADO
→ REQUISITOS
→ MVP
→ ARQUITETURA
→ RISCOS
→ PLANO NO LINEAR
→ IMPLEMENTAÇÃO NO GITHUB
→ PREVIEW OU BACKEND GERENCIADO, QUANDO APLICÁVEL
→ TESTES E CI
→ CANDIDATO ISOLADO
→ TESTE REAL POR LEO
→ CORREÇÃO OU APROVAÇÃO
→ VERSÃO ESTÁVEL
→ REUTILIZAÇÃO EM NOVOS PRODUTOS
```

A arquitetura decide se Vercel, Supabase, ambas ou nenhuma serão usadas. A ferramenta deve ser consequência do requisito, não ponto de partida obrigatório.

## 10. Fluxo de desenvolvimento

Para cada unidade de implementação:

```text
Tarefa no Linear
→ branch própria
→ commits rastreáveis
→ PR
→ CI
→ correção até PASS
→ preview ou validação de infraestrutura, quando aplicável
→ integração no trem ou branch de destino
→ candidato isolado
→ teste de aceite
→ atualização das fontes de verdade
```

### Regras

- não desenvolver diretamente na `main` sem exceção formal;
- não declarar conclusão apenas porque o código foi escrito;
- não ignorar falha de CI;
- não promover candidato sem identificação e isolamento;
- não misturar tarefas independentes na mesma branch sem justificativa;
- preservar possibilidade de retorno para versão estável;
- não publicar em produção sem identificar commit, branch ou versão correspondente;
- não alterar banco ou políticas críticas sem migration, evidência e estratégia de retorno quando aplicável.

## 11. Trem de desenvolvimento

O trem é uma linha intermediária que organiza múltiplas entregas antes da promoção para a versão estável.

Analogia:

- LEA/tarefa = vagão;
- branch = via de preparação;
- CI = inspeção;
- PR = pedido de acoplamento;
- merge = acoplamento;
- preview Vercel = área de demonstração do vagão antes da operação;
- ambiente Supabase = infraestrutura compartilhada de dados, quando necessária;
- trem = composição em validação;
- `main` = linha oficial em operação.

Se a ordem, o estado ou as fontes divergirem, executar reconciliação antes de continuar.

## 12. Reconciliação

Reconciliação é alinhar, quando aplicável:

- Linear;
- GitHub;
- branches;
- commits;
- PRs;
- CI;
- documentação;
- deployments e previews da Vercel;
- migrations, políticas e estado técnico do Supabase;
- candidatos instalados.

Procedimento:

1. identificar o estado real;
2. localizar a evidência técnica;
3. comparar código, planejamento, implantação e dados aplicáveis;
4. corrigir inconsistências;
5. repetir validações necessárias;
6. preservar entregas válidas;
7. atualizar todas as fontes de verdade;
8. somente então retomar a sequência.

## 13. Organização de chats e projetos

### Nova pasta de projeto

Criar quando existir produto, objetivo estratégico ou ciclo de vida próprio.

### Novo chat

Criar quando houver objetivo operacional claramente diferente, sem necessidade de carregar toda a conversa anterior.

### Chat fora de projeto

Pode ser usado para descoberta, aprendizado geral ou ideias ainda sem produto definido.

Quando a ideia ganhar continuidade, consolidar o contexto durável no projeto correto.

### Arquivamento e limpeza

Antes de excluir conversas relevantes:

1. identificar decisões, ativos e pendências;
2. consolidar somente o conteúdo durável;
3. registrar o estado no GitHub ou Linear;
4. arquivar ou excluir o ruído restante.

Excluir chats não substitui a consolidação.

## 14. Uso de imagens e prints

Usar print quando a informação depende de:

- interface;
- estado visual;
- erro exibido;
- configuração selecionada;
- disposição de elementos;
- sequência observada na tela.

Preferir texto quando nomes, logs ou valores puderem ser copiados com precisão.

## 15. Seleção de ferramentas

Usar a ferramenta pelo tipo de trabalho, não por hábito.

- **Chat:** descoberta, estratégia, ensino, decisões e coordenação.
- **GitHub:** código, documentação oficial, histórico, revisão e versionamento de infraestrutura reproduzível.
- **Linear:** planejamento, dependências, estado e critérios.
- **Vercel:** preview por branch/PR, deploy de aplicações web e observação do ambiente publicado.
- **Supabase:** banco, autenticação, armazenamento e backend gerenciado quando os requisitos justificarem.
- **Codex:** implementação ou revisão de código em repositórios quando disponível e apropriado.
- **Work ou execução prolongada:** tarefas extensas, auditorias e processamento de grande volume, conforme disponibilidade da plataforma.

### Regra de adoção

```text
Necessidade do produto
→ decisão de arquitetura
→ escolha da ferramenta
→ implementação versionada
→ validação
```

Nenhuma ferramenta é obrigatória apenas porque pertence ao conjunto padrão da fábrica.

Os nomes e capacidades das ferramentas podem mudar; a decisão deve seguir a função necessária.

## 16. Universalização da metodologia

A instrução geral da plataforma deve conter apenas os princípios universais e indicar que a MOP é a fonte operacional oficial quando estiver acessível.

Limite técnico:

> Um chat somente consegue consultar o repositório quando houver acesso ao GitHub ou quando o conteúdo relevante for fornecido no contexto.

Portanto, a universalização depende de três elementos:

1. princípios curtos na instrução geral;
2. MOP versionada no GitHub;
3. acesso ou referência suficiente para consultar a versão aplicável.

Nenhuma instrução deve fingir acesso automático inexistente.

## 17. Evolução da MOP

Mudanças na metodologia seguem o próprio processo:

```text
necessidade observada
→ proposta
→ branch
→ alteração da MOP
→ PR
→ revisão operacional
→ aprovação de Leo
→ merge
→ nova versão
```

A MOP não deve crescer por sugestão abstrata. Cada nova regra precisa responder a um problema real ou risco comprovado.

## 18. Critério de aprovação da versão 0.1

A versão 0.1 será considerada aprovada quando:

- Leo confirmar que representa sua forma de trabalhar;
- a ligação entre ChatGPT, GitHub, Linear, Vercel, Supabase e chats estiver operacionalmente clara;
- estiver claro que Vercel e Supabase são condicionais aos requisitos do projeto;
- a instrução geral mínima for derivada sem duplicar toda a MOP;
- o fluxo for aplicado em pelo menos uma retomada real de projeto;
- ajustes observados na prática forem incorporados.
