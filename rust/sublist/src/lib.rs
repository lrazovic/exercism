#[derive(Debug, Eq, PartialEq)]
pub enum Comparison {
    Equal,
    Sublist,
    Superlist,
    Unequal,
}

fn contains<T: PartialEq>(list_one: &[T], list_two: &[T]) -> bool {
    list_two.windows(list_one.len()).any(|w| w == list_one)
}

pub fn sublist<T: PartialEq>(_first_list: &[T], _second_list: &[T]) -> Comparison {
    match (_first_list.is_empty(), _second_list.is_empty()) {
        (true, true) => return Comparison::Equal,
        (false, true) => return Comparison::Superlist,
        (true, false) => return Comparison::Sublist,
        (false, false) => {
            if _first_list.eq(_second_list) {
                Comparison::Equal
            } else if contains(_first_list, _second_list) {
                Comparison::Sublist
            } else if contains(_second_list, _first_list) {
                Comparison::Superlist
            } else {
                Comparison::Unequal
            }
        }
    }
}
