#include<graphics.h>
#include<stdlib.h> 
#include<stdio.h> 
#include<conio.h> 
#include<iostream> 
using namespace std;

int x1,y1,x2,y2,x,y,x3,y3,x4,y4,ch; 
int main()
{
    int gd=DETECT,gm;
    initgraph(&gd,&gm, (char*)"");
    do
    {
    
        cout<<"\n\n##########MAIN-MENU##########\n";
        cout<<"          TRANSLATION\n";
        cout<<"1. LINE\n";
        cout<<"2. RECTANGLE\n";
        cout<<"3. TRIANGLE\n";
        cout<<"enter your choice : 0 for exit\n";
        cin>>ch;
        switch(ch)
        {
            case 1: cout<<"enter the values of line coordinates: ";
                    cin>>x1>>y1>>x2>>y2;
                    cout<<"\nenter the translation coordinates:";
                    cin>> x >> y;
                    line(x1, y1, x2, y2);
                    
                    delay(1000);
                    cout <<"\nnow hit a key to see translation :";                    
                    line(x1 + x, y1 + y, x2 + x, y2 + y);
                    break;

            case 2: cout<<"enter the top left coordinates: ";
                    cin>>x1>>y1;
                    cout<<"\nenter the bottom right coordinates: ";
                    cin>>x2>>y2;
                    cout<<"\nenter the values of translation coordinate: \n";
                    cin>>x>>y;
                    cleardevice();
                    rectangle(x1,y1,x2,y2);

                    delay(1000);
                    cout<<"\nnow hit a key to see translation: ";                    
                    rectangle(x1 + x, y1 + y, x2 + x, y2 + y);
                    break;

            case 3: cout<<"enter coordinates of line1: \n";
                    cin>>x1>>y1>>x2>>y2;
                    cout<<"\nenter coordinates for relative line: \n";
                    cin>>x3>>y3;
                    cout<<"\nenter translation coordinates: ";
                    cin>>x>>y;
                    cleardevice();
                    line(x1,y1,x2,y2);

                    delay(1000);
                    moveto(x2,y2);
                    lineto(x3,y3);
                    moveto(x3,y3);
                    lineto(x1,y1);

                    delay(1000);  
                    cout<<"\nnow hit a key to see translation:";                                      
                    moveto(x1+x,y1+y);
                    lineto(x2+x,y2+y);
                    moveto(x2+x,y2+y);
                    lineto(x3+x,y3+y);
                    moveto(x3+x,y3+y);
                    lineto(x1+x,y1+y);
                    break;

            case 0: break;
            default: cout<<"invalid choice"; break;
        }
    }while(ch!=0);
    getch();
    closegraph();
}