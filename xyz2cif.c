#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(int argc, char **argv) {
    FILE *fp;
    char buffer[1000];
    int lines = 0;
    char *filename = argv[1];

    double** A;
    double *data;
    char** Element;
    char* symbol;

    double xmax= 0, xmin= 0, ymax= 0, ymin= 0, zmax= 0, zmin = 0;
    double xlim= 0, ylim= 0, zlim = 0;
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

            xmin = fminl(xmin, A[i][0]);
            ymin = fminl(ymin, A[i][1]);
            zmin = fminl(zmin, A[i][2]);

            xmax = fmaxl(xmax, A[i][0]);
            ymax = fmaxl(ymax, A[i][1]);
            zmax = fmaxl(zmax, A[i][2]);

            //printf("%s %lf %lf %lf",Element[i], A[i][0],A[i][1], A[i][2]);
            //printf("\n");

            i++;
        }

        xlim = xmax - xmin;
        ylim = ymax - ymin;
        zlim = zmax - zmin;

        printf("Xlim %lf Ylim: %lf Zlim: %lf \n", xmin, ymin, zmin);

        for(i = 2; i < lines; i++){

            double tempX =  A[i][0]*cos(theta) - A[i][1]*sin(theta);
            double tempY =  A[i][0]*sin(theta) + A[i][1]*cos(theta);

            A[i][0] = tempX;
            A[i][1] = tempY;

            A[i][0] -= xmin;
            A[i][0] /= xlim;

            A[i][1] -= ymin;
            A[i][1] /= ylim;

            A[i][2] -= zmin;
            A[i][2] /= zlim;

            printf("%s %lf %lf %lf\n",Element[i], A[i][0],A[i][1], A[i][2]);
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
