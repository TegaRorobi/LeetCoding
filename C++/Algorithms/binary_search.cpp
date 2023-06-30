#include <iostream> 
#include <vector>

using std::cout; 
using std::vector;

int search (vector<int> array, int target) {
	int l = 0, r = array.size()-1;

	while (l <= r) {

		int mid = (l+r) / 2;
		if (target == array[mid])
			return mid;

		if (target > array[mid]) 
			l = mid + 1;
		else 
			r = mid - 1;
	}
	return -1;
}

int main() {
	vector<int> array {1, 2, 4, 6, 7, 9, 11, 13, 16, 20};
	cout << search(array, 7);
}
