const RectangularStarPattern = () => {
    for (let index = 0; index < 6 ; index++) {
        let row = '';
        for (let inner_index = 0; inner_index < 5; inner_index++) {
            row += '* ';
        }
        console.log(row);
    }
}

RectangularStarPattern()