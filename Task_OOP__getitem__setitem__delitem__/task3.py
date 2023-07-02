# В этой задаче мы создадим аналог плейлиста, для этого понадобиться реализовать два
# класса Song и Playlis
# Класс Song должен содержать:
# метод __init__, который сохраняет в экземпляре два атрибута title и artist:
# название песни и исполнитель
# Класс Playlist должен содержать:
# метод __init__. , который создает в экземпляре атрибут songs.
# Изначально должен быть пустым списком;
# метод __getitem__ , который возвращает песню из атрибута songs по индексу

# метод __setitem__ , который добавляет песню в атрибут songs в указанный индекс.
# При этом нужно сдвинуть уже имеющиеся песни вправо, у которых индекс был до момента
# вставки равен или больше переданного
# метод add_song, который добавляет песню в конец плейлиста
# Sample Input:
# Sample Output:
# Good


class Song:

    def __init__(self, title, artist):
        self.title = title
        self.artist = artist


class Playlist(Song):

    def __init__(self):
        self.songs = []

    def __getitem__(self, item):
        if 0 <= item < len(self.songs):
            return self.songs[item]

    def __setitem__(self, key, value):
        if isinstance(self, Song):
            self.songs.insert(key, value)
            return self.songs

    def add_song(self, title):
        self.songs.append(title)



playlist = Playlist()
assert len(playlist.songs) == 0
assert isinstance(playlist, Playlist)
playlist.add_song(Song("Paradise", "Coldplay"))
assert playlist[0].title == 'Paradise'
assert playlist[0].artist == 'Coldplay'
assert len(playlist.songs) == 1

playlist[0] = Song("Resistance", "Muse")
assert playlist[0].title == 'Resistance'
assert playlist[0].artist == 'Muse'
assert playlist[1].title == 'Paradise'
assert playlist[1].artist == 'Coldplay'

playlist[1] = Song("Helena", "My Chemical Romance")
assert playlist[1].title == 'Helena'
assert playlist[1].artist == 'My Chemical Romance'

assert playlist[2].title == 'Paradise'
assert playlist[2].artist == 'Coldplay'
print('Good')