#include <iostream>
#include<unordered_map>

using namespace std; 

class Solution {
public:
	string minWindow(string s, string t) {
		unordered_map<char, int> count_s, count_t;
		for (char x : t) {
			count_t[x]++;
		}
		string ans = "", tem_ans = "";
		int left = 0;
		for (int right = 0; right < s.size(); right++) {
			count_s[s[right]]++;
			bool contain = true;
			for (const auto& [key, val] : count_t) {
				if (count_s[key] < count_t[key]) {
					contain = false;
				}
			}
			while (count_s[s[left]] > count_t[s[left]]) {
				count_s[s[left]]--;
				left++;
			}
			if (contain) {
				tem_ans = s.substr(left, right - left + 1);
				if (tem_ans.size() < ans.size() || ans == "") {
					ans = tem_ans;
				}
			}
		}
		return ans;
	}
};

int main() {
	Solution sol1;
	cout << sol1.minWindow("OUZODYXAZV", "XYZ");
	return 0;
}