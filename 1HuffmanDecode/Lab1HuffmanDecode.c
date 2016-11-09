//* Swetha Prabakaran , 9/11/2016*/
#include <stdio.h>
#include <string.h>
#include <strings.h>
#include <math.h>
//
int main()
{
	FILE* fin = fopen( "decodeME.txt" , "r" ) ;
	char ch ;
	int n = 0 ; /*number of characters in the file; counter*/
	int numbytes;

	//tree
	char tree[100000];

	//readfilebyline
	char* line = NULL;
    size_t len = 0;
    ssize_t read;

    //building the tree
    int numLines;
    int linesRead = 0;
    int numPlaced = 0;
    int pathlength = 0;
    char holdChar;
    int k;
    char temp;

    //decoding our message
    char currentChar;
    int messlength = 0;
    char hold;

    //shannon stuff
    int frequency[256];
    int totalChars = 1;
    int temporary;
	//fill array with empty values
	for(int j = 0; j < 100000; j++)
	{
		tree[j] = '\0';
	}
	//numbytes = fread( &ch , sizeof(char) , 1 , fin ) ; 
	/*reads __ items of data,each __ bytes long,from the stream pointed to by stream,obtaining them from the location given by ptr*/
	///*do these commented lines serve a purpose?*/
	//if( numbytes == 0 ) break ;
	//n++ ;
	//printf( "%c" , ch )	
    while ((read = getline(&line, &len, fin)) != EOF) 
    {
        //printf("Retrieved line of length %zu :\n", read-1);
        printf("%s", line);
        if(linesRead == 0) //set the number of chars to go into the tree
        {
        	//combine into one string
        	//char string[] = line;
        	//parse it into integer
        	int thing = atoi(line);
        	//set numLines to be that integer
        	numLines = thing;
        	linesRead++;
        }
        else if(linesRead < numLines+1) //so read the 28 lines but compensate for the line with tree length
        {

    		pathlength = strlen(line); //set a variable to the line length 
        	holdChar = line[0]; //parse the first character into a holding cell;
			k = 1; //start looking at cell 1 in the tree
			for(int i = 1; i < pathlength; i++) //make the path in the tree with the rest of the variables
			{
				temp = line[i]; //set the holding character for the next pathway
				//printf("%c\n", temp);
        		if(temp == '1')
        		{
					//if next char is a 0 -> 2k, if next char is a 1 -> 2k+1
        			k = (2*k) + 1;
        		}
        		else if(temp == '0')
        		{
					k = 2*k;
        		}
			}
			tree[k] = holdChar; //once the end is reached, put this value (e.g. A) in that array cell
			printf("Final K: %d\n", k);
			k = 1;
			linesRead++;
			numPlaced++; //how many chars have been put in;
   		} 
   		else if (linesRead >= numLines+1)//yay time to decode stuff, we've made the tree
   		{
   			messlength = strlen(line);
   			for(int x = 0; x < messlength; x++)
   			{
   				currentChar = line[x];
   				if(currentChar == '0')
   				{
   					hold = tree[k];
   					//printf("Extra: %c ", hold);
   					if(hold == '\0')
                    {
                    	k = 2*k;
                    }
                    else
                    {
                       printf("%c", hold);
                       totalChars++;
                       //figureout ascii for that specific hold letter
                       temporary = (int) hold;
                       //increment that cell of the frequency array
                       frequency[temporary]++;
                       k = 1;
                       x = x-1;
                    }
   				}
   				else if(currentChar == '1')
   				{
   					hold = tree[k];
                    //printf("Boo: %c ", hold);
                    if(hold == '\0')
                    {
                        k = (2*k) + 1;
                    }
                    else
                    {
                    	printf("%c", hold);
                    	totalChars++;
                    	temporary = (int) hold;
                        frequency[temporary]++;
                    	k = 1;
                    	x = x-1;
                    }
   				}
   			}	
   		}  
    }

	//
	fclose( fin ) ; /*close file*/
	printf( "\n" ) ;
	//printf( "%d\n" , n ) ;
	printf("Number of lines: %d\n", numLines); //numLines check
	printf("Number of chars in tree: %d\n", numPlaced);
	printf("Number of lines read total: %d\n" , linesRead);

	
	//Shannon Stuff
	float shannonBits = 0.0;//2511.726; //ish
	float bits = 0.0;
	float holder = 0.0;
	float tempo = 0.0;
	for(int j = 0; j < 256; j++)
	{
		if(frequency[j] > 0)
		{
			//figure out the number of bits
			holder = frequency[j]/(float)totalChars;
			//printf("holder: %f\n", holder);
			tempo = -log2f(holder);
			//printf("tempo: %f\n", tempo);
			bits = tempo * frequency[j];
			//printf("bits: %f\n", bits);
			shannonBits+= bits;
		}
	}
	//minimum number of bits = SUM(frequency * -log2(probability))
	printf("Shannon min number of bits: %f\n", shannonBits);
	//Huffman Stuff
	printf("Total Chars: %d\n", totalChars);
	int asciiBits = totalChars * 8;//616*8;
	printf("ASCII bits: %d\n", asciiBits);
	//How close was Huffman to shannon?
	float compressionOne = asciiBits - shannonBits;
	float compressionTwo = compressionOne/asciiBits;
	printf("Compression Ratio: %f\n", compressionTwo);
	return 0 ;
}