# Last updated: 7/5/2026, 7:42:22 PM
class Solution:
  def rotate(self, matrix: list[list[int]]) -> None:
    matrix.reverse()
    for i, j in itertools.combinations(range(len(matrix)), 2):
      matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]