#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>


typedef struct produit{
    int poids;
    int valeur;
    char nom[100];
    //float rapport;

    

}produit;

produit* readline(int *size); //algorithme qui lit dans le fichier expedition les differents articles potentiellment expediable
int* generating2();
int* generating1();

produit* readline(int *size){
    FILE* fichier;
    fichier=fopen("expedition.txt", "r");
    char *nom;
    int prix;
    int poids;
    int j, i, k;
    produit nv_prod;
    produit* tableau;
    produit* tableau2;
    tableau=malloc(1*sizeof(produit));
    
    
    i=0;
    rewind(fichier);
    k=1;
    
    while(feof(fichier)==0){
        printf("fonction calles\n");
        fscanf(fichier, "%s", &tableau[i].nom);
        fscanf(fichier, "%d", &tableau[i].valeur);
        fscanf(fichier, "%d", &tableau[i].poids);
        printf("%s\n", tableau[i].nom);
        k+=1;
        printf("k=%d\n", k);
        tableau=realloc(tableau, k*sizeof(produit));

        
        i+=1;

    }
    *size=k-1;
    
    fclose(fichier);
    fichier=fopen("expedition.txt", "r");
    fscanf(fichier, "%s", &tableau[0].nom);
    fscanf(fichier, "%d", &tableau[0].valeur);
    fscanf(fichier, "%d", &tableau[0].poids);
    fclose(fichier);
    i=0;    
    
    
    return tableau;
}
int* generating1(){    //algorithme permettant de generer toutes les possibilites sous forme de tableaux de combianaison pour les objets a mettre dans le sac a dos puis de choisir la meilleur
    int n; 
    int size;   
    int i, j;
    produit* tab_produit_2;
    tab_produit_2=readline(&size);
    n=size;

    int k;
    int max, i_max, prix;
    int poids;
    
    
    int tab[n*n][n];    
    
    int capacite;
    int* combinaison_2;   
    tab[1][0]=1;
    tab[0][0]=0;
    i=2;
    printf("yo\n");

    while(i<=n){
        
        if(i%2==0){
            j=i*i/2;
            while(j<i*i){
                //tab[j]=copy(tab[j-int(i*i/2)])
                for(k=0;k<i-1;k++){
                    tab[j][k]=tab[j-(i*i/2)][k];

                }
                tab[j][i-1]=0;
                j+=1;}
            
            j=0;
            while(j<(i*i/2)){
                tab[j][i-1]=1;
                j+=1;}
            }
        if(i%2!=0){
            
            j=(i*i/2);
            while(j<i*i-1){
                for(k=0;k<i-1;k++){
                    tab[j][k]=tab[j-(i*i/2)][k];}

                //tab[j]=copy(tab[j-int(i*i/2)])
                tab[j][i-1]=0;
                j+=1;}                
            j=0;
            while(j<(i*i/2)){
                tab[j][i-1]=1;
                j+=1;}   
            } 
        i+=1;}
    
    printf("yo\n");
    capacite=600;
    max=0;
    i_max=0;
    for(i=0;i<n*n;i++){
        poids=0;
        prix=0;
        for(j=0;j<n-2;j++){
            poids+=tab[i][j]*tab_produit_2[j].poids;
            //printf("poids:%d\n", poids);

            prix+=tab[i][j]*tab_produit_2[j].valeur;
            //printf("%d\n", prix);
        }
        if(poids<=capacite && prix>=max){
            i_max=i;
            max=prix;
        }
    }

    printf("la valeur maximale 1 est de %d et l'indice correspondant est de %d\n", max, i_max);
    combinaison_2=(int*)malloc(n*sizeof(int));
    for(i=0;i<n;i++){
        combinaison_2[i]=tab[i_max][i];
    }
    for(i=0;i<n;i++){
        printf("j=%d\n",combinaison_2[i]);
    }
    

    return combinaison_2;    
}



int* generating2(){
    int n; 
    int size;   
    int i, j;
    produit* tab_produit_2;
    tab_produit_2=readline(&size);
    n=size;

    int k;
    int max, i_max, prix;
    int poids;
    
    
    int tab[n*n][n];    
    
    int capacite;
    int* combinaison_2;   
    tab[1][0]=1;
    tab[0][0]=0;
    i=2;
    printf("yo\n");

    while(i<=n){
        
        if(i%2==0){
            j=i*i/2;
            while(j<i*i){
                //tab[j]=copy(tab[j-int(i*i/2)])
                for(k=0;k<i-1;k++){
                    tab[j][k]=tab[j-(i*i/2)][k];

                }
                tab[j][i-1]=1;
                j+=1;}
            
            j=0;
            while(j<(i*i/2)){
                tab[j][i-1]=0;
                j+=1;}
            }
        if(i%2!=0){
            
            j=(i*i/2);
            while(j<i*i-1){
                for(k=0;k<i-1;k++){
                    tab[j][k]=tab[j-(i*i/2)][k];}

                //tab[j]=copy(tab[j-int(i*i/2)])
                tab[j][i-1]=1;
                j+=1;}                
            j=0;
            while(j<(i*i/2)){
                tab[j][i-1]=0;
                j+=1;}   
            } 
        i+=1;}
    
    printf("yo\n");
    capacite=200;
    max=0;
    i_max=0;
    for(i=0;i<n*n;i++){
        poids=0;
        prix=0;
        for(j=0;j<n-2;j++){
            poids+=tab[i][j]*tab_produit_2[j].poids;
            //printf("poids:%d\n", poids);

            prix+=tab[i][j]*tab_produit_2[j].valeur;
            //printf("%d\n", prix);
        }
        if(poids<=capacite && prix>=max){
            i_max=i;
            max=prix;
        }
    }

    printf("la valeur maximale 2 est de %d et l'indice correspondant est de %d\n", max, i_max);
    combinaison_2=(int*)malloc(n*sizeof(int));
    for(i=0;i<n;i++){
        combinaison_2[i]=tab[i_max][i];
    }
    for(i=0;i<n;i++){
        printf("j=%d\n",combinaison_2[i]);
    }
    

    return combinaison_2;    
}





void liste_exped(){  //algorithme qui genere la liste des produits a expedier
    int size;
    int n;
    
    int* combinaison1;
    int* combinaison2;
    int i, j, k;
    int val_max1, val_max2;
    printf("liste\n");
    produit* tab_produit;
    produit* liste_expedier;
    liste_expedier=malloc(sizeof(produit));
    printf("la taille de liste est de %d et la taille du produit est de %d", sizeof(*liste_expedier), sizeof(produit));
    k=1;
    combinaison1=generating1();
    printf("liste gen1\n");
    combinaison2=generating2();
    printf("liste gen2\n");
    
    tab_produit=readline(&size);
    printf("liste gentab\n");
    n=size;
    

    val_max1=0;
    val_max2=0;
    
    printf("yo le big\n");
    
    for(i=0;i<n;i++){
        val_max1+=combinaison1[i]*tab_produit[i].valeur;
        
    }

    for(i=0;i<n;i++){
        val_max2+=combinaison2[i]*tab_produit[i].valeur;
    }
    printf("la valeur 1 est %d et la valeur 2 est %d\n", val_max1, val_max2);

    i=0;
    j=0;
    if(val_max1>val_max2){
        while(i<n){
            if(combinaison1[i]==1){
                liste_expedier[j]=tab_produit[i];
                j+=1;
                k+=1;
                liste_expedier=realloc(liste_expedier, k*sizeof(produit));
                printf("la taille de liste est %d\n", sizeof(*liste_expedier)/sizeof(produit));
            }
            i+=1;
        }
    }
    else{
        while(i<n){
            if(combinaison2[i]==1){
                liste_expedier[j]=tab_produit[i];
                j+=1;
                k+=1;
                liste_expedier=realloc(liste_expedier, k*sizeof(produit));
                printf("la taille de liste est %d\n", sizeof(*liste_expedier)/sizeof(produit));
            }
            i+=1;
        }

    }
    for(i=0;i<k-1;i++){
        printf("nom a expedier: %s\n", liste_expedier[i].nom);
    }
}
int main(){
    liste_exped();
    
    return 0;
}