/* Two strings,  and , are called anagrams if they contain all the same 
 * characters in the same frequencies. For example, the anagrams of CAT 
 * are CAT, ACT, TAC, TCA, ATC, and CTA.
 *
 * Complete the function in the editor. If  and  are case-insensitive 
 * anagrams, print "Anagrams"; otherwise, print "Not Anagrams" instead
 *
 * Input Format
 *
 * The first line contains a string denoting . 
 * The second line contains a string denoting .
 *
 * Constraints
 *
 * Strings  and  consist of English alphabetic characters.
 * The comparison should NOT be case sensitive.
 *
 * Output Format
 *
 * Print "Anagrams" if  and  are case-insensitive anagrams of each other; 
 * otherwise, print "Not Anagrams" instead.

    Sample Input 0

    anagram
    margana

    Sample Output 0

    Anagrams

*/

import java.io.*;
import java.util.*;

public class Anagram1 {

    static boolean isAnagram(String a, String b) {
        if (a.length() != b.length()) {
            return false;
        }
        else {
            String[] a2 = a.toLowerCase().split("");
            String[] b2 = b.toLowerCase().split("");
            Arrays.sort(a2); 
            Arrays.sort(b2);
            return Arrays.equals(a2, b2);
        }
    }

    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        String b = scan.next();
        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
    }

}
