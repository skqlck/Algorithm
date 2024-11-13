package BFS;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.*;

public class B14466 {
    static int N,K,R;
    static boolean[][][][] isRoad;
    static boolean[][] visited;
    static boolean[][] isCow;
    static int[] dx = {-1,1,0,0};
    static int[] dy = {0,0,1,-1};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());       K = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());

        isRoad = new boolean[N+1][N+1][N+1][N+1];
        visited = new boolean[N+1][N+1];
        isCow = new boolean[N+1][N+1];

        for (int i = 0; i < R; i++) {
            st = new StringTokenizer(br.readLine());
            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());
            isRoad[x1][y1][x2][y2] = true;
            isRoad[x2][y2][x1][y1] = true;
        }

        for (int i = 0; i < K; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            isCow[x][y] = true;
        }

        ArrayList<Integer> cowPerGroup = new ArrayList<>();
        for (int x = 1; x < N+1; x++) {
            for (int y = 1; y < N+1; y++) {
                if (!visited[x][y]) {
                    int cnt = bfs(x,y);
                    if (cnt > 0) {
                        cowPerGroup.add(cnt);
                    }
                }
            }
        }

        int answer = 0;
        for (int i = 0; i < cowPerGroup.size()-1; i++) {
            for (int j = i+1; j < cowPerGroup.size(); j++) {
                answer += cowPerGroup.get(i) * cowPerGroup.get(j);
            }
        }
        System.out.println(answer);
    }

    static int bfs(int x, int y) {
        visited[x][y] = true;
        int cnt = 0;

        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{x,y});
        while (!queue.isEmpty()) {
            int[] xy = queue.remove();

            if (isCow[xy[0]][xy[1]]) cnt++;

            for (int i = 0; i < 4; i++) {
                int nx = xy[0] + dx[i];
                int ny = xy[1] + dy[i];

                if (1 > nx || 1 > ny || nx > N || ny > N || visited[nx][ny]) continue;

                if (isRoad[xy[0]][xy[1]][nx][ny]) continue;

                visited[nx][ny] = true;
                queue.add(new int[]{nx,ny});
            }
        }
        return cnt;
    }
}
