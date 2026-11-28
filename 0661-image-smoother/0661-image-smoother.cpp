
class Solution {
public:
    vector<vector<int>> imageSmoother(vector<vector<int>>& img) {
        int m = img.size();
        int n = img[0].size();

        vector<vector<int>> ans(m, vector<int>(n, 0));

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int sum = 0, count = 0;

                for (int x = -1; x <= 1; x++) {
                    for (int y = -1; y <= 1; y++) {
                        int nr = i + x;
                        int nc = j + y;

                        if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                            sum += img[nr][nc];
                            count++;
                        }
                    }
                }

                ans[i][j] = sum / count;
            }
        }

        return ans;
    }
};
