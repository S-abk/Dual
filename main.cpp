#include <GL/glut.h>
#include <cmath>
#include <cstdlib>

int screenWidth, screenHeight;

struct Ball {
    float x, y, dx, dy, radius;
    float r, g, b;
};

Ball balls[5];

void initBalls() {
    for (int i = 0; i < 5; i++) {
        balls[i].x = (float)rand() / RAND_MAX * screenWidth;
        balls[i].y = (float)rand() / RAND_MAX * screenHeight;
        balls[i].dx = ((float)rand() / RAND_MAX - 0.5f) * 0.02f * screenWidth;
        balls[i].dy = ((float)rand() / RAND_MAX - 0.5f) * 0.02f * screenHeight;
        balls[i].radius = 0.05f * screenWidth;
        balls[i].r = (float)rand() / RAND_MAX;
        balls[i].g = (float)rand() / RAND_MAX;
        balls[i].b = (float)rand() / RAND_MAX;
    }
}

void drawBall(const Ball& ball) {
    glColor3f(ball.r, ball.g, ball.b);
    glBegin(GL_POLYGON);
    for (int i = 0; i < 100; i++) {
        float angle = 2.0f * 3.14159f * i / 100;
        glVertex2f(ball.x + ball.radius * cos(angle), ball.y + ball.radius * sin(angle));
    }
    glEnd();
}

void display() {
    glClear(GL_COLOR_BUFFER_BIT);
    for (const Ball& ball : balls) {
        drawBall(ball);
    }
    glutSwapBuffers();
}

void update(int value) {
    for (Ball& ball : balls) {
        ball.x += ball.dx;
        ball.y += ball.dy;
        if (ball.x < ball.radius || ball.x > screenWidth - ball.radius) ball.dx = -ball.dx;
        if (ball.y < ball.radius || ball.y > screenHeight - ball.radius) ball.dy = -ball.dy;
    }
    glutPostRedisplay();
    glutTimerFunc(16, update, 0);
}

void reshape(int width, int height) {
    screenWidth = width;
    screenHeight = height;
    glViewport(0, 0, screenWidth, screenHeight);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(0.0, screenWidth, 0.0, screenHeight);
    glMatrixMode(GL_MODELVIEW);
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
    glutCreateWindow("OpenGL Screensaver");
    glutFullScreen();
    glutDisplayFunc(display);
    glutReshapeFunc(reshape);
    glutTimerFunc(0, update, 0);
    initBalls();
    glutMainLoop();
    return 0;
}