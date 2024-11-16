"""
1) Armazenar as credenciais dos usu�rios em uma base de dados, conforme descrito no
topico 'Credenciais do usu�rio' que est� abaixo;
2) Receber o cadastro de novas credenciais do usuario;
3) Receber as requisi�oes vindas dos clientes;
4) Consultar a base de dados de usuarios;
5) Armazenar a tentativa de acesso um arquivo de registro, conforme descrito no topico
"Arquivo de registro";
6) Enviar para os clientes informa��es de autoriza�ao.
"""

"""
----------------- Parte de arquivo TXT INICIO ---------------------------------------------------

As credencias do usu�rio ser�o armazenadas em um arquivo TXT, onde cada linha conter� tr�s
informa��es: c�digo do usu�rio, nome do usu�rio e n�vel de acesso
"""
#   status: por enquanto pronto
import re

arquivo_credenciais = "Nao_mexa_aqui.txt"

class Texto:
    def __init__(self,arquivo):
        self.arquivo = arquivo
        
    def atualizar_txt(self, arquivo,id_,nome,prioridade):
        f = open(self.arquivo,"r+")
        f.seek(0,2)
        f.write( str(id_) + ", " + str(nome) + ", " + str(prioridade) + "\n")
        f.close()
    
    def procurar_txt(self,nome):
        temp_nome_encontrado = False
        f = open(self.arquivo,"r+")    
        for line in f:
            temp = re.split(r'\W+',line)
            if (temp[1] == nome):
                temp_nome_encontrado = True
                break
        f.close()
        if(temp_nome_encontrado == True):
            return temp[2]
        return -1
        
txt = Texto(arquivo_credenciais)

"""
----------------- Parte de arquivo TXT FIM -------------------------------------------------------
"""

"""
----------------- Parte de arquivo LOG INICIO ---------------------------------------------------
O arquivo de registro de tentativas de acesso ser� um arquivo no formato TXT. Cada
tentativa de acesso reportada pelos clientes dever� ser registrada em uma linha deste arquivo.
Cada linha do arquivo deve conter as seguintes informa��es: data e hora no formado
dd/mm/aaaa � hh:mm:ss, identifica��o da porta, identifica��o do usu�rio, autorizado
ou negado.

* Feito no ChatGPT:
    "podes fazer um programa em python que implemente um arquivo LOG para um servidor: O arquivo de registro de tentativas de acesso ser� um arquivo no formato TXT. Cada
    tentativa de acesso reportada pelos clientes dever� ser registrada em uma linha deste arquivo.
    Cada linha do arquivo deve conter as seguintes informa��es: data e hora no formado
    dd/mm/aaaa � hh:mm:ss, identifica��o da porta, identifica��o do usu�rio, autorizado
    ou negado. Exemplo:
        04/09/2018 � 13:20:14, p1, 1458, autorizado
        04/09/2018 � 14:11:35, p2, 7458, negado"
"""
# requisi��es poss�veis: 
#    Tentar entrar - falhar ou suceder
#    Tentar se inscrever - suceder -> id e prioridade    

#   status: no in�cio

import datetime

# Fun��o para registrar a tentativa de acesso no arquivo de log
def registrar_tentativa_acesso(arquivo_log, porta, usuario, autorizado):
    # Obter a data e hora atual no formato dd/mm/aaaa � hh:mm:ss
    data_hora_atual = datetime.datetime.now().strftime("%d/%m/%Y � %H:%M:%S")
    
    # Formatar a linha do log
    linha_log = f"{data_hora_atual}, {porta}, {usuario}, {autorizado}\n"
    
    # Abrir o arquivo de log no modo de adi��o ('a' para append) e gravar a linha
    with open(arquivo_log, 'a') as file:
        file.write(linha_log)

# Fun��o para simular o processo de acesso (em um caso real, voc� faria valida��es)
def tentar_acesso(arquivo_log, porta, usuario, senha):
    # Vamos supor que o sistema permita acesso para qualquer senha '1234'
    if senha == '1234':
        autorizado = 'autorizado'
    else:
        autorizado = 'negado'
    
    # Registrar a tentativa no arquivo de log
    registrar_tentativa_acesso(arquivo_log, porta, usuario, autorizado)

# Exemplo de uso:
arquivo_log = "acessos.log"

# Simulando algumas tentativas de acesso
#tentar_acesso(arquivo_log, 'p1', '1458', '1234')   # Acesso autorizado
#tentar_acesso(arquivo_log, 'p2', '7458', 'abcd')   # Acesso negado
#tentar_acesso(arquivo_log, 'p1', '1458', 'wrong')  # Acesso negado
#tentar_acesso(arquivo_log, 'p3', '3201', '1234')   # Acesso autorizado
    
"""
----------------- Parte de arquivo LOG FIM -------------------------------------------------------
"""


import socket 

host = '' 
porta = 7000 
addr = (host, porta) 
#criar o socket para o servidor passando a família do protocolo de transporte 
#socket.AF_INET define que é um protocolo para rede IP (AF_BLUETOOTH definiria comunicação bluetooth, por exemplo)
#socket.SOCK_STREAM para TCP
#socket.SOCK_DGRAM para UDP
socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#reserva o socket para a nossa aplicação
socket_servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
#define quais IP's e em qual porta o server vai aguardar conexão
socket_servidor.bind(addr) 
#define que servidor aguarda conexões e quantas conexão serão recebidas. Não é necessário caso UDP
socket_servidor.listen(10) 

#while(1):
    
print ('aguardando conexao')
con, cliente = socket_servidor.accept() #espera por conexão
print ('conectado') 
print ("aguardando mensagem") 
recebe = con.recv(1024) #recebe mensagem (em bytes, com tamanho max definido pelo parâmetro)
print ("mensagem recebida: ")  
print(recebe.decode()) 
prioridade = txt.procurar_txt(recebe.decode())
if(prioridade != -1):
    print("Voc� entrou")
        
socket_servidor.close()