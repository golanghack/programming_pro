fn main() {
    let fruit = vec!['_', '_', '_'];

    let buffer_overflow = fruit[8];
    assert_eq!(buffer_overflow, '_');
}