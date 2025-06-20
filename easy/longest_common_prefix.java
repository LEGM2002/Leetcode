import java.util.Arrays;

class Solution {
    public String longestCommonPrefix(String[] strs) {
        String ans = "";
        Arrays.sort(strs); //sort the array to check the first and the last string
        String first = strs[0];
        String last = strs[strs.length - 1];
        int minLength = Math.min(first.length(), last.length()); //take the length of the shortest string
        for(int i = 0; i < minLength; i++){
            if(first.charAt(i) == last.charAt(i))
                ans += first.charAt(i);
            else
                break; //we don't need to iterate more
        }
        return ans;
    }
}