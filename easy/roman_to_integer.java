class Solution {
    public int romanToInt(String s) {
        int number = 0, sum = 0;
        s = s.replace("IV", "IIII");
        s = s.replace("IX", "VIIII");
        s = s.replace("XL", "XXXX");
        s = s.replace("XC", "LXXXX");
        s = s.replace("CD", "CCCC");
        s = s.replace("CM", "DCCCC");
        for(int i = s.length() - 1; i >= 0; i--){
            switch(s.charAt(i)){
                case 'I': 
                    number = 1; 
                    break;
                case 'V': 
                    number = 5;
                    break;
                case 'X': 
                    number = 10; 
                    break;
                case 'L': 
                    number = 50; 
                    break;
                case 'C': 
                    number = 100; 
                    break;
                case 'D': 
                    number = 500;
                    break;
                case 'M': 
                    number = 1000;
                    break;
            }
            sum += number;
        }
        return sum;
    }
}