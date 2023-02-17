from random import choice


def additionner(nombre1,nombre2):
    return (nombre1+nombre2);
def soustraire(nombre1,nombre2):
    return (nombre1-nombre2);
def multiplier(nombre1,nombre2):
    return (nombre1*nombre2);
def diviser(nombre1,nombre2):
    return (nombre1/nombre2);

nombre1=eval(input("Entrer le premier nombre: "));
nombre2=eval(input("Entrer le deuxieme nombre: "));
print("-----------------Menu---------------------");
print("1. Additionner");
print("2. Soustraire");
print("3. Multiplier");
print("4. Diviser");

while(True):
    choix=int(input("Entrer votre choix: "));
    if choix in (1,2,3,4,5):
      if choix == 1:
          print("Le resultat est: ",additionner(nombre1,nombre2));
      elif choix == 2:
              print("Le resultat est: ",soustraire(nombre1,nombre2));
      elif choix == 3:
          print("Le resultat est: ",multiplier(nombre1,nombre2));
      elif choix == 4:
          print("Le resultat est: ",diviser(nombre1,nombre2));
     
      elif choix=="5":
          print("Au revoir");
          exit();
     
       
    else:
        print("Choix invalide");
                      
                      
        
              
              