#include<stdio.h>
#include<conio.h>
#include<graphics.h>

void ripple(int s, int d){
    int i=0;
    for(int x=320,y=240,r=s; r<=220,i<=17; r+=d+i){
        circle(x,y,r);
        delay(100);
        i+=2;
    }
}

int main(){
    int gd=DETECT;
    int gm;
    initgraph(&gd,&gm,(char*)"");
    
    int s,d;
    printf("Enter the starting radius: ");
    scanf("%d", &s);
    printf("Enter the difference between radius: ");
    scanf("%d", &d);
    ripple(s,d);

    getch();
    closegraph();
    return 0;
}