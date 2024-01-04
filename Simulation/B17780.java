package Simulation;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class B17780 {

    static int[] dx = {0,0,-1,1};
    static int[] dy = {1,-1,0,0};
    static Block[][] graph;
    static Node[] nodes;
    static int N;
    static int K;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        graph = new Block[N][N];
        nodes = new Node[K];

        for (int x = 0; x < N; x++){
            st = new StringTokenizer(br.readLine());
            for (int y = 0; y < N; y++) {
                graph[x][y] = new Block(x, y, Integer.parseInt(st.nextToken()));
            }
        }

        for (int i = 0; i < K; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken()) - 1;
            int y = Integer.parseInt(st.nextToken()) - 1;
            int direction = Integer.parseInt(st.nextToken()) - 1;
            nodes[i] = new Node(x, y, direction);
            graph[x][y].bottom = graph[x][y].top = nodes[i];
            graph[x][y].size++;
        }

        int answer = 0;
        while (answer <= 1000) {
            answer += 1;
            if (move()) {
                break;
            }
        }
        System.out.println(answer > 1000 ? -1 : answer);
    }

    public static boolean move() {
        for (int i = 0; i < K; i++) {
            Node node = nodes[i];
            if (graph[node.x][node.y].bottom != node) {
                continue;
            }
            int x = node.x;
            int y = node.y;
            int nx = x + dx[node.direction];
            int ny = y + dy[node.direction];

            // 범위 밖이거나 이동할 칸이 파란색
            if (nx < 0 || ny < 0 || nx >= N || ny >= N || graph[nx][ny].color == 2) {
                node.direction = node.direction >= 2 ? (node.direction + 1) % 2 + 2 : (node.direction + 1) % 2;
                nx = x + dx[node.direction];
                ny = y + dy[node.direction];
                // 또 파랑색이면 (범위 밖으로 나갈 순 없음) 그냥 정지
                // 이미 방향은 바꿨기 때문에 아무것도 하지 않음
                if (nx < 0 || ny < 0 || nx >= N || ny >= N || graph[nx][ny].color == 2) continue;

                if (graph[nx][ny].color == 0) { // 하얀 블럭이면
                    graph[nx][ny].store(graph[x][y]);
                }
                else if (graph[nx][ny].color == 1) { // 빨간 블럭이면
                    graph[nx][ny].reverseStore(graph[x][y]);
                }
            }
            // 이동할 칸이 하얀색
            else if (graph[nx][ny].color == 0) {
                graph[nx][ny].store(graph[x][y]);
            }
            // 이동할 칸이 빨간색
            else if (graph[nx][ny].color == 1) {
                graph[nx][ny].reverseStore(graph[x][y]);
            }

            if (graph[nx][ny].size >= 4) {
                return true;
            }
        }
        return false;
    }

}

class Block {
    int x;
    int y;
    int color;
    Node bottom;
    Node top;
    int size;

    public Block(int x, int y, int color) {
        this.x = x;
        this.y = y;
        this.color = color;
        this.size = 0;
    }

    public void clear() {
        this.bottom = null;
        this.top = null;
        this.size = 0;
    }

    public void store(Block block) {
        if (this.bottom == null) {
            this.bottom = block.bottom;
            this.bottom.x = this.x;
            this.bottom.y = this.y;
        }
        this.top = block.top;
        this.size += block.size;
        block.clear();
    }

    public void reverseStore(Block block) {
        if (this.bottom == null) {
            this.bottom = block.top;
            this.bottom.x = this.x;
            this.bottom.y = this.y;
        }
        this.top = block.bottom;
        this.size += block.size;
        block.clear();
    }
}

class Node {
    int x;
    int y;
    int direction;

    public Node(int x, int y, int direction) {
        this.x = x;
        this.y = y;
        this.direction = direction;
    }
}
