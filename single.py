from manager import Manager

# Importation des variables d'environnement
import os


class Single:
    """
    Représente un single musical avec un titre, un artiste, une date de sortie et des informations audio.

    Attributes:
        titre (str): Le titre du single.
        artiste (str): L'artiste du single.
        date (str): La date de sortie du single au format "YYYY-MM-DD".
        manager (Manager): Une instance de la classe Manager pour effectuer des opérations de gestion de la musique.
        lien_spotify (str): Lien Spotify du single (optionnel).
        extrait_audio (str): URL de l'extrait audio du single (optionnel).

    Methods:
        rechercher_audio_artiste_titre(): Recherche et retourne les informations audio du single (lien Spotify et extrait audio).
        afficher_informations(): Affiche les informations du single (titre, artiste, date, lien Spotify, extrait audio).
        jouer_extrait_audio(): Joue l'extrait audio du single s'il est trouvé, sinon affiche un message d'avertissement.
        stocker_info(liste_info): Stocke les informations du single dans une liste.

    Usage:
        # Création d'une instance de la classe Single
        single = Single("Titre du single", "Artiste du single", "Date du single")

        # Affichage des informations du single
        single.afficher_informations()

        # Lecture de l'extrait audio du single
        single.jouer_extrait_audio()

        # Stockage des informations du single dans une liste
        liste_info = []
        single.stocker_info(liste_info)
    """

    def __init__(self, titre, artiste, date):
        """
        Initialise une instance de la classe Single avec un titre, un artiste et une date.

        Args:
            titre (str): Le titre du single.
            artiste (str): L'artiste du single.
            date (str): La date de sortie du single au format "YYYY-MM-DD".
        """
        self.titre = titre
        self.artiste = artiste
        self.date = date
        
        client_id = os.getenv("SPOTIFY_CLIENT_ID")
        client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
        
        self.manager = Manager(client_id, client_secret)
        
        self.lien_spotify = None
        self.extrait_audio = None

    def rechercher_audio_artiste_titre(self):
        """
        Recherche et retourne les informations audio du single (lien Spotify et extrait audio).

        Returns:
            dict: Un dictionnaire contenant les informations audio du single (lien Spotify et extrait audio).
        """
        audio_info = self.manager.rechercher_audio_artiste_titre(self.artiste, self.titre)
        if audio_info:
            self.lien_spotify = audio_info["lien_spotify"]
            self.extrait_audio = audio_info["extrait_audio"]
        return audio_info

    def afficher_informations(self):
        """
        Affiche les informations du single (titre, artiste, date, lien Spotify, extrait audio).
        """
        print("Titre :", self.titre)
        print("Artiste :", self.artiste)
        print("Date :", self.date)
        print("Lien Spotify :", self.lien_spotify)
        print("Extrait Audio :", self.extrait_audio)

    def jouer_extrait_audio(self):
        """
        Joue l'extrait audio du single s'il est trouvé, sinon affiche un message d'avertissement.

        **Note:** Cette implémentation simule la lecture en affichant un message.
        Vous devrez implémenter la lecture réelle en fonction de votre bibliothèque audio préférée (par exemple, pygame, playsound).
        """
        if self.extrait_audio:
            # Simule la lecture
            print(f"Lecture de l'extrait audio de {self.titre}...")
        else:
            print("Aucun extrait audio trouvé pour ce single")

    def stocker_info(self, liste_info):
        """
        Stocke les informations du single (titre, artiste, date, lien Spotify, extrait audio) dans une liste.

        Args:
            liste_info (list): La liste dans laquelle stocker les informations du single.
        """
        audio_info = self.rechercher_audio_artiste_titre()
        info_single = {
            "titre": self.titre,
            "artiste": self.artiste,
            "date": self.date,
            "lien_spotify": self.lien_spotify,
            "extrait_audio": self.extrait_audio}

        liste_info.append(info_single)

        return liste_info




from single import Single



# Chargement des variables d'environnement
client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

# Création du gestionnaire avec les informations d'identification
manager = Manager(client_id, client_secret)

# Création d'une instance de la classe Single
single = Single("Coup du marteau", "Tam sir", "Date du single")

# Affichage des informations du single
single.afficher_informations()

# Jouez l'extrait audio du single
#single.jouer_extrait_audio()
