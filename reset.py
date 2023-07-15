import os, shutil

def reset():
    try:
        shutil.rmtree('users')
        print('Removed users')
    except:
        print('No folder \'users\', making...')

    with open('users.txt', 'w') as f:
        f.write('')
    
    os.mkdir('users')

    try:
        shutil.rmtree('videos')
        print('Removed all videos')
    except:
        print('No folder \'videos\', making...')

    os.mkdir('videos')

    with open('last_video_id.txt', 'w') as f:
        f.write('0')
    print('Reset video ids')
    
    with open('video_index.yml', 'w') as f:
        f.write('')
    print('Cleared video index')

    print('done')

if __name__ == '__main__':
    reset()