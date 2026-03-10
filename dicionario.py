# sem dicionário

matriculas= 2026001
nome1= "Ana Silva"
telefone1 = " 99925 8979"

#com dicionário 
aluno = { "matricula" : 2026001,  "matricula" : 2026001, 
    "nome" : "Ana Silva"
    "telefone" : "53 99925 8979"
    "nome" : "Ana Silva"
    "telefone" : " 99925 8979"}

print(aluno)

contato = {
   "@camila" : "Camila",
   "@paola": "Paola",
   "@sheron": "sheron", 
   "@bruna": "Bruna"

}

print.pop("@camila")
print(type(contato))

#Dicionario vazio
dados = {}

#Dicionario com tipos mistos
dados = {
    "nome": "João"
    "idade": 25,
    "altura":1,70, 
    
}


print("Original :", contato) # acessando a lista orginal

#add novo elemento
contato["@giovanna"] = "Giovanna"
print("APós add:", contato)

#atualiza elementos assistentes 
contato["@paola"] = "Paola Silveira "
print("Após add", contato)

#del colocar sem retomar 
del contato ["@paola"]
print ( "Após o del: ", contato)

#clear esvazia tudo 
copia = dict ( contato)
contato.clear()
print("Após clear :", contato)
print("Copía:", copia)

print("Numeos de conato", len (contato))

if contato.pop ("@camila")
print("Após remover um:" , len(contato("@joao")))

#verificar existência


if "@inexsistente "in contato:
    print("Existe")


#Dicionário Vazio

vazio = {}

#Dicionário com tipos mistos
dados = {


}
