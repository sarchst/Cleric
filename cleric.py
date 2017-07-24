from Video import Video
from User import User
from Catalog import Catalog
from Link import Link

video = Video((640, 480))
catalog = Catalog()
user = User()
# Game load
video.blit_title_screen()
video.flip()
video.load()
catalog.load("dawnlike")
# First frame display before game starts
video.blit_clear()
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
    if user.is_clearing_log:
        del video.entries[:]
        user.is_clearing_log = False
    # Output
    video.blit_clear()
    if user.map_pixel_selected and user.cat_pixel_selected:
        video.place(Link(user, catalog), user)
    if user.is_catalogging:
        video.blit_catalog(catalog)
    else:
        video.blit_map(catalog, user)
    video.blit_selector(user, catalog)
    video.blit_log()
    video.flip()
# Cleanup
video.off()
