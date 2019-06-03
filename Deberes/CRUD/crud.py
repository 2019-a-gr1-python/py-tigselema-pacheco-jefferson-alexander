import os

path = "./inventario.txt"
def leer_archivo(path):
    archivo_a_leer = open(path,mode='r')    
    return archivo_a_leer

def escribir_archivo(path, contenido):
    archivo_a_escribir = open(path,mode='a+')
    archivo_a_escribir.writelines(contenido)
    archivo_a_escribir.close()
    return archivo_a_escribir 

def eliminar():    
    listar()
    registro_a_eliminar = input('Ingrese numero de registro a eliminar: ')   
    id_registro = int(registro_a_eliminar) 
    arreglo_nuevo=leer_archivo(path).readlines()
    arreglo_nuevo.pop(id_registro)    
    os.remove('inventario.txt')
    escribir_archivo(path,arreglo_nuevo)
    listar()
    switch_accion()    

def listar():
    print('LISTADO DE PRODUCTOS DISPONIBLES')
    try:
        lista_dispositivos = leer_archivo(path)
        for index , line in enumerate(lista_dispositivos.readlines()): 
                print(f'{index} {line}')
        lista_dispositivos.close()
    except Exception as error:
        print(f'Error: {error}')

def crear():
    marca= input('Ingrese marca del dispositivo movil:  ')
    modelo= input(f'Ingrese el modelo del dispositivo movil marca {marca}:  ')
    precio= input(f'Ingrese precio del dispositivo {marca} - {modelo}:  ')
    contenido = f'{marca}     {modelo}     {precio}\n'
    try:                
        registrar = escribir_archivo(path,contenido)
        print('REGISTRO CREADO CON EXITO!')
        listar()
        switch_accion()
    except Exception as error:
        return f'Error en el archivo: {error}'
    return registrar
            
def modificar():
    listar()
    registro = input('Ingresar el registro a modificar')    
    marca= input('Ingrese marca del dispositivo movil:  ')
    modelo= input(f'Ingrese el modelo del dispositivo movil marca {marca}:  ')
    precio= input(f'Ingrese precio del dispositivo {marca} - {modelo}:  ')
    id_registro = int(registro)
    contenido = f'{marca}     {modelo}     {precio}\n'
    try:            
        print(id_registro, contenido)
        registro_modificar = leer_archivo(path).readlines()        
        registro_modificar[id_registro] = contenido
        os.remove('inventario.txt')
        registrar_modificacion = escribir_archivo(path,registro_modificar)
        registrar_modificacion.close()  
        listar()        
        switch_accion()
    except Exception as error:
            print(f'Error: {error}')

def switch_accion():     
    accionAbuscar=input('Ingrese numero de la accion a realizar \n 1.- Crear \n 2.- Listar \n 3.- Eliminar \n')
    return { 
        '3':modificar(),
        '2':listar(),
        '1':crear(),   
        '4':eliminar()
        }[accionAbuscar]
       
     
switch_accion()



