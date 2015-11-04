#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *fp;
    char buffer[1000];
    int lines = 0;
    char filename[] = "STO-110.xyz";

    double** A;
    double *data;
    char** Element; 
    char* symbol;

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
            printf("%s %lf %lf %lf",Element[i], A[i][0],A[i][1], A[i][2]);
            printf("\n");
            
            i++;
        }
        free(data);
        free(A);
        int k;
        for (k = 0; k<lines; k++)
            free(Element[k]);
        free(Element);

        printf("%d \n",lines);
        fclose(fp);
    } else {
        printf("File not found !\n");
    }

    return 0;
}
