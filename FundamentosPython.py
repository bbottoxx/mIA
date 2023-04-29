def nuevoTema(tema):
    print("\n ----------", tema, "----------\n")
    
nuevoTema("Operadores Aritméticos")
print("operador suma, 5+3=",5+3)
print("operador resta, 10-2=",10-2 )
print("operador multiplicación 3*3=",3*3)
print("operador división entera 20//3=",20//3)
print("operador módulo 20%3=",20%3)
print("operador cambio de singo -3",-3)
print("operador exponente 5*5",5*5)
 
nuevoTema("Operadores Lógicos") 
#Este es un comentario de una linea. 
'''Este es un comentario''' 
print("True and True:", True and True)#Operadopr lógico and. 
#Actividad: Imprimir la tabla de verdad  
print("True and False:", True and False) 
print("False and True:", False and True) 
print("False and False:",False and False) 
#Operador lógico or 
print("True or True:", True or True) 
print("True or False:", True or False) 
print("False or True:", False or True) 
print("False or False:",False or False) 
#Operador lógicos not 
print("not False:",not False) 
print("not True:",not True) 
 
nuevoTema("Operadores de Comparación") 
print("Es igual que 1=2:", 1==2) 
print("Es distinto de 1!=2:", 1!=2) 
print("Es menor que 1<2:", 1<2) 
print("Es menor o igual que 1<=2:", 1<=2) 
print("Es mayor que 1>2:", 1>2) 
print("Es mayor o igual que 1>=2:", 1>=2) 
 
nuevoTema("Variables") 
variable1 = 10 
_variable2 = 6.2547 
Variable3 = "Pepe" 
nombreVariable = 8 
nombre_variable = 34.2 
print(variable1, _variable2, Variable3, nombre_variable) 
 
a, b, c=5, 10.8, "Hola" 
print(a) 
print(b) 
print(c) 
 
nuevoTema("Enteros") 
w=105 
x=123456789584 
y=-58 
z=0b00110011 
h=0xff 
print(w,type(w)) 
print(x,type(x)) 
print(y,type(y)) 
print(z,type(z)) 
print(h,type(h)) 
 
nuevoTema("Flotantes") 
x= 1234.56 
print(x, type(x)) 
y=-9874.56 
print(y,type(y)) 
 
nuevoTema("Números Complejos") 
x=-46j 
y=12+45j 
z=2j 
print(type(x)) 
print(type(y)) 
print(type(z)) 
 
nuevoTema("Boleanos") 
lis=[] 
print("lis, 'is'", bool(lis)) 
t=() 
print("t,'is'",bool(t)) 
new='Hello' 
print("new,'is'",bool(t)) 
num=99 
print("new,'is'",bool(num)) 
comp=0+0j 
print(comp,'is',bool(comp)) 
val=None 
print(val,'is',bool(val)) 
 
nuevoTema("Listas") 
a=[10,20.5,"Python List"] 
print(a) 
a=[10,20.5,"Python List"] 
print(a[1]) 
 
 
nuevoTema("Tuplas") 
t=(25,'tuple',1+10j) 
print(t) 
print(t[1]) 
#t[1]="Hola" #Operación no válid en tuplas. 
print("t[1]=,t[1]") 
print("t[0:3]=",t[0:3]) 
 
nuevoTema("Cadenas") 
cadena1="Esto es una cadena" 
cadena2='Esto también es una cadena' 
print(cadena1, type(cadena1)) 
print(cadena2, type(cadena2)) 
print(cadena1[5]) 
s="This is a single line string" 
print(s) 
s2='''A multiline string''' 
print(s2) 
cadenaMultilinea='''Esto es una cadena 
de varias líeas con tabulares y  
saltos 
de  
linea''' 
print(cadenaMultilinea, type(cadenaMultilinea)) 
 
cadena3="Hola"*5 
print(cadena3) 
 
nuevoTema("Conjuntos") 
conjunto={10,20,30,40,10,50} 
print(conjunto) 
 
nuevoTema("Diccionarios") 
d={1:'val1',2:'val2'} 
print(type(d)) 
diccionario={"Nombre":"Conrado",  "Edad":38, "Tel" :12345678} 
print(diccionario) 
 
nuevoTema("FIN")