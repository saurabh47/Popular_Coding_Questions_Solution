/**
 * https://leetcode.com/problems/smallest-string-with-swaps/
 * @param {string} s
 * @param {number[][]} pairs
 * @return {string}
 */
var smallestStringWithSwaps = function (s, pairs) {
    let uf = new UnionFind(s.length);

    for (let p of pairs) {
        const s = p[0];
        const d = p[1];

        uf.union(s, d);
    }

    let rootToComponent = new Map();

    for (let vertex = 0; vertex < s.length; vertex++) {
        let root = uf.find(vertex);

        if (!rootToComponent.has(root)) {
            rootToComponent.set(root, []);
        }

        rootToComponent.get(root).push(vertex);
    }

    let smallestStr = [];

    for (const indices of rootToComponent.values()) {
        let chars = [];
        for (let index of indices) {
            chars.push(s[index]);
        }

        chars.sort();

        for (let i = 0; i < indices.length; i++) {
            smallestStr[indices[i]] = chars[i];
        }
    }

    return smallestStr.join('');
};

class UnionFind {
    constructor(size) {
        this.root = new Array(size).fill().map((_, i) => i);
        this.rank = new Array(size).fill(1);
    }

    find(x) {
        if (x == this.root[x]) {
            return x;
        }
        return this.root[x] = this.find(this.root[x]);
    }

    union(x, y) {
        const rootX = this.find(x);
        const rootY = this.find(y);

        if (rootX != rootY) {
            if (this.rank[rootY] >= this.rank[rootX]) {
                this.root[rootY] = rootX;
                this.rank[rootX] += this.rank[rootY];
            } else {
                this.root[rootX] = rootY;
                this.rank[rootY] += this.rank[rootX];
            }
        }
    }
}

console.log(smallestStringWithSwaps("dcab", [[0, 3], [1, 2]])); // ans -> bcad