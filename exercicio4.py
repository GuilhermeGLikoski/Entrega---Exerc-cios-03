usuario = input("Identifique-se (Usuário): ").strip()
senha = input("Diga a palavra-chave (Senha): ").strip()

if usuario == "admin" and senha == "1234":
    print("Acesso permitido")
elif usuario == "convidado" and senha == "":
    print("Acesso restrito")
else:
    print("Acesso bloqueado")
