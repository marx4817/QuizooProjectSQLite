from itil import itilizate
from itil import anrejistre_iti
import itil
import itil2
import getpass

# print(b)
# itil.kreye_kwiz(1, "Informatique", 3)
#itil.jwe_kwiz()
#itil2.sko_jwe()
#itil2.retou_meniPrensipal()

def premyePaj():
    print("+___________________________________________________________________ +")
    print("+                                                                    +")
    print("+                                                                    +")
    print("+                                                                    +")
    print("+                                                                    +")
    print("+                 BYENVINI SOU PLATFOM QUIZOO AN                     +")
    print("+                       1-Konekte                                    +")
    print("+                       2-Kreye Kont                                 +")
    print("+                       3-Kite                                       +")
    print("+                                                                    +")
    print("+                                                                    +")
    print("+                                                                    +")
    print("+                                                                    +")
    print("+____________________________________________________________________+")

    chwa =input("\nChwazi youn nan opsyon: ")
    print()

    if chwa =="1":
        nonIti =input("Antre non ou svp: ")
        modpas=getpass.getpass("Antre yon modpas: ")
        b =itil.koneksyon(nonIti, modpas)
        if b== True:
            itil2.meniPrensipal()
        
    elif chwa =='2':
        print("Ou pral kreye yon kont\n")
        non =input("Antre non ou svp: ")
        modpas_iti=getpass.getpass("Antre yon modpas: ")
        itilizate()
        anrejistre_iti(non, modpas_iti)
        itil2.meniPrensipal()
    elif chwa=='3':
        exit()
        
premyePaj()

    