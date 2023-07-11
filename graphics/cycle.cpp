#include<stdio.h>
#include<graphics.h>
#include<stdlib.h>
#include<math.h>
int main()
{
int gd,gm,x;
gd=DETECT;
initgraph(&gd,&gm,"C:\\TURBOC3\\BGI");

  for(x=0;x<650;x++)
  {
   cleardevice();

   line(10,401,630,401);
   circle(40+x,370,30);
   circle(150+x,370,30);
   line(40+x,370,100+x,370);
   line(40+x,370,60+x,340);
   line(100+x,370,120+x,340);
   line(120+x,340,60+x,340);
   line(60+x,340,60+x,335);
   line(55+x,335,65+x,335);

   line(150+x,370,100+x,320);
   line(100+x,320,90+x,320);
   delay(10);
  }
getch();
closegraph();
}