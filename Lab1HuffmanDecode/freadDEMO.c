//* Swetha Prabakaran , 9/11/2016*/
#include <stdio.h>
#include <string.h>
#include <strings.h>
//
int main()
{
	FILE* fin = fopen( "decodeME.txt" , "r" ) ;
	char ch ;
	int n = 0 ; /*number of characters in the file; counter*/
	int numbytes;
	
	//for creating the tree
	int numKey = 28, j;
	char tree[10000];
	int countInitSpace = 0;
	char holdChar;
	int k = 1; // k starts at 1
	int initComplete = 0;
	int numPlaced = 0;

	//for decoding the message:
	char current;
	char message[] = "Message is ";
	char temp;
	int yKeyLength = 7;
	int yCharCount = 0;
	int isY = 0;
	
	//fill array with empty values
	for(j = 0; j < 10000; j++)
	{
		tree[j] = '\0';
	}
	//
	while( 1 )
	{
		numbytes = fread( &ch , sizeof(char) , 1 , fin ) ; 
		/*reads __ items of data,each __ bytes long,from the stream pointed to by stream,obtaining them from the location given by ptr*/
		///*do these commented lines serve a purpose?*/
		if( numbytes == 0 ) break ;
		n++ ;
		printf( "%c" , ch ) ;
		//
		
		//building the tree
		if(numPlaced < 28) //read code line by line and keep track of number of lines read
		{
			//first char read is the 2, second char is the 8
			if(ch == 'Y')
			{
				//currently I can't figure out how to stop at the end of the line for Y and not bleed into the message
				//while building the tree for this last variable
				//temporary hardcode in to get it to stop
				tree[68] = 'Y';
				numPlaced++;
				isY = 1;
				k = 1;
			}
			if(ch != '2' && ch !='8' && ch != '1' && ch != '0') //if we have a character that needs to be put in the tree
			{
				if(initComplete == 5) //if we have already finished the space char//boolean ish
				{
					tree[k] = holdChar; ////once the end is reached, put this value (e.g. A) in that array cell
					k = 1; //reset tree index
					numPlaced++; //increment the count of chars put in
				}
				holdChar = ch; //set the new holding character for the next tree construction
				//go back to the top and repeate the loop
			}
			else if (ch == '1')
			{
				//if next char is a 0 -> 2k, if next char is a 1 -> 2k+1
				k = (2*k) + 1;
			}
			else if(ch == '0')
			{
				k = 2*k;
			}
			if(ch != '2' && ch !='8')
			{
				initComplete = 5; //temp boolean setup
			}
		}
		//decoding the message
		if(numPlaced == 28 || numPlaced < 28)
		{
			///temp hard code to skip the chars for Y's key:
			if(isY == 1 && yCharCount < yKeyLength)
			{
				yCharCount++;
			}
			else if(isY == 1 && yCharCount >= yKeyLength)
			{
				current = ch;// whatever we have to decode rn
				if(current == '0')
				{
					temp = tree[k];
					if(temp == '\0')
					{
						k = 2 * k;
					}
					else
					{
						strcat(message,temp);//just print out the message text don't bother with concatenation
					}
				}
				else if (current == '1')
				{	
					temp = tree[k];
					if(temp == '\0')
					{
						k = (2 * k) + 1;
					}
					else
					{
						strcat(message,temp);//just print out the message text don't bother with concatenation
					}
				}
			}
		}
	}

	//
	fclose( fin ) ; /*close file*/
	printf( "\n" ) ;
	printf( "%d\n" , n ) ;
	//
	printf("%s\n" , message);
	return 0 ;
}
//
// end of file
//