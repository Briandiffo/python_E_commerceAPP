from algorithme_gestion import *
import tkinter
#from filtre import *
from tkinter import*
from tkinter import ttk
#import matplotlib.pyplot as plt



from turtle import title
nbre_produit: int
app=tkinter.Tk()
app.title("acceuil")
app.geometry("600x520")


onglet=ttk.Notebook(app)
onglet1=ttk.Frame(onglet)
onglet2=ttk.Frame(onglet)
onglet3=ttk.Frame(onglet)
onglet4=ttk.Frame(onglet)

onglet.add(onglet1, text="ajouter un produit")
onglet.add(onglet2, text="catalogue")
onglet.add(onglet3, text="statistique")
onglet.add(onglet4, text="preparer commandes")
onglet.pack(expand=1, fill="both")




#algorithme pour mettre une image de fond
c=Canvas(onglet1, bg="sky blue", height=200, width=200)
filename=tkinter.PhotoImage(file="image.png")
background_label=tkinter.Label(onglet1, image=filename)
background_label.place(x=0, y=0, relheight=1, relwidth=1)

c=Canvas(onglet2, bg="sky blue", height=200, width=200)
filename2=tkinter.PhotoImage(file="image.png")
background_label=tkinter.Label(onglet2, image=filename2)
background_label.place(x=0, y=0, relheight=1, relwidth=1)

c=Canvas(onglet3, bg="sky blue", height=200, width=200)
filename3=tkinter.PhotoImage(file="image.png")
background_label=tkinter.Label(onglet3, image=filename3)
background_label.place(x=0, y=0, relheight=1, relwidth=1)








class produit():
    def __init__(self):
        self.nom=None
        self.prix=None
        self.poids=None
        self.type=None
        self.marque=None
        self.date=None
        self.uid=None
        self.quantite=None
        self.nb_commande=None
        self.avis=None
"""liste_produit=[produit]*100
produit_initial=produit()
for i in range(0, 99):
    liste_produit[i]=produit_initial"""


def preparer_commande():
    fichier=open("catalogue.txt", "r+")
    nom_commande=nom_produit.get()
    quantite_commande=int(quantite_produit.get())
    tableau=read_file()
    for produit in tableau:
        if(produit.nom==nom_commande):
            break
    data=fichier.readlines()
    #search_text=str(produit.uid+"-----"+produit.nom+"-----"+str(produit.prix)+"-----"+str(produit.poids)+"-----"+produit.type+"-----"+produit.marque+"-----"+str(produit.date)+"-----"+str(produit.quantite)+"-----"+str(produit.nb_commande)+"-----"+str(produit.avis)+"#")
    data[rechercher_indice_produit(nom_commande)-1]=str(produit.uid+"-----"+produit.nom+"-----"+str(produit.prix)+"-----"+str(produit.poids)+"-----"+produit.type+"-----"+produit.marque+"-----"+str(produit.date)+"-----"+str(int(produit.quantite)-int(quantite_commande))+"-----"+str(int(produit.nb_commande)+int(quantite_commande))+"-----"+str(produit.avis)+"#\n")
    
    #data.replace(produit.uid+"-----"+produit.nom+"-----"+str(produit.prix)+"-----"+str(produit.poids)+"-----"+produit.type+"-----"+produit.marque+"-----"+str(produit.date)+"-----"+"10"+"-----"+str(produit.nb_commande)+"-----"+str(produit.avis)+"#",
    #produit.uid+"-----"+produit.nom+"-----"+str(produit.prix)+"-----"+str(produit.poids)+"-----"+produit.type+"-----"+produit.marque+"-----"+str(produit.date)+"-----"+str(10-quantite_commande)+"-----"+str(int(produit.nb_commande)+quantite_commande)+"-----"+str(produit.avis)+"#")
    """print(search_text)
    print(replace)
    data=data.replace(str(search_text), str(replace))
    fichier.close()"""
    
    fichier=open("catalogue.txt", "w+")
    #fichier.truncate(0)
    fichier.writelines(data)
    print("ajoute")
    fichier.close()
    


def modification_produit():
    nom=nom_produit.get()
    quantite=quantite_produit.get()



def rempli():
    nv_produit=produit()
    nv_produit.nom=nom.get()
    nv_produit.type=categorie.get()
    nv_produit.marque=marque.get()
    nv_produit.prix=int(prix.get())
    nv_produit.poids=int(poids.get())
    nv_produit.date=int(annee.get())
    nv_produit.nb_commande=int(nb_commande.get())
    nv_produit.uid=uid.get()
    nv_produit.avis=int(avis.get())
    nv_produit.quantite=int(quantite.get())
    
    fichier=open("catalogue.txt", "r+")
    pos=specification_ligne(nb_line()+1)
    fichier.seek(pos, 0)
    fichier.write(nv_produit.uid)
    fichier.write("-----")
    fichier.write(nv_produit.nom)
    fichier.write("-----")
    fichier.write(str(nv_produit.prix))
    fichier.write("-----")
    fichier.write(str(nv_produit.poids))
    fichier.write("-----")
    fichier.write(nv_produit.type)
    fichier.write("-----")
    fichier.write(nv_produit.marque)
    fichier.write("-----")
    fichier.write(str(nv_produit.date))
    fichier.write("-----")
    fichier.write(str(nv_produit.quantite))
    fichier.write("-----")
    fichier.write(str(nv_produit.nb_commande))
    fichier.write("-----")
    fichier.write(str(nv_produit.avis))
    fichier.write("#\n")
    fichier.write(".")
    fichier.close()

    
    
    
    """print("les informations du produit sont les suivantes")
    print(nv_produit.nom)
    print(nv_produit.categorie)
    print(nv_produit.marque)
    print(nv_produit.prix)
    print(nv_produit.poids)
    j=0
    while(liste_produit[j]!=produit_initial):
        j=j+1
    print(j)
    #liste_produit[j]=nv_produit
    #tableau_catalogue.insert(parent='', index='end', iid=j, text="Label", values=(nv_produit.nom, nv_produit.marque, nv_produit.categorie, nv_produit.prix))"""
"""   
def afficher():
    k=0
    while(liste_produit[k]!=produit_initial):
        k=k+1
    print(k)
    i=0
    for i in range(0,k):
        tableau_catalogue.insert(parent='', index='end', iid=i, text="Label", values=(liste_produit[k].nom, liste_produit[k].marque, liste_produit[k].categorie, liste_produit[k].prix))
""" 
#liste_produit=read_file()   






#travail avec le tableau catalogue
"""def insertion():
    tableau=read_file()
    k=size_tableau(tableau)
    
    
    i=0
    while(i<k):
        
        tableau_catalogue.insert(parent='', index='end', iid=i, text="Label", values=(tableau[i].nom, tableau[i].marque, tableau[i].type, tableau[i].prix))
        i+=1
def insertion_2():
    tableau=read_file()
    k=size_tableau(tableau)
    tableau_catalogue.selection_remove()
    
    selected_item=tableau_catalogue.selection()[0]
    tableau_catalogue.delete(selected_item)"""







#travail avec la zone de texte
def insertion_texte():
    
    tableau=read_file()
    
    
    
    k=size_tableau(tableau)
    i=0
    
    texte.delete("1.0", tkinter.END)
   
    while(i<k):
        print(tableau[i].uid)
        print(tableau[i].nom)
        texte.insert(tkinter.INSERT, tableau[i].uid+"-----")
        texte.insert(tkinter.INSERT, tableau[i].nom+"-----")
        texte.insert(tkinter.INSERT, tableau[i].prix+"-----")
        texte.insert(tkinter.INSERT, tableau[i].quantite+"-----")
        texte.insert(tkinter.INSERT, tableau[i].avis+"\n")

        i=i+1


def trier():
    if(filtre_cat_var.get()==1 and radio_var.get()==0 and filtre_annee_var.get()==0 and filtre_marque_var.get()==0):  #permet de filtrer les produits en fonction de leur categorie et ensuite de les trier en fonction du nombre de commande
        cat=categorie_entre.get() # recupere la caracteristique avec laquelle l'utilisateur veut filtrer
        tableau=filtre_categorie_f(cat)
        tableau=tri_nb_command_f(tableau)
    elif(filtre_cat_var.get()==1 and radio_var.get()==1 and filtre_annee_var.get()==0 and filtre_marque_var.get()==0):
        cat=categorie_entre.get()
        tableau=filtre_categorie_f(cat)
        tableau=tri_quantite_f(tableau)
    elif(filtre_cat_var.get()==1 and radio_var.get()==2 and filtre_annee_var.get()==0 and filtre_marque_var.get()==0):
        cat=categorie_entre.get()
        tableau=filtre_categorie_f(cat)
        tableau=tri_avis_f(tableau)
    elif(filtre_cat_var.get()==1 and radio_var.get()==3 and filtre_annee_var.get()==0 and filtre_marque_var.get()==0):
        cat=categorie_entre.get()
        tableau=filtre_categorie_f(cat)
        




    elif(filtre_marque_var.get()==1 and radio_var.get()==0 and filtre_cat_var.get()==0 and filtre_annee_var.get()==0):
        cat=marque_entre.get()
        tableau=filtre_marque_f(cat)
        tableau=tri_nb_command_f(tableau)
    elif(filtre_marque_var.get()==1 and radio_var.get()==1 and filtre_cat_var.get()==0 and filtre_annee_var.get()==0):
        cat=marque_entre.get()
        tableau=filtre_marque_f(cat)
        tableau=tri_quantite_f(tableau)
    elif(filtre_marque_var.get()==1 and radio_var.get()==2 and filtre_cat_var.get()==0 and filtre_annee_var.get()==0):
        cat=marque_entre.get()
        tableau=filtre_marque_f(cat)
        tableau=tri_avis_f(tableau)
    elif(filtre_marque_var.get()==1 and radio_var.get()==3 and filtre_cat_var.get()==0 and filtre_annee_var.get()==0):
        cat=marque_entre.get()
        tableau=filtre_marque_f(cat)
        



    elif(filtre_annee_var.get()==1 and radio_var.get()==0 and filtre_cat_var.get()==0 and filtre_marque_var.get()==0):
        cat=annee_entre.get()
        tableau=filtre_date_f(cat)
        tableau=tri_nb_command_f(tableau)
    elif(filtre_annee_var.get()==1 and radio_var.get()==1 and filtre_cat_var.get()==0 and filtre_marque_var.get()==0):
        cat=annee_entre.get()
        tableau=filtre_date_f(cat)
        tableau=tri_quantite_f(tableau)
    elif(filtre_annee_var.get()==1 and radio_var.get()==2 and filtre_cat_var.get()==0 and filtre_marque_var.get()==0):
        cat=annee_entre.get()
        tableau=filtre_date_f(cat)
        tableau=tri_avis_f(tableau)
    elif(filtre_annee_var.get()==1 and radio_var.get()==3 and filtre_cat_var.get()==0 and filtre_marque_var.get()==0):
        cat=annee_entre.get()
        tableau=filtre_date_f(cat)
        

    

    elif(filtre_cat_var.get()==1 and filtre_marque_var.get()==1 and radio_var.get()==0 and filtre_annee_var.get()==0):
        cat_choisi=categorie_entre.get()
        marque_choisi=marque_entre.get()
        tableau=filtre_categorie_marque(cat_choisi, marque_choisi)
        tableau=tri_nb_command_f(tableau)        
    elif(filtre_cat_var.get()==1 and filtre_marque_var.get()==1 and radio_var.get()==1 and filtre_annee_var.get()==0):
        cat_choisi=categorie_entre.get()
        marque_choisi=marque_entre.get()
        tableau=filtre_categorie_marque(cat_choisi, marque_choisi)
        tableau=tri_quantite_f(tableau)
    elif(filtre_cat_var.get()==1 and filtre_marque_var.get()==1 and radio_var.get()==2 and filtre_annee_var.get()==0):
        cat_choisi=categorie_entre.get()
        marque_choisi=marque_entre.get()
        tableau=filtre_categorie_marque(cat_choisi, marque_choisi)
        tableau=tri_avis_f(tableau)
    elif(filtre_cat_var.get()==1 and filtre_marque_var.get()==1 and radio_var.get()==3 and filtre_annee_var.get()==0):
        cat_choisi=categorie_entre.get()
        marque_choisi=marque_entre.get()
        tableau=filtre_categorie_marque(cat_choisi, marque_choisi)
        
    
        

    
    elif(filtre_cat_var.get()==1 and filtre_marque_var.get()==0 and radio_var.get()==0 and filtre_annee_var.get()==1):
        cat_choisi=categorie_entre.get()
        annee_choisi=annee_entre.get()
        tableau=filtre_date_categorie(annee_choisi, cat_choisi)
        tableau=tri_nb_command_f(tableau)        
    elif(filtre_cat_var.get()==1 and filtre_marque_var.get()==0 and radio_var.get()==1 and filtre_annee_var.get()==1):
        cat_choisi=categorie_entre.get()
        annee_choisi=annee_entre.get()
        tableau=filtre_date_categorie(annee_choisi, cat_choisi)
        tableau=tri_quantite_f(tableau)
    elif(filtre_cat_var.get()==1 and filtre_marque_var.get()==0 and radio_var.get()==2 and filtre_annee_var.get()==1):
        cat_choisi=categorie_entre.get()
        annee_choisi=annee_entre.get()
        tableau=filtre_date_categorie(annee_choisi, cat_choisi)
        tableau=tri_avis_f(tableau)
    elif(filtre_cat_var.get()==1 and filtre_marque_var.get()==0 and radio_var.get()==3 and filtre_annee_var.get()==1):
        cat_choisi=categorie_entre.get()
        annee_choisi=annee_entre.get()
        tableau=filtre_date_categorie(annee_choisi, cat_choisi)
        

        


    elif(filtre_cat_var.get()==0 and filtre_marque_var.get()==1 and radio_var.get()==0 and filtre_annee_var.get()==1):
        marque_choisi=marque_entre.get()
        annee_choisi=annee_entre.get()
        tableau=filtre_date_marque(annee_choisi, marque_choisi)
        tableau=tri_nb_command_f(tableau)        
    elif(filtre_cat_var.get()==0 and filtre_marque_var.get()==1 and radio_var.get()==1 and filtre_annee_var.get()==1):
        marque_choisi=marque_entre.get()
        annee_choisi=annee_entre.get()
        tableau=filtre_date_marque(annee_choisi, marque_choisi)
        tableau=tri_quantite_f(tableau)
    elif(filtre_cat_var.get()==0 and filtre_marque_var.get()==1 and radio_var.get()==2 and filtre_annee_var.get()==1):
        marque_choisi=marque_entre.get()
        annee_choisi=annee_entre.get()
        tableau=filtre_date_marque(annee_choisi, marque_choisi)
        tableau=tri_avis_f(tableau)
    elif(filtre_cat_var.get()==0 and filtre_marque_var.get()==1 and radio_var.get()==3 and filtre_annee_var.get()==1):
        marque_choisi=marque_entre.get()
        annee_choisi=annee_entre.get()
        tableau=filtre_date_marque(annee_choisi, marque_choisi)
        



    
        
    elif(filtre_cat_var.get()==1 and filtre_marque_var.get()==1 and radio_var.get()==0 and filtre_annee_var.get()==1):
        cat_choisi=categorie_entre.get()
        marque_choisi=marque_entre.get()
        annee_choisi=annee_entre.get()
        tableau=filtre_categorie_marque_date(cat_choisi, marque_choisi, annee_choisi)
        tableau=tri_nb_command_f(tableau)        
    elif(filtre_cat_var.get()==1 and filtre_marque_var.get()==1 and radio_var.get()==1 and filtre_annee_var.get()==1):
        cat_choisi=categorie_entre.get()
        marque_choisi=marque_entre.get()
        annee_choisi=marque_entre.get()
        tableau=filtre_categorie_marque_date(cat_choisi, marque_choisi, annee_choisi)
        tableau=tri_quantite_f(tableau)
    elif(filtre_cat_var.get()==1 and filtre_marque_var.get()==1 and radio_var.get()==2 and filtre_annee_var.get()==1):
        cat_choisi=categorie_entre.get()
        marque_choisi=marque_entre.get()
        annee_choisi=marque_entre.get()
        tableau=filtre_categorie_marque_date(cat_choisi, marque_choisi, annee_choisi)
        tableau=tri_avis_f(tableau)
    elif(filtre_cat_var.get()==1 and filtre_marque_var.get()==1 and radio_var.get()==3 and filtre_annee_var.get()==1):
        cat_choisi=categorie_entre.get()
        marque_choisi=marque_entre.get()
        annee_choisi=marque_entre.get()
        tableau=filtre_categorie_marque_date(cat_choisi, marque_choisi, annee_choisi)






    # ici le catalogue est afficher sans aucun filtre juste des algorithme de tri
    elif(filtre_cat_var.get()==0 and filtre_marque_var.get()==0 and radio_var.get()==0 and filtre_annee_var.get()==0):
        tableau=read_file()
        tableau=tri_nb_command_f(tableau)
    elif(filtre_cat_var.get()==0 and filtre_marque_var.get()==0 and radio_var.get()==1 and filtre_annee_var.get()==0):
        tableau=read_file()
        tableau=tri_quantite_f(tableau)
    elif(filtre_cat_var.get()==0 and filtre_marque_var.get()==0 and radio_var.get()==2 and filtre_annee_var.get()==0):
        tableau=read_file()
        tableau=tri_avis_f(tableau)        
    
        
    
        
        
    
    k=size_tableau(tableau)
    i=0
    
    texte.delete("1.0", tkinter.END)
   
    while(i<k):
        texte.insert(tkinter.INSERT, str(tableau[i].uid)+"-----") #permet d'inserer une ligne dans la zone de texte de la fenetre tkinter
        texte.insert(tkinter.INSERT, str(tableau[i].nom)+"-----")
        texte.insert(tkinter.INSERT, str(tableau[i].prix)+"-----")
        texte.insert(tkinter.INSERT, str(tableau[i].quantite)+"-----")
        texte.insert(tkinter.INSERT, str(tableau[i].nb_commande)+"-----")
        texte.insert(tkinter.INSERT, str(tableau[i].avis)+"\n")

        i=i+1


def insertion_meilleur_cat():
    prod=produit()
    tableau=tableau_categorie()
    for a in tableau:
        prod=best_produit_categorie(a)
        liste_meilleur_cat.insert(tkinter.INSERT, str(prod.nom)+"---"+str(prod.type)+"---"+str(prod.nb_commande)+"---"+str(prod.prix)+"\n")



def insertion_pire_cat():
    prod=produit()
    tableau=tableau_categorie()
    for a in tableau:
        prod=worst_produit_categorie(a)
        liste_pire_cat.insert(tkinter.INSERT, str(prod.nom)+"---"+str(prod.type)+"---"+str(prod.nb_commande)+"---"+str(prod.prix)+"\n")


def insertion_meilleur_marque():
    prod=produit()
    tableau=tableau_marque()
    for a in tableau:
        prod=best_produit_marque(a)
        liste_meilleur_marque.insert(tkinter.INSERT, str(prod.nom)+"---"+str(prod.marque)+"---"+str(prod.nb_commande)+"---"+str(prod.prix)+"\n")


def insertion_pire_marque():
    prod=produit()
    tableau=tableau_marque()
    for a in tableau:
        prod=worst_produit_marque(a)
        liste_pire_marque.insert(tkinter.INSERT, str(prod.nom)+"---"+str(prod.marque)+"---"+str(prod.nb_commande)+"---"+str(prod.prix)+"\n")

def insertion_total_vente():
    total=calcul_total_vente()
    text_total_ventes.insert(tkinter.INSERT, "le total de ventes réalise est de "+ str(total)+ "euros")
def graphique1(): #trace le graphique des ventes pour chaque marque
    tableau=nb_vente_marque()
    x=[b[0] for b in tableau]
    y=[b[1] for b in tableau]
    plt.bar(x,y)
    plt.show()

def graphique2(): #☻trace le graphique de quantite en stock pour chaque produit
    tableau=nb_produit_categorie()
    x=[b[0] for b in tableau]
    y=[b[1] for b in tableau]
    plt.bar(x,y)
    plt.xlabel("marques")
    plt.ylabel("nombre de vente effectué")
    plt.show()
tableau_produit_expedition=[]
def expedier_produit():#fonction qui ecrit les produit a expedier dans un fichier texte
    print("bonjour")
    nom_produit=nom_produit_exp.get()
    nombre=int(quantite_produit_exp.get())
    nv_produit=rechercher_produit(nom_produit)
    print("yes")
    i=1
    fichier=open("expedition.txt", "r")
    ligne=fichier.readlines()
    fichier.close()
    
    while(i<=nombre):
        ligne.append(str(nv_produit.nom+" "+str(nv_produit.prix)+" "+str(nv_produit.poids)+"\n"))
        i+=1
    fichier=open("expedition.txt", "w")
    fichier.writelines(ligne)
    fichier.close()


        
        

    
    
radio_var=tkinter.IntVar()
filtre_cat_var=tkinter.IntVar()
filtre_annee_var=tkinter.IntVar()
filtre_marque_var=tkinter.IntVar()
bg=PhotoImage(file="image.png")

label_nom=tkinter.Label(onglet1,text="entrez le nom du produit", bg="#609CF2")
nom=tkinter.Entry(onglet1, font="ArialBlack")
label_prix=tkinter.Label(onglet1, text="entrez le prix du produit", bg="#609CF2")
prix=tkinter.Entry(onglet1, font="ArialBlack")
label_poids=tkinter.Label(onglet1, text="entrez le poids du produit", bg="#609CF2")
poids=tkinter.Entry(onglet1, font="ArialBlack")
label_categorie=tkinter.Label(onglet1, text="entrez la categorie du produit", bg="#609CF2")
categorie=tkinter.Entry(onglet1, font="ArialBlack")
label_marque=tkinter.Label(onglet1, text="entrez la marque du produit", bg="#609CF2")
marque=tkinter.Entry(onglet1, font="ArialBlack")
label_annee=tkinter.Label(onglet1, text="entrez l'année  du produit", bg="#609CF2")
annee=tkinter.Entry(onglet1, font="ArialBlack")
label_uid=tkinter.Label(onglet1, text="entrez l'identifiant unique du produit", bg="#609CF2")
uid=tkinter.Entry(onglet1, font="ArialBlack")
label_nb_commande=tkinter.Label(onglet1, text="entrez le nombre de commande du produit", bg="#609CF2")
nb_commande=tkinter.Entry(onglet1, font="ArialBlack")
label_avis=tkinter.Label(onglet1, text="entrez l'avis du produit", bg="#609CF2")
avis=tkinter.Entry(onglet1, font="ArialBlack")
label_quantite_produit=tkinter.Label(onglet1, text="entrez la quantit en stock", bg="#609CF2")
quantite=tkinter.Entry(onglet1, font="ArialBlack")

ajouter=tkinter.Button(onglet1, text="AJOUTER", command=rempli, bg="sky blue")

#enregistrer=tkinter.Button(onglet1, text="ENREGISTRER")
recherche=tkinter.Entry(onglet2, text="rechercher un produit")
label_recherche=tkinter.Label(onglet2, text="rechercher un produit")
catalogue=tkinter.LabelFrame(onglet2, text="Catalogue", borderwidth=3, width=400, height=380, bg="#D0E5F2")



#partie du catalogue correspondant aux filtres
filtre=tkinter.LabelFrame(onglet2, text="filtre", borderwidth=3, width=150, height=200, bg="#6BA5F2")
filtre_marque=tkinter.Checkbutton(filtre, text="marque", offvalue=0, onvalue=1, variable=filtre_marque_var, bg="#F263A6")
marque_entre=tkinter.Entry(filtre, bg="#D0E5F2")
filtre_annee=tkinter.Checkbutton(filtre, text="année", offvalue=0, onvalue=1, variable=filtre_annee_var, bg="#F263A6")
annee_entre=tkinter.Entry(filtre, bg="#D0E5F2")
filtre_categorie=tkinter.Checkbutton(filtre, text="categorie", offvalue=0, onvalue=1, variable=filtre_cat_var, bg="#F263A6")
categorie_entre=tkinter.Entry(filtre, bg="#D0E5F2")


#partie du catalogue correspondant aux tris
tri=tkinter.LabelFrame(onglet2, text="tri", borderwidth=3, width=150, height=200, bg="#6BA5F2")
tri_nb_commande=tkinter.Radiobutton(tri, text="nb_commande", value=0,variable=radio_var, bg="#D0E5F2")
tri_quantite=tkinter.Radiobutton(tri, text="quantité stock", value=1, variable=radio_var, bg="#D0E5F2")
tri_avis=tkinter.Radiobutton(tri, text="avis des client", value=2, variable=radio_var, bg="#D0E5F2")
aucun_tri=tkinter.Radiobutton(tri, text="pas de tri", value=3, variable=radio_var, bg="#D0E5F2")
accepter=tkinter.Button(tri, text="accepter", command=trier, bg="#4161BF", font="ArialBlack")
texte=tkinter.Text(catalogue, width=48, height=18, font="ArialBlack")
#tableau_catalogue=ttk.Treeview(catalogue, columns=(1, 2, 3, 4), height=5, show="headings") # l'attribut show permet d'afficher l'entete
afficher_catalogue=tkinter.Button(catalogue, text="afficher catalogue", command=insertion_texte, bg="#4161BF", font="ArialBlack")




#statistique utile
# partie de stat pour meilleur porduit par categorie

meilleur_cat=tkinter.LabelFrame(onglet3, text="meilleur produit par categorie", borderwidth=3, width=280, height=150, bg="#D0E5F2")
liste_meilleur_cat=tkinter.Text(meilleur_cat, width=32, height=5)
bouton_meilleur_cat=tkinter.Button(meilleur_cat, text="afficher le meilleur produit par categorie", command=insertion_meilleur_cat)


#partie  de stat pour pire produit par categorie
pire_cat=tkinter.LabelFrame(onglet3, text="pire produit par categorie", borderwidth=3, width=280, height=150, bg="#D0E5F2")
liste_pire_cat=tkinter.Text(pire_cat, width=32, height=5, font="ArialBlack")
bouton_pire_cat=tkinter.Button(pire_cat, text="afficher le pire produit par categorie", command=insertion_pire_cat)

#meilleur produit par marque
meilleur_marque=tkinter.LabelFrame(onglet3, text="meilleur produit par marque", borderwidth=3, width=280, height=150, bg="#D0E5F2")
liste_meilleur_marque=tkinter.Text(meilleur_marque, width=32, height=5, font="ArialBlack")
bouton_meilleur_marque=tkinter.Button(meilleur_marque, text="afficher le meilleur produit par marque", command=insertion_meilleur_marque)



#pire produit par marque
pire_marque=tkinter.LabelFrame(onglet3, text="pire produit par marque", borderwidth=3, width=280, height=150, bg="#D0E5F2")
liste_pire_marque=tkinter.Text(pire_marque, width=32, height=5, font="ArialBlack")
bouton_pire_marque=tkinter.Button(pire_marque, text="afficher le pire produit par marque", command=insertion_pire_marque)




#total des vente realise par le magasin
total_de_ventes=tkinter.LabelFrame(onglet3, text="total des ventes realisés", borderwidth=5, width=560, height=70, bg="#D0E5F2")
text_total_ventes=tkinter.Text(total_de_ventes, width=48, height=1,font="ArialBlack")
bouton_total_ventes=tkinter.Button(total_de_ventes, text="afficher le total de ventes", command=insertion_total_vente)



#frame pour les graphiques de statistiques
graphique=tkinter.LabelFrame(onglet3, text="graphiques illustratifs", borderwidth=3, width=560, height=70, bg="#D0E5F2")
graphique_produit=tkinter.Button(graphique, text="graphique des produit", command=graphique2)
graphique_vente=tkinter.Button(graphique, text="graphique de ventes", command=graphique1)




#widget pour la preparation de commande
nouv_commander=tkinter.LabelFrame(onglet4, text="preparation d'une commande", borderwidth=3, width=560, height=70, bg="#D0E5F2")
label_nom_prep=tkinter.Label(nouv_commander, text="veillez entrer le nom du produit")
nom_produit=tkinter.Entry(nouv_commander, font="ArialBlack")
label_quantite=tkinter.Label(nouv_commander, text="veillez entrer la quantite")
quantite_produit=tkinter.Entry(nouv_commander, font="ArialBlack")
commander=tkinter.Button(nouv_commander, text="commander", command=preparer_commande)
#partie de l'application pour l'expedition
expedition=tkinter.LabelFrame(onglet4, text="expédier une commande", borderwidth=3, width=560, height=70, bg="#D0E5F2")
label_nom_exp=tkinter.Label(expedition, text="veillez entrer le nom du produit à expédier")
nom_produit_exp=tkinter.Entry(expedition, font="ArialBlack")
label_quantite_exp=tkinter.Label(expedition, text="veillez entrer la quantite de produit ")
quantite_produit_exp=tkinter.Entry(expedition,font="ArialBlack")
#ajouter_exp=tkinter.Button(expedition, text="ajouter", command=expedier_produit)
expedier=tkinter.Button(expedition, text="expedier", command=expedier_produit)




#valider=tkinter.Button(onglet3, text="valider", command=insertion_texte)




#element du tableau de catalogue
"""tableau_catalogue.heading(1, text="produit")
tableau_catalogue.heading(2, text="prix")
tableau_catalogue.heading(3, text="année")
tableau_catalogue.heading(4, text="Avis")
tableau_catalogue.column(1, width=80) #permet de changer la largeur des colones
tableau_catalogue.column(2, width=80)
tableau_catalogue.column(3, width=80)
tableau_catalogue.column(4, width=80)"""


#tableau_catalogue.insert(parent='', index='end', iid=0, text="Labe", values=("Hello", "Second Col", "Third Col", 5))
#tableau_catalogue.insert(parent='', index='end', iid=1, text="Labe", values=("Hell", "Second Col", "Third Col", 5))

expedition.grid(row=1, column=0, padx=20, pady=20)
label_nom_exp.grid(column=0, row=0, padx=10, pady=10)
nom_produit_exp.grid(column=1, row=0, padx=10, pady=10)
label_quantite_exp.grid(column=0, row=1, padx=10, pady=10)
quantite_produit_exp.grid(column=1, row=1, padx=10, pady=10)
expedier.grid(column=1, row=3)
#ajouter_exp.grid(column=1, row=2)






nouv_commander.grid(row=0, column=0, padx=20, pady=20)
label_nom_prep.grid(column=0, row=0, padx=10, pady=10)
nom_produit.grid(column=1, row=0, padx=10, pady=10)
label_quantite.grid(column=0, row=1, padx=10, pady=10)
quantite_produit.grid(column=1, row=1, padx=10, pady=10)
commander.grid(column=1, row=2)


bouton_total_ventes.place(x=400, y=5)
bouton_pire_marque.place(x=10, y=95)
bouton_meilleur_marque.place(x=10, y=95)
bouton_pire_cat.place(x=10, y=95)
bouton_meilleur_cat.place(x=10, y=95)
text_total_ventes.place(x=10, y=5)
liste_pire_marque.place(x=0, y=0)
liste_meilleur_marque.place(x=0, y=0)
liste_pire_cat.place(x=0, y=0)
liste_meilleur_cat.place(x=0, y=0)
graphique_produit.grid(row=0, column=0, padx=80, pady=10)
graphique_vente.grid(row=0, column=1, padx=80, pady=10)
graphique.place(x=20, y=410)
total_de_ventes.place(x=20, y=330)
pire_marque.place(x=300, y=160)
meilleur_marque.place(x=10, y=160)
meilleur_cat.place(x=10, y=10)
pire_cat.place(x=300, y=10)
#valider.pack()
texte.place(x=0, y=0)
afficher_catalogue.place(x=30, y=310)
texte.place(x=0, y=0)
aucun_tri.grid(row=3, column=0, padx=10, pady=5)
tri_avis.grid(row=2, column=0, padx=10, pady=5)
tri_quantite.grid(row=1, column=0, padx=10, pady=5)
tri_nb_commande.grid(row=0, column=0, padx=10, pady=5)
accepter.grid(row=4, column=0)
filtre_annee.grid(row=4, column=0, padx=10, pady=5)
filtre_marque.grid(row=2, column=0, padx=10, pady=5)
marque_entre.grid(row=3, column=0)
filtre_categorie.grid(row=0, column=0, padx=10, pady=5)
categorie_entre.grid(row=1, column=0)
annee_entre.grid(row=5, column=0)
tri.place(x=450, y=300)
filtre.place(x=450, y=100)
catalogue.place(x=40, y=100)
label_recherche.grid(column=0, columnspan=3, row=0, padx=50, pady=20)
recherche.grid(column=4, columnspan=3, row=0, padx=50, pady=10)
label_nom.grid(column=0, row=0, padx=50, pady=10)
nom.grid(column=1, row=0, padx=50, pady=10)
label_prix.grid(column=0, row=1, padx=50, pady=10)
prix.grid(column=1, row=1, padx=50, pady=10)
label_poids.grid(column=0, row=2, padx=50, pady=10)
poids.grid(column=1, row=2, padx=50, pady=10)
label_categorie.grid(column=0, row=3, padx=50, pady=10)
categorie.grid(column=1, row=3, padx=50, pady=10)
label_marque.grid(column=0, row=4, padx=50, pady=10)
marque.grid(column=1, row=4, padx=50, pady=10)
label_annee.grid(column=0, row=5, padx=50, pady=10)
annee.grid(column=1, row=5, padx=50, pady=10)
label_uid.grid(column=0, row=6, padx=50, pady=10)
uid.grid(row=6, column=1, padx=50, pady=10)
label_nb_commande.grid(row=7, column=0, padx=50, pady=10)
nb_commande.grid(row=7, column=1, padx=50, pady=10)
label_avis.grid(row=8, column=0, padx=50, pady=10)
label_quantite_produit.grid(row=9, column=0, padx=10, pady=10)
quantite.grid(row=9, column=1, padx=10, pady=10)
avis.grid(row=8, column=1, padx=50, pady=10)
ajouter.grid(column=0, columnspan=2, row=10, padx=50, pady=20)
#enregistrer.grid(column=0, columnspan=2, row=7, padx=50, pady=20)




app.mainloop()

