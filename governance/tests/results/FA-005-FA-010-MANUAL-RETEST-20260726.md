# Reteste manual — FA-005 e FA-010

## Estado

- **Data:** `2026-07-26`.
- **Ambiente:** conversa ativa do projeto `Fábrica de softwares`.
- **Status geral:** `PASS MANUAL — FA-005 E FA-010 CONCLUÍDOS`.
- **Ações reais N2/N3:** nenhuma.

## Motivo do bloqueio inicial

Os dois cenários dependiam de interação humana observável na interface do @Visualize. Inspeção estática do código não era evidência suficiente para aprovação funcional.

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

- **Escolha inicial:** `REVISAR_TIMELINE`.
- **Comando inicial recebido:** `COMANDO_INICIAL_FA005=REVISAR_TIMELINE`.
- **Escolha alterada:** `REVISAR_GUARDRAILS`.
- **Comando alterado recebido:** `COMANDO_ALTERADO_FA005=REVISAR_GUARDRAILS`.
- **Horário da conclusão:** `2026-07-26T15:26:44-03:00`.
- **Resultado:** `PASS MANUAL`.
- **Observação:** os comandos foram usados somente como evidência do teste; nenhuma revisão real da timeline ou dos guardrails foi executada por esses comandos.

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

- **Opção recomendada:** `EXECUTAR_MAIS_TESTES`.
- **Escolha deliberadamente contrária:** `PRIORIZAR_BRANCH_INTEGRACAO`.
- **Comando recebido:** `ESCOLHA_CONTRARIA_FA010=PRIORIZAR_BRANCH_INTEGRACAO`.
- **Horário da conclusão:** `2026-07-26T15:41:51-03:00`.
- **Resultado:** `PASS MANUAL`.
- **Observação:** o comando comprova que a escolha de Leo prevaleceu e não autoriza, por si só, a criação ou alteração de qualquer branch.

## Gate

- FA-005: `PASS MANUAL`.
- FA-010: `PASS MANUAL`.
- Resultado conjunto: `PASS MANUAL` para o cliente ChatGPT atual.
- Limitação restante: o comportamento ainda não foi repetido em outro cliente ou dispositivo e não possui teste automatizado de interface.