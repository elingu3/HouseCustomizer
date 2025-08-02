from ursina import *

app = Ursina(size=(589.55,510.9))
music = Audio('resources/bonsai-chill-lofi-365943.mp3', loop=True, autoplay=True)

# --- Window resize update ---
def update_window_layout():
    background.scale = (window.aspect_ratio * 15, 15)

window.on_resize = update_window_layout
# --- Background ---
background = Entity(
    model='quad',
    texture='resources/background/village.png',
    scale=(window.aspect_ratio * 15, 15),
    z=3
)

# --- Camera setup ---
mouse.visible = True
current_location = "start"
camera.orthographic = True
camera.fov = 15
camera.position = (0, 0)
Text.default_resolution *= 2 

# --- Current part selection ---
currentPart = "houses"

# --- Track indexes for each part ---
currentIndexes = {
    "houses": 0,
    "roofs": 0,
    "doors": 0,
    "windows": 0,
    "bushes": 0
}

# --- parts lists ---
houses = [
    'resources/house/white.png',
    'resources/house/blue.png',
    'resources/house/cream.png',
    'resources/house/dark_blue.png',
    'resources/house/green.png',
    'resources/house/light_green.png',
    'resources/house/pink.png',
    'resources/house/yellow.png'
]

roofs = [
    'resources/roof/Brown_Roof.png',
    'resources/roof/Green_Roof.png',
    'resources/roof/LightBlue_Roof.png',
    'resources/roof/Pink_Roof.png',
    'resources/roof/Red_Roof.png'
]

doors = [
    'resources/doors/arch.png',
    'resources/doors/square1.png',
    'resources/doors/square2.png'   
]

windows = [
    'resources/windows/oval.png',
    'resources/windows/circle.png',
    'resources/windows/square.png'
]

bushes = [
    'resources/bushes/color.png',
    'resources/bushes/rose.png',
    'resources/bushes/sunflower.png'
]

# --- Entities for displaying parts ---
house_entity = Entity(model='quad', texture=houses[0], scale=(8,8), z=-1)
roof_entity = Entity(model='quad', texture=roofs[0], scale=(8,6.5), position=(0.01,3.4,-2))
door_entity = Entity(model='quad', texture=doors[0], scale=(1.3,1.6), position=(0,-1.8,-3))
window_group = Entity()
bushes_group = Entity()

# Left window

left_window = Entity(
    parent=window_group,
    model='quad',
    texture=windows[0],
    scale=(1, 1.5),
    position=(-2, -1, -1.5)
)

# Right window (mirrored)
right_window = Entity(
    parent=window_group,
    model='quad',
    texture=windows[0],
    scale=(1, 1.5), 
    position=(2, -1, -1.5)
)

left_bush = Entity(
    parent=bushes_group,
    model='quad',
    texture=bushes[0],
    scale=(3,1.5),
    position=(-2, -3, -4)
)

right_bush = Entity(
    parent=bushes_group,
    model='quad',
    texture=bushes[0],
    scale=(3,1.5),
    position=(2, -3, -4)
)

roof_entity.texture_scale = (1, 1)  # Ensures full texture is drawn

# --- Map parts to their textures & entities ---
partData = {
    "houses": {"textures": houses, "entity": house_entity},
    "roofs": {"textures": roofs, "entity": roof_entity},
    "doors": {"textures": doors, "entity": door_entity},
    "windows": {"textures": windows, "entity": window_group},
    "bushes": {"textures": bushes, "entity": bushes_group}
}

# --- Set current part ---
def set_current_part(part):
    global currentPart
    currentPart = part
    print(f"Selected part: {currentPart}")

# --- Part buttons ---
houses_button = Button(texture="resources/house_button.png", color=color.white, scale=(0.1,0.1), position=(-0.4, -0.3), z=5, on_click=lambda: set_current_part("houses"))
roofs_button = Button(texture="resources/roof_button.png", color=color.white, scale=(0.1,0.1), position=(-0.2, -0.3), z=5, on_click=lambda: set_current_part("roofs"))
doors_button = Button(texture="resources/door_button.png", color=color.white, scale=(0.1,0.1), position=(0, -0.3), z=5, on_click=lambda: set_current_part("doors"))
windows_button = Button(texture="resources/window_button.png", color=color.white, scale=(0.1,0.1), position=(0.2, -0.3), z=5, on_click=lambda:set_current_part("windows"))
bushes_button = Button(texture="resources/bushes_button.png", color=color.white, scale=(0.1,0.1), position=(0.4, -0.3), z=5, on_click=lambda:set_current_part("bushes"))

# --- Generic cycle function ---
def cycle_part(direction):
    part = currentPart
    index = currentIndexes[part]
    textures = partData[part]["textures"]
    entity = partData[part]["entity"]

    # Cycle index
    index = (index + direction) % len(textures)
    currentIndexes[part] = index

    # Update texture
    if part == "windows" or part == "bushes":
        # Update both left and right windows
        for child in entity.children:
            child.texture = textures[index]
    else:
        entity.texture = textures[index]

# --- Arrow buttons ---
left_arrow = Button(model='quad', texture="resources/left_arrow.png", color=color.white, scale=(0.08,0.08), position=(-0.35, -0.05), z=5, on_click=lambda: cycle_part(-1))
right_arrow = Button(model='quad', texture="resources/right_arrow.png", color=color.white, scale=(0.08,0.08), position=(0.35, -0.05), z=5, on_click=lambda: cycle_part(1))

app.run()
