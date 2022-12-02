const fs = require('fs');

fs.readFile('./input.txt', 'utf-8', (err, data) => {
    if(err){
        console.error(err);
        return;
    }


    let split = data.split('\n');
    let parsedData = [];
    let elve = []
    for(let i = 0; i < split.length; i++){
        if(split[i] == ''){
            parsedData.push(elve);
            elve = []
        }else{
            elve.push(parseInt(split[i]));
        }
    }

    let maxCalories = 0;
    for(let i = 0; i < parsedData.length; i++){
        let totalCalories = 0;
        for(let j = 0; j < parsedData[i].length; j++){
            totalCalories += parsedData[i][j];
        }

        if(totalCalories > maxCalories){
            maxCalories = totalCalories;
        }
    }

    console.log(maxCalories);
})
