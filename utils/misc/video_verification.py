from typing import Union
from telebot.types import Video
from exceptions.video_exceptions import NotSquare, Not360, WrongDuration


def is_video_available(video: Video) -> Union[bool, NotSquare, Not360]:
    if video.width != video.height:
        raise NotSquare

    if video.width > 640:
        raise Not360

    if video.duration > 60:
        raise WrongDuration

    return True
