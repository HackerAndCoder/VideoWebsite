import os, yaml, video

debugging = False

def debug(contents):
    global debugging
    if debugging:
        print(f'[DEBUG] {contents}')

def add_video(video, user):
    if not type(user) == User:
        Exception('Argument \'user\' for function add_video() is not an instance of class User')
    
    if not is_user(user):
        Exception(f'User {user.username} does not exist')
    
    user.add_video_id(video.id)

    debug(f'Added video id {video.id} to user {user.username}')
    
    os.mkdir(os.path.join(os.getcwd(), 'videos', str(video.id)))
    debug('Made video directory')

    with open(os.path.join('videos', str(video.id), 'video.mp4'), mode='wb') as f:
        f.write(video.video)
        debug('Wrote video contents to file')

    with open(os.path.join('videos', str(video.id), 'info.yml'), mode='w') as f:
        video_info = {'author': user.username, 'views': 0, 'title': str(video.title)}
        f.write(yaml.dump(video_info))
        debug('Wrote info.yml to video folder')

    return True

def get_video_id():
    with open('last_video_id.txt') as f:
        id = int(f.read())
    return id

def set_video_id(id):
    with open('last_video_id.txt', 'w') as f:
        f.write(str(id))

def increment_video_id():
    set_video_id(get_video_id() + 1)
    return True

def get_next_id():
    increment_video_id()
    return get_video_id()

def is_user(user):
    with open('users.txt') as f:
        if user.username in f.readlines():
            return True
    return False

def add_user_to_file(user):
    with open('users.txt', 'a') as f:
        f.write(user.username + '\n')

def add_video_id_to_user(video_id, user):
    user.add_video_id(video_id)

def set_subscribers(username, num_subs):
    with open('users.txt') as f:
        if not username in f.readlines():
            return False
    with open(os.path.join('users', username + '.yml')) as f:
        contents = yaml.load(f.read())
    contents['subscribers'] = str(int(num_subs))
    with open(os.path.join('users', username + '.yml'), 'w') as f:
        f.write(yaml.dump(contents))
    return True

def create_user(user):
    if len(user.username) < 3:
        Exception(f'User\'s name {user.username} cannot be shorter than 3 characters')
    if is_user(user):
        Exception(f'user {user.username} already exists')
    add_user_to_file(user)
    with open(os.path.join(os.getcwd(), 'users', str(user.username) + '.yml'), 'w') as f:
        f.write(yaml.dump(user.get_dump_output()))
    return user

def get_user(username):
    with open('users.txt') as f:
        if not str(username) in f.readlines():
            Exception(f'No user with name {username}')
    with open(os.path.join('users', username + '.yml')):
        contents = yaml.load(f.read())

    user = User()
    user.load_from_dump(contents)
    return user

class User:
    def __init__(self, username = 'generateduser', password = 'generatedpassword', subscribers=0, videos = []):
        self.username = username
        self.password = password
        self.subscribers = subscribers
        self.videos = []
    
    def get_config(self):
        with open(os.path.join('users', self.username + '.yml')) as f:
            config = yaml.full_load(f.read())
            debug(f'Loaded user\'s {self.username} config: {config}')
        return config
    
    def set_config(self, config):
        with open(os.path.join('users', self.username + '.yml'), 'w') as f:
            f.write(yaml.dump(config))
    
    def add_video_id(self, id):
        config = self.get_config()
        config['videos'].append(str(id))
        self.set_config(config)
    
    def get_dump_output(self):
        return {'username': self.username, 'password': self.password, 'subscribers': self.subscribers, 'videos': self.videos}
    
    def load_from_dump(self, dump : dict):
        self.username = dump['username']
        self.password = dump['password']
        self.subscribers = dump['subscribers']
        self.videos = dump['videos']