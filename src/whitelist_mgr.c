/*

TODO:

clear --DONE

add ip
add list
remove ip
remove list
get whitelist
change config

*/


#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#include "../libs/cJSON.h"

#define list_size 100
#define default_config_filename "./bin/whitelist_config.json";
#define default_whitelist_filename "whitelist.wl";


int* white_list;
char* whitelist_filename;
char* config_filename;



int readConfigFile(){
	
	int config_file_size = 1000;

	FILE* file;
	file = fopen(config_filename,"r");

	char *file_string;
    size_t n = 0;
    int c;

    if (file == NULL){
        return 1; //could not open file
    }

    file_string = malloc(config_file_size);

    while ((c = fgetc(file)) != EOF)
    {
        file_string[n++] = (char) c;
    }
    //terminate with the null character
    file_string[n] = '\0';  

    fprintf(stderr, "FULL JSON: \n%s\n", file_string);

    cJSON* config_data = cJSON_Parse(file_string);

    fprintf(stderr, "%s\n", cJSON_GetObjectItem(config_data,"whitelist_filename")->valuestring);
    whitelist_filename = cJSON_GetObjectItem(config_data,"whitelist_filename")->valuestring;
	return fclose(file);
}

int handleArgs(int argc, char** argv){

	config_filename = default_config_filename;

    int opt;

	while ((opt = getopt(argc, argv, "")) != -1) {
        switch (opt) {
        default:
            break;
        }
    }

    return readConfigFile();
}

int clearFile(){
	FILE* file;
	file = fopen(whitelist_filename,"w");
	return fclose(file);
}

int readWhitelist(){
	return 0;
}



int main( int argc, char** argv ) {
	int err = handleArgs(argc,argv);
	if(err != 0){
		fprintf(stderr, "%s", "ERROR: An error has occured in setting up configuration variables.");
		return 1;
	}
	clearFile();
	return 0;
}