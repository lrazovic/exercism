pub fn reply(message: &str) -> &str {
    let message = message.trim();
    let is_question = message.ends_with("?");
    let is_uppercase = |s: &str| -> bool { s.to_uppercase() == s && s.to_lowercase() != s };
    match (is_question, is_uppercase(message)) {
        (true, false) => "Sure.",
        (false, true) => "Whoa, chill out!",
        (true, true) => "Calm down, I know what I'm doing!",
        (false, false) if message.is_empty() => "Fine. Be that way!",
        _ => "Whatever.",
    }
}
