from pico2d import *



def handle_events():
    global running
    global x
    global y
    global dir

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                dir -= 1
                character.clip_draw(frame * 100, 100 * 0, 100, 100, x, 90)
            elif event.key == SDLK_RIGHT:
                dir += 1
                character.clip_draw(frame * 100, 100 * 1, 100, 100, x, 90)
            elif event.key == SDLK_UP:
                dir += 1
                character.clip_draw(frame * 100, 100, 100, 100, x, y)
            elif event.key == SDLK_DOWN:
                dir -= 1
                character.clip_draw(frame * 100, 100, 100, 100, x, y)
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
                character.clip_draw(frame * 100, 100 * 3, 100, 100, x, 90)
            elif event.key == SDLK_LEFT:
                dir += 1
                character.clip_draw(frame * 100, 100 * 2, 100, 100, x, 90)


open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')
kpu_ground = load_image('TUK_GROUND.png')

running = True
KPU_WIDTH, KPU_HEIGHT = 1280, 1024
x = 1280 // 2
y = 1024 // 2
frame = 0
dir = 0

cx, cy = KPU_WIDTH // 2, KPU_HEIGHT // 2
open_canvas(KPU_WIDTH, KPU_HEIGHT)

while running:
    clear_canvas()
    grass.draw(400, 30)
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 2, 100, 100, x, 90)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    x += dir * 5
    y += dir * 5
    delay(0.01)

close_canvas()

