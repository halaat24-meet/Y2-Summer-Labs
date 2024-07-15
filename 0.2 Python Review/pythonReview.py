def create_youtube_video( title, description):
	youtube= { "title":title,  
			  "description":description,
              "likes": 0,
              "dislikes":0,
              "comments":{}
              }
	return(youtube)

youtube1= create_youtube_video("Ballet equipment", "All the ballet equipment you need to buy")



def like(youtube_video):
	for i in range(495):
		if "likes" in youtube_video:
			youtube_video["likes"]+=1 
	return(youtube_video)
youtube2=like(youtube1)



def dislike(youtube_video2):
	if "dislikes" in youtube_video2:
		youtube_video2["dislikes"]+=1
	return(youtube_video2)
youtube3= dislike(youtube1)

comment_txt= input("Enter a comment")
username= input("Enter your username")

def add_comment(youtube, username, comment_txt):
	youtube["comments"].update({username:comment_txt})
	return(youtube)
youtube4 = add_comment(youtube1, "hh", "hh")
print(youtube4)



