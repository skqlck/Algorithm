import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class B5073 {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        while (true) {
            st = new StringTokenizer(br.readLine());
            int[] edges = new int[3];
            edges[0] = Integer.parseInt(st.nextToken());
            edges[1] = Integer.parseInt(st.nextToken());
            edges[2] = Integer.parseInt(st.nextToken());

            if (edges[0] == 0 || edges[1] == 0 || edges[2] == 0) {
                return;
            }

            Arrays.sort(edges);

            if ( edges[0] + edges[1] <= edges[2]){
                System.out.println("Invalid");
            }
            else if ( edges[0] == edges[1] && edges[1] == edges[2]){
                System.out.println("Equilateral");
            }
            else if ( edges[0] == edges[1] || edges[1] == edges[2] ) {
                System.out.println("Isosceles");
            }
            else {
                System.out.println("Scalene");
            }
        }
    }
}
