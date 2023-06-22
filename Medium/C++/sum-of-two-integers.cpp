
# include <iostream>
/*
int getSum(int a, int b){
	// std::cout << a << ' ' << b << std::endl;
	while (b){
		unsigned int carry = (a & b) << 1 ;
		a = a ^ b;
		b = carry;
	}
	return a;
}
*/

int getSum(int a, int b) {
    while (b){
        int carry = (a&b);
        a = a^b;
        b = (unsigned int)carry << 1;
    }
    return a;
}


int main(){
	std::cout << getSum(32, -17);
	return 0;
}