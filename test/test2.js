function add() {
    const _args = [...arguments];
    function fn() {
        _args.push(...arguments);
        return fn;
    }
    fn.toString = function () {
        return _args.reduce((sum, cur) => sum + cur);
    };
    return fn;
}


let a = add(1)(1,2,3)(3)
console.log('a :>> ', a);

