class Solution {
    public boolean isPalindrome(int x) {
        String num = Integer.toString(x);
        int i = 0, j = num.length() - 1;
        while(i <= j){
            if(num.charAt(i) == num.charAt(j)){ //check the digits from left to right and from right to left
                i++;
                j--;
            }
            else
                return false;
        }
        return true;
    }
}
