//Ratthaphon Khan 6730202734 
//Nichakamon Tapaohirun 6730202173



#include <stdio.h>   
#include <stdlib.h>  

struct Node {
    int data;            
    struct Node* next;   
    struct Node* prev;
};

struct Node* head = NULL;

struct Node* createNode(int value) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    if (newNode == NULL) {
        printf("Memory allocation failed!\n");
        exit(1);
    }
    newNode->data = value;
    newNode->next = NULL;
    newNode->prev = NULL;
    return newNode;
}

void insertAtBeginning(int value) {
    struct Node* newNode = createNode(value);
    if (head != NULL) {
        newNode->next = head;
        head->prev = newNode;
    }
    head = newNode;
    printf("Node with data %d inserted at the beginning.\n", value);
}

void insertAtEnd(int value) {
    struct Node* newNode = createNode(value);

    if (head == NULL) {
        head = newNode;
        printf("Node with data %d inserted at the end (list was empty).\n", value);
        return;
    }

    struct Node* current = head;
    while (current->next != NULL) {
        current = current->next;
    }
    current->next = newNode;
    newNode->prev = current;
    printf("Node with data %d inserted at the end.\n", value);

}

void insertAfter(int afterValue, int valueToInsert) {
    if (head == NULL) {
        printf("List is empty. Cannot insert after %d as it might not exist.\n", afterValue);
        return;
    }

    struct Node* current = head;
    while (current != NULL && current->data != afterValue) {
        current = current->next;
    }

    if (current == NULL) {
        printf("Node with data %d not found in the list. Cannot insert after it.\n", afterValue);
        return;
    }

    struct Node* newNode = createNode(valueToInsert);
    newNode->next = current->next;
    newNode->prev = current;
    if (current->next != NULL) {
        current->next->prev = newNode;
    }
    current->next = newNode;
    printf("Node with data %d inserted after node with data %d.\n", valueToInsert, afterValue);

}

void deleteFromBeginning() {
    if (head == NULL) {
        printf("List is empty, nothing to delete from beginning.\n");
        return;
    }

    struct Node* temp = head;
    head = head->next;
    if (head != NULL) {
        head->prev = NULL;
    }
    printf("Node with data %d deleted from the beginning.\n", temp->data);
    free(temp);

}

void deleteFromEnd() {
    if (head == NULL) {
        printf("List is empty, nothing to delete from end.\n");
        return;
    }

    if (head->next == NULL) {
        printf("Node with data %d deleted from the end.\n", head->data);
        free(head);
        head = NULL;
        return;
    }

    struct Node* current = head;
    struct Node* prev = NULL;

    while (current->next != NULL) {
        prev = current;
        current = current->next;
    }

    prev->next = NULL;
    printf("Node with data %d deleted from the end.\n", current->data);
    free(current);

}

void deleteNodeByValue(int valueToDelete) {
    if (head == NULL) {
        printf("List is empty, nothing to delete by value %d.\n", valueToDelete);
        return;
    }
    struct Node* current = head;
    while (current != NULL && current->data != valueToDelete) {
        current = current->next;
    }
    if (current == NULL) {
        printf("Node with data %d not found in the list.\n", valueToDelete);
        return;
    }
    
    if (current->prev != NULL) {
        current->prev->next = current->next;
    } else {
        head = current->next;
    }

    if (current->next != NULL) {
        current->next->prev = current->prev;
    }

    printf("Node with data %d deleted.\n", current->data);
    free(current);

}

void displayList() {
    if (head == NULL) {
        printf("Linked List is empty.\n");
        return;
    }

    struct Node* current = head;
    printf("Linked List: ");
    while (current != NULL) {
        printf("%d <-> ", current->data);
        current = current->next;
    }
    printf("NULL\n");
}
void showMenu() {
    printf("\n====== Doubly Linked List Menu ======\n");
    printf("1. Display list\n");
    printf("2. Insert data in the begining\n");
    printf("3. Insert data in the end\n");
    printf("4. Insert data after a node with specific value\n");
    printf("5. Delete data from beginning\n");
    printf("6. Delete data from end\n");
    printf("7. Delete data by value\n");
    printf("0. Exit Program\n");
    printf("Select Menu: ");
}

int main() {
    int choice, value, afterValue;
    while (1) {
        showMenu();
        scanf("%d", &choice);
        switch (choice) {
            case 1:
                displayList();
                break;
            case 2:
                printf("Enter value to insert at beginning: ");
                scanf("%d", &value);
                insertAtBeginning(value);
                break;
            case 3:
                printf("Enter value to insert at end: ");
                scanf("%d", &value);
                insertAtEnd(value);
                break;
            case 4:
                printf("Insert after which value?:  ");
                scanf("%d", &afterValue);
                printf("Enter Value to insert: ");
                scanf("%d", &value);
                insertAfter(afterValue, value);
                break;
            case 5:
                deleteFromBeginning();
                break;
            case 6:
                deleteFromEnd();
                break;
            case 7:
                printf("Enter value to delete: ");
                scanf("%d", &value);
                deleteNodeByValue(value);
                break;
            case 0:
                printf("Exiting the program...\n");
                exit(0);
            default:
                printf("Please choose a valid option (0-7)\n");
        }
    }

    return 0;
}
