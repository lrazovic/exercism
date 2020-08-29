const DELTAS: [(isize, isize); 8] = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
];

pub fn annotate(minefield: &[&str]) -> Vec<String> {
    if minefield.len() == 0 {
        return vec![];
    }
    let mut board = minefield
        .iter()
        .map(|s| s.chars().collect::<Vec<_>>())
        .collect::<Vec<_>>();
    let rows = board.len();
    let cols = board[0].len();
    for row in 0..rows {
        for col in 0..cols {
            // Skip cell if it contains a mine
            if board[row][col] == '*' {
                continue;
            }
            // Checking all the neighbours
            let neighbors_count = DELTAS
                .iter()
                // Calc the coordinates
                .map(|(rd, cd)| (row as isize + rd, col as isize + cd))
                // Skip non valid coordinates
                .filter(|(r, c)| *r >= 0 && (*r as usize) < rows && *c >= 0 && (*c as usize) < cols)
                // Keep only mines
                .filter(|(r, c)| board[*r as usize][*c as usize] == '*')
                // Count the elements, the mines
                .count();

            // If there are any mines, save the counter
            if neighbors_count > 0 {
                board[row][col] = (neighbors_count as u8 + b'0') as char;
            }
        }
    }

    // Convert to Vec<String> as expexted
    board.iter().map(|x| x.iter().collect()).collect()
}
