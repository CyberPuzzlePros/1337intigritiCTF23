#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

int array[] = {42, 77, 3, 8, 69, 86, 60, 99, 50, 76, 15, 14, 41, 87, 45, 61, 16, 50, 20, 5, 13, 33, 62, 70, 70, 77, 28, 85, 82, 26, 28, 32, 56, 22, 21, 48, 38, 42, 98, 20, 44, 66, 21, 55, 98, 17, 20, 93, 99, 54, 21, 43, 80, 99, 64, 98, 55, 3, 95, 16, 56, 62, 42, 83, 72, 23, 71, 61, 90, 14, 33, 45, 84, 25, 24, 96, 74, 2, 1, 92, 25, 33, 36, 6, 26, 14, 37, 33, 100, 3, 30, 1, 31, 31, 86, 92, 61, 86, 81, 38};

void process_string(char* input_string, int length) {
   assert(length == 24);
   for (int i = 0; i < length; ++i) {
       input_string[i] ^= array[i % sizeof(array)] ^ 0x266E + 0x1537 + 0x1B37 - 0x43A5;
   }
}

int get_file_size(FILE* file) {
   if (fseek(file, 0, SEEK_END) < 0) {
       fclose(file);
       return -1;
   }
   int size = ftell(file);
   rewind(file);
   return size;
}

int main(int argc, const char * argv[]) {
   if (argc != 2) {
       printf("Usage: %s <input_file>\n", argv[0]);
       exit(-1);
   }

   FILE* input_file = fopen(argv[1], "r");
   if (input_file == NULL) {
       perror("Error opening input file");
       return -1;
   }

   int file_size = get_file_size(input_file);
   char* input_string = (char*) malloc(file_size + 1);
   if (input_string == NULL) {
       perror("Memory allocation failed");
       fclose(input_file);
       return -1;
   }

   fgets(input_string, file_size, input_file);
   fclose(input_file);

   process_string(input_string, file_size);

   FILE* output_file = fopen("output", "wb");
   if (output_file == NULL) {
       perror("Error opening output file");
       free(input_string);
       return -1;
   }

   fwrite(input_string, file_size, sizeof(char), output_file);
   fclose(output_file);

   free(input_string);

   return 0;
}
