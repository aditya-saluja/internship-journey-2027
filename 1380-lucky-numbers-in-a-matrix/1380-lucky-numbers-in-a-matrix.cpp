
class Solution {
public:
    vector<int> luckyNumbers (vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();

        vector<int> ans;

        for (int i = 0; i < m; i++) {
            int mini = *min_element(matrix[i].begin(), matrix[i].end());

            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == mini) {
                    bool lucky = true;

                    for (int k = 0; k < m; k++) {
                        if (matrix[k][j] > mini) {
                            lucky = false;
                            break;
                        }
                    }

                    if (lucky)
                        ans.push_back(mini);
                }
            }
        }

        return ans;
    }
};
