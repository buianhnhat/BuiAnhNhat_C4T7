#d
# from __future__ import unicode_literals
# import youtube_dl

# ydl_opts = {}
# with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#     ydl.download(['https://www.youtube.com/watch?v=Wv2rLZmbPMA'])

# #f
# import youtube_dl

# lst=[]
# ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})
# while True:
#     yt=input("Enter youtube link: ")
#     if(yt=='ok'):
#         break
#     else:
#         with ydl:
#             result = ydl.extract_info(
#                 yt,
#                 download=False # We just want to extract the info
#             )

#         if 'entries' in result:
#             # Can be a playlist or a list of videos
#             video = result['entries'][0]
#         else:
#             # Just a video
#             video = result

#         # print(video)
#         video_url = video['formats'][0]['url']
#         lst.append(video_url)
# for i, item in enumerate(lst):
#     print (i+1, ".", item)

with open("hhh.json", "a") as out:
    out.write("I love coding, more than anything else")