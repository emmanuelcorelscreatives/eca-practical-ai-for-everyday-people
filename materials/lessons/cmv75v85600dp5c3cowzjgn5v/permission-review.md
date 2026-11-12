# Connected mail access — conceptual worksheet
This is a provider-neutral explanation, not a screenshot of authorization controls or a claim about a particular provider's current menus.

| Ability | Possible consequence | Question to check |
|---|---|---|
| Read mail | App may access message content | Which account and which messages? |
| Create or change drafts | App may create or edit unsent messages | Does the scope also include sending? |
| Send mail | App may communicate to external recipients | Is this needed and explicitly authorized? |

Provider A might separate draft creation and sending. Provider B might grant a broader scope covering both. These are conceptual examples, not verified products. Inspect the exact access requested; do not infer a provider's real permissions from these labels. Choose the narrowest available access and ask your administrator when required. If no connection is needed, do not grant one. Review/remove unneeded existing access using your provider's actual connected-app controls; menus vary. This kit requires no mailbox permission.
