# -*- coding: utf-8 -*-
# (c) YashDK [yash-dk@github]
# (c) modified by AmirulAndalib [amirulandalib@github]


from hachoir.metadata import extractMetadata
from hachoir.parser import createParser


async def get_thumbnail(file_path, user_id=None):
    metadata = extractMetadata(createParser(file_path))
    try:
        metadata.get("duration")
    except:
        pass

    if user_id is not None:
        pass  # todo code for custom thumbnails here mostly will be with db
    else:
        path = "irupc.jpg"
        return path
