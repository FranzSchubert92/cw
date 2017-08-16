import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.Scanner;

class RegularExpressions {

    static String ipv4octet = "(\\d{1,2}|(0|1)\\d{2}|2[0-4]\\d|25[0-5])";
    static String ipv4pattern = ipv4octet + "\\." + ipv4octet + "\\." + ipv4octet + "\\." + ipv4octet; 

    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        while(in.hasNext()){
            String IP = in.next();
            System.out.println(IP.matches(ipv4pattern));
        }

    }
}

