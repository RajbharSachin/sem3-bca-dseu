#include<stdio.h>
#include<graphics.h>

int main(){
    int gd= DETECT ,gm;
    initgraph(&gd, &gm, (char*)"");

    float r=10,x,y;
    for(x=10,y=480; x<=325; x+=1.32,y--)
    {
        circle(x,y,r);
        circle(650-x, 480-y, r);
        delay(15);
        cleardevice();
    }
    float a,b;
    for(a=325,b=240; a>=0; a-=1.3,b++)
    {
        circle(a,b,r);
        circle(650-a, 480-b, r);
        delay(15);
        cleardevice();
    }

    getch();
    closegraph();
    return 0;
}