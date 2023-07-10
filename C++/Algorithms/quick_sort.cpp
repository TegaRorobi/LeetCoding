# include <iostream>
# include <vector>

using std::vector;
using std::cout;
using std::endl;


// recursive implementation
vector<int> quickSort (vector<int> array) {
	// base case
	if (array.size() < 2) return array; 

	int pivot = *(array.end()-1);
	vector<int>::iterator j = array.begin() -1, i = array.begin();
	while (i != array.end()) {
		if (*i <= pivot){
			++j;
			int temp = *j;
			*j = *i;
			*i = temp;
		}
		++i;
	}

	int pivot_index = j-array.begin();

	vector<int> res;
	for (int n: quickSort(vector<int>(array.begin(), array.begin()+pivot_index))) res.push_back(n);
	res.push_back(pivot);
	for (int n: quickSort(vector<int>(array.begin()+pivot_index+1, array.end()))) res.push_back(n);

	return res;
}


// iterative implementation
vector<int> quickSort_iterative(vector<int> array) {
	vector<int>res;
	vector<vector<int>> stack{array};

	while (!stack.empty()) {
		vector<int>vec = stack.back();
		stack.pop_back();

		if (vec.size() < 2){ 
			if (!vec.empty())
				res.push_back(vec.front());
			continue;
		}

		int pivot = vec.back();
		auto i = vec.begin();
		auto j = i - 1;

		while (i != vec.end()) {
			if (*i <= pivot){
				++j;
				int tmp = *j;
				*j = *i;
				*i = tmp;
			}
			++i;
		}


		stack.push_back(vector<int>(j+1, vec.end()));
		stack.push_back(vector<int>{pivot});
		stack.push_back(vector<int>(vec.begin(), j));
	}
	return res;
}


int main() {
	vector<int> arr = {20, 7, 4, 19, 12, 17, 13, 6, 8, 11};
	auto res = quickSort_iterative(arr);
	cout << "{";
	for (int n:arr) cout << n << ' ';
	cout << "} =>> {";
	for (int n:res) cout << n << ' ';
	cout << '}';

	return 0;
}