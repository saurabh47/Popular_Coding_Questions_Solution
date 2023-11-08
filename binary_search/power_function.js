function power(num, pow) {
    num = pow < 0 ? 1 / num : num;
    let result = 1;
    for(let i=0;i< Math.abs(pow);i++) {
        result = result * num;
    }
    return result;
}
console.log(power(2,-2));
console.log(1/2 * 1/2);