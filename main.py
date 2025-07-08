import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import pywavefront

# Global state
rotation = [0, 0]     # x, y rotation
zoom = -10.0          # zoom level (Z position)
pan = [0.0, 0.0]      # x, y panning offset

left_mouse_down = False
right_mouse_down = False
last_mouse_pos = [0, 0]

def load_model(path):
    print(f"Loading model: {path}")
    scene = pywavefront.Wavefront(path, collect_faces=True)
    print("Loaded vertices:", len(scene.vertices))
    return scene

def draw_model(scene):
    glEnable(GL_DEPTH_TEST)
    glPushMatrix()

    glTranslatef(pan[0], pan[1], zoom)     # Apply panning and zoom
    glRotatef(rotation[0], 1, 0, 0)
    glRotatef(rotation[1], 0, 1, 0)
    glColor3f(1.0, 1.0, 1.0)

    for name, mesh in scene.meshes.items():
        glBegin(GL_TRIANGLES)
        for face in mesh.faces:
            for vertex_i in face:
                glVertex3f(*scene.vertices[vertex_i])
        glEnd()

    glPopMatrix()


def draw_hud_axes(length=50):
    # Save current matrices
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()

    # Orthographic projection: left, right, bottom, top, near, far
    glOrtho(0, 800, 0, 600, -1, 1)  # Match window size

    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()

    glLineWidth(3.0)
    glBegin(GL_LINES)

    # Position the axes somewhere in the bottom-left corner
    origin_x, origin_y = 50, 50

    # X axis (red)
    glColor3f(1, 0, 0)
    glVertex2f(origin_x, origin_y)
    glVertex2f(origin_x + length, origin_y)

    # Y axis (green)
    glColor3f(0, 1, 0)
    glVertex2f(origin_x, origin_y)
    glVertex2f(origin_x, origin_y + length)

    # Z axis (blue) - let's draw it diagonally for visualization
    glColor3f(0, 0, 1)
    glVertex2f(origin_x, origin_y)
    glVertex2f(origin_x + length * 0.7, origin_y + length * 0.7)

    glEnd()
    glLineWidth(1.0)

    # Restore matrices
    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)

def main():
    global rotation, zoom, pan, left_mouse_down, right_mouse_down, last_mouse_pos

    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("3D Model Viewer - Mouse Rotate, Zoom, Pan")

    glClearColor(0.1, 0.1, 0.1, 1.0)

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0] / display[1]), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

    scene = load_model('cube.obj')  # Replace with your .obj

    clock = pygame.time.Clock()
    running = True

    while running:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    left_mouse_down = True
                    last_mouse_pos = list(pygame.mouse.get_pos())
                elif event.button == 3:
                    right_mouse_down = True
                    last_mouse_pos = list(pygame.mouse.get_pos())
                elif event.button == 4:  # Scroll up
                    zoom += 1.0
                elif event.button == 5:  # Scroll down
                    zoom -= 1.0

            elif event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    left_mouse_down = False
                elif event.button == 3:
                    right_mouse_down = False

            elif event.type == MOUSEMOTION:
                x, y = pygame.mouse.get_pos()
                dx = x - last_mouse_pos[0]
                dy = y - last_mouse_pos[1]

                if left_mouse_down:
                    rotation[1] += dx * 0.5
                    rotation[0] += dy * 0.5
                elif right_mouse_down:
                    pan[0] += dx * 0.01
                    pan[1] -= dy * 0.01

                last_mouse_pos = [x, y]

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        draw_model(scene)
        draw_hud_axes()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()

