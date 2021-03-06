from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import xmlrpc.client
import threading
import os
from enviarDatos2 import sendTrack, sendAlbum
# Python 3.7
# Cliente RPC

# -------------------------------------------------CONFIGURACION CONEXION--------------------------------------------------
# socket.gethostname
# direcciones para los servidores
# Servidor 1
host1 = "127.0.0.1"
port1 = 9998
# Servidor2
host2 = "127.0.0.1"
port2 = 9898

portTest = 2869

# direcciones para los clientes que se conecten
global host3
global port3
host3 = "127.0.0.1"
port3 = 9798
host4 = "127.0.0.1"
port4 = 9698

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

print("\n**************NAPSTER RPC****************")  

# Funcion que conecta con servidores

# Variables bandera para conocer el servidor al que esta conectado este cliente
global clientConnected 
clientConnected = False
global clientConnected2
clientConnected2 = False
# Si el servidor1 esta activo se conecta con ese
if clientConnected == False:
    try:
        # Crear conexion para un Servidor RPC, con el metodo client de xmlrpc 
        cliente1 = xmlrpc.client.ServerProxy('http://' + host1 + ':' + str(port1), allow_none=True)
        print("\nCliente conectando a servidor Principal...")
        clientConnected = True
        cliente1.connectionExist(clientConnected)
    except:
        print("\nError. No se puede establecer conexion a servidor Principal.")
        clientConnected = False
        # Si el servidor1 esta inactivo intenta conectar con servidor2
        if clientConnected == False: 
            global cliente2           
            cliente2 = xmlrpc.client.ServerProxy('http://' + host2 + ':' + str(port2), allow_none=True)
            print("\nCliente conectando a servidor Secundario...")
            clientConnected2 = True
            cliente2.connectionExist(clientConnected2)

        else:
            print("\nError. No se puede establecer conexion a servidor Secundario.")  
            clientConnected2 = False
else:
    print("\nError fatal. No consiguio conectarse con ningun servidor.")             

#conexion tipo servidor para el cliente que quiere descargar una cancion 
serverCli = SimpleXMLRPCServer((host3, port3), requestHandler=RequestHandler, allow_none=True) 
serverCli.register_introspection_functions()

def dataClient():

    global username
    username = "Socrates" # input("Digita un nombre de usuario para identificarte en NAPSTER: ")

    if clientConnected == True:  
        print("\nHola", username, "Bienvenido a NAPSTER.\nTe conectaste al servidor Principal desde: Direccion: ", host1, " Puerto: ", port1)    
        print("La Direccion de ", username, "para conectarse a otros clientes es: ", host3, " y el puerto es: ", port3)
        return username, host3, port3   

    if clientConnected2 == True:  
        print("\nHola", username, "Bienvenido a NAPSTER.\nTe conectaste desde el servidor Secundario desde: Direccion: ", host2, " Puerto: ", port2)    
        print("La Direccion de ", username, "para conectarse a otros clientes es: ", host3, " y el puerto es: ", port3)
        return username, host3, port3       


def main():
    print("\nMENU PRINCIPAL DE NAPSTER\n")
    print("\n 1. Buscar por canci??n")
    print("\n 2. Buscar por artista")
    print("\n 3. Buscar por ??lbum") 
    print("\n 4. Salir") 
   
    while True:
        opcion = (input("Escriba el n??mero de la opci??n para buscar: "))

        if opcion == "1":
            
            song = input("Escribe el nombre de una cancion: ")
            songServer, artistServer, durationServer, sizeServer, userServer, hostServer, portServer, message = cliente1.searchTrack(song)
            print(message)
            print ("- Nombre cancion:",songServer, "- artista:",artistServer,  "- duracion:",durationServer, "- tama??o:",sizeServer, "- usuario:",userServer)
            print ("host usuario:",hostServer, "port usuario:",portServer)

            clienteCliente = xmlrpc.client.ServerProxy('http://' + hostServer + ':' + str(portServer), allow_none=True)
            print("\nCliente conectando a servidor Principal...")
            
        elif opcion == "2":
            song = input("Escribe el nombre de un artista: ")
                    
        elif opcion == "3":
            song = input("Escribe el nombre de un album: ")

        elif opcion == "0":
            print("\nCerrando cliente NAPSTER...")   
            break
    return song


def shareSong (song)
    nameSong = "" 
    newArtist = ""

    for nameSong in lsTotalTracks:
        if nameSong[0] == song:









# --------------------------------------------EJECUCION E HILOS------------------------------------------------------

# Hilo Responsable de enviar informacion al servidor1
class ClientThread(threading.Thread):
	def _init_(self):
		threading.Thread._init_(self)      

	def run(self):
         username, host, port = dataClient()
         lsTracks, numTrack, lsFileTracks  = sendTrack(username)
         lsAlbums, numAlbum, lsTrackAlbums, numTrackAlbum, lsFileTracksA = sendAlbum(username)
         
         cliente1.listenClientData(username, host, port)
         cliente1.listenClientSong(lsTracks, numTrack, lsFileTracks)
         cliente1.listenClientAlbum(lsAlbums, numAlbum, lsTrackAlbums, numTrackAlbum, lsFileTracksA)
         print("\nSe han compartido tus archivos locales con el servidor Principal de NAPSTER RPC.")

# Hilo Responsable de enviar informacion al servidor2
class ClientThread2(threading.Thread):
	def _init_(self):
		threading.Thread._init_(self)      

	def run(self):
         username, host, port = dataClient()       
         lsTracks, numTrack, lsFileTracks  = sendTrack(username)
         lsAlbums, numAlbum, lsTrackAlbums, numTrackAlbum, lsFileTracksA = sendAlbum(username)

         cliente2.listenClientData(username, host, port)
         cliente2.listenClientSong(lsTracks, numTrack, lsFileTracks)
         cliente2.listenClientAlbum(lsAlbums, numAlbum, lsTrackAlbums, numTrackAlbum, lsFileTracksA)
         print("\nSe han compartido tus archivos locales con el servidor Secundarios de NAPSTER RPC.") 

# Hilo Responsable de buscar musica en el servidor
class ClientThread3(threading.Thread):
	def _init_(self):
		threading.Thread._init_(self)      

	def run(self):
         main()
         print("\nSe han compartido tus archivos locales con el servidor Secundarios de NAPSTER RPC.")                   

# Dependiendo el servidor a que este conectado Ejecuta los hilos 
if clientConnected == True: 
    clientSend = ClientThread()
    clientSend.start()
    clientSearch = ClientThread3()
    clientSearch.start()
elif clientConnected2 == True:
    clientSend2 = ClientThread2()
    clientSend2.start()
    clientSearch = ClientThread3()
    clientSearch.start()
else :
    print("Error fatal al ejecutar servicios del cliente!")



