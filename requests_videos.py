from googleapiclient.discovery import build
from pytube import YouTube
# Initialisation des titres des vidéos à rechercher
#videos_titles = ["minecraft parkour video tiktok format","fortnite parkour video tiktok format","fortnite parkour video tiktok format","parkour gameplay video tiktok" ]
# Initialisez le service YouTube en utilisant vos clés d'API
youtube = build('youtube', 'v3', developerKey='AIzaSyAYRPKUccJhxDRF5fvzjNG40D8OgZpxg5U')

# Recherchez des vidéos du jeu Subway Surfers sur YouTube
search_response = youtube.search().list(
    q='fortnite parkour video tiktok format',
    type='video',
    videoDefinition='high',
    videoDimension='2d',
    videoLicense='youtube',
    videoSyndicated='true',
    videoType='any',
    fields='items(id(videoId))',
    maxResults=10,
    part='id,snippet',
    videoDuration='short'
).execute()

# Récupérez les ID des vidéos de Subway Surfers trouvées
video_ids = [item['id']['videoId'] for item in search_response['items']]

# Récupérez les détails des vidéos de Subway Surfers trouvées
videos_response = youtube.videos().list(
    id=','.join(video_ids),
    fields='items(id,snippet)',
    part='id,snippet'
).execute()

# Parcourez les vidéos pour les afficher et les télécharger
for video in videos_response['items']:
    # Afficher les informations de la vidéo
    print(f"Titre: {video['snippet']['title']}")
    print(f"Lien: https://www.youtube.com/watch?v={video['id']}")

    # Télécharger la vidéo au format mobile
    yt = YouTube(f"https://www.youtube.com/watch?v={video['id']}&t=1m")
    if yt.age_restricted:
            print("La vidéo est restreinte par âge. Ignorer le téléchargement.")
            continue

    stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').first()

    if stream:
        yt.streams.get_by_itag(18).download()
        print("La vidéo a été téléchargée avec succès.")
    else:
        print("Impossible de trouver une vidéo correspondant aux critères de recherche.")
        
    print("------------------------------------")