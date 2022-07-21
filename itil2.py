import sqlite3
from itil import itilizate
from itil import anrejistre_iti
import itil

def sko_jwe():
    try:
        conn = sqlite3.connect("Quizoo.db")
        cur = conn.cursor()
    except sqlite3.Error as error:
        print("Pa gen koneksyon")
    try:
        tab_sko= "create table sko(nimero integer primary key autoincrement,Nom text,sko integer, foreign key(Nom)  references Itilizate(Nom) )"
        cur.execute(tab_sko)
        conn.commit()
        cur.close()
        conn.close()
    except sqlite3.Error as error:
        print("Pa gen koneksyon")

def retou_meniPrensipal():
    retou = input("Peze 1 Pou retounen nan meni principal: ")
    if retou =='1':
        meniPrensipal()
    else:
        retou_meniPrensipal()

def meniPrensipal():
    print("+___________________________________________________________________ +")
    print("+                                                                    +")
    print("+                                                                    +")
    print("+                                                                    +")
    print("+                                                                    +")
    print("+                 BYENVINI SOU PLATFOM QUIZOO AN                     +")
    print("+                       1-Kreye Kwiz                                 +")
    print("+                       2-Jwe Kwiz                                   +")
    print("+                       3-Afiche Sko                                 +")
    print("+                       4-Kite                                       +")
    print("+                                                                    +")
    print("+                                                                    +")
    print("+                                                                    +")
    print("+____________________________________________________________________+")

    chwa =input("\nChwazi youn nan opsyon: ")
    print()

    if chwa =="1":
        nimerokwiz =int(input("Antre Nimero kwiz lan: "))
        nonkwiz= input("Antre non kwiz lan: ")
        kntite =int(input("Antrete Kantite kesyon an: "))
        itil.kreye_kwiz(nimerokwiz, nonkwiz, kntite)
        retou_meniPrensipal()
    elif chwa =='2':
        print("Ou pral jwe yon kwiz \n")
        itil.jwe_kwiz()
        retou_meniPrensipal()
    elif chwa=='3':
       pass
       retou_meniPrensipal()
    elif chwa =="4":
        exit()

