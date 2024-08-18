from time import sleep


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует.')
                return
        user = User(nickname, password, age)
        self.users.append(user)
        self.current_user = user

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for video in args:
            if isinstance(video, Video):
                for i in self.videos:
                    if video.title == i.title:
                        return
            self.videos.append(video)

    def get_videos(self, search):
        result = []
        for video in self.videos:
            if str(search).lower() in video.title.lower():
                result.append(video.title)
        return result

    def watch_video(self, video_title):
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
        else:
            for video in self.videos:
                if video_title == video.title:
                    if video.adult_mode and self.current_user.age < 18:
                        print('Вам нет 18 лет. Пожалуйста, покиньте страницу')
                        return
                else:
                    continue
                for i in range(video.duration):
                    print(i + 1)
                    sleep(1)
                print('Конец видео')


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = str(title)
        self.duration = int(duration)
        self.time_now = 0
        self.adult_mode = adult_mode


class User:
    def __init__(self, nickname, password, age):
        self.nickname = str(nickname)
        self.password = hash(password)
        self.age = int(age)


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

ur.add(v1, v2)

print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user.nickname)

ur.watch_video('Лучший язык программирования 2024 года!')
