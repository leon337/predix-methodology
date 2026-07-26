# Investigação do estado não mesclável do PR #2 — 2026-07-26

## Estado observado

- **PR:** #2.
- **Base:** `main`.
- **Head:** `mop/timeline-conversas-20260726`.
- **PR em rascunho:** sim.
- **Campo `mergeable`:** `false`.
- **Merge realizado:** não.

## Evidências

### Comparação com `main`

A comparação do branch atual com `main` retornou:

- `status: ahead`;
- `ahead_by: 52`;
- `behind_by: 0`;
- merge base igual ao HEAD atual de `main`: `ef296e2b2404c6acf47676c01d224ae478e6e569`.

### CI

Não foram encontrados workflow runs associados ao HEAD consultado anteriormente. Portanto, não existe evidência de que o estado `mergeable: false` seja causado por CI reprovada.

## Análise

Os dados disponíveis são contraditórios:

1. a branch possui ancestralidade direta a partir da `main` e não está atrás;
2. o PR continua reportado como não mesclável;
3. não há workflow executado que explique bloqueio por status;
4. o PR permanece em rascunho, mas o rascunho por si só não prova conflito de conteúdo.

Com os dados expostos pelo conector, não é possível afirmar com segurança se o valor `false` representa:

- conflito real de merge não exposto no resumo;
- cálculo de mergeability ainda não atualizado;
- normalização do conector;
- estado transitório do GitHub.

## Conclusão

**Causa técnica definitiva: não comprovada.**

O estado deve continuar tratado como bloqueador até uma destas verificações ocorrer:

1. inspeção em checkout Git limpo com tentativa de merge local sem commit;
2. consulta independente ao PR após estabilização do HEAD;
3. criação de uma branch de integração limpa a partir da fonte normativa escolhida;
4. novo PR rascunho a partir da branch reconciliada.

## Restrições

- não fechar ou recriar o PR apenas para tentar alterar o indicador;
- não forçar atualização de referência;
- não realizar merge;
- não declarar o conflito resolvido sem evidência reproduzível.
