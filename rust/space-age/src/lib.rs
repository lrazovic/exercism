// The code below is a stub. Just enough to satisfy the compiler.
// In order to pass the tests you can add-to or change any of this code.

#[derive(Debug)]
pub struct Duration {
    seconds: f64,
}

impl From<u64> for Duration {
    fn from(s: u64) -> Self {
        Self { seconds: s as f64 }
    }
}

pub trait Planet {
    const PLANET_TIME: f64;
    fn years_during(duration: &Duration) -> f64 {
        duration.seconds / Earth::SEC_IN_YEAR / Self::PLANET_TIME
    }
}

pub struct Mercury;
pub struct Venus;
pub struct Earth;
pub struct Mars;
pub struct Jupiter;
pub struct Saturn;
pub struct Uranus;
pub struct Neptune;

impl Planet for Mercury {
    const PLANET_TIME: f64 = 0.2408467;
}
impl Planet for Venus {
    const PLANET_TIME: f64 = 0.61519726;
}
impl Planet for Earth {
    const PLANET_TIME: f64 = 1.0;
}

impl Earth {
    const SEC_IN_YEAR: f64 = 31_557_600.0;
}

impl Planet for Mars {
    const PLANET_TIME: f64 = 1.8808158;
}
impl Planet for Jupiter {
    const PLANET_TIME: f64 = 11.862615;
}
impl Planet for Saturn {
    const PLANET_TIME: f64 = 29.447498;
}
impl Planet for Uranus {
    const PLANET_TIME: f64 = 84.016846;
}
impl Planet for Neptune {
    const PLANET_TIME: f64 = 164.79132;
}
