from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import xmlrpc.client
import os
import threading
from tinytag import TinyTag, TinyTagException
## Python 3.7
## Servidor Principal: 
# Los clientes se conectan en primera instancia con este servidor,
# si el servidor Principal tiene una excepcion o falla, el cliente se conecta al servidor Secundario

# ----------------------------------- CONFIGURACION DE SERVIDOR -----------------------------------------
# ---------------------------- CONFIGURACION PARTE CLIENTE DEL SERVIDOR-------------------------------------

# socket.gethostname
# Direcciones para cada cliente
# CLiente1
host1 = "127.0.0.1"
port1 = 9999
# Cliente2
host2 = "127.0.0.1"
port2 = 9998
# CLiente3
host3 = "127.0.0.1"
port3 = 9997

# Direccion de servidor Secundario
# hostS = "127.0.0.1"
# portS = 8999

portTest = 2869

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

def createClient(host, puerto):
    

    return server

# Conexion para clientes
server1 = SimpleXMLRPCServer((host1, port1), requestHandler=RequestHandler, allow_none=True) 
server1.register_introspection_functions()
server2 = SimpleXMLRPCServer((host2, port2), requestHandler=RequestHandler, allow_none=True) 
server2.register_introspection_functions()
# server3 = SimpleXMLRPCServer((host3, port3), requestHandler=RequestHandler, allow_none=True) 
# server3.register_introspection_functions()

# # Conexion servidor secundario
# serverS = SimpleXMLRPCServer((hostS, portS), requestHandler=RequestHandler, allow_none=True) 
# serverS.register_introspection_functions()

# Variables globales
lsTotalDataCli = []
lsTotalTracks = []

print("\n**********BETA NAPSTER RPC************")    
print("Servidor NAPSTER Principal escuchando...")

def connectionExist(clientConnected):
    print("Cliente conectado: ", clientConnected)

    return 0

def listenClientData(username, host, port):
    # Datos del cliente
    print("\n________________________________________\n")
    print("\nCargando datos de cliente...")
    print(".....")
    # Recibimos la informacion de los clientes
    global user
    user = username
    h = host
    p = port
    lsDataClient = [user, h, p]

    global lsTotalDataCli
    lsTotalDataCli.append(lsDataClient)

    print("DATOS DEL CLIENTE: ", lsDataClient)

def listenClientSong(lsTracks, numTrack, lsFileTracks):

    global lsTotalTracks
    lsTotalTracks+=lsTracks
               
    print("\nLISTA METADATOS DE CANCIONES: ", lsTracks) 
    print("\nNUMERO DE CANCIONES: ", numTrack)
    
def listenClientAlbum(lsAlbums, numAlbum, lsTracksAlbums, numTrackAlbum, lsFileTracksA):
    global lsTotalTracks
    lsTotalTracks+=lsTracksAlbums

    print("\nLISTA DE ALBUMS: ", lsAlbums)
    print("\nNUMERO DE ALBUMS: ", numAlbum) 
    print("\nLISTA METADATOS DE CANCIONES EN ALBUMS: ", lsTracksAlbums) 
    print("\nNUMERO DE CANCIONES EN ALBUMS: ", numTrackAlbum)  

    print("\nDatos del cliente " + user +" cargados con exito!")
    print("\n________________________________________\n")

    print("\nLISTA TOTAL DE CLIENTES EXISTENTES EN EL SERVIDOR: ", lsTotalDataCli)
    print("\nNUMERO DE CLIENTES EXISTENTES EN EL SERVIDOR: ", len(lsTotalDataCli))

    print("\nLISTA TOTAL DE CANCIONES EXISTENTES EN EL SERVIDOR: ", lsTotalTracks)
    print("\nNUMERO DE CANCIONES EXISTENTES EN EL SERVIDOR: ", len(lsTotalTracks))
    
# Funcion para buscar una cancion
def searchTrack(song):
    newSong = ""
    newArtist = ""
    # newSongAl = ""
    newDuration = ""
    newSize= 0
    newUsername = ""
    message = ""
    host = ""
    port = 0
    # recorre la lista lsTotalTracks e itera cada cancion en track
    for track in lsTotalTracks:
        if track[0] == song:
            newSong = track[0]
            newArtist = track[1]
            newDuration = track[2]
            newSize = track[3]
            newUsername = track[4]
            for usern in lsTotalDataCli:
                if usern[0] == newUsername:
                    host = usern[1]
                    port = usern[2]
            message = "Cancion encontrada!"
            print("\n" + message)
            
    if newSong == "":
        message = "Nombre incorrecto. La cancion no se encuentra!"
        print("\n" + message)   
    print(newSong)

    return newSong, newArtist, newDuration, newSize, newUsername, host, port, message




# ------------------------------------HILOS SERVIDOR----------------------------------------
                 
# Hilo Responsable de recibir infomacion de los clientes
class ServerThread(threading.Thread):
	def _init_(self):
		threading.Thread._init_(self)

	def run(self):
        # Ejecutando funciones de servidor  
         server1.register_function(connectionExist)      
         server1.register_function(listenClientData)
         server1.register_function(listenClientSong)
         server1.register_function(listenClientAlbum)
         print("Servidor Conectado...")
        #  server1.handle_request()
        #  server1.handle_request()
        #  server1.handle_request()
        #  server1.handle_request()

         server1.register_function(searchTrack)
         server1.serve_forever()
         print("Datos de cancion enviados a cliente")
        
# Hilo Responsable del buscador de musica y enviar datos de musica encontrada
class ServerThread2(threading.Thread):
	def _init_(self):
		threading.Thread._init_(self)

	def run(self):
        
         server2.register_function(connectionExist)    
         server2.register_function(listenClientData)
         server2.register_function(listenClientSong)
         server2.register_function(listenClientAlbum)
         print("Servidor Conectado...")
        #  server2.handle_request()
        #  server2.handle_request()
        #  server2.handle_request()
        #  server2.handle_request()
        # Ejecutando funciones de servidor 
         server2.register_function(searchTrack)
         print("Datos de cancion enviados a cliente")
         server2.serve_forever()
        



# class ServerThread2(threading.Thread):
# 	def _init_(self):
# 		threading.Thread._init_(self)

# 	def run(self):         
        # server3.register_function(listenClientData)
        #  server3.register_function(listenClientSong)
        #  server3.register_function(listenClientAlbum)
        #  server3.register_function(searchTrack)
        #  print("Servidor Conectado...")
        #  server3.handle_request()
        #  server3.handle_request()
        #  server3.handle_request()
        #  print("cerrado")

# clientSend = clientThread()
# clientSend.start()   
# serverReceive = serverThread()
# serverReceive.start() 

serverReceive1 = ServerThread()
serverReceive1.start()  
serverReceive2 = ServerThread2()
serverReceive2.start()    


