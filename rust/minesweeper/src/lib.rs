/*
pub fn annotate(minefield: &[&str]) -> Vec<String> {
    minefield
        .iter() // Iterate over the lines.
        .enumerate() // Keep track of the row and col.
        .map(|(row, line)| {
            line.chars()
                .enumerate()
                .map(|(col, c)| match c {
                    '*' => String::from(c),
                    _ => minefield
                        .iter()
                        .skip(row.checked_sub(1).unwrap_or(0))
                        .take(3.min(2 + row))
                        .map(|s| {
                            s.chars()
                                .skip(col.checked_sub(1).unwrap_or(0))
                                .take(3.min(2 + col))
                                .filter(|c| *c == '*')
                                .count()
                        })
                        .fold(0, |acc, x| acc + x)
                        .to_string()
                        .replace("0", " "),
                })
                .collect::<String>()
        })
        .collect()
}
*/
use std::collections::HashSet;

const DELTAS: [(isize, isize); 8] = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
    (-1, -1),
    (1, -1),
    (1, 1),
    (-1, 1),
];

pub fn annotate(field: &[&str]) -> Vec<String> {
    let mines: HashSet<_> = field
        .iter()
        .enumerate()
        .flat_map(|(y, row)| {
            row.chars()
                .enumerate()
                .filter(|(_, col)| *col == '*')
                .map(move |(x, _)| (x, y))
        })
        .collect();

    field
        .iter()
        .enumerate()
        .map(|(y, row)| {
            row.chars()
                .enumerate()
                .map(|(x, col)| {
                    let cnt = DELTAS
                        .iter()
                        .map(|(dx, dy)| ((x as isize + dx) as usize, (y as isize + dy) as usize))
                        .filter(|offset| mines.contains(offset))
                        .count();
                    match (col, cnt) {
                        ('*', _) => '*',
                        (_, 0) => ' ',
                        _ => (cnt as u8 + b'0') as char,
                    }
                })
                .collect::<String>()
        })
        .collect()
}
