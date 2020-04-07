package inSearchOfAnEasyProblem;
import java.io.*;

public class InSearchOfAnEasyProblem1030A {

    public static void main(String[] args) throws IOException
    {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(rd.readLine());
        String[] line = rd.readLine().split(" ");
        boolean flag = true;
        for(int i = 0; i < n; i++)
        {
            if(line[i] == "1")
            {
                flag = false;
            } 
        }
        if(flag)
        {
            System.out.println("EASY");
        }
        else
        {
            System.out.println("HARD");
        }
    }
}