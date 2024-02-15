 #import matplotlib.pyplot as plt

#algorithme pour filtrer les produits
class produit():
    def __init__(self):
        self.nom=None
        self.type=None
        self.prix=None
        self.date=None
        self.uid=None
        self.marque=None
        self.quantite=None
        self.poids=None
        self.nb_commande=None
        self.avis=None

def nombre_lettre(pos_curseur: int): #permet de calculer le nombre de lettre d'un mot dans le fichier
    fichier=open("catalogue.txt", "r+")
    nb_lettre: int
    nb_lettre=0
    fichier.seek(pos_curseur, 0)
    while((fichier.read(1))!="-"):
        nb_lettre+=1
    fichier.close()
    return nb_lettre



    
    
def specification_ligne(ligne: int): #permet de positioner le curseur a une ligne dans le fichier
    fichier=open("catalogue.txt", "r+")
    position_curseur: int
    current_line=1
    while(current_line!=ligne):
        a=fichier.readline(1)
        while(a!="#"):
            a=fichier.readline(1)
        fichier.seek(fichier.tell()+1, 0)
        current_line+=1
    position_curseur=fichier.tell()
    fichier.close
    return position_curseur





def specification_ligne_2(ligne: int): #permet de positioner le curseur a une ligne dans le fichier pour la partie expedition
    fichier=open("catalogue.txt", "r+")
    position_curseur: int
    current_line=1
    while(current_line!=ligne):
        a=fichier.readline(1)
        while(a!="#"):
            a=fichier.readline(1)
        fichier.seek(fichier.tell()+1, 0)
        current_line+=1
    position_curseur=fichier.tell()
    fichier.close
    return position_curseur









#les fonction read_caracteristique permettent de lire chaque caractéristiques d'un produit de la ligne i donnée







def read_uid(num_line):  #permet de lire l'identifiant du rpoduit a la ligne num_line
    pos_curseur=specification_ligne(num_line)
    fichier=open("catalogue.txt", "r+")
    fichier.seek(pos_curseur, 0)
    uid=fichier.readline(nombre_lettre(pos_curseur))
    print(uid)
    fichier.close()
    return uid



def read_name(num_line): #permet de lire le nom du rpoduit a la ligne num_line
    pos_curseur=specification_ligne(num_line)
    fichier=open("catalogue.txt", "r+")
    fichier.seek(pos_curseur+nombre_lettre(pos_curseur)+5, 0)
    position_nom=fichier.tell()
    name=fichier.readline(nombre_lettre(position_nom))
    #print(name)
    fichier.close()
    return name





def read_price(num_line): #permet de lire le prix du rpoduit a la ligne num_line
    pos_curseur=specification_ligne(num_line)
    fichier=open("catalogue.txt", "r+")
    fichier.seek(pos_curseur, 0)
    nb_bar=0
    
    while(nb_bar<10):
        if(fichier.read(1)=="-"):
            nb_bar=nb_bar+1
    price=fichier.readline(nombre_lettre(fichier.tell()))
    #print(price)
    fichier.close()
    return price





def read_weight(num_line):   #permet de lire le poids du rpoduit a la ligne num_line
    pos_curseur=specification_ligne(num_line)
    fichier=open("catalogue.txt", "r+")
    fichier.seek(pos_curseur, 0)
    nb_bar=0
    while(nb_bar<15):
        if(fichier.read(1)=="-"):
            nb_bar=nb_bar+1
    weight=fichier.readline(nombre_lettre(fichier.tell()))
    #print(weight)
    fichier.close()
    return weight






def read_type(num_line): #permet de lire le type du rpoduit a la ligne num_line
    pos_curseur=specification_ligne(num_line)
    fichier=open("catalogue.txt", "r+")
    fichier.seek(pos_curseur, 0)
    nb_bar=0
    while(nb_bar<20):
        if(fichier.read(1)=="-"):
            nb_bar=nb_bar+1
    type=fichier.readline(nombre_lettre(fichier.tell()))
    #print(type)
    fichier.close()
    return type






def read_brand(num_line): #permet de lire la marque du rpoduit a la ligne num_line
    pos_curseur=specification_ligne(num_line)
    fichier=open("catalogue.txt", "r+")
    fichier.seek(pos_curseur, 0)
    nb_bar=0
    while(nb_bar<25):
        if(fichier.read(1)=="-"):
            nb_bar=nb_bar+1
    brand=fichier.readline(nombre_lettre(fichier.tell()))
    #print(brand)
    fichier.close()
    return brand




def read_date(num_line): #permet de lire la date du rpoduit a la ligne num_line
    pos_curseur=specification_ligne(num_line)
    fichier=open("catalogue.txt", "r+")
    fichier.seek(pos_curseur, 0)
    nb_bar=0
    while(nb_bar<30):
        if(fichier.read(1)=="-"):
            nb_bar=nb_bar+1
    date=fichier.readline(nombre_lettre(fichier.tell()))
    #print(date)
    fichier.close()
    return date




def read_qte(num_line):  #permet de lire la quantite du rpoduit a la ligne num_line
    pos_curseur=specification_ligne(num_line)
    fichier=open("catalogue.txt", "r+")
    fichier.seek(pos_curseur, 0)
    nb_bar=0
    while(nb_bar<35):
        if(fichier.read(1)=="-"):
            nb_bar=nb_bar+1
    qte=fichier.readline(nombre_lettre(fichier.tell()))
    #print(qte)
    fichier.close()
    return qte


    

def read_nb_command(num_line):  #permet de lire le nombre de commandes du rpoduit a la ligne num_line
    pos_curseur=specification_ligne(num_line)
    fichier=open("catalogue.txt", "r+")
    fichier.seek(pos_curseur, 0)
    nb_bar=0
    while(nb_bar<40):
        if(fichier.read(1)=="-"):
            nb_bar=nb_bar+1
    nb_command=fichier.readline(nombre_lettre(fichier.tell()))
    #print(nb_command)
    fichier.close()  
    return nb_command




def read_avis(num_line): #permet de lire les avis du rpoduit a la ligne num_line
    pos_curseur=specification_ligne(num_line)
    fichier=open("catalogue.txt", "r+")
    fichier.seek(pos_curseur, 0)
    nb_bar=0
    while(nb_bar<45):
        if(fichier.read(1)=="-"):
            nb_bar=nb_bar+1
    avis=fichier.readline(1)
    #print(avis)
    fichier.close()
    return avis


def read_produit(num_line): #permet de lire un produit a la ligne num_line
    fichier=open("catalogue.txt", "r+")
    red_produit=produit()
    fichier.seek(specification_ligne(num_line), 0) #place le curseur à la position correspondant au numero de ligne
    red_produit.nom=fichier.readline(nombre_lettre(fichier.tell()))
    fichier.seek(10+fichier.tell(), 0)
    red_produit.type=fichier.readline(nombre_lettre(fichier.tell()))
    fichier.seek(10+fichier.tell(), 0)
    red_produit.prix=int(fichier.readline(nombre_lettre(fichier.tell())))
    fichier.seek(10+fichier.tell(), 0)
    red_produit.date=int(fichier.readline(4))
    #fichier.seek(1+fichier.tell(), 0) permet de faire passer le cuseur à la ligne
    fichier.close()
    return red_produit 




def read_produit_2(num_line): #deuxime algo pour lire un produit
    fichier=open("catalogue.txt", "r+")
    red_produit=produit()
    red_produit.uid=read_uid(num_line)
    red_produit.nom=read_name(num_line)
    red_produit.prix=read_price(num_line)
    red_produit.poids=read_weight(num_line)
    red_produit.type=read_type(num_line)
    red_produit.marque=read_brand(num_line)
    red_produit.date=read_date(num_line)
    red_produit.quantite=read_qte(num_line)
    red_produit.nb_commande=read_nb_command(num_line)
    red_produit.avis=read_avis(num_line)
    fichier.close()
    return red_produit




def nb_line(): #permet de claculer le nombre de ligne dans le fichier
    #print("calcul le nombre de ligne du fichier")
    fichier=open("catalogue.txt", "r+")
    a="a"
    nb_line=0
    while(a!="."):
        a=fichier.readline(1)
        if(a=="#"):
            nb_line+=1
    #print("on a exactement {} dans le fichier" .format(nb_line))
    fichier.close()
    return nb_line












#les fonction  de filtre renvoient 0 si elle n'ont trouvé aucuns produits corrrespondant au filtre et renvoie le tableau de produit si elles en ont trouvés


def filtre_date_f(date_min): #permet de filtrer les produit de date superieur à date_min
    fichier=open("catalogue.txt", "r+")
    nbre_ligne=nb_line()
    tableau=[produit]*nbre_ligne
    i=1
    j=0
    
    while(i<=nbre_ligne):
        if(int(read_date(i))>int(date_min)):
            tableau[j]=read_produit_2(i)
            j+=1
        i+=1
    fichier.close()
    if(j==0):
        return 0

    else:
        
        return tableau
  

def filtre_marque_f(marque_voulu): #recupere tous les produit de la marque marque voulu
    fichier=open("catalogue.txt", "r+")
    nbre_ligne=nb_line()
    tableau=[produit]*nbre_ligne
    i=1
    j=0
    
    while(i<=nbre_ligne):
        if(read_brand(i)==marque_voulu):
            tableau[j]=read_produit_2(i)
            j+=1
        i+=1
    fichier.close()
    if(j==0):
        return 0

    else:
        return tableau




def filtre_categorie_f(type_voulu): #recupere tous les produit de categorie type voulu
    fichier=open("catalogue.txt", "r+")
    nbre_ligne=nb_line()
    tableau=[produit]*nbre_ligne
    i=1
    j=0
    
    while(i<=nbre_ligne):
        if(read_type(i)==type_voulu):
            tableau[j]=read_produit_2(i)
            j+=1
        i+=1
    fichier.close()
    if(j==0):
        return 0     #retourne 0 dans la mesure ou on atrouvé aucun produit correspondant au filtre

    else:
        return tableau





def filtre_date_marque(date_min: int, marque_voulu):  #recupere tous les produit de date sup à date min et de marque marque voulu
    fichier=open("catalogue.txt", "r+")
    nbre_ligne=nb_line()
    tableau=[produit]*nbre_ligne
    i=1
    j=0
    while(i<=nbre_ligne):
        if(read_brand(i)==marque_voulu and int(read_date(i))>=date_min):
            tableau[j]=read_produit_2(i)
            j+=1
        i+=1
    fichier.close()
    if(j==0):
        return 0

    else:
        return tableau






def filtre_date_categorie(date_min: int, type_voulu):   #recupere tous les produit de date sup à date min et de type type voulu
    fichier=open("catalogue.txt", "r+")
    nbre_ligne=nb_line()
    tableau=[produit]*nbre_ligne
    i=1
    j=0
    while(i<=nbre_ligne):
        if(read_type(i)==type_voulu and int(read_date(i))>=date_min):
            tableau[j]=read_produit_2(i)
            j+=1
        i+=1
    fichier.close()
    if(j==0):
        return 0

    else:
        return tableau




def filtre_categorie_marque(type_voulu, marque_voulu): #recupere tous les produit de type type voulu et de marque voulu
    fichier=open("catalogue.txt", "r+")
    nbre_ligne=nb_line()
    tableau=[produit]*nbre_ligne
    i=1
    j=0
    while(i<=nbre_ligne):
        if(read_brand(i)==marque_voulu and read_type(i)==type_voulu):
            tableau[j]=read_produit_2(i)
            j+=1
        i+=1
    fichier.close()
    if(j==0):
        return 0

    else:
        return tableau





def filtre_categorie_marque_date(type_voulu, marque_voulu, date_min: int): #recupere tous les produit de type type voulu et de marque voulu et de date superieur à date min
    fichier=open("catalogue.txt", "r+")
    nbre_ligne=nb_line()
    tableau=[produit]*nbre_ligne
    i=1
    j=0
    while(i<=nbre_ligne):
        if(read_brand(i)==marque_voulu and read_type(i)==type_voulu and int(read_date(i))>=date_min):
            tableau[j]=read_produit_2(i)
            j+=1
        i+=1
    fichier.close()
    if(j==0):
        return 0

    else:
        return tableau


def read_file(): #fonction qui permet de recuperer  les informations de tous les articles disponible
    fichier=open("catalogue.txt", "r+")
    nbre_ligne=nb_line()
    tableau=[produit]*(nbre_ligne)
    i=1
    while(i<=nbre_ligne):
        tableau[i-1]=read_produit_2(i)
        i+=1
        
    fichier.close()
    return tableau

def size_tableau(tableau): #fonction qui calucule la taillle d'un tableau
    
    i=0
    size=nb_line()
    print(size)
    while(i<size):
        if((type(tableau[i]))==type):
            break
        i=i+1
            
    return i













#algorithme de tri decroissant des produit en fonction du nombre de commande , de la quantite et des avis

def tri_quantite_f(tableau): # cette fonction permet de trier en fonction de la quantité de facon croissante un tableau donné 

    i=0
    a=size_tableau(tableau)
    print("la taillle est {}" .format(a))
    
    
    
    nv_tableau=[produit]*nb_line()
    while(i<=a-1):
        place=0
        j=0
        while(j<=a-1):
            if(int(tableau[j].quantite)<int(tableau[i].quantite)):
                place+=1
            j+=1
        print(place)
        
        while(type(nv_tableau[place])!=type): #cette boucle while permet de gerer les potentielles erreures cause par les egalites lors de la comparaison
            place+=1
        nv_tableau[place]=tableau[i]
        i=i+1
        
    
    return nv_tableau


def tri_nb_command_f(tableau): #cette fonction permet de trier en fonction du nombre de commande de facon croissante un tableau donné
    i=0
    a=size_tableau(tableau)
    print("la taillle est {}" .format(a))
    
    
    
    nv_tableau=[produit]*nb_line()
    while(i<=a-1):
        place=0
        j=0
        while(j<=a-1):
            if(int(tableau[j].nb_commande)<int(tableau[i].nb_commande)):
                place+=1
            j+=1
        print(place)
        while(type(nv_tableau[place])!=type): #cette boucle while permet de gerer les potentielles erreures cause par les egalites lors de la comparaison
            place+=1
        nv_tableau[place]=tableau[i]
        i=i+1
        
    
    return nv_tableau




def tri_avis_f(tableau): #cette fonction permet de trier en fonction des avis des produit de facon croissante
    i=0
    a=size_tableau(tableau)
    print("la taillle est {}" .format(a))
    
    
    
    nv_tableau=[produit]*nb_line()
    while(i<=a-1):
        place=0
        j=0
        while(j<=a-1):
            if(int(tableau[j].avis)<int(tableau[i].avis)):
                place+=1
            j+=1
        print(place)
        while(type(nv_tableau[place])!=type): #cette boucle while permet de gerer les potentielles erreures cause par les egalites lors de la comparaison
            place+=1
        nv_tableau[place]=tableau[i]
        i=i+1
        
    
    return nv_tableau


def best_produit_marque(marque):  #choisit le meilleur produit pour chaque marque
    tableau=filtre_marque_f(marque)
    size=size_tableau(tableau)
    
    ind_best_prduit=0
    i=1
    while(i<size):
        if((int(tableau[i].nb_commande)*int(tableau[i].prix))>(int((tableau[ind_best_prduit].nb_commande))*int((tableau[ind_best_prduit].prix)))):
            ind_best_prduit=i
        i+=1
    return tableau[ind_best_prduit]




def best_produit_categorie(categorie): #choisit le meilleur produit pour chaque categorie
    tableau=filtre_categorie_f(categorie)
    size=size_tableau(tableau)
    
    ind_best_prduit=0
    i=1
    while(i<size):
        if((int(tableau[i].nb_commande)*int(tableau[i].prix))>(int((tableau[ind_best_prduit].nb_commande))*int((tableau[ind_best_prduit].prix)))):
            ind_best_prduit=i
        i+=1
    return tableau[ind_best_prduit]






def worst_produit_marque(marque): #pire produit pour chaque marque
    tableau=filtre_marque_f(marque)
    size=size_tableau(tableau)
    
    ind_worst_prduit=0
    i=1
    while(i<size):
        if((int(tableau[i].nb_commande)*int(tableau[i].prix))<(int((tableau[ind_worst_prduit].nb_commande))*int((tableau[ind_worst_prduit].prix)))):
            ind_worst_prduit=i
        i+=1
    return tableau[ind_worst_prduit]




def worst_produit_categorie(categorie): #pire produit pour chaque categorie
    tableau=filtre_categorie_f(categorie)
    size=size_tableau(tableau)
    
    ind_worst_prduit=0
    i=1
    while(i<size):
        if((int(tableau[i].nb_commande)*int(tableau[i].prix))<(int((tableau[ind_worst_prduit].nb_commande))*int((tableau[ind_worst_prduit].prix)))):
            ind_worst_prduit=i
        i+=1
    return tableau[ind_worst_prduit]






def calcul_total_vente():
    tableau=read_file()
    size=size_tableau(tableau)
    i=0
    total_vente=0
    while(i<size):
        total_vente+=(int(tableau[i].nb_commande)*int(tableau[i].prix))
        i+=1
    return total_vente





def tableau_categorie(): #permet de creer un tableau contenant toute les marques
    tableau=read_file()
    cat_preced=tableau[0].type
    size=size_tableau(tableau)
    i=1
    tab_categorie=[cat_preced]
    while(i<size):
        j=0
        for a in tab_categorie:
            if(a==tableau[i].type):
                j=1
        if(j==0):
            tab_categorie.append(tableau[i].type)
        i=i+1
    print(len(tab_categorie))
    return tab_categorie



def tableau_marque():#crée un tableau contenant toutes les marques
    tableau=read_file()
    marque_preced=tableau[0].marque
    size=size_tableau(tableau)
    i=1
    tab_marque=[marque_preced]
    while(i<size):
        j=0
        for a in tab_marque:
            if(a==tableau[i].marque):
                j=1
        if(j==0):
            tab_marque.append(tableau[i].marque)
        i=i+1
    print(len(tab_marque))
    return tab_marque


def nb_produit_categorie():#cree un tableau a deux dimension contenan pour chaque categorie le nombre de produit present
    
    tableau=read_file()
    tab_categorie=tableau_categorie()
    tab_produit_categorie=[]
    
    
    for categorie in tab_categorie:
        nb_produit=0
        for produit in tableau:
            if(produit.type==categorie):
                nb_produit+=int(produit.quantite)
        donnee_graph=[categorie, nb_produit]
        
        tab_produit_categorie.append(donnee_graph)
    return tab_produit_categorie


def nb_vente_marque(): #pemet de creer un tableau  a deux dimension contenant pour chaque marque le nombre de total de commandes effectue
    
    tableau=read_file()
    tab_marque=tableau_marque()
    tab_vente_marque=[]
    
    
    for marque in tab_marque:
        nb_vente=0
        for produit in tableau:
            if(produit.marque==marque):
                nb_vente+=int(produit.nb_commande)
        donnee_graph=[marque, nb_vente]
        
        tab_vente_marque.append(donnee_graph)
    return tab_vente_marque
def rechercher_produit(nom_chercher):
    trouve=0
    i=1
    
    while(trouve==0):
        current=read_produit_2(i)
        if(current.nom==nom_chercher):
            trouve=1
        i+=1

    
    return current
def rechercher_indice_produit(nom_chercher):
    trouve=0
    i=1
    
    while(trouve==0):
        current=read_produit_2(i)
        if(current.nom==nom_chercher):
            trouve=1
            break
        i+=1
    return i


    




        

"""
actual_product=produit()
actual_product=read_produit(2)
if(actual_product.date>2018):
    print("on en a un !!")
else:
    print("on en a pas un")"""
#read_weight(1)






# autre chose
"""tableau=[produit]*nb_line()

tableau=read_file()
print(tableau[0].nom)
print(tableau[1].nom)
tableau=read_file()
tableau=tri_quantite_f(tableau)
print(tableau[0].nom)
print(tableau[1].nom)
print(tableau[2].nom)
print(tableau[3].nom)
print(tableau[4].quantite)"""

#total=tableau_marque()
#print(total)
print(rechercher_indice_produit("iphone12"))


