/***
Class Bullet calculates the movement of diagonal throw with air resistance.
antsol
***/
#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>
#include <fstream>

// constant value of acceleration of gravity
const double G = 9.81;

// time step
const double DELTA = 0.01;

// to save results and test class
std::ofstream file;

class Bullet {

private:
    // factor of air resistance
    double k = 0.4;
    // coordinates of movement
    double x, y, v_x, v_y, a_x, a_y;
    // initial conditions
    double alpha, v_0, m;
    // time of movement
    double t;

protected:
    /*
        calculates new movement's coordinates after one time step
    */
    void step(double delta) {
        file << x << ' ' << y << '\n';

        t += delta;

        a_x = -k * v_x * abs(v_x) / m;
        a_y = -k * v_y * abs(v_y) / m - G;

        v_x += delta * a_x;
        v_y += delta * a_y;

        x += v_x * delta;
        y += v_y * delta;
    }

public:
    /* constructor */
    Bullet(double alpha, double v_0, double m)
    : alpha(alpha * M_PI / 180.0), v_0(v_0), m(m) {
        t = 0; x = 0; y = 0;
        v_x = v_0 * cos(this->alpha);
        v_y = v_0 * sin(this->alpha);
        a_y = G;
        a_x = 0;
    }

    /* initializing of throw */
    void start(double delta) {
        this->step(delta);
        while (y > 0) {
            this->step(delta);
        }
    }

    // return total time of throw
    double get_time() {
        return t;
    }

    // return total range of throw
    double get_range() {
        return x;
    }
};

int main(int argc, char *argv[]) {
    file.open("wyniki.txt");
    char *ptr;
    Bullet B = Bullet(strtod(argv[1], &ptr), strtod(argv[2], &ptr), strtod(argv[3], &ptr));
    //Bullet B = Bullet(75, 45, 0.15);
    B.start(DELTA);
    std::cout << B.get_range() << " m, " << B.get_time() << " s\n";
    file.close();
}
