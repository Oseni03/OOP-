class Manager:
	def __init__(self, artist_name):
		self.artist_name=artist_name
		self.album = {}
		self.all_songs=[]
		self.artist_info={}
		self.all_datas={}
		
	def save_data(self):
		filename="music.txt"
		
		data=self.all_datas
		data[self.artist_name]={
			"Artist_info":self.artist_info,
			"Album":self.album,
			"Songs":self.all_songs,
		}
		for x, y in data.items():
			with open(filename, "a") as file:
				file.write(f"\n\n{x}:")
			for p, q in y.items():
				with open(filename, "a") as file:
					file.write(f"\n{p}:{q}")
			
	def del_artist(self, artist_name):
		filename="music.txt"
		with open(filename) as obj:
			file=obj.read()
		for datas in file.items():
			D=datas
			if artist_name in D.keys():
				del D[artist_name]
			else:
				print(f"I do not manage {artist_name.title()}")
				
	def artist_infos(self, first_name, last_name, middle_name=None):
		self.artist_info["first_name"]=first_name.title()
		self.artist_info["last_name"]=last_name.title()
		if middle_name:
			self.artist_info["middle_name"]=middle_name.title()
		else:
			pass
			
class Album(Manager):
	def __init__(self, title, artist_name=None):
		super().__init__(artist_name)
		
		self.title=title
		self.tracks=[]
		
	def add_tracks(self, song):
		self.tracks.append(song.title())
		
	def del_track(self, song):
		tracks=self.track
		if song in tracks:
			tracks.remove(song)
		else:
			print(f"{song} does not exist in the list of tracks")
			
	def save_album(self):
		# title=self.title
		# tracks=self.tracks
		self.album[self.title.title()]=self.tracks

class Songs(Manager):
	def __init__(self, artist_name=None):
		super().__init__(artist_name)
		
		
	def add_song(self, song):
		# songs=self.all_songs
		self.all_songs.append(song.title())
		
	def del_song(self, song):
		songs=self.all_songs
		if song in songs:
			songs.remove(song)
		
		
artist=Manager("seyi vibes")
artist.artist_infos("oluwaseyi", "adeniran", "samuel")

album=Album("NSNV")
album.add_tracks("big vibes")
album.add_tracks("save me")
album.add_tracks("pro. peller")
album.add_tracks("rhymes")
album.save_album()

# tracks=album.tracks
# for track in tracks:
# 	print(track)

songs=Songs()
songs.add_song("save me")
songs.add_song("pro. peller")
songs.add_song("rhymes")
songs.add_song("O.Y.O")
songs.add_song("rora")
songs.add_song("catalyst")

# all_songs= songs.all_songs
# for song in all_songs:
# 	print(song)


# album.save_data()
# songs.save_data()
songs=artist.all_songs
for song in songs:
	print(song)
artist.save_data()




		




