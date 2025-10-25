# Crie uma função que receba uma lista de strings (potenciais e-mails) e um parâmetro 
# opcional dominio_desejado (com valor padrão "gmail.com"). A função deve retornar uma nova lista, 
# usando list comprehension, contendo apenas os e-mails que terminam com o domínio desejado.

def filtrar_emails(lista_emails, dominio_desejado="gmail.com"):
    emails_filtrados = [email for email in lista_emails if email.endswith(f"@{dominio_desejado}")]
    for email in emails_filtrados:
        print(email)

emails = ["joao@gmail.com","maria@yahoo.com","pedro@hotmail.com",
          "ana@gmail.com","lucas@outlook.com","rafael@gmail.com",
          "jose@yahoo.com","lucia@hotmail.com","catia@gmail.com",
          "marcelo@outlook.com","flavia@hotmail.com","natalia@gmail.com"
         ]

print(f"\n=== Lista de e-mails 'gmail' ===\n")
filtrar_emails(emails)
print(f"\n*************************")