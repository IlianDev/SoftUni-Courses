function pieceOfPie(pies, startPie, endPie) {
    let start = pies.indexOf(startPie)
    let end = pies.indexOf(endPie);

    return pies.slice(start, end + 1);
}
console.log(pieceOfPie(['Pumpkin Pie',
'Key Lime Pie',
'Cherry Pie',
'Lemon Meringue Pie',
'Sugar Cream Pie'],
'Key Lime Pie',
'Lemon Meringue Pie'
))
