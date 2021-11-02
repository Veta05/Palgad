from random import*
inimesed=["Anna","Aave","Darja","Vladislav","Semjon","Kirill","Valentina"]
palgad=[10000,850,2000,5000,4000,2652,584]
def sisesta_andmed(i,p):
    N=4
    for n in range(N):
        inimene=input("Palun sisesta töötaja nimi: ")
        i.append(inimene)
        p.append(randint(100,10000))
    return i,p

def andmed_ekraanile(i,p):
    N=len(i)
    for n in range(N):
        print(i[n],"-",p[n])

def kustutamine(i,p):
    nimi=input("Sisesta nimi, keda vaja kustutada: ")
    n=i.count(nimi)
    abi_list=[]
    if n>0:
        t=0
        for e in range(len(i)):
            if i[e]==nimi:
                t+=1
                abi_list.append(int(e)) #spisok indexov
                print(t,". ",i[e],"-", p[e])
        j=int(input("Järjekordne number: ")) 
        i.pop(abi_list[j-1])
        p.pop(abi_list[j-1])
        andmed_ekraanile(i,p)
    return i,p

def otsi(i,p):
    nimi=input("Sisesta nimi, kelle palk sa tahad vaadata: ")
    n=i.count(nimi)
    if n>0:
        t=0
        for e in range(len(i)):
            if i[e]==nimi:
                t+=1
                print(t,". ",i[e], "-",p[e])

def suurim_palk(i,p):
    suurim=max(p)
    n=p.count(suurim)
    abi_list=[]
    for e in range(len(p)):
        if p[e]==suurim:
            abi_list.append(int(e))
            print(i[e],"-", p[e])
    return i,p

def vaiksem_palk(i,p):
    vaiksem=min(p)
    n=p.count(vaiksem)
    abi_list=[]
    for e in range(len(p)):
        if p[e]==vaiksem:
            abi_list.append(int(e))
            print(i[e],"-",p[e])
    return i,p

def sorteerimine(i,p,v):
    N=len(p)
    if v==1:
        for n in range(0,N):
            for m in range(n,N):
                if p[n]<p[m]:
                    abi=p[n]
                    p[n]=p[m]
                    p[m]=abi
                    abi=i[n]
                    i[n]=i[m]
                    i[m]=abi
        andmed_ekraanile(i,p)
    else:
        for n in range(0,N):
            for m in range(n,N):
                if p[n]>p[m]:
                    abi=p[n]
                    p[n]=p[m]
                    p[m]=abi
                    abi=i[n]
                    i[n]=i[m]
                    i[m]=abi
        andmed_ekraanile(i,p)

def vordsed_palgad(i,p):
    N=len(p)
    dublikaatid=[x for x in palgad if palgad.count(x)>1]
    dublikaatid=list(set(dublikaatid))
    print(dublikaatid) 
    for palk in dublikaatid:
        n=p.count(palk)
        k=-1
        for j in range(n):
            k=p.index(palk,k+1)
            nimi=i[k]
            print(palk, "saab kätte", nimi)

def rohkem_vahem (i,p,v):
    num=int(input("palk: "))
    abi_list=[]
    t=0
    if v==1:
        for e in range(len(p)):
            if p[e]>num:
                t+=1
                abi_list.append(int(e))
                print(t, ". ", p[e], "-", i[e])
    elif v==2:
        for e in range(len(p)):
            if p[e]<num:
                t+=1
                abi_list.append(int(e))
                print(t, ". ", p[e], "-", i[e])
  
def top3(i,p,v):
    if v==1:
        p.sort()
        p.reverse()
        i.sort()
        i.reverse()
        for e in range(0,len(p)):
            if e>=3:
                break
            print(i[e],"-",p[e])
    elif v==2:
        p.sort()
        i.sort()
        for j in range(0,len(p)):
            if j>=3:
                break
            print(i[j],"-",p[j])
            
def keskmine(i,p):
    summa=0
    for palk in p:
        summa+=palk
    summa/=len(p)
    print("Keskmine palk: ",summa)
    for palk in p:
        if palk==summa:
            n=p.index(palk)
            print("Saab kätte: ",i[n])
        else:
            print("Selliseid inimesi pole")

def netto(i,p):
    tulumaks=0
    x=0
    for e in range(len(p)):
        if p[e]<=1200:
            x=int(p[e])
            tulumaks=(x-((x-500)*0.2))
            print(tulumaks,"-", i[e])
        elif p[e]>1200 and p[e]<2099:
            x=int(p[e])
            tulumaks=x-(500-0.55556*(x-1200))*0.2
            print(tulumaks,"-", i[e])
        elif p[e]>2100:
            x=int(p[e])
            tulumaks=x-(x*0.2)
            print(tulumaks,"-", i[e])
            
def sort_nimi_jargi(p,i,v):
    N=len(p)
    if v==1:
        for n in range(0,N):
            for m in range(n,N):
                if p[n]>p[m]:
                    abi=p[n]
                    p[n]=p[m]
                    p[m]=abi
                    abi=i[n]
                    i[n]=i[m]
                    i[m]=abi
        andmed_ekraanile(i,p)
    else:
        for n in range(0,N):
            for m in range(n,N):
                if p[n]<p[m]:
                    abi=p[n]
                    p[n]=p[m]
                    p[m]=abi
                    abi=i[n]
                    i[n]=i[m]
                    i[m]=abi
        andmed_ekraanile(i,p)

def palga_kustutamine(i,p):
    summa=0
    for palk in p:
        summa+=palk
    d=int(summa/len(p))
    print("Keskmine palk: ", d)
    y=0
    while y < len(p):
        if p[y]<d:
            del p[y]
            del i[y]
        else:
            y+=1
    print("All näidatud inimesed, kellel palk on suurem keskmist")
    andmed_ekraanile(i,p)

while True:
    print("a-andmete sisestamine\ne-andmed ekraanile\nk-kustutamine\nmax-kellel on suurim palk\nmin-kellel on väiksem palk\nsort-sorteerime\nv-võrdsed palgad\notsi-otsi palka nime järgi\nrv-rohkem või vähem\ntop-kõige rikkamad ja kõige vaesemad\nkesk-keskmine palk\nnetto-palk mis saab kätte\nsrt-Sorteerime nimede järgi\npk-kustutamine alla keskmist palgast")
    valik=input()
    if valik.lower()=="a":
        inimesed,palgad=sisesta_andmed(inimesed,palgad)
    elif valik.lower()=="e":
        andmed_ekraanile(inimesed, palgad)
    elif valik.lower()=="k":
        inimesed,palgad=kustutamine(inimesed,palgad)
    elif valik.lower()=="otsi":
        inimesed,palgad=otsi(inimesed,palgad)
    elif valik.lower()=="max":
         suurim_palk(inimesed,palgad)
    elif valik.lower()=="min":
        vaiksem_palk(inmesed,palgad)
    elif valik.lower()=="sort":
        sorteerimine(inimesed, palgad, int(input("1-kahaneb,2-kasvab: ")))
    elif valik.lower()=="srt":
        sort_nimi_jargi(inimesed,palgad, int(input("1 - A--> Z, 2 - Z---> A: ")))
    elif valik.lower()=="v":
        vordsed_palgad(inimesed, palgad)
    elif valik.lower()=="rv":
        rohkem_vahem(inimesed,palgad, int(input("1-Suurem kui, 2-Väiksem kui: ")))
    elif valik.lower()=="top":
        top3(palgad,inimesed, int(input("1. 3 Kõige rikkamad, 2. 3 Kõige vaesemad: ")))
    elif valik.lower()=="kesk":
        keskmine(inimesed,palgad)
    elif valik.lower()=="netto":
        netto(inimesed,palgad)
    elif valik.lower()=="pk":
        palga_kustutamine(inimesed,palgad)
    else:
        break
