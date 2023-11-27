
class Gestion: # ce sont les sauvegardes et chargements du bloc note
    def sauvegarder_bloc_notes(self, fichier, notes):
        try:
            with open(fichier, 'w') as file: # ouvre le fichier en mode écriture
                file.write("\n".join(notes))
            print("Bloc-notes sauvegardé.") # la sauvegarde à bien été effectué
        except IOError:
            print("Erreur. Veuiller Reeessayer.") #la sauvegarde n'a pas été effectué

    def charger_bloc_notes(self, fichier): # charge le bloc note
        try:
            with open(fichier, 'r') as file:
                return file.readlines()
        except FileNotFoundError:
            print("Fichier non trouvé. Aucun bloc-notes chargé.") #fichier n'a pas été trouvé
            return []
        except :
            print("Erreur lors du chargement du bloc-notes.")
            return []

class BlocNote(Gestion): # les fonctions du bloc note (ajouter, afficher, rechercher, supprimer)
    def __init__(self): # constructeur
        super().__init__()
        self.notes = []

    def ajouter(self, note): # fonction ajouter, qui va ajouter des notes dans un txt (fichier) qui sera ensuite sauvegardé dans la class gestion
        self.notes.append(note)

    def afficher(self): # demande d'afficher les notes / l'affiche directement sur le terminal
        for note in self.notes:
            print(note)

    def rechercher(self, mot_cle):  # recherche dans le bloc note
        for note in self.notes:
            if mot_cle in note:
                print(note)

    def supprimer(self, index): # supprime une note
        if 0 <= index < len(self.notes):
            del self.notes[index]
        else:
            print("Index invalide. Aucune note supprimée.")

if __name__ == "__main__": # menu du bloc note
    bloc_notes = BlocNote() # création du bloc note
    while True: # boucle infinie
        print("Menu:\n1. Ajouter une note\n2. Lire le bloc-note\n3. Rechercher dans le bloc-notes\n4. Supprimer une note\n5. Sauvegarder le bloc-notes\n6. Charger le bloc-notes\n7. Quitter")
        choix = input("Entrez le numéro de votre choix : ")
        if choix == '1':
            bloc_notes.ajouter(input("Entrez le contenu de votre note : "))
        elif choix == '2':
            bloc_notes.afficher()
        elif choix == '3':
            bloc_notes.rechercher(input("Entrez le mot-clé à rechercher : "))
        elif choix == '4':
            bloc_notes.supprimer(int(input("Entrez le numéro de la note à supprimer : ")))
        elif choix == '5':
            bloc_notes.sauvegarder_bloc_notes(input("Entrez le nom du fichier de sauvegarde : "), bloc_notes.notes)
        elif choix == '6':
            bloc_notes.notes = bloc_notes.charger_bloc_notes(input("Entrez le nom du fichier à charger : "))
        elif choix == '7':
            break
        else:
            print("Choix invalide.")
    print("Au revoir!")
