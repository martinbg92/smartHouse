import paho.mqtt.client as mqtt
import paho.mqtt.properties as Properties
from random import randrange
import time

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    # client.subscribe("test")


def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    
    pass


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


def on_disconnect(client, userdata,  rc=0):
    print("Disconnected")
  

    #Teperatura
##Bajo
def tempBajoCreate(on_connect,on_message,on_publish):
    clientBajo = mqtt.Client()
    clientBajo.on_connect    = on_connect
    clientBajo.on_message    = on_message
    clientBajo.on_publish    = on_publish 
    clientBajo.on_disconnect = on_disconnect
    clientBajo.connect("localhost", 1883, 60)
    clientBajo.publish("micasa/bajo/temperatura",randrange(36))
    #clientBajo.loop_forever()
    #con = clientBajo.connect("localhost", 1883, 60)
    #clientBajo.loop_start()
    #clientBajo.publish("micasa/bajo/temperatura",randrange(36),0,False)         
    #clientBajo.loop_stop()
    #
    #clientBajo.disconnect("localhost",1883)

##Bed1
def Bed1Create(on_connect,on_message,on_publish):
 clientBed1 = mqtt.Client()
 clientBed1.on_connect = on_connect
 clientBed1.on_message = on_message
 clientBed1.on_publish = on_publish 
 clientBed1.on_disconnect = on_disconnect  
 clientBed1.connect("localhost", 1883, 60) 
 clientBed1.publish("micasa/dormitorio/1/temperatura",randrange(36))

##Bed2
def Bed2Create(on_connect,on_message,on_publish):
 clientBed2 = mqtt.Client()
 clientBed2.on_connect = on_connect
 clientBed2.on_message = on_message
 clientBed2.on_publish = on_publish 
 clientBed2.on_disconnect = on_disconnect   
 clientBed2.connect("localhost", 1883, 60) 
 clientBed2.publish("micasa/dormitorio/2/temperatura",randrange(36))
 #clientBed2.loop_forever()
 #clientBed2.connect("localhost", 1883, 60)
 #clientBed2.loop_start()
 #clientBed2.loop_stop() 
 #clientBed2.disconnect("localhost",1883)

##Bed3
def Bed3Create(on_connect,on_message,on_publish):
 clientBed3 = mqtt.Client()
 clientBed3.on_connect = on_connect
 clientBed3.on_message = on_message
 clientBed3.on_publish = on_publish 
 clientBed3.on_disconnect = on_disconnect 
 clientBed3.connect("localhost", 1883, 60)   
 clientBed3.publish("micasa/dormitorio/3/temperatura",randrange(36))

def Pasillo1Create(on_connect,on_message,on_publish):
    movement = False
    if (randrange(4)<2):
        movement = True
    else:
        movement = False

    Pasillo1Create = mqtt.Client()
    Pasillo1Create.on_connect = on_connect
    Pasillo1Create.on_message = on_message
    Pasillo1Create.on_publish = on_publish 
    Pasillo1Create.on_disconnect = on_disconnect 
    Pasillo1Create.connect("localhost", 1883, 60)   
    Pasillo1Create.publish("micasa/pasillo/1/movimiento",movement)


def Pasillo2Create(on_connect,on_message,on_publish):      
    movement = False
    if (randrange(4)<2):
        movement = True
    else:
        movement = False  

    Pasillo2Create = mqtt.Client()
    Pasillo2Create.on_connect = on_connect
    Pasillo2Create.on_message = on_message
    Pasillo2Create.on_publish = on_publish 
    Pasillo2Create.on_disconnect = on_disconnect 
    Pasillo2Create.connect("localhost", 1883, 60)
    Pasillo2Create.publish("micasa/pasillo/2/movimiento",movement)

def Banio1Create(on_connect,on_message,on_publish):
    movement = False
    if (randrange(4)<2):
        movement = True
    else:
        movement = False   

    Banio1Create = mqtt.Client()
    Banio1Create.on_connect = on_connect
    Banio1Create.on_message = on_message
    Banio1Create.on_publish = on_publish 
    Banio1Create.on_disconnect = on_disconnect 
    Banio1Create.connect("localhost", 1883, 60)   
    Banio1Create.publish("micasa/banio/1/movimiento",movement)

def Banio2Create(on_connect,on_message,on_publish):
    movement = False
    if (randrange(4)<2):
        movement = True
    else:
        movement = False 

    Banio2Create = mqtt.Client()
    Banio2Create.on_connect = on_connect
    Banio2Create.on_message = on_message
    Banio2Create.on_publish = on_publish 
    Banio2Create.on_disconnect = on_disconnect 
    Banio2Create.connect("localhost", 1883, 60)   
    Banio2Create.publish("micasa/banio/2/movimiento",movement)


def Jardin1Create(on_connect,on_message,on_publish):
    
    Jardin1Create = mqtt.Client()
    Jardin1Create.on_connect = on_connect
    Jardin1Create.on_message = on_message
    Jardin1Create.on_publish = on_publish 
    Jardin1Create.on_disconnect = on_disconnect 
    Jardin1Create.connect("localhost", 1883, 60)   
    Jardin1Create.publish("micasa/jardin/1/humedad",randrange(700))


def Jardin2Create(on_connect,on_message,on_publish):
      
    Jardin2Create = mqtt.Client()
    Jardin2Create.on_connect = on_connect
    Jardin2Create.on_message = on_message
    Jardin2Create.on_publish = on_publish 
    Jardin2Create.on_disconnect = on_disconnect 
    Jardin2Create.connect("localhost", 1883, 60)   
    Jardin2Create.publish("micasa/jardin/2/humedad",randrange(700))

for i in (range(300)):
    tempBajoCreate(on_connect,on_message,on_publish)
    Bed1Create(on_connect,on_message,on_publish)
    Bed2Create(on_connect,on_message,on_publish)
    Bed3Create(on_connect,on_message,on_publish)
    Pasillo1Create(on_connect,on_message,on_publish)
    Pasillo2Create(on_connect,on_message,on_publish)
    Banio1Create(on_connect,on_message,on_publish)
    Banio2Create(on_connect,on_message,on_publish)
    Jardin1Create(on_connect,on_message,on_publish)
    Jardin2Create(on_connect,on_message,on_publish)
    time.sleep(11)


print("fin")


