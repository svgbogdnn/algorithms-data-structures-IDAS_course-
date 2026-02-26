#include <algorithm>
#include <cstdint>
#include <iostream>
#include <utility>
#include <vector>

struct Node {
    long long key;
    int prio;
    Node* left;
    Node* right;
    long long sum;

    Node(long long k, int p)
        : key(k), prio(p), left(nullptr), right(nullptr), sum(k) {}
};

inline long long subtree_sum(const Node* node) {
    return node ? node->sum : 0LL;
}

inline void update(Node* node) {
    if (!node) {
        return;
    }
    node->sum = node->key + subtree_sum(node->left) + subtree_sum(node->right);
}

std::pair<Node*, Node*> split(Node* root, long long key) {
    if (!root) {
        return {nullptr, nullptr};
    }

    if (root->key < key) {
        std::pair<Node*, Node*> splitted = split(root->right, key);
        root->right = splitted.first;
        update(root);
        return {root, splitted.second};
    }

    std::pair<Node*, Node*> splitted = split(root->left, key);
    root->left = splitted.second;
    update(root);
    return {splitted.first, root};
}

Node* merge(Node* left, Node* right) {
    if (!left) {
        return right;
    }
    if (!right) {
        return left;
    }

    if (left->prio < right->prio) {
        left->right = merge(left->right, right);
        update(left);
        return left;
    }

    right->left = merge(left, right->left);
    update(right);
    return right;
}

Node* insert_node(Node* root, long long key, int prio) {
    std::pair<Node*, Node*> split_left = split(root, key);
    std::pair<Node*, Node*> split_mid = split(split_left.second, key + 1);
    Node* left = split_left.first;
    Node* middle = split_mid.first;
    Node* right = split_mid.second;

    if (!middle) {
        middle = new Node(key, prio);
    }

    Node* merged = merge(left, middle);
    return merge(merged, right);
}

long long range_sum(Node*& root, long long left_key, long long right_key) {
    std::pair<Node*, Node*> split_left = split(root, left_key);
    std::pair<Node*, Node*> split_mid = split(split_left.second, right_key + 1);
    Node* left = split_left.first;
    Node* middle = split_mid.first;
    Node* right = split_mid.second;

    long long result = subtree_sum(middle);

    Node* merged_mid = merge(middle, right);
    root = merge(left, merged_mid);
    return result;
}

int next_seed(int seed) {
    const long long multiplier = 1103515245LL;
    return static_cast<int>((static_cast<long long>(seed) * multiplier + 12345) & 0x7fffffff);
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n;
    if (!(std::cin >> n)) {
        return 0;
    }

    Node* root = nullptr;
    std::vector<long long> answers;
    long long last = 0;
    bool after_query = false;
    int seed = 123456789;
    constexpr int MOD = 1000000000;

    for (int i = 0; i < n; ++i) {
        char op;
        std::cin >> op;

        if (op == '+') {
            long long x;
            std::cin >> x;
            if (after_query) {
                x = (x + last) % MOD;
            }
            seed = next_seed(seed);
            root = insert_node(root, x, seed);
            after_query = false;
        } else {
            long long l;
            long long r;
            std::cin >> l >> r;
            if (l > r) {
                std::swap(l, r);
            }
            long long ans = range_sum(root, l, r);
            answers.push_back(ans);
            last = ans;
            after_query = true;
        }
    }

    for (long long value : answers) {
        std::cout << value << '\n';
    }

    return 0;
}
