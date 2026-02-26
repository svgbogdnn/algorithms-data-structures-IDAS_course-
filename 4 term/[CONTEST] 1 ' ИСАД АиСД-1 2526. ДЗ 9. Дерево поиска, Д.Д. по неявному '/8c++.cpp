#include <bits/stdc++.h>
using namespace std;

struct Node {
    int key;
    int left;
    int right;
    unsigned prio;
};

vector<Node> nodes;

int new_node(int value, unsigned prio) {
    nodes.push_back(Node{value, 0, 0, prio});
    return static_cast<int>(nodes.size()) - 1;
}

pair<int, int> split(int node, int value) {
    if (node == 0) {
        return {0, 0};
    }
    if (nodes[node].key < value) {
        auto [l, r] = split(nodes[node].right, value);
        nodes[node].right = l;
        return {node, r};
    }
    auto [l, r] = split(nodes[node].left, value);
    nodes[node].left = r;
    return {l, node};
}

int merge(int left, int right) {
    if (left == 0) {
        return right;
    }
    if (right == 0) {
        return left;
    }
    if (nodes[left].prio < nodes[right].prio) {
        nodes[left].right = merge(nodes[left].right, right);
        return left;
    }
    nodes[right].left = merge(left, nodes[right].left);
    return right;
}

int get_next_value(int root, int value) {
    int node = root;
    int ans = -1;
    while (node != 0) {
        if (nodes[node].key >= value) {
            ans = nodes[node].key;
            node = nodes[node].left;
        } else {
            node = nodes[node].right;
        }
    }
    return ans;
}

unsigned next_rand(unsigned seed) {
    return (seed * 1103515245u + 12345u) & 0x7fffffffu;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) {
        return 0;
    }

    nodes.reserve(n * 2 + 5);
    nodes.push_back(Node{0, 0, 0, 0});

    int root = 0;
    bool last_was_query = false;
    int last = 0;
    unsigned seed = 123456789u;
    vector<string> output;
    output.reserve(n / 2 + 5);

    for (int i = 0; i < n; ++i) {
        char op;
        int x;
        cin >> op >> x;

        if (op == '+') {
            if (last_was_query) {
                x = static_cast<int>((static_cast<long long>(x) + last) % 1000000000);
            }
            seed = next_rand(seed);
            auto [left_subtree, mid] = split(root, x);
            auto [mid_node, right_subtree] = split(mid, x + 1);
            if (mid_node == 0) {
                mid_node = new_node(x, seed);
            }
            root = merge(merge(left_subtree, mid_node), right_subtree);
            last_was_query = false;
        } else {
            int ans = get_next_value(root, x);
            if (ans == -1) {
                output.emplace_back("-1");
                last = -1;
            } else {
                output.emplace_back(to_string(ans));
                last = ans;
            }
            last_was_query = true;
        }
    }

    for (const string& line : output) {
        cout << line << '\n';
    }

    return 0;
}
