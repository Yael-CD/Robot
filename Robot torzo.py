from vpython import *
titulo = canvas(title="CUBO EN 3D")
import math

#BRAZOS Y PIERNAS 
cilindrop=cylinder(pos=vector(-15,5,0),axis=vector(0,0,0),radius=1,color=color.red)
cilindro2=cylinder(pos=vector(15,5,0),axis=vector(0,0,0),radius=1,color=color.red)
cilindro3=cylinder(pos=vector(-5,-15,0),axis=vector(0,0,0),radius=1,color=color.blue)
cilindro4=cylinder(pos=vector(5,-15,0),axis=vector(0,0,0),radius=1,color=color.blue)
#BOLITAS BRAZOS 
bolita1=sphere(color=color.blue, pos=vector(-15,5,0), radius=1)
bolita2=sphere(color=color.blue, pos=vector(15,5,0), radius=1)

#Valores del balanceo 
amplitud=45 #Angulo maximo de inclinacion 
amplitud2=-45 
frecuencia = 0.2 #Control de la velocidad del balanceo 
tiempo = 0

#Balanceo 
while True: 
    rate(30)
    #BRAZOS
    angulo= amplitud * math.sin(frecuencia*tiempo) #Movimiento armonico 
    cilindrop.axis=vector(0,-6,0) #Aseguramos la posicion en y 
    cilindrop.rotate(angle=math.radians(angulo),axis=vector(2,1,1),origin=cilindrop.pos) #ROTACION SOLO EN X
    tiempo += 0.1
    
    angulo= amplitud2 * math.sin(frecuencia*tiempo) #Movimiento armonico 
    cilindro2.axis=vector(0,-6,0) #Aseguramos la posicion en y 
    cilindro2.rotate(angle=math.radians(angulo),axis=vector(1,0,0),origin=cilindro2.pos) #ROTACION SOLO EN X
    tiempo += 0.1

    #PIERNAS
    angulo= amplitud * math.sin(frecuencia*tiempo) #Movimiento armonico 
    cilindro3.axis=vector(0,-6,0) #Aseguramos la posicion en y 
    cilindro3.rotate(angle=math.radians(angulo),axis=vector(1,0,0),origin=cilindro3.pos) #ROTACION SOLO EN X
    tiempo += 0.1

    angulo= amplitud2 * math.sin(frecuencia*tiempo) #Movimiento armonico 
    cilindro4.axis=vector(0,-6,0) #Aseguramos la posicion en y 
    cilindro4.rotate(angle=math.radians(angulo),axis=vector(1,0,0),origin=cilindro4.pos) #ROTACION SOLO EN X
    tiempo += 0.1
    break  

#parte cabeza
#cabeza----------------------------------------¬
cabeza = sphere(color=color.cyan, pos=vector(0,16,-10), radius= 7)
#circulo blanco----------------------------------¬
ojo1 = sphere(color=color.white, pos=vector(0.75,16,-8.5),radius= 5.5)
ojo2 = sphere(color=color.white, pos=vector(-0.75,16,-8.5),radius= 5.5)
#circulo negro------------------------------------¬
ojo1p = sphere(color=color.black, pos=vector(2.8,15.5,-4),radius= 1.5)
ojo2p = sphere(color=color.black, pos=vector(-2.8,15.5,-4),radius= 1.5)
#cilindro rojo----------------¬
antena1=cylinder(pos=vector(6,16,-10),axis=vector(1.5,0,0),radius=4,color=color.red)
antena2=cylinder(pos=vector(-6,16,-10),axis=vector(-1.5,0,0),radius=4,color=color.red)
#palo azul-------------¬
palo1=box(pos=vector(8,19,-10), size=vector(1,10,1), color=color.blue)
palo2=box(pos=vector(-8,19,-10), size=vector(1,10,1), color=color.blue)
#circulo rojo-------------------------------¬
ball1=sphere(color=color.red, pos=vector(8,24,-10),radius=1.5)
ball2=sphere(color=color.red, pos=vector(-8,24,-10),radius=1.5)
#boca----------------------¬
boca=cylinder(pos=vector(0,12.8,-5.5),axis=vector(0,0.5,1),radius=2,color=color.black)
#sombrero-------------------¬
base=cylinder(pos=vector(0,22,-10),axis=vector(0,1.5,0),radius=5.5,color=color.red)
copa=cylinder(pos=vector(0,23,-10),axis=vector(0,3.5,0),radius=4,color=color.red)

#Crecion de un cubo
cubo1= box(pos=vector(0,0,-10),size=vector(30,20,15),color=color.blue)#x(ancho),y(alto),z(profundidad)
cubo1= box(pos=vector(-8,5,-2),size=vector(7,5,1),color=color.green)
cubo1= box(pos=vector(0,5,-2),size=vector(2,2,1),color=color.red)
cubo1= box(pos=vector(-10,-5,-2),size=vector(3,5,1),color=color.yellow)
cubo1= box(pos=vector(-5,-5,-2),size=vector(3,5,1),color=color.black)
cubo1= box(pos=vector(0,-5,-2),size=vector(3,5,1),color=color.purple)

cubo1= box(pos=vector(8,7,-2),size=vector(10,1,1),color=color.black)
cubo1= box(pos=vector(8,-7,-2),size=vector(10,1,1),color=color.black)
cubo1= box(pos=vector(3,0,-2),size=vector(1,15,1),color=color.black)
cubo1= box(pos=vector(13,0,-2),size=vector(1,15,1),color=color.black)
cubo2= box(pos=vector(5,3,-2),size=vector(1,1,1),color=color.orange)
cubo4= box(pos=vector(8,2,-2),size=vector(1,1,1),color=color.white)
cubo3= box(pos=vector(11,1,-2),size=vector(1,1,1),color=color.cyan)
#Cuadritos tornicllos
cubo1= box(pos=vector(-13,8,-2),size=vector(1,1,1),color=color.white)
cubo1= box(pos=vector(-13,-8,-2),size=vector(1,1,1),color=color.white)
cubo1= box(pos=vector(13,8,-2),size=vector(1,1,1),color=color.white)
cubo1= box(pos=vector(13,-8,-2),size=vector(1,1,1),color=color.white)
#Velocidades iniciales de las cubos
incremento2= vector(0,-0.3,0)#Velocidades en Ball 1 = x, y
incremento3= vector(0,0.4,0)
incremento4= vector(0,0.5,0)
#Establcer limintes para x,y
limite_x = 5
limite_y = 6
limite_z=5
while  True:
    rate(30)
    #Mover las esferas en los ejes x,y
    cubo2.pos +=incremento2
    cubo3.pos +=incremento3
    cubo4.pos +=incremento4
    #Para el control de rebote
    #Rebote en x de ball 1
    if cubo2.pos.y > limite_y or cubo2.pos.y < -limite_y:
        incremento2.y = -incremento2.y #Ivertir direccion
    if cubo3.pos.y > limite_y or cubo3.pos.y < -limite_y:
        incremento3.y = -incremento3.y #Ivertir direccion
    if cubo4.pos.y > limite_y or cubo4.pos.y < -limite_y:
        incremento4.y = -incremento4.y #Ivertir direccion
