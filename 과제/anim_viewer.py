from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('kindpng_4074742.png')

x = 0
frame = 0
for x in range(0, 800, 5):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 75, 170, 70, 80, x, 80, 100, 100)
    update_canvas()
    frame = (frame + 1) % 10
    delay(0.05)
    get_events()


close_canvas()

