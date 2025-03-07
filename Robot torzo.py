from vpython import *
titulo = canvas(title="CUBO EN 3D")
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