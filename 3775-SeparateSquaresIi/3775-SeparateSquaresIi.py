# Last updated: 7/5/2026, 7:39:36 PM
class Solution(object):
    def separateSquares(self, squares):
        # Step 1: collect x-coordinates
        xs = set()
        events = []

        for x, y, s in squares:
            xs.add(x)
            xs.add(x + s)
            events.append((y, 1, x, x + s))
            events.append((y + s, -1, x, x + s))

        xs = sorted(xs)
        x_id = {v: i for i, v in enumerate(xs)}

        events.sort()
        n = len(xs)

        # Segment tree
        count = [0] * (4 * n)
        length = [0] * (4 * n)

        def push_up(node, l, r):
            if count[node] > 0:
                length[node] = xs[r] - xs[l]
            elif l + 1 == r:
                length[node] = 0
            else:
                length[node] = length[node * 2] + length[node * 2 + 1]

        def update(node, l, r, ql, qr, val):
            if qr <= l or r <= ql:
                return
            if ql <= l and r <= qr:
                count[node] += val
                push_up(node, l, r)
                return
            mid = (l + r) // 2
            update(node * 2, l, mid, ql, qr, val)
            update(node * 2 + 1, mid, r, ql, qr, val)
            push_up(node, l, r)

        # Step 2: sweep y
        total_area = 0
        prev_y = events[0][0]

        areas = []  # (y_start, y_end, width)

        for y, typ, xl, xr in events:
            dy = y - prev_y
            if dy > 0:
                w = length[1]
                if w > 0:
                    areas.append((prev_y, y, w))
                    total_area += w * dy
            update(1, 0, n - 1, x_id[xl], x_id[xr], typ)
            prev_y = y

        # Step 3: find split height
        half = total_area / 2.0
        acc = 0.0

        for y1, y2, w in areas:
            strip_area = w * (y2 - y1)
            if acc + strip_area >= half:
                return y1 + (half - acc) / w
            acc += strip_area

        return areas[-1][1]
