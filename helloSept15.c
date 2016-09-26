#include <stdio.h>
#include <stdlib.h> //for malloc, own addition outside of Dr.T's notes

struct TreeNodes
{
	char symb;

	int freq;
};
//alternative way around the struct thing:
typedef struct Node
{
	char symbol;
	int frequency;

	struct Node left ; 
	struct Node right ; 
	/*
	TreeNode left; //this is doubly wrong
	TreeNode right; //1. typedef has not actually ocurred yet
	//gotta use the struct Node thing just here because typedef needs to happen; after that you're fine
	*/
} TreeNode; //ask about this line with the TreeNode at the end??

int main()
{
	//struct TreeNode a; /*equivalent of having to say "class TreeNode" everytime you used a TreeNode in Java. Very annoying. */
	TreeNode a ;
	struct Node g = a;
	//
	a.symbol = 'N' ;
	a.frequency = 777 ;
	//
	//
	TreeNode* ptr ;
	TreeNode* root ;
	//
	root = (TreeNode*)malloc(sizeof(TreeNode) ); //malloc is like saying new and would make the object, but no constructor being called
	//
	(*root).symbol = 'X';//root isn't a treenode, it's a pointer
	/*
	*root.symbol = 'X';
	By default, computer tries to do this: *(root.symbol) = 'X';
	to override this we need parentheses:
	(*root).symb = 'X'; // takes precedence over *;
	*/
	root - > frequency = 5; // this is legit it's not a joke; it's a kind of pointer. Root is pointer, frequency is the field of type you want
	//spaces and comments just make code a bit more legible, not needed to actually run C.
	root -> left = NULL;
	root -> right = NULL;
	//
	//
	printf("hi\n");
	//
	//
	//
	return 0;
}