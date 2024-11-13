package Mathematics;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B23971 {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int H,W,N,M,X,Y;
        H = Integer.parseInt(st.nextToken());
        W = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        X = H % (N+1) == 0 ? H / (N+1) : H / (N+1) + 1;
        Y = W % (M+1) == 0 ? W / (M+1) : W / (M+1) + 1;
        System.out.println(X*Y);
        return;
    }
}
