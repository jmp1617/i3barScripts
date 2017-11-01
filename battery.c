#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void find_tokens(int tokens[100], char output[100]){
    int token=0;
    for(int cha=0; cha<100; cha++)
        if(output[cha]==' ')
            tokens[token++] = cha;
}

int get_percent(int tokens[100], char output[100]){
    char sub[tokens[3]-tokens[2]-2];
    memcpy(sub, &output[tokens[2]+1], tokens[3]-tokens[2]-3);
    sub[tokens[3]-tokens[2]-3]='\0';
    return strtol(sub, NULL, 10);
}

int get_remain(int tokens[100], char output[100], char remain[6]){
    memcpy(remain, &output[tokens[3]+1], 5);
    remain[5]='\0';
}

int main(){
    static char icon[][6] = {"", "", "", "", "", ""};
    FILE* fp;
    char output[100]={0};
    
    char status=0;
    int state=0;
    int percent=0;
    char remain[6]={0};

    fp = popen("acpi","r");
    if(!fp){
        printf("%s","Failed");   
        exit(1);
    }
   
    fgets(output, sizeof(output)-1, fp);

    pclose(fp);
    
    status = output[11];
    
    if(status=='U'){
        printf("%s 100%% Full",icon[4]);
        exit(0);
    }

    int tokens[100]={0};
    find_tokens(tokens, output); 
    percent = get_percent(tokens,output);
    get_remain(tokens,output,remain);

    if(status=='C') //if charging
        state = 5;
    else //determine state based on percentage
        if(percent>=80)
            state=4;
        else if(percent>=60)
            state=3;
        else if(percent>=40)
            state=2;
        else if(percent>=20)
            state=1;
        else
            state=0; 

    printf(" %s %d%% %s ",icon[state],percent,remain);

    return 0;
}
