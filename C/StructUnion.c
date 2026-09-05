#include <stdio.h>
#include <stdbool.h>
#include <string.h>

int main()
{
    // union packet {
    //     int id;
    //     double size;
    //     char descr[50];
    // };

    // union packet packet1;

    struct packet {
        int id;
        double size;
        char descr[50];
    };

    struct packet packet1;

    packet1.id = 4621;
    packet1.size = 56730.54;
    strcpy(packet1.descr, "ALERT: There is congestion in routers!");

    printf("id: %d", packet1.id);
    printf("\nsize: %lf", packet1.size);
    printf("\ndescription: %s", packet1.descr);

    return 0;

}