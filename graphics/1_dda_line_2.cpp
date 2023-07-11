#include <iostream>
#include <conio.h>
#include <graphics.h>
using namespace std;

void ddaline(int, int, int, int);

int main(){
    int gd = DETECT, gm;
    int x1, y1, xn, yn;
    initgraph(&gd, &gm, (char*)"");
    cout<<"Enter starting coordinates:\n";
    cin>>x1>>y1;
    cout<<"Enter ending coordinates:\n";
    cin>>xn>>yn;

    ddaline(x1,y1,xn,yn);

    getch();
    closegraph();
    return 0;
}

void ddaline(int x1,int y1,int xn,int yn){
    int m,dx,dy,i;
    m = (yn-y1)/(xn-x1);
    for(i = x1; i<xn; i++)
    {
        if(m<=1)
        {
            dx = 1;
            dy = m*dx;
        }
        else
        {
            dy = 1;
            dx = dy/m;
        }
        x1 = x1+dx;
        y1 = y1+dy;

        putpixel(x1,y1,RED);
        delay(5);
    }
}
    