import cv2 as cv

video_file = 'rtmp://210.99.70.120/live/cctv001.stream'
target_format = 'avi'
target_fourcc = 'XVID'

video = cv.VideoCapture(video_file)

if video.isOpened():
    fps = video.get(cv.CAP_PROP_FPS)
    wait_msec = int(1 / fps * 1000)
    target = cv.VideoWriter()
    is_recording = False
    
    while True:
        valid, img = video.read()
        if not valid:
            break
        
        if is_recording:
            cv.circle(img, (20, 20), 10, (0, 0, 255), -1)
        
        target.write(img)
        
        cv.imshow('Video Player',img)
        
        key = cv.waitKey(wait_msec)
        if key == 27:
            break
        elif key == 32:
            is_recording = not is_recording
            if is_recording:
                target_file = 'video.' + target_format
                h, w, *_ = img.shape
                is_color = (img.ndim > 2) and (img.shape[2] > 1)
                target.open(target_file, cv.VideoWriter_fourcc(*target_fourcc), fps, (w, h), is_color)
            else:
                target.release()
            
        if is_recording:
            target.write(img)
        
    if is_recording:
        target.release()
    video.release()
    cv.destroyAllWindows()