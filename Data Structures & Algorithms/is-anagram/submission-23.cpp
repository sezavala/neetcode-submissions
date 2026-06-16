class Solution {
public:
    bool isAnagram(string s, string t) {
        vector<int> res(26);
        
        for (char ch : s) {
            res[(int)ch - (int)'a'] += 1;
        }

        for (char ch: t) {
            res[(int)ch - (int)'a'] -= 1;
        }

        for (int num : res) {
            if (num != 0) {
                return false;
            }
        }
        return true;
    }
};
