#include <stdio.h>
#include <string.h>

void word_finder(char string[], char word[]) {
    
    int len_string = strlen(string);
    int len_word = strlen(word);
    int flag;

    for (int i=0; i<len_string - len_word; i++) {
        flag = 1;
        for (int j=0; j<len_word; j++) {
            if (string[i+j] != word[j]) {
                flag = 0;
                break;
            }
        }
        if (flag == 1) {
            printf("\nFound the word at: %d", i);
        }
    } 
}


int main() {

    char string[] = "Albert Enstein was a brilliant genius by the way! Albert!";
    char word[] = "Albert";

    printf("Trying to find the word inside text..");
    word_finder(string, word);

    return 0;
}
