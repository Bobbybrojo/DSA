n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

max_sum = 0

# A tilted rectangle is defined by a center and two radii (horizontal and vertical)
# But based on the problem, it seems we need to consider all cells on the perimeter
for r in range(2, n):
    for c in range(1, n - 1):
        # Try different rectangle sizes
        for dist1 in range(1, n):
            for dist2 in range(1, n):
                # Calculate the 4 vertices
                v1_r, v1_c = r, c                          # Bottom
                v2_r, v2_c = r - dist1, c + dist1          # Right
                v3_r, v3_c = v2_r - dist2, v2_c - dist2    # Top
                v4_r, v4_c = r - dist2, c - dist2          # Left
                
                # Check bounds
                vertices = [(v1_r, v1_c), (v2_r, v2_c), (v3_r, v3_c), (v4_r, v4_c)]
                if any(vr < 0 or vr >= n or vc < 0 or vc >= n for vr, vc in vertices):
                    continue
                
                current_sum = 0
                
                # Edge 1: v1 to v2 (include both endpoints)
                for i in range(dist1 + 1):
                    current_sum += grid[v1_r - i][v1_c + i]
                
                # Edge 2: v2 to v3 (skip v2 as it's already counted)
                for i in range(1, dist2 + 1):
                    current_sum += grid[v2_r - i][v2_c - i]
                
                # Edge 3: v3 to v4 (skip v3)
                for i in range(1, dist1 + 1):
                    current_sum += grid[v3_r + i][v3_c - i]
                
                # Edge 4: v4 to v1 (skip v4 and v1)
                for i in range(1, dist2):
                    current_sum += grid[v4_r + i][v4_c + i]
                
                max_sum = max(max_sum, current_sum)

print(max_sum)