import glfw
from OpenGL.GL import *

delta = 0.1
angle = 0.0
posx = 0.0
posy = 0.0
size = 0.0


def main():
    if not glfw.init():
        return
    window = glfw.create_window(1000, 1000, "", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    glfw.set_key_callback(window, key_callback)
    glfw.set_scroll_callback(window, scroll_callback)
    while not glfw.window_should_close(window):
        display(window)

    glfw.destroy_window(window)
    glfw.terminate()


def display(window):
    global angle
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glPushMatrix()
    glRotatef(angle, 0, 0, 1)
    glBegin(GL_POLYGON)
    glColor3f(5, 0, 0)
    glVertex2f(posx + size + 0.5, posy + size + 0.5)
    glColor3f(5, 0, 0)
    glVertex2f(posx - size + -0.5, posy + size + 0.5)
    glColor3f(5, 0, 0)
    glVertex2f(posx - size + -0.5, posy - size + -0.5)
    glColor3f(5, 0, 0)
    glVertex2f(posx + size + 0.5, posy - size + -0.5)
    glColor3f(5, 0, 0)
    glVertex2f(posx + size + 1.0, posy)  # Вершина в центре пятиугольника
    glVertex2f(posx + size + 0.5, posy + size + 0.5) #Вершина справа от центра пятиугольника
    glVertex2f(posx - size + -0.5, posy + size + 0.5) #Вершина сверху от центра пятиугольника
    glVertex2f(posx - size - 0.5, posy) #Вершина слева от центра пятиугольника
    glVertex2f(posx - size + -0.5, posy - size + -0.5) #Вершина снизу от центра пятиугольника
    glEnd()
    glPopMatrix()
    angle += delta
    glfw.swap_buffers(window)
    glfw.poll_events()


def key_callback(window, key, scancode, action, mods):
    global delta
    global angle
    if action == glfw.PRESS:
        if key == glfw.KEY_RIGHT:
            delta = -1
        if key == glfw.KEY_LEFT:
            delta = 1


def scroll_callback(window, xoffset, yoffset):
    global size
    if xoffset > 0:
        size -= yoffset / 10
    else:
        size += yoffset / 10


if __name__ == '__main__':
    main()
