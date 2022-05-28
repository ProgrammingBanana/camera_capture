from database import Database as DB

# opens database connection
db = DB()

# When starting video recording for the first time, update path to path created by folder_creation.py and run this code.
db.insert_sign("ayuda", "/Users/codingdan/Documents/University/Semestre 2 2021-2022/Tesina/codigo/ML_Camera_Capture/MP_Data/ayuda")
db.insert_sign("clase", "/Users/codingdan/Documents/University/Semestre 2 2021-2022/Tesina/codigo/ML_Camera_Capture/MP_Data/clase")
db.insert_sign("donde", "/Users/codingdan/Documents/University/Semestre 2 2021-2022/Tesina/codigo/ML_Camera_Capture/MP_Data/donde")
db.insert_sign("gracias", "/Users/codingdan/Documents/University/Semestre 2 2021-2022/Tesina/codigo/ML_Camera_Capture/MP_Data/gracias")
db.insert_sign("hola", "/Users/codingdan/Documents/University/Semestre 2 2021-2022/Tesina/codigo/ML_Camera_Capture/MP_Data/hola")
db.insert_sign("necesitar", "/Users/codingdan/Documents/University/Semestre 2 2021-2022/Tesina/codigo/ML_Camera_Capture/MP_Data/necesitar")
db.insert_sign("no_entender", "/Users/codingdan/Documents/University/Semestre 2 2021-2022/Tesina/codigo/ML_Camera_Capture/MP_Data/no_entender")
db.insert_sign("repetir", "/Users/codingdan/Documents/University/Semestre 2 2021-2022/Tesina/codigo/ML_Camera_Capture/MP_Data/repetir")
db.insert_sign("n-a", "/Users/codingdan/Documents/University/Semestre 2 2021-2022/Tesina/codigo/ML_Camera_Capture/MP_Data/n-a")
db.insert_sign("empty", "/Users/codingdan/Documents/University/Semestre 2 2021-2022/Tesina/codigo/ML_Camera_Capture/MP_Data/empty")


sign_data = db.get_signs()
print(len(sign_data))

for sign in sign_data:
    print(sign)