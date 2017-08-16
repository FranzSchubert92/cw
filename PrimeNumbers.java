import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class PrimeNumbers {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        BigInteger n = in.nextBigInteger();
        in.close();
        System.out.println(n.isProbablePrime(8) ? "prime" : "not prime");
    }

}

/*
 * java.math.BigInteger.isProbablePrime(int certainty) returns true if this 
 * BigInteger is probably prime, false if it's definitely composite. If 
 * certainty is ≤ 0, true is returned.
 *
 * Declaration
 * Following is the declaration for java.math.BigInteger.isProbablePrime() method.
 *
 * public boolean isProbablePrime(int certainty)
 *
 * Parameters
 * certainty − a measure of the uncertainty that the caller is willing to 
 * tolerate: if the call returns true the probability that this BigInteger 
 * is prime exceeds (1 - 1/(2**certainty)). The execution time of this method 
 * is proportional to the value of this parameter.
 *
 * Return Value
 * This method returns true if this BigInteger is probably prime, false if it's definitely composite.
 */
