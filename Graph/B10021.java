package Graph;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class Main {
    private static int N, C;
    private static int[] X, Y, PARENT;

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        X = new int[N];
        Y = new int[N];
        PARENT = new int[N];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            X[i] = Integer.parseInt(st.nextToken());
            Y[i] = Integer.parseInt(st.nextToken());
            PARENT[i] = i;
        }

        PriorityQueue<Edge> edges = new PriorityQueue<>((o1, o2) -> o1.weight - o2.weight);
        for (int i = 0; i < N-1; i++) {
            for (int j = i+1; j < N; j++) {
                int distance = (X[i] - X[j]) * (X[i] - X[j]) + (Y[i] - Y[j]) * (Y[i] - Y[j]);

                if (distance < C) continue;

                edges.add(new Edge(i,j,distance));
            }
        }

        int cnt = 0;
        int answer = 0;

        while (!edges.isEmpty() && cnt < N-1) {
            Edge edge = edges.poll();

            if (find(edge.u) == find(edge.v)) continue;

            cnt++;
            answer += edge.weight;
            union(edge.u, edge.v);
        }

        if (cnt != N-1) {
            System.out.println(-1);
            return;
        }
        System.out.println(answer);
    }

    private static int find(int x) {
        while (PARENT[x] != x) {
            x = PARENT[x];
        }
        return x;
    }

    private static void union(int x, int y) {
        PARENT[y] = find(x);
    }
}

class Edge {
    int u;
    int v;
    int weight;

    public Edge(int u, int v, int weight) {
        this.u = u;
        this.v = v;
        this.weight = weight;
    }
}
