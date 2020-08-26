use std::fmt::{Display, Formatter, Result};

#[derive(Debug, PartialEq)]
pub struct Clock {
    time: i32,
}

impl Display for Clock {
    fn fmt(&self, f: &mut Formatter) -> Result {
        write!(f, "{:02}:{:02}", self.time / 60, self.time % 60)
    }
}

impl Clock {
    pub fn new(hours: i32, minutes: i32) -> Self {
        Clock {
            time: (60 * hours + minutes).rem_euclid(24 * 60),
        }
    }

    pub fn add_minutes(&self, minutes: i32) -> Self {
        Clock::new(0, self.time + minutes)
    }
}
