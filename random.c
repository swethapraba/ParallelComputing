/*char key[30]; /*Array for the "tree" of values*/
	/*int k = 1; /*first index we care about for the array-tree*/
	/*int numEnterArray = 0;
		while(numEnterArray < n)
	{
		/*while the number of items actually put in the array are less than the number of values that should be leaves- n**/
	/*	fread(&ch , sizeof(char), 1 , fin);

	}*/	

	/* rosettacode*/
	//****//
	void decode(const char *s, node t)
	{
		node n = t;
		while (*s) {
		if (*s++ == '0') n = n->left;
		else n = n->right;
 
		if (n->c) putchar(n->c), n = t;
	}
 
	putchar('\n');
	if (t != n) printf("garbage input\n");
	}
 
	int main(void)
	{
	int i;
	const char *str = "this is an example for huffman encoding";
        char buf[1024];
 
	init(str);
	for (i = 0; i < 128; i++)
		if (code[i]) printf("'%c': %s\n", i, code[i]);
 
	encode(str, buf);
	printf("encoded: %s\n", buf);
 
	printf("decoded: ");
	decode(buf, q[1]);
 
	return 0;
	}
//****//