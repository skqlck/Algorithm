import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class B18500 {

    static int R,C;
    static char[][] graph;
    static int[] dx = {-1,1,0,0};
    static int[] dy = {0,0,1,-1};

    public static void main(String[] args) throws Exception{
        System.setIn(new FileInputStream("B18500.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        graph = new char[R][C];
        for (int r = 0; r < R; r++) {
            String line = br.readLine();
            for (int c =0; c < C; c++) {
                graph[r][c] = line.charAt(c);
            }
        }

        int N = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            int row = Integer.parseInt(st.nextToken());
            shook(R-row, (i%2) == 0);
        }

        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                System.out.print(graph[i][j]);
            }
            System.out.print("\n");
        }
    }

    public static void shook(int height, boolean direction) {
        int targetY = -1;
        if (direction) {
            for (int c = 0; c < C; c++) {
                if (graph[height][c] == 'x') {
                    targetY = c;
                    break;
                }
            }
        }
        else {
            for (int c = C-1; c >= 0; c--) {
                if (graph[height][c] == 'x') {
                    targetY = c;
                    break;
                }
            }
        }

        if (targetY == -1) { // 미네랄 없음
            return;
        }

        graph[height][targetY] = '.';

        for (int i = 0; i < 4; i++) {
            int nx = height + dx[i];
            int ny = targetY + dy[i];
            if (0 > nx || R <= nx || 0 > ny || C <= ny) continue;
            if (graph[nx][ny] == 'x') {
                if (drop(nx,ny)) {
                    break;
                }
            }
        }
    }

    public static boolean drop(int x, int y){

        HashSet<Integer> cluster = new HashSet<>();
        cluster.add(encodeXY(x,y));
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{x,y});

        // 클러스터 구하기
        while (!queue.isEmpty()) {
            int[] xy = queue.poll();
            for (int i = 0; i < 4; i++) {
                int[] nxy = {xy[0]+dx[i], xy[1]+dy[i]};

                if (0 > nxy[0] || R <= nxy[0] || 0 > nxy[1] || C <= nxy[1]) continue;
                if (graph[nxy[0]][nxy[1]] == '.') continue;
                if (cluster.contains(encodeXY(nxy[0],nxy[1]))) continue;

                queue.add(nxy);
                cluster.add(encodeXY(nxy[0],nxy[1]));
            }
        }

        // 내려갈 칸 수 정하기
        int down = 0;
        boolean flag = false;
        while (true) {
            for (int exy : cluster) {
                int[] xy = decodeXY(exy);
                int nx = xy[0] + down + 1;
                int ny = xy[1];
                if (nx >= R){ //
                    flag = true;
                    break;
                }
                if (graph[nx][ny] == 'x' && !cluster.contains(encodeXY(nx,ny))) {
                    flag = true;
                    break;
                }
            }
            if (flag) break;
            down++;
        }

        if (down > 0) {
            for (int exy: cluster) {
                int[] xy = decodeXY(exy);
                graph[xy[0]][xy[1]] = '.';
            }
            for (int exy: cluster) {
                int[] xy = decodeXY(exy);
                graph[xy[0]+down][xy[1]] = 'x';
            }
            return true;
        }
        return false;
    }

    public static int encodeXY(int x, int y) {
        return (x + 1) * 1000 + y;
    }

    public static int[] decodeXY(int encodeValue) {
        int x = encodeValue / 1000 - 1;
        int y = encodeValue % 1000;
        return new int[]{x,y};
    }
}
