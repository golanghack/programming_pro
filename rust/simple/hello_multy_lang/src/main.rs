fn greet_words() {
    println! ("Hello, world!");
    let germany = "GriiB Gott!";
    let japan = "こんにちは世界！";
    let regions = [germany, japan];
    for region in regions.iter() {
        println!("{}", &region);
    }
}

fn main() {
    greet_words();
}