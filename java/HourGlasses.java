/*
  You are given a  2D array. An hourglass in an array is a portion shaped like this:

    a b c
      d
    e f g
   
   For example, if we create an hourglass using the number 1 within an array 
   full of zeros, it may look like this:

       1 1 1 0 0 0
       0 1 0 0 0 0
       1 1 1 0 0 0
       0 0 0 0 0 0
       0 0 0 0 0 0
       0 0 0 0 0 0

   Actually, there are many hourglasses in the array above. The three leftmost
   hourglasses are the following:

       1 1 1     1 1 0     1 0 0
         1         0         0
       1 1 1     1 1 0     1 0 0

   The sum of an hourglass is the sum of all the numbers within it. The sum for 
   the hourglasses above are 7, 4, and 2, respectively.

   In this problem you have to print the largest sum among all the hourglasses in 
   the array.

   Input Format
   There will be exactly  lines, each containing  integers seperated by spaces. 
   Each integer will be between  and  inclusive.

   Output Format
   Print the answer to this problem on a single line.

   Sample Input
     1 1 1 0 0 0
     0 1 0 0 0 0
     1 1 1 0 0 0
     0 0 2 4 4 0
     0 0 0 2 0 0
     0 0 1 2 4 0

   Sample Output
     19
     
   Explanation: The hourglass which has the largest sum is:
     2 4 4
       2
     1 2 4

*/

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class HourGlasses {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int arr[][] = new int[6][6];
        for(int i=0; i < 6; i++){
            for(int j=0; j < 6; j++){
                arr[i][j] = in.nextInt();
            }
        }

        final int maxHourglass = -2_147_483_648; // can't initialize at 0 because of negative values

        for (int row = 0; row < 4; ++row) {
            for (int col = 0; col < 4; ++col) {
                int sum = 0;
                sum += arr[row][col] + arr[row][col+1] + arr[row][col+2]; 
                sum += arr[row+1][col+1];
                sum += arr[row+2][col] + arr[row+2][col+1] + arr[row+2][col+2];
                if (sum > maxHourglass) maxHourglass = sum;
            }
        }
        System.out.println(maxHourglass);
    }
}
