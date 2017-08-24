import java.io.*;
import java.util.*;
import java.time.*;

public class DateTime1 {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int month = s.nextInt();
        int day = s.nextInt();
        int year = s.nextInt();
        s.close();
        LocalDate dt = LocalDate.of(year, month, day);
        System.out.println(dt.getDayOfWeek());
    }

}

