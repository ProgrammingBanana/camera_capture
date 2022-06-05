from database import Database as DB

# opens database connection
db = DB()

db.insert_sign("ayuda", "./MP_Data/ayuda")
db.insert_sign("clase", "./MP_Data/clase")
db.insert_sign("donde", "./MP_Data/donde")
db.insert_sign("gracias", "./MP_Data/gracias")
db.insert_sign("hola", "./MP_Data/hola")
db.insert_sign("necesitar", "./MP_Data/necesitar")
db.insert_sign("no_entender", "./MP_Data/no_entender")
db.insert_sign("repetir", "./MP_Data/repetir")
db.insert_sign("n-a", "./MP_Data/n-a")
db.insert_sign("empty", "./MP_Data/empty")


sign_data = db.get_signs()
print(len(sign_data))

for sign in sign_data:
    print(sign)