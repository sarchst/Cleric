from Video import Video
from User import User
from Catalog import Catalog
from Link import Link
from Music import Music
import pygame as pg

if __name__ == "__main__":
    pg.init()
    pg.display.set_caption("Cleric")
    # Primary game objects
    video = Video((800, 480))
    catalog = Catalog()
    user = User()
    music = Music("music/sand_theme.mp3")
    # Catalog loads all sprite images
    catalog.load("dawnlike")
    # First frame displays before game starts
    video.load()
    video.blit_map(catalog, user)
    video.flip()
    video.log("Welcome to Cleric!")
    # Game loops until the user stops playing
    while not user.is_done:
        # User input - keyboard / mouse
        user.get_input(video.pixel_res)
        catalog.bound(user)
        # Saving
        if user.is_saving:
            video.save(catalog)
            user.is_saving = False
        # Erases video log
        if user.is_erasing:
            video.erase()
            user.is_erasing = False
        # Clears video log
        if user.is_clearing_log:
            video.clear_log()
            user.is_clearing_log = False
        # Queury a tile
        if user.is_querying:
            video.query(user, catalog)
            user.is_querying = False
        # Output for user - video
        video.blit_clear()
        if user.map_pixel_selected and user.cat_pixel_selected:
            video.place(Link(user, catalog), user)
        if user.is_catalogging:
            video.blit_catalog(catalog, user)
        else:
            video.blit_map(catalog, user)
        video.blit_selector(user, catalog)
        video.blit_log()
        video.flip()
    # User stopped - Cleanup
    pg.quit()
