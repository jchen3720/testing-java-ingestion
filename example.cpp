#include <iostream>
#include <random>
#include <vector>

using namespace std;

int generateRandomNumber(int min, int max) {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> distrib(min, max);
    return distrib(gen);
}

void DFS(int node, vector<vector<int>>& adj, vector<bool>& visited) {
    cout << node << " ";
    visited[node] = true;

    for (int neighbor : adj[node]) {
        if (!visited[neighbor]) {
            DFS(neighbor, adj, visited);
        }
    }
}
