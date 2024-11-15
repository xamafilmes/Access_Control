"""
1) Armazenar as credenciais dos usuários em uma base de dados, conforme descrito no
tópico “Credenciais do usuário” que está abaixo;
2) Receber o cadastro de novas credenciais do usuário;
3) Receber as requisições vindas dos clientes;
4) Consultar a base de dados de usuários;
5) Armazenar a tentativa de acesso um arquivo de registro, conforme descrito no tópico
“Arquivo de registro”;
6) Enviar para os clientes informações de autorização.
"""

"""
----------------- Parte de arquivo TXT INICIO ---------------------------------------------------
"""
arquivo = "Não_mexa_aqui.txt"

class Texto:
    def __init__(self,arquivo):
        self.arquivo = arquivo
        
        
    def atualizar_txt(self, arquivo,id_,nome,prioridade):
        f = open(self.arquivo,"r+")
        # em construção
        f.seek(0,2)
        f.write( str(id_) + ", " + str(nome) + ", " + str(prioridade) + "\n")
        f.close()
    
    def procurar_txt(self, arquivo,id_ = None,nome  = None,prioridade  = None):
        f = open(self.arquivo,"r+")    
        # em construção
        f.close()

txt = Texto(arquivo)
"""
----------------- Parte de arquivo TXT FIM -------------------------------------------------------
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
print ('aguardando conexao')
con, cliente = socket_servidor.accept() #espera por conexão
print ('conectado') 
print ("aguardando mensagem") 
recebe = con.recv(4) #recebe mensagem (em bytes, com tamanho max definido pelo parâmetro)
print ("mensagem recebida: ")  
print(recebe.decode()) 
txt.atualizar_txt(arquivo,recebe.decode(),recebe.decode(),recebe.decode())
socket_servidor.close()