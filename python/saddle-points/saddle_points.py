def saddle_points(matrix):
  result = set()
  if matrix == []:
    return result
  else:
    l = len(matrix[0])
    for lst_el in matrix:
      if len(lst_el) != l:
        raise ValueError("Irregular matrix")

  for r in range(len(matrix)):
    max_row = max(matrix[r])
    for c in range(len(matrix[r])):
      el = matrix[r][c]
      min_col = min([matrix[r1][c] for r1 in range(len(matrix))])
      if el >= max_row and el <= min_col:
        result.add((r, c))

  return result
