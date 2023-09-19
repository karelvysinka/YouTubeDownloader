from pytube import YouTube

def stahnout_video(url):
    try:
        # Inicializace objektu YouTube
        yt = YouTube(url)
        
        # Získání nejvyšší kvality videa
        video = yt.streams.get_highest_resolution()
        
        # Stáhnutí videa
        video.download()
        
        print(f"Video '{yt.title}' bylo úspěšně staženo.")
        
    except Exception as e:
        print(f"Nastala chyba: {e}")

# Zadání URL videa
url = input("Zadejte URL videa, které chcete stáhnout: ")

# Spuštění funkce
stahnout_video(url)
