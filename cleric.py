from Video import Video
from User import User
from Catalog import Catalog
from Link import Link

"""
Copyright (c) Sarchen Starke, Gustav Louw
"""
# Game setup
video = Video((640, 480))
# Sarch Step:
# Remove the video.layers assignment and have
# done inside video.load
video.layers = video.load()
catalog = Catalog()
catalog.load("dawnlike")
user = User()
# First frame display before game starts
video.blit_map(catalog, user)
video.flip()
# Game loop
while not user.is_done:
    # Input
    user.get_input()
    catalog.bound(user)
    if user.is_saving:
        video.save()
        user.is_saving = False
    # Render
    video.blit_clear()
    if user.map_pixel_selected and user.cat_pixel_selected:
        video.place(Link(user, catalog), user)
    if user.is_catalogging:
        video.blit_catalog(catalog)
    else:
        video.blit_map(catalog, user)
    video.blit_selector(user, catalog)
    video.flip()
# Cleanup
video.off()
