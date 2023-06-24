# include <stdio.h>

int getSum(int a, int b){
	while (b){
		int carry = (a&b);
		a = a^b;
		b = (unsigned int)carry << 1;
	}
	return a;
}


int main(){
	int a = 5, b = -8;
	printf("(%d) + (%d) = %d\n", a, b, getSum(a, b));
	return 0;
}