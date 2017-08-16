import java.io.*;
import java.util.*;

public class Reverse {
    public static String reverseString(String str) {
        if (str.length() <= 1) return str;
        String prev = reverseString(str.substring(0,str.length()-1));
        return str.substring(str.length()-1, 1) + prev;
    }
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        scan.close();
        String result = reverseString(a);
        System.out.println(result);
    }
}

