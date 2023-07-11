#include <iostream>
#include <graphics.h>
#include <conio.h>
using namespace std;

void breline(int, int, int, int);

int main(){
    int gd = DETECT, gm;
    int x1, y1, xn, yn;
    initgraph(&gd, &gm, (char*)"");
    cout<<"Enter starting coordinates:\n";
    cin>>x1>>y1;
    cout<<"Enter ending coordinates:\n";
    cin>>xn>>yn;

    breline(x1,y1,xn,yn);

    getch();
    closegraph();
    return 0;
}

void breline(int x1, int y1, int xn, int yn){
    int dx,dy,ds,dt,di;
    dx=xn-x1;
    dy=yn-y1;
    di=2*dy-dx;
    ds=2*dy;
    dt=2*(dy-dx);

    putpixel(x1,y1,WHITE);

    while(x1<xn)
    {
        x1++;
        if(di<0)
            di=di+ds;
        else
        {
            y1++;
            di=di+dt;
        }
        putpixel(x1,y1,WHITE);
        delay(5);
    }
}