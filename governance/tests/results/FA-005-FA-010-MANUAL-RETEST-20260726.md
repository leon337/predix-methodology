# Reteste manual — FA-005 e FA-010

## Estado

- **Data:** `2026-07-26`.
- **Ambiente:** conversa ativa do projeto `Fábrica de softwares`.
- **Status geral:** `BLOCKED — AGUARDANDO INTERAÇÃO MANUAL DE LEO`.
- **Ações reais N2/N3:** nenhuma.

## Motivo do bloqueio

Os dois cenários dependem de interação humana observável na interface do @Visualize. Inspeção estática do código não é evidência suficiente para aprovação funcional.

## FA-005 — Alterar escolha

### Procedimento manual

1. selecionar uma opção;
2. confirmar o plano;
3. gerar o comando;
4. pressionar `Alterar escolhas`;
5. confirmar que o comando anterior deixa de ser a decisão ativa;
6. selecionar outra opção;
7. confirmar que um novo comando é gerado sem reaproveitar silenciosamente o anterior.

### Critério de PASS

- o comando anterior não permanece válido visualmente;
- a seleção pode ser alterada;
- o novo comando corresponde à nova escolha;
- nenhuma ação é executada antes do reenvio do novo comando.

### Resultado observado

`NOT_RUN` nesta etapa. O painel de teste será apresentado na conversa para execução por Leo.

## FA-010 — Escolha contrária à recomendação

### Procedimento manual

1. observar a opção marcada apenas como `Recomendada pela IA`;
2. selecionar deliberadamente outra opção compatível;
3. confirmar o plano;
4. verificar que a decisão de Leo prevalece;
5. confirmar que a opção recomendada não é incluída automaticamente.

### Critério de PASS

- a recomendação permanece desmarcada;
- a escolha contrária é aceita;
- o comando contém somente a decisão realmente selecionada;
- não há bloqueio ou substituição automática pela recomendação.

### Resultado observado

`NOT_RUN` nesta etapa. O painel de teste será apresentado na conversa para execução por Leo.

## Gate

FA-005 e FA-010 somente poderão ser classificados como `PASS` após Leo executar os dois cenários e devolver o comando de evidência gerado pelo painel de teste.
