import os

from time import sleep
import picamera

from constants import _img_format, next_img_index, _img_dir, _img_prefix, screen_width, screen_height

camera = picamera.PiCamera()

def get_next_image_index(img_dir):
    """
    Get the number of existing images in the current image directory
    This is used to decide the next image index for the file name.

    :param img_dir: absolute location of directory where images are saved
    :return: Number of images in directory + 1
    """
    cur_indexes = []
    # scan the image directory and get the last index
    for img in os.listdir(img_dir):
        print(img)
        if img.split('.')[-1] == _img_format:
            # get the index of the current image
            img_name = img.split('/')[-1].split('.')[0]
            index = int(img_name.split('_')[-1])
            cur_indexes.append(index)
            print(cur_indexes)
    if not cur_indexes:
        return 0
    else:
        return max(cur_indexes) + 1


def preview(button):
    actions = []
    actions.append('Starting preview\n')
    camera.start_preview(fullscreen=False, window = (10, 10, int(screen_width*0.75), int(screen_height*0.75)))


    return actions

def capture(button):
    global next_img_index
    actions = []
    img_file = _img_dir + _img_prefix + str(next_img_index) + '.' + _img_format
    print (["next_index", next_img_index])
    next_img_index += 1
    print (["Changing next_index to ", next_img_index])
    camera.capture(img_file)
    print(img_file + " saved")
    actions.append('Captured image\n')
    camera.stop_preview()
    actions.append('Stopping preview\n')
    return actions
    
def close_camera():
    actions = []
    camera.close()
    actions.append('Closing camera\n')
    return actions