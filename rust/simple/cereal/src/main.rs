#[derive(Debug)]
enum Celeal {
    Barley, Millet, Rice,
    Rye, Spelt, Wheat,
}

fn main() {
    let mut grains: Vec<Celeal> = vec![];
    grains.push(Celeal::Rye);
    drop(grains);
    println!("{:?}", grains);
}