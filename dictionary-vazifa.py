# 1-misol 1. Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting). 
# Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. Foydalanuvchi kiritgan 
# taomlarni menu bilan solishtiring, agar taom menuda bo'lsa narhini ko'rsating,
#  aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.

# restoran = {
#     "taomlar" : {
#         "quyuq ovqatlar": {
#             "osh" : {
#                 "to'y osh" : 22000,
#                 "choyxona osh" : 26000
#             },
#             'manti' : 5000,
#             'lagmon' : {
#                 "suyuq lagmon" : 24000,
#                 "qovurma lagmon" : 24000
#             },
#             'kabob' : 30000,
#             'norin' : 25000,
#             'shashlik' : {
#                 "qiyma" : 18000,
#                 "jaz" : 20000
#             }
            
#         },
#         "suyuq ovqatlar" : {
#             "shorva" : {
#                 "qaynatma shorva" : 22000,
#                 "ko'za sho'rva" : 28000,
#             },
#             "mastava" : 24000,
#         }
#     },
# }

# mijoz = input("Assalomu alaykum Menyu bilan tanishasizmi? /ha yoki /yoq kabi belgilang:  ")

# if mijoz == '/ha':
#     for i in restoran["taomlar"].keys():
#         print(i)
#     taom = input("Nima buyurasiz: Suyuq /s, quyuq /q : ")
#     if taom == '/q':
#         for j in restoran["taomlar"]['quyuq ovqatlar'].keys():
#             print(j)
#         t = input("Biror taom tanlang: ")
#         for a ,b in restoran["taomlar"]['quyuq ovqatlar'].items():
#             if a == t:
#                 print(f"{a} ning narxi {b} som")
#             else:
#                 print(f"Mavjud taom: {a}")
#     elif taom == '/s':
#         for j in restoran["taomlar"]['suyuq ovqatlar'].keys():
#             print(j)
#         t = input("Biror taom tanlang: ")
#         for a ,b in restoran["taomlar"]['suyuq ovqatlar'].items():
#             if a == t:
#                 print(f"{a} ning narxi {b} som")
#             else:
#                 print(f"Mavjud taom: {a}")
                
                
                
# 2. Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar
#  haqida ma'lumotlarni lug'at ko'rinishida saqlang. Har bir davlat haqida
#  ma'lumotni konsolga chiqaring.

# davlatlar = {
#     "Uzbekistan" : {
#         "Aholisi" : 36000000,
#         "Maydoni" : 448978,
#         "Poytaxti" : "Tashkent",
#         "Mintaqa" : "Asia",      
#     },
#     "Portugal" : {
#         "Aholisi" : 32500000,
#         "Maydoni" : 651564,
#         "Poytaxti" : "Lissabon",
#         "Mintaqa" : "Yevropa",  
#     },
#     "Turkiya" : {
#         "Aholisi" : 1854621,
#         "Maydoni" : 462314,
#         "Poytaxti" : "Anqara",
#         "Mintaqa" : "Yervropa",         
#     },
#     "Ispaniya" : {
#         "Aholisi" : 1562244,
#         "Maydoni" : 65412,
#         "Poytaxti" : "Madrid",
#         "Mintaqa" : "Yevropa",       
#     }
# }
# for i in davlatlar:
#     print(i)
# a = input("Qaysi davlat haqida ma'lumot olmoqchisiz ")
# if a == 'Uzbekistan':
#     for k,l in davlatlar["Uzbekistan"].items():
#         print(f"{k} -- {l}")
# elif a == 'Portugal':
#     for k,l in davlatlar["Portugal"].items():
#         print(f"{k} -- {l}")
# elif a == 'Turkiya':
#     for k,l in davlatlar["Turkiya"].items():
#         print(f"{k} -- {l}")
# elif a == 'Ispaniya':
#     for k,l in davlatlar["Ispaniya"].items():
#         print(f"{k} -- {l}")
# else:
#     print("Bunday davlat bizda yoq")