console.log('hello world');

const name = 'charles';
console.log(`hello ${name}!`);

const age = 15;
console.log(`you are ${age} years old`);

if(age >= 18){
  console.log(`vroom vroom and vote out cheetoe puff`);
  }else if(age >= 15){
      console.log(`no vote but u can drive`);
    }else{
      console.log(`nah dog you taking the patita express`);
      }

function order(name1, name2=null){
  if(name2 == null){
    return `hello ${name1}`;
  }else{
    return `hello ${name1} and ${name2}`
    }
  }

  console.log(`yeah im ${name}`);
order(`ready to order`);

const multiplyBy3 = (x) => x * 3;
console.log(multiplyBy3(3));

const names =[`aly`,`bob`,`charlie`,`deborah`]
for (let i = 0; i < name.length; i ++) {
console.log(names[i]);
console.log(names[i]);
}
//let i = 0
//console.log(names[i]);
//console.log(names[i]);
//i++
//console.log(names[i]);
//console.log(names[i]);
//i++
//console.log(names[i]);
//console.log(names[i]);
//i++
let count = 0;
while (count < 0) {
  count++;
  console.log(count);
}
  const article = {
    name:'dog family give birth to 1o pups',
    views: 1234,
    dataPublished: `03/25/2018`,
    author:{
      name:`j`,
      title:`j1`
    }
};


document.addEventListener(`DOMContentLoaded`, () => {
let boxTop = 100;
let boxLeft = 100;
const floatingBox = document.querySelector(`.floatingBox`);
document.addEventListener(`keydown`,(event) => {
  const key = event.key;
  if (key === `ArrowDown`){
boxTop += 5;
  }
  if (key === `ArrowUp`){
boxTop -=5;
  }
  if (key === `ArrowLeft`){
boxLeft-=5
  }
  if (key === `ArrowRight`){
boxLeft+=5
  }
floatingBox.style.top = boxTop + `px`;
floatingBox.style.left = boxLeft + `px`;
console.log(event);
})
})
