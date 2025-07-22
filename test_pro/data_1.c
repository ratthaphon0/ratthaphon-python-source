#include <stdio.h>
int max_size = 10;
int current_size = 5;
int array[10] = {10,20,30,40,50};
int position_to_insert = 2;
int element_to_insert = 25;
void print_array();

int main(){
	printf("\tOld Array \n");
	print_array();
    if (current_size < max_size){
        for (int i = current_size; i > position_to_insert; i--){
            array[i] = array[i-1];
        }
        array[position_to_insert] = element_to_insert;
        current_size = current_size + 1;
    }
    printf("\tNew Array \n");
    print_array();
}

void print_array(){

	for (int i = 0; i < current_size ; i++){
		printf("array[%d] = %d\n",i,array[i]);
	}
}