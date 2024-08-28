# KD-Tree

KD-Tree is a data structure useful when organizing data by several criteria all at once. Consider an example where you have a set of points on a 2 dimensional plane. Now suppose you are asked to find the nearest neighbor of some target point. What data structure would you use to store these points to be able to solve that problem?


### Implementation

```C++
#define MAX_DIM 3   // Dimensions
struct node_t
{
    double x[MAX_DIM];
    struct node_t *left, *right;
};

double dist(struct node_t *a, struct node_t *b)
{
    int dim = MAX_DIM;
    double t, d = 0;
    while (dim--)
    {
        t = a->x[dim] - b->x[dim];
        d += t * t;
    }
    return d;
}
void swap(struct node_t *x, struct node_t *y)
{
    double tmp[MAX_DIM];
    memcpy(tmp, x->x, sizeof(tmp));
    memcpy(x->x, y->x, sizeof(tmp));
    memcpy(y->x, tmp, sizeof(tmp));
}

/* see quickselect method */
struct node_t *find_median(struct node_t *start, struct node_t *end, int idx)
{
    if (end <= start)
        return NULL;
    if (end == start + 1)
        return start;

    struct node_t *p, *store, *md = start + (end - start) / 2;
    double pivot;
    while (1)
    {
        pivot = md->x[idx];

        swap(md, end - 1);
        for (store = p = start; p < end; p++)
        {
            if (p->x[idx] < pivot)
            {
                if (p != store)
                    swap(p, store);
                store++;
            }
        }
        swap(store, end - 1);

        /* median has duplicate values */
        if (store->x[idx] == md->x[idx])
            return md;

        if (store > md)
            end = store;
        else
            start = store;
    }
}

struct node_t *make_tree(struct node_t *t, int len, int i)
{
    struct node_t *n;

    if (!len)
        return 0;

    if ((n = find_median(t, t + len, i)))
    {
        i = (i + 1) % MAX_DIM;
        n->left = make_tree(t, n - t, i);
        n->right = make_tree(n + 1, t + len - (n + 1), i);
    }
    return n;
}

void nearest(struct node_t *root, struct node_t *nd, int i,
             struct node_t **best, double best_dist)
{
    double d, dx, dx2;

    if (!root)
        return best_dist;
    d = dist(root, nd);
    dx = root->x[i] - nd->x[i];
    dx2 = dx * dx;

    if (!*best || d < best_dist)
    {
        best_dist = d;
        *best = root;
    }

    /* if chance of exact match is high */
    if (!best_dist)
        return best_dist;

    if (++i >= MAX_DIM)
        i = 0;

    best_dist = nearest(dx > 0 ? root->left : root->right, nd, i, best, best_dist);
    if (dx2 < best_dist)
        best_dist = nearest(dx > 0 ? root->right : root->left, nd, i, best, best_dist);

    return best_dist;
}

int main(void)
{
    int i;
    struct node_t wp[] = {
        {{2, 3}}, {{5, 4}}, {{9, 6}}, {{4, 7}}, {{8, 1}}, {{7, 2}}
    };
    struct node_t testNode = {{9, 2}};
    struct node_t *root, *found, *million;
    double best_dist;

    root = make_tree(wp, sizeof(wp) / sizeof(wp[1]), 0, 2);

    found = 0;
    best_dist = nearest(root, &testNode, 0, &found, best_dist);

    printf(">> WP tree\nsearching for (%g, %g)\n"
            "found (%g, %g) dist %g\nseen %d nodes\n\n",
            testNode.x[0], testNode.x[1],
            found->x[0], found->x[1], sqrt(best_dist), visited);

    return 0;
}


```



## Ref

- https://www.youtube.com/watch?v=Glp7THUpGow
- https://rosettacode.org/wiki/K-d_tree#C