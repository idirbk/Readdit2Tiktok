from googleapiclient.discovery import build
from pytube import YouTube
import os
import random
# Initialisez le service YouTube en utilisant vos clés d'API
youtube = build('youtube', 'v3', developerKey='AIzaSyAYRPKUccJhxDRF5fvzjNG40D8OgZpxg5U')
def generate_video(title) : 
    # Recherchez des vidéos du jeu Subway Surfers sur YouTube
    search_response = youtube.search().list(
        q = title +' parkour video tiktok format',
        type='video',
        videoDefinition='high',
        videoDimension='2d',
        videoLicense='youtube',
        videoSyndicated='true',
        videoType='any',
        fields='items(id(videoId))',
        maxResults=10,
        part='id,snippet',
        videoDuration='short',
        safeSearch='none'
    ).execute()

    # Récupérez les ID des vidéos de Subway Surfers trouvées
    video_ids = [item['id']['videoId'] for item in search_response['items']]

    # Mélangez les ID des vidéos
    random.shuffle(video_ids)

    # Sélectionnez un ID de vidéo au hasard parmi les meilleures vidéos
    selected_video_id = video_ids[0]

    # Récupérez les détails de la vidéo sélectionnée
    video_response = youtube.videos().list(
        id=selected_video_id,
        fields='items(id,snippet)',
        part='id,snippet'
    ).execute()

    # Téléchargez la vidéo sélectionnée
    video = video_response['items'][0]
    video_title = video['snippet']['title']
    video_link = f"https://www.youtube.com/watch?v={video['id']}"

    yt = YouTube(f"https://www.youtube.com/watch?v={selected_video_id}&t=1m")
    if yt.age_restricted or not yt.streams:
        print("La vidéo est restreinte par âge ou aucune version téléchargeable n'est disponible.")
    else:
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').first()

        if stream:
            video_path = stream.download()
            new_path = os.path.join(os.path.dirname(video_path), "video.mp4")
            os.rename(video_path, new_path)
            print("La vidéo a été téléchargée avec succès.")
        else:
            print("Impossible de trouver une vidéo correspondant aux critères de recherche.")

        print("------------------------------------")
        print(f"Titre: {video_title}")
        print(f"Lien: {video_link}")

generate_video('minecraft')
 