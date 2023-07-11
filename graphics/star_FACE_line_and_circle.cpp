#include <stdio.h>
#include <conio.h>
#include <graphics.h>

int main(){
    int gdriver = DETECT, gmode;
    initgraph(&gdriver, &gmode, (char*)"");

    setcolor(RED);
    line(200,350,400,350);
    setcolor(YELLOW);
    circle(300,250,200);

    getch();
    closegraph();
    return 0;
}