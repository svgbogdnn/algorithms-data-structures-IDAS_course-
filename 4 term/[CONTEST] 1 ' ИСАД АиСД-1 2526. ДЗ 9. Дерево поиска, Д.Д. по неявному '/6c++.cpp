#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

struct Node {
    long long key;
    Node* left;
    Node* right;
    int height;
    int size;

    explicit Node(long long value)
        : key(value), left(nullptr), right(nullptr), height(1), size(1) {}
};

inline int node_height(Node* node) {
    return node ? node->height : 0;
}

inline int node_size(Node* node) {
    return node ? node->size : 0;
}

inline void update(Node* node) {
    if (!node) {
        return;
    }
    node->height = 1 + std::max(node_height(node->left), node_height(node->right));
    node->size = 1 + node_size(node->left) + node_size(node->right);
}

inline int balance_factor(Node* node) {
    return node_height(node->right) - node_height(node->left);
}

Node* rotate_left(Node* x) {
    Node* y = x->right;
    Node* t2 = y->left;

    y->left = x;
    x->right = t2;

    update(x);
    update(y);

    return y;
}

Node* rotate_right(Node* y) {
    Node* x = y->left;
    Node* t2 = x->right;

    x->right = y;
    y->left = t2;

    update(y);
    update(x);

    return x;
}

Node* rebalance(Node* node) {
    if (!node) {
        return nullptr;
    }
    update(node);
    int bf = balance_factor(node);

    if (bf > 1) {
        if (balance_factor(node->right) < 0) {
            node->right = rotate_right(node->right);
        }
        return rotate_left(node);
    }

    if (bf < -1) {
        if (balance_factor(node->left) > 0) {
            node->left = rotate_left(node->left);
        }
        return rotate_right(node);
    }

    return node;
}

Node* insert_node(Node* node, long long key) {
    if (!node) {
        return new Node(key);
    }

    if (key < node->key) {
        node->left = insert_node(node->left, key);
    } else if (key > node->key) {
        node->right = insert_node(node->right, key);
    } else {
        return node;
    }

    return rebalance(node);
}

Node* get_min(Node* node) {
    while (node->left) {
        node = node->left;
    }
    return node;
}

Node* remove_min(Node* node) {
    if (!node->left) {
        return node->right;
    }
    node->left = remove_min(node->left);
    return rebalance(node);
}

Node* remove_node(Node* node, long long key) {
    if (!node) {
        return nullptr;
    }

    if (key < node->key) {
        node->left = remove_node(node->left, key);
        return rebalance(node);
    }

    if (key > node->key) {
        node->right = remove_node(node->right, key);
        return rebalance(node);
    }

    Node* left = node->left;
    Node* right = node->right;

    if (!right) {
        return left;
    }

    Node* min_node = get_min(right);
    min_node->right = remove_min(right);
    min_node->left = left;
    return rebalance(min_node);
}

bool exists(Node* node, long long key) {
    while (node) {
        if (key < node->key) {
            node = node->left;
        } else if (key > node->key) {
            node = node->right;
        } else {
            return true;
        }
    }
    return false;
}

std::pair<bool, long long> find_next(Node* node, long long key) {
    long long candidate = 0;
    bool found = false;
    while (node) {
        if (node->key > key) {
            candidate = node->key;
            found = true;
            node = node->left;
        } else {
            node = node->right;
        }
    }
    return {found, candidate};
}

std::pair<bool, long long> find_prev(Node* node, long long key) {
    long long candidate = 0;
    bool found = false;
    while (node) {
        if (node->key < key) {
            candidate = node->key;
            found = true;
            node = node->right;
        } else {
            node = node->left;
        }
    }
    return {found, candidate};
}

std::pair<bool, long long> find_kth(Node* node, long long k) {
    if (k <= 0) {
        return {false, 0};
    }
    while (node) {
        int left_sz = node_size(node->left);
        if (k == left_sz + 1) {
            return {true, node->key};
        }
        if (k <= left_sz) {
            node = node->left;
        } else {
            k -= left_sz + 1;
            node = node->right;
        }
    }
    return {false, 0};
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    Node* root = nullptr;
    std::vector<std::string> output;
    std::string action;
    long long value;

    while (std::cin >> action >> value) {
        if (action == "insert") {
            root = insert_node(root, value);
        } else if (action == "delete") {
            root = remove_node(root, value);
        } else if (action == "exists") {
            output.push_back(exists(root, value) ? "true" : "false");
        } else if (action == "next") {
            auto [found, result] = find_next(root, value);
            output.push_back(found ? std::to_string(result) : "none");
        } else if (action == "prev") {
            auto [found, result] = find_prev(root, value);
            output.push_back(found ? std::to_string(result) : "none");
        } else if (action == "kth") {
            auto [found, result] = find_kth(root, value);
            output.push_back(found ? std::to_string(result) : "none");
        }
    }

    for (const auto& line : output) {
        std::cout << line << '\n';
    }

    return 0;
}
