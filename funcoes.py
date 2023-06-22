#adicionando parâmetro nome_do_curso
def dar_boas_vindas(nome, sobrenome,nome_do_curso):
    print("Ola", nome, sobrenome)
    print("Bem vindo ao curso de", nome_do_curso)

#dar_boas_vindas("Priscilla", "Kawakami", "Javascript") #é um argumento, e será passado no parâmetro nome_do_curso
#argumentos sao chamados de POSICIONAIS, pois possuem posição na qual passo os valores, para os parâmetros importa
# Função com argumentos posicionais


#Função com argumentos nomeados ou 
#keywords arguments:
dar_boas_vindas(nome="Priscilla", sobrenome="Kawakami", nome_do_curso="Javascript")

