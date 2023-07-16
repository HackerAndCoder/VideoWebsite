import info_handler, os
from video import Video

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

def upload_video(video : Video, user):
    video.id = get_next_id()
    info_handler.add_video(video, user)

def create_a_user(name, password):
    user = info_handler.User(name, password)
    if info_handler.is_user(user):
        return False
    else:
        info_handler.add_user(user)
        return True

def get_user(username):
    user = info_handler.get_user(username)
    if user:
        return user
    else:
        return False

def get_videos_title_include(search_text):
    return info_handler.get_videos_from_title_contains(search_text)

if __name__ == '__main__':
    # test upload
    with open(os.path.join('to_upload', 'test.mp4'), 'rb') as f:
        try:
            info_handler.add_user(info_handler.User())
        except:
            print('user already exists. Passing...')
        user = info_handler.get_user('generateduser')
        video_data = f.read()