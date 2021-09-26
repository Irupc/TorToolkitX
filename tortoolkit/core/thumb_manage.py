# -*- coding: utf-8 -*-
# (c) YashDK [yash-dk@github]
# (c) modified by AmirulAndalib [amirulandalib@github]


from hachoir.metadata import extractMetadata
from hachoir.parser import createParser

from ..functions import vids_helpers


async def get_thumbnail(file_path, user_id=None):
    metadata = extractMetadata(createParser(file_path))
    try:
        metadata.get("duration")
    except:
        pass

    if user_id is not None:
        pass  # todo code for custom thumbnails here mostly will be with db
    else:
        path = "https://raw.githubusercontent.com/Irupc/TorToolkitX/5ec60f2cfa58b21a7d53c88d631c640d28679f1d/irupc.jpeg"
        path = await vids_helpers.resize_img(path, 320)
        return path
