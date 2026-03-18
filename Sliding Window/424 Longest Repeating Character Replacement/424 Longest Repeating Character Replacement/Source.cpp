#include <iostream>
#include<unordered_map>

using namespace std;

class Solution {
public:
	int characterReplacement(string s, int k) {
		int left = 0, replace = 0, max_dup = 0, dup = 0;
		int max_count = 0;
		int counting[26] = { 0 };
		for (int right = 0; right < s.size(); right++) {
			counting[s[right] - 'A']++;
			if (counting[s[right] - 'A'] > max_count) {
				max_count = counting[s[right] - 'A'];
			}
			dup = right - left + 1;
			replace = dup - max_count;
			if (replace > k) {
				counting[s[left] - 'A']--;
				left++;
				dup--;
			}
			if (dup > max_dup) {
				max_dup = dup;
			}
		}
		return max_dup;
	}
};
int main() {
	Solution sol1;
	cout << (sol1.characterReplacement("AAABABB", 1));
	return 0;
}