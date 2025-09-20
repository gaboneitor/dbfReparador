import dbf
import os
import shutil

class generadorDBF:
        
    def __init__(self, archivoOrigen, archivoDestino):
        self.archivoOrigen = archivoOrigen
        self.archivoDestino = archivoDestino
    def generar(self):
        print("Generando DBF")
        nuevo = dbf.Table(self.archivoOrigen)
        print("Abriendo DBF")
        nuevo.open(mode=dbf.READ_WRITE)

        print("Borrando datos")
        with nuevo as tab:
            for record in dbf.Process(tab):
                    dbf.delete(record)
        nuevo.pack()
        print("Datos borrados")
        print("Abriendo DBF")
        table = dbf.Table(self.archivoDestino)
        table.open(mode=dbf.READ_WRITE)
        print("Copiando datos")
        with table as tab:
            for record in tab:
                try:
                    nuevo.append(tuple(record))
                except Exception as e:
                    print(e)
                    print(record[1])
                    print(record[2])
                    continue
        print("Datos copiados")
        nuevo.pack()
        nuevo.close()
        table.close()
        print("DBF generado")
