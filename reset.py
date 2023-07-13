import os, shutil

def reset():
    shutil.rmtree('users')
    with open('users.txt', 'w') as f:
        f.write('')
    print('Removed users')
    os.mkdir('users')

    shutil.rmtree('videos')
    print('Removed all videos')
    os.mkdir('videos')

    with open('last_video_id.txt', 'w') as f:
        f.write('0')

    print('reset base video id')
    print('done')

if __name__ == '__main__':
    reset()