
# include <iostream>
# include <vector>

using std::cout;
using std::vector; 

vector<int> mergeSort(vector<int> array){
	if(array.size() < 2) 
		return array;

	int mid = array.size() / 2;

	auto sub1 = mergeSort(vector<int> (array.begin(), array.begin()+mid));
	auto sub2 = mergeSort(vector<int> (array.begin()+mid, array.end()));

	vector<int> merged;
	merged.reserve(sub1.size() + sub2.size());

	auto it1 = sub1.begin();
	auto it2 = sub2.begin();

	while (it1 != sub1.end() && it2 != sub2.end()){
		if(*it1 < *it2){
			merged.push_back(*it1);
			++it1;
		} else{
			merged.push_back(*it2);
			++it2;
		}
	}

	merged.insert(merged.end(), it1, sub1.end());
	merged.insert(merged.end(), it2, sub2.end());
	
	return merged;
}





int main()
{
	vector<int> array1{4, 2, 8, 3, 6, 9, 1, 7};
	vector<int> array2{9, 8, 7, 6, 5, 4, 3, 2, 1, 0};

	cout << "sorted(array1) -> {" ;
	for(int i:mergeSort(array1)) cout << ' ' << i ;
	cout << " }\nsorted(array2) -> {";
	for(int i:mergeSort(array2)) cout << ' ' << i;
	cout << " }";

	return 0;
}

