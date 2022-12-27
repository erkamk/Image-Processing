from moviepy.editor import VideoFileClip

path = r"path"
file = VideoFileClip(path)

new = file.subclip(t_start = (23,39), t_end = (23,43))
new.write_videofile(r"path")