usuario={
    'juca@gmail.com':{
        "login": "juca@gmail.com",
        "senha": "tef576689",
        "usuario": "juca",
        "dataNaci" : "5769423",
    },
     'joao@gmail.com':{
        "login": "joao@gmail.com",
        "senha": "123",
        "usuario": "joao",
        "dataNaci" : "050597",
    },
         'chico@gmail.com':{
        "login": "chico@gmail.com",
        "senha": "45487",
        "usuario": "chico",
        "dataNaci" : "050597",
    }
}
login =input(f"digite seu login:  \n")
senha=input(f"digite sua senha:  \n")
temp={}
if login in usuario.keys():
   temp.update(usuario.setdefault(login)) 
   if senha in temp.values():
       print("voce esta logado")
   else:
       print("login ou senha incorreto, tente novamente ")

else:
    print("login ou senha incorreto, tente novamente")

