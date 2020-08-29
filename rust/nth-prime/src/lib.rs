pub fn nth(n: u32) -> u32 {
    match n {
        0 => 2,
        1 => 3,
        _ => match (2..).filter(|&i| is_prime(i)).nth(n as usize) {
            Some(n) => n,
            None => panic!("Conversion error"),
        },
    }
}

fn is_prime(n: u32) -> bool {
    let up = ((n as f32).sqrt() as u32) + 1;
    !(2..up).any(|i| n % i == 0)
}
