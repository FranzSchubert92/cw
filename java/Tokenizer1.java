/*
 * Given a string, , matching the regular expression [A-Za-z !,?._'@]+, split 
 * the string into tokens. We define a token to be one or more consecutive 
 * English alphabetic letters. Then, print the number of tokens, followed by 
 * each token on a new line.
 *
 * Note: You may find the String.split method helpful in completing this challenge.
 *
 * INPUT: a single string s
 *
 * CONSTRAINTS
 *   1 <= s.length() <= 40,000
 *   s is composed of any of the following: 
 *     English letters, blank spaces, exclamation points,
 *     commas, question marks, periods, underscores, apostrophes, 
 *     and at-symbols.
 *
 *  OUTPUT FORMAT
 *
 *  On the first line, print an integer, , denoting the number of tokens in 
 *  string  (they do not need to be unique). Next, print each of the  tokens 
 *  on a new line in the same order as they appear in input string .
 *
 *  SAMPLE INPUT
 *
 *  He is a very very good boy, isn't he?
 *  
 *  SAMPLE OUTPUT
 *
 *  10
 *  He
 *  is
 *  a
 *  very
 *  very
 *  good
 *  boy
 *  isn
 *  t
 *  he
 *
 */

import java.io.*;
import java.util.*;

public class Tokenizer1 {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();
        if ( s != null && !s.trim().isEmpty() && !(s.length()==0) && !(s.length() >= 400000) ) {
            String[] chars = {};
            chars = s.trim().split("([ .'?,!@\\_])+");
            System.out.println(chars.length);
            for(String c : chars) {
                System.out.println(c);
            }
        }
        else {
            System.out.println("0");
        }
        scan.close();
    }
}

