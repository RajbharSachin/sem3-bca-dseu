#include<stdio.h>
#include<conio.h>
#include<graphics.h>

int main(){
    int gd= DETECT ,gm;
    initgraph(&gd, &gm, (char*)"");

    float r=10,x,y;
    for(x=10,y=480; x<=630; x+=1.32,y--)
    {
        circle(x,y,r);
        delay(10);
        cleardevice();
    }

    getch();
    closegraph();
    return 0;
}