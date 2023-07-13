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
    info_handler.add_video(video, user)

if __name__ == '__main__':
    # test upload
    with open(os.path.join('to_upload', 'test.mp4'), 'rb') as f:
        user = info_handler.create_user(info_handler.User())
        video_data = f.read()
        print(f'Video_data size {video_data.__sizeof__()}')
        for i in range(10):
            upload_video(Video('test', video_data, get_next_id()), user)
            print(f'Uploaded video number {i}')