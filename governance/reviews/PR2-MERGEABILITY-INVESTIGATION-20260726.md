# Investigação do estado de mergeability do PR #2 — 2026-07-26

## Estado inicial observado

- **PR:** #2.
- **Base:** `main`.
- **Head:** `mop/timeline-conversas-20260726`.
- **PR em rascunho:** sim.
- **Campo `mergeable` inicial:** `false`.
- **Merge realizado:** não.

## Evidências iniciais

### Comparação com `main`

A comparação inicial do branch com `main` retornou:

- `status: ahead`;
- `ahead_by: 52`;
- `behind_by: 0`;
- merge base igual ao HEAD de `main`: `ef296e2b2404c6acf47676c01d224ae478e6e569`.

### CI inicial

No primeiro HEAD consultado não havia workflow run capaz de explicar o valor `mergeable: false`.

## Hipóteses iniciais

Os dados iniciais permitiam estas hipóteses, sem comprovação:

- conflito real não exposto pelo resumo;
- cálculo ainda não atualizado;
- normalização do conector;
- estado transitório do GitHub.

## Revalidação após implementação do TL-005

### Estado atualizado

- **HEAD revalidado:** `e0da5c73ddbed2ded88f679396eba9d4729d3b51`.
- **Campo `mergeable` atualizado:** `true`.
- **PR:** continua aberto e Draft.
- **Merge:** não realizado.

### Comparação atualizada

A comparação `main...mop/timeline-conversas-20260726` retornou:

- `status: ahead`;
- `ahead_by: 67`;
- `behind_by: 0`;
- merge base: `ef296e2b2404c6acf47676c01d224ae478e6e569`.

### CI atualizado

O workflow `Timeline validation` associado ao HEAD do TL-005 foi concluído com `success`.

### Tentativa de checkout limpo

Foi tentado um clone limpo em ambiente isolado antes da revalidação. A tentativa falhou antes de baixar o repositório porque o ambiente não conseguiu resolver `github.com` por DNS.

Esse erro:

- não demonstra conflito de merge;
- não demonstra falha do repositório;
- impede somente a confirmação local por `git merge --no-commit` nesta sessão.

## Conclusão atual

O bloqueio `mergeable: false` **não permanece reproduzido na API do GitHub**. O PR #2 agora é reportado como `mergeable: true`.

A causa exata do valor anterior continua não comprovada; a explicação mais compatível com as evidências é estado transitório ou cálculo desatualizado. Isso é uma inferência, não uma prova causal.

A verificação por checkout limpo continua desejável para a RC independente, mas não existe atualmente evidência de conflito técnico entre a branch do PR #2 e a `main`.

## Restrições preservadas

- não fechar ou recriar o PR para manipular o indicador;
- não forçar referências;
- não realizar merge;
- não tratar `mergeable: true` como aprovação normativa;
- manter PR em Draft até testes, reconciliação e RC independente.
