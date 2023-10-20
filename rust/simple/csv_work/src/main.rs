fn main() {
    let penguin_data = "\
    common name,lenght (cm)
    Little penguin, 33
    Yellow penguin,65
    Fiordiand penguin, 60
    Invalid,data
    ";

    let records = penguin_data.lines();

    for (i, record) in records.enumerate() {
        if i == 0 || record.trim().len() == 0 {
            continue;
        }
        let fields: Vec<_> = record
                .split(',')
                .map(|field| field.trim())
                .collect();
                if cfg!(debug_assertions) {
                    eprint!("debug: {:?} -> {:?}",
                            record, fields);
                }
                let name = fields[0];
                if let Ok(lenght) = fields[1].parse::<f32>() {
                    println!("{}, {}cm", name, lenght);
                }
    }
}