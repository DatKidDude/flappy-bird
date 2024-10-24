def scroll_background(screen, bg, bg_width, tiles, scroll):
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))
    
    # scroll background
    scroll -= 5

    # Reset scroll
    if abs(scroll) > bg_width:
        scroll = 0

    return scroll