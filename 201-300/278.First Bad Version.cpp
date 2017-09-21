// Forward declaration of isBadVersion API.
bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int low = 1;
        int high = n;
        int ver = 0;
        while (low < high) {
            ver = low + (high - low) / 2;
            if (isBadVersion(ver)) {
                high = ver;
            } else {
                low = ver + 1;
            }
        }
        return low;
    }
};
//二分查找减小时间消耗