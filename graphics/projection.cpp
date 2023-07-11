#include<stdio.h>
#include<conio.h>
#include<graphics.h>
#include<math.h>
int midx,midy,maxx,maxy;
void main()
{
  int gd,gm,x,y,z;
  
  detectgraph(&gd,&gm);
  initgraph(&gd,&gm,"C:\\tc\\bgi");
  setfillstyle(3,2);
  maxx=getmaxx();
  maxy=getmaxy();
  midx=maxx/2;
  midy=maxy/2;
  line(midx,0,midx,maxy);
  line(0,midy,maxx,midy);
  bar3d(midx-250,midy+150,midx-150,midy+225,20,4);
  printf("\n Enter the projection vector:\t");
  scanf("%d%d%d",&x,&y,&z);
  bar3d(midx-(x*5),midy-(y*9),midx-(x*3),midy-(y*5),10*z,4);
  getch();
  closegraph();
}