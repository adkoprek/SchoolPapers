const DATA = [["G-Dur", "D-Dur", "A-Dur",  "E-Dur",  "H-Dur",   "Fis-Dur"],
              ["F-Dur", "B-Dur", "Es-Dur", "As-Dur", "Des-Dur", "Ges-Dur"]]


const random = (max) => Math.floor(Math.random() * max);

function get_next_element(params) {
    let array = random(2);
    if (DATA[array].lenght == 0) array = array == 0 ? 1 : 0;
}

