#include <iostream>
#include<string>

using namespace std;

class Solution {
public:
	bool checkInclusion(string s1, string s2) {
		if (s1.size() > s2.size()) return false;
		int count1[26] = { 0 }, count2[26] = { 0 };
		for (char x : s1) {
			count1[x - 'a']++;
		}
		int left = 0;
		for (int right = 0; right < s2.size(); right++) {
			count2[s2[right] - 'a']++;
			if ((right - left + 1) == s1.size()) {
				bool exist = true;
				for (int i = 0; i < 26; i++) {
					if (count1[i] != count2[i]) {
						exist = false;
					}
				}
				if (exist) return true;
				count2[s2[left] - 'a']--;
				left++;
			}
		}
		return false;
	}
};
int main() {
	Solution sol1;
	cout << sol1.checkInclusion("abc", "lecabee");
	return 0;
}
