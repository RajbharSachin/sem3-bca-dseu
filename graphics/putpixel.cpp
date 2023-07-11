#include <stdio.h>
#include <graphics.h>

int main(){
    int x,y;
    int gd= DETECT, gm;
    initgraph(&gd,&gm,(char*)"");

    printf("Enter value of x & y : ");
    scanf("%d %d",&x,&y);
    putpixel(x,y,RED);

    getch();
    closegraph();
    return 0;
}