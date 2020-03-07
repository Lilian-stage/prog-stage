import random
import time
while True:
    jeu = input("Choisissez le jeu que vous voulez \n-Pierre feuille ciseaux(1)\n-Trouvez le nombre(2)\n")
    if jeu == "1":
        #boucle pierre feuille ciseaux
        while True:
            recommencer = 1
            points = 0
            perdu = 0

            modemultistr = str()
            modemultistr = input("Choississez m pour multi ,s pour solo\nou x pour retourner a l'ecran de selection\n")
            modemultistr.lower()
            modemultibool = False

            if modemultistr == "s":
                modemultibool = False
            elif modemultistr == "m":
                modemultibool = True
            elif modemultistr == "x":
                quit()
            else:
                print("tu as du faire une erreur, recommence")
                break

            try:
                bool(modemultistr)
            except:
                print("tu t'es trompé,tu as peut etre oublié la majuscule au debut du mot")
                break

            if modemultibool == False:
                #boucle jeu solo
                while True:
                    print("mode solo")
                    recommencer == 0
                    var_choice_a = input(
                        "Ecrivez 1 pour choisir la pierre , 2 pour la feuille et 3 pour les ciseaux\nOu 0 pour quitter et changer de mode de jeu\n")

                    enemy_var_choice = random.randint(1, 3)

                    try:
                        var_choice_b = int(var_choice_a)
                    except:
                        print("Vous n'avez pas saisi de chiffre")
                        break

                    if var_choice_b == 0:
                        break
                    elif enemy_var_choice == 1:
                        print("L'adversaire a choisi la pierre")
                    elif enemy_var_choice == 2:
                        print("L'adversaire a choisi la feuille")
                    elif enemy_var_choice == 3:
                        print("L'adversaire a choisi les ciseaux")

                    if var_choice_b == enemy_var_choice:
                        print("Egalité, recommencez")
                    elif var_choice_b == 1 and enemy_var_choice == 2:
                        print("Perdu,la feuille enroule la pierre")
                        perdu = perdu + 1
                        perdu2 = str(perdu)
                        points2 = str(points)

                    elif var_choice_b == 1 and enemy_var_choice == 3:
                        print("Gagné , la pierre casse les ciseaux")
                        points = points + 1
                        points2 = str(points)
                        perdu2 = str(perdu)
                        print("Tu as gagné " + points2 + " fois et perdu " + perdu2 + " fois")

                    elif var_choice_b == 2 and enemy_var_choice == 1:
                        print("Gagné,la pierre casse les ciseaux")
                        points = points + 1
                        points2 = str(points)
                        perdu2 = str(perdu)
                        print("Tu as gagné " + points2 + " fois et perdu " + perdu2 + " fois")

                    elif var_choice_b == 2 and enemy_var_choice == 3:
                        print("Perdu,les ciseaux découpent la feuille")
                        perdu = perdu + 1
                        perdu2 = str(perdu)
                        points2 = str(points)
                        print("Tu as gagné " + points2 + " fois et perdu " + perdu2 + " fois")

                    elif var_choice_b == 3 and enemy_var_choice == 2:
                        print("Gagné,les ciseaux découpent la feuille")
                        points = points + 1
                        points2 = str(points)
                        perdu2 = str(perdu)
                        print("Tu as gagné " + points2 + " fois et perdu " + perdu2 + " fois")

                    elif var_choice_b == 3 and enemy_var_choice == 1:
                        print("Perdu,les ciseaux découpent la feuille")
                        perdu = perdu + 1
                        perdu2 = str(perdu)
                        points2 = str(points)
                        print("Tu as gagné " + points2 + " fois et perdu " + perdu2 + " fois")
            else:
                winp1 = 0
                winp2 = 0
                #boucle jeu multi
                while True:

                    print("Mode multi")
                    print("Tour du joueur 1 , joueur 2 retournez vous")
                    var_choice_player1 = input(
                        "Ecrivez 1 pour choisir la pierre , 2 pour la feuille et 3 pour les ciseaux\nOu 0 pour quitter\n")

                    if var_choice_player1 == "1":
                        var_choice_player1str = "pierre"
                        var_choice_player1int = 1
                    elif var_choice_player1 == "2":
                        var_choice_player1str = "feuille"
                        var_choice_player1int = 2
                    elif var_choice_player1 == "3":
                        var_choice_player1str = "ciseaux"
                        var_choice_player1int = 3
                    elif var_choice_player1 == "0":
                        break
                    else:
                        print("vous vous etes trompé vous devez recommencer")
                        break
                    time.sleep(2)
                    print("Tour  du joueur 2, Joueur 1 retournez vous")
                    var_choice_player2 = input(
                        "Ecrivez 1 pour choisir la pierre , 2 pour la feuille et 3 pour les ciseaux et 0 pour quitter")

                    if var_choice_player2 == "1":
                        var_choice_player2str = "la pierre"
                        var_choice_player2int = 1
                    elif var_choice_player2 == "2":
                        var_choice_player2str = "la feuille"
                        var_choice_player2int = 2
                    elif var_choice_player2 == "3":
                        var_choice_player2str = " les ciseaux"
                        var_choice_player2int = 3
                    elif var_choice_player2 == "0":
                        break
                    else:
                        print("vous vous etes trompé vous devez recommencer")
                        break
                    print("Le joueur 1 avait choisi "+var_choice_player1str+" et le joueur 2 "+var_choice_player2str+" donc")

                    if var_choice_player1int == 1 and var_choice_player2int== 2:
                        print("c'est une victoire pour le joueur 2,la feuille enroule la pierre\n \n")
                        winp2 = winp2 +1
                    elif var_choice_player1int == 1 and var_choice_player2int == 3:
                        print("C'est gagné pour le joueur 1 , la pierre casse les ciseaux\n \n")
                        winp1 = winp1 +1

                    elif var_choice_player1int== 2 and var_choice_player2int == 1:
                        print("Gagné,la pierre casse les ciseaux\n \n")
                        winp1 = winp1 +1

                    elif var_choice_player1int == 2 and var_choice_player2int == 3:
                        print("Perdu,les ciseaux découpent la feuille\n \n")
                        winp2 = winp2 +1

                    elif var_choice_player1int == 3 and var_choice_player2int== 2:
                        print("Gagné,les ciseaux découpent la feuille\n \n")
                        winp1 = winp1 + 1

                    elif var_choice_player1int == 3 and var_choice_player2int == 1:
                        print("Perdu,les ciseaux découpent la feuille\n \n")
                        winp2 = winp2 + 1
                    elif var_choice_player1int == var_choice_player2int:
                        print("Egalité\n \n")
    elif jeu  == "2":
        nb = random.randint(1,20)
        essais =0
        answer = input(
            "Le nombre que tu dois trouver est entre 1 et 20 ,tu as 10 essais pour le retrouver ,lequel est-il\n")
        #boucle Trouvez le nombre
        while answer != nb :
            if essais !=10 :
                if int(answer) > nb:
                    essais = essais + 1
                    essaisrest= 10-essais
                    essaisrestr=str(essaisrest)
                    print("ton nombre est plus elevé que le nombre que tu dois trouver il te reste "+essaisrestr+" essais")
                    answer = (input("Réessaie\n"))

                elif int(answer) < nb:
                    essais = essais+1
                    essaisrest= 10-essais
                    essaisrestr=str(essaisrest)
                    print("ton nombre est moins elevé que le nombre que tu dois trouver il te reste "+essaisrestr+" essais")
                    answer = (input("Réessaie\n"))

                else:
                    essaisstr= str(essais)
                    print("Bravo, tu as trouvé le bon nombre en "+essaisstr+" essai/s\n\n")
                    break

            else:
                print("Tu n'as pas trouvé en 10 essais.Fin de la partie\n\n")
                break



    else:
        print("Tu as du te tromper ,ce n'est pas un des chiffres qui te sont proposés")
        quit()