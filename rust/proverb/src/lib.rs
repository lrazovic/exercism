pub fn build_proverb(list: &[&str]) -> String {
    match list.len() {
        0 => String::new(),
        1 => format!("And all for the want of a {}.", list[0]),
        _ => list
            .windows(2)
            .map(|words| format!("For want of a {} the {} was lost.", words[0], words[1]))
            .chain(std::iter::once(format!(
                "And all for the want of a {}.",
                list[0]
            )))
            .collect::<Vec<String>>()
            .join("\n"),
    }
}
