import sqlite3
from random import shuffle
def itilizate():
    try:
        #kreye yon baz de done
        conn = sqlite3.connect("Quizoo.db")
        cur = conn.cursor()
        req1 ="create table Itilizate(Nom text integer primary key, modpas text)"
        cur.execute(req1)
        conn.commit()
        cur.close()
        conn.close()

    except sqlite3.Error as error:
        print("Pa gen koneksyon")


def anrejistre_iti(non, modpas):
    conn = sqlite3.connect("Quizoo.db")
    cur = conn.cursor()
    sql = "INSERT INTO Itilizate(Nom, modpas) VALUES (?, ?)"
    vale= (non, modpas)
    cur.execute(sql, vale)
    conn.commit()
    cur.close()
    conn.close()

def koneksyon(non, modpas):
    conn = sqlite3.connect("Quizoo.db")
    cur = conn.cursor()
    done = "select * from Itilizate"
    cur.execute(done)
    lis_iti = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    for i in lis_iti:
        if i[0]==non and i[1]==modpas:
            bn= True
        else:
            bn= False
    return bn
def kreye_kwiz(nimerokwiz, nonkwiz, kantitekesyon):
    try:#sa e pou kreye quiz lan.
        conn = sqlite3.connect("Quizoo.db")
        cur = conn.cursor()
        kwiz ="Create table Quiz(nime integer primary key, nomkwiz text, kantitekes integer)"
        kesyon ="create table kesyon(id integer primary key autoincrement, nime integer, tit text, repons1 text, repons2 texte, repons3 text, foreign key(nime) references Quiz(nime) )"
        cur.execute(kwiz)
        cur.execute(kesyon)
        conn.commit()
        cur.close
        conn.close()
    except sqlite3.Error as error:
        print("Pa gen koneksyon")
    
    try:
        conn = sqlite3.connect("Quizoo.db")
        cur = conn.cursor()
        req ="insert into Quiz(nime, nomkwiz, kantitekes) Values(?, ?, ?)"
        vale_req =(nimerokwiz, nonkwiz, kantitekesyon)
        cur.execute(req, vale_req)
        conn.commit()
        cur.close()
        conn.close()
    except sqlite3.Error as error:
        print("Pa gen koneksyon")
    try:
        for i in range(kantitekesyon):
            Question = input("Antre kesyon an: ")
            print("\nAntre 3 repons pou kesyon ou an. Antre bon repons lan avan")
            
    
            rep1 =input("Antre premye repons lan (bon repons): ")
            rep2 =input("Antre dezyem repons lan (fo): ")
            rep3 =input("Antre twazyem repons lan (fo): ")
        
            conn = sqlite3.connect("Quizoo.db")
            cur = conn.cursor()

            kes ="insert into kesyon(nime, tit, repons1, repons2, repons3) values(?, ?, ?, ?, ?)"
            v=(nimerokwiz, Question, rep1, rep2, rep3)
            cur.execute(kes, v)
            conn.commit()
            cur.close()
            conn.close()
    except sqlite3.Error as error:
        print("Pa gen koneksyon")

def jwe_kwiz():
    try:
        conn = sqlite3.connect("Quizoo.db")
        cur = conn.cursor()
    except sqlite3.Error as error:
        print("Pa gen koneksyon")
    try:
        non_kwiz ="select nime, nomkwiz from Quiz"
        cur.execute(non_kwiz)
        liskwiz = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()

        # {"1": {"id":4,"...."} }
        ch = {}
        for idx, v in enumerate(liskwiz):
            ch[idx] = v
            print(f"{idx}-{v[1]}")
    except sqlite3.Error as error:
        print("Pa gen koneksyon...")
    print()
    chwa =input("fe yon chwa: ")
    for v, k in ch.items():
        if int(chwa)==v:
            idk =k[0]
    try:
        conn = sqlite3.connect("Quizoo.db")
        cur = conn.cursor()
    except sqlite3.Error as error:
        print("Pa gen koneksyon...")
    try:
        non=f"select tit, repons1, repons2, repons3 from Quiz, kesyon where Quiz.nime={idk} and Quiz.nime=kesyon.nime"
        cur.execute(non)
        liske = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
    except sqlite3.Error as error:
        print("Pa gen koneksyon....")
    
    p="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    q=0
    for i in liske:
        q +=1
        c=0
        print(f"{p[q]}-{i[0]}")
        lis=[]
        for b in range(len(i)):
            #print(i)
            if b<=0:
                continue
            else:
                lis.append(i[b])
                #print(f"{c-2}-{i[b]}")
        kl= sorted(lis)
        for n in sorted(lis):
            print(f"{c}-{n}")
            c+=1
        qe = input("fe yon chwa: ")
    
        if kl[int(qe)]== i[1]:
            print("Tre byen!\nOu genyen")
        else:
            print("Ou pedi")
        q+=1
        print()