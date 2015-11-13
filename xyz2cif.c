#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {
    FILE *fp;
    char buffer[1000];
    int lines = 0;
    char filename[] = "STO-110.xyz";

    double** A;
    double *data;
    char** Element;
    char* symbol;

    double xmax, xmin, ymax, ymin = 0;
    double xlim, ylim = 0;
    double theta = 0;

    fp = fopen(filename, "r");
    if (fp != NULL){
        while(fgets(buffer, sizeof(buffer), fp) != NULL){
           lines++;
        }
        fseek(fp, 0, SEEK_SET);
        int i = 0;
        data = (double*) malloc(sizeof(double)*lines*3);
        A = (double**) malloc(sizeof(double*)*lines);
        Element = (char**) malloc(lines*sizeof(char*));

        int j;
        for(j = 0; j<lines; j++)
            A[j] = &data[j*3];

        for(j = 0; j<lines; j++)
            Element[j] = (char*) malloc(2*sizeof(char));

        while(fgets(buffer, sizeof(buffer), fp) != NULL){

            sscanf(buffer, "%s %lf %lf %lf",Element[i], &A[i][0], &A[i][1], &A[i][2]);
            xmin = fmin(xmin,A[i][0]);
            ymin = fmin(ymin,A[i][1]);
            zmin = fmin(ymin,A[i][2]);
            xmax = fmax(xmax,A[i][0]);
            ymax = fmax(ymax,A[i][1]);
            zmax = fmax(ymin,A[i][2]);
            printf("%s %lf %lf %lf",Element[i], A[i][0],A[i][1], A[i][2]);
            printf("\n");

            i++;
        }

        xlim = xmax - xmin;
        ylim = ymax - ymin;
        zlim = zmax - zmin;

        //printf("Xlim %lf Ylim: %lf Zlim: %lf ", xlim, ylim, zlim);
        for(i = 2; i < lines; i++){
            for(j=0; j < 3; j++) {
                double tempX =  A[i][0]*cos(theta) - A[i][1]*sin(theta)
                double tempY =  A[i][0]*sin(theta) + A[i][1]*cos(theta)
                A[i][0] = tempX/xlim;
                A[i][1] = tempY/ylim;
                printf("Rotated Data %s %lf %lf %lf\n",Element[i], A[i][0],A[i][1], A[i][2]);
            }
        }

        free(data);
        free(A);
        int k;
        for (k = 0; k<lines; k++)
            free(Element[k]);
        free(Element);
    } else {
        printf("File not found !\n");
    }

    fclose(fp);
    return 0;
}
