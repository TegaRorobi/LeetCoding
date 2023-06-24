
#include <iostream>
#include <vector>

using std::cout;
using std::min;
using std::max;
using std::vector;

int maxArea(vector<int> heights){
	int l=0, r=heights.size()-1;
	int maxArea = 0;

	while (l < r){
		int area = (r-l) * min(heights[r], heights[l]);
		maxArea = max(maxArea, area);

		if (heights[l] < heights[r]) 
			++l;
		else 
			--r;
	}

	return maxArea;
}


int main(){
	cout << maxArea(vector<int>{1, 8, 6, 2, 5, 4, 8, 3, 7});
	return 0;
}