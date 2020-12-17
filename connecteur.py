import mysql.connector as mysqlpyth

class MySQL:

    @classmethod
    def ouvrir_connexion(cls):
        cls.db = mysqlpyth.connect(
            host = 'localhost',
            user = 'root',
            passwd = 'root',
            port = 8081,
            db = 'breizhibus'            
        )
        cls.cursor = cls.db.cursor(buffered = True)

    @classmethod
    def deconnexion(cls):
        cls.cursor.close()
        cls.db.close()

    @classmethod
    def recup_lignes(cls):
        cls.ouvrir_connexion()
        query = f"SELECT id_ligne, nom_ligne FROM lignes"
        cls.cursor.execute(query)
        liste = []
        for elements in cls.cursor:
            liste.append(elements)
        cls.deconnexion()
        return liste

    @classmethod
    def recup_arrets(cls, choix):
        cls.ouvrir_connexion()
        cls.choix = str(choix)
        query = f"SELECT id_ligne, id_arret FROM arrets_lignes WHERE id_ligne={cls.choix}"
        cls.cursor.execute(query)
        liste = []
        for elements in cls.cursor:
            liste.append(elements[1])

        liste2 = []
        for elem in liste:
            query = f"SELECT id_arret, nom_arret, adresse_arret FROM arrets WHERE id_arret={str(elem)}"
            cls.cursor.execute(query)
            for elems in cls.cursor:
                liste2.append(elems)
        cls.deconnexion()
        return liste2

    @classmethod
    def recup_bus(cls, choix):
        cls.ouvrir_connexion()
        cls.choix = str(choix)
        query = f"SELECT id_bus, numero_bus, immatriculation_bus, nombre_place_bus FROM bus WHERE id_ligne={cls.choix}"
        cls.cursor.execute(query)
        liste = []
        for elems in cls.cursor:
            liste.append(elems)
        cls.deconnexion()
        return liste

    @classmethod
    def recup_bus2(cls):
        cls.ouvrir_connexion()
        query = f"SELECT * FROM bus"
        cls.cursor.execute(query)
        liste = []
        for bus in cls.cursor:
            liste.append(bus[1:])
        cls.deconnexion()
        return liste

    @classmethod
    def recup_bus3(cls, choix):
        cls.ouvrir_connexion()
        cls.choix = str(choix)
        query = f"SELECT id_bus, numero_bus, immatriculation_bus, nombre_place_bus, id_ligne FROM bus WHERE numero_bus='{cls.choix}'"
        cls.cursor.execute(query)
        liste = []
        for elems in cls.cursor:
            liste.append(elems)
        cls.deconnexion()
        return liste

    # @classmethod
    # def inserer_bus(cls, numero_bus, immatriculation_bus, nombre_place_bus, ligne):
    #     cls.ouvrir_connexion()
    #     try:
    #         cls.ligne = str(ligne)
    #         query = f"INSERT INTO bus (id_bus, numero_bus, immatriculation_bus, nombre_place_bus, id_ligne) VALUES (NULL,'{numero_bus}','{immatriculation_bus}','{nombre_place_bus}','{ligne}')"
    #         cls.cursor.execute(query)
    #         cls.db.commit()
    #         cls.deconnexion()
    #         return 'Element inséré !'
    #     except:
    #         cls.deconnexion()
    #         return None

    @classmethod
    def modifier_bus(cls, ident, numero_bus, immatriculation_bus, nombre_place_bus, ligne):
        cls.ouvrir_connexion()
        query = f"INSERT INTO bus (id_bus, numero_bus, immatriculation_bus, nombre_place_bus, id_ligne) VALUES ({ident},'{numero_bus}', '{immatriculation_bus}', '{nombre_place_bus}', '{ligne}') ON DUPLICATE KEY UPDATE numero_bus='{numero_bus}', immatriculation_bus='{immatriculation_bus}', nombre_place_bus={nombre_place_bus}, id_ligne='{ligne}'"
        cls.cursor.execute(query)
        cls.db.commit()
        cls.deconnexion()

    @classmethod
    def suppr_bus(cls, num):
        cls.ouvrir_connexion()
        query = f"DELETE FROM bus WHERE numero_bus='{num}'"
        cls.cursor.execute(query)
        cls.db.commit()
        cls.deconnexion()

