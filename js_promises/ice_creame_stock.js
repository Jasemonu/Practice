let stocks = {
  Fruits: ["Strawberry", "grapes", "banana", "apple"],
  Liquid: ["water", "ice"],
  Holder: ["cone", "cup", "stick"],
  toppings: ["chocolate", "peanuts"]
};

let is_shop_open = true;

let order = (time, work) => {
  return new Promise( (resolve, reject) => {
    if (is_shop_open){
      setTimeOut( ()=> {resolve( work() );
      }, time );
      
    } else{
      reject(console.log("our shop is closed")) 
    }
  });

};


order(2000, () =>console.log(`${stocks.Fruits[0]} was selected`))

.then(()=> {
  return order(0000, ()=> console.log("Production has started"))
})

.then(() => {
  return order(2000, () => console.log("The fruit was chopped"))
})

.then(() => {
  return order(1000, () => console.log(`${stocks.liquid[0]} and ${stocks.liquid[1]}`))

})

.then(() => {
  return order(1000, () => console.log("start the machine"))
})

.then(() => {
  return order(2000, () => console.log(`ice cream placed on ${stocks.holder[0]}`))

})

.then(() =>{
  return order(3000, () => console.log(`${stock.toppings[0]} was selected`))

})

.then(() =>{
  return order(1000, () => console.log("ice cream was served"))
});

.catch(() => {
  console.log("customer lsft")
})

.finally(() = > {
  console.log("day ended, shop is closed");
});

